#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera il PDF «PSN — Analisi dei Profili di Sovranità Digitale» A PARTIRE DALLA
PAGINA COSTRUITA, non da un testo gemello.

Vincolo di progetto (CLAUDE.md, regola 12): pagina e PDF non si scrivono due
volte. La sorgente unica è il layout Hugo; questo script legge l'HTML già
renderizzato e ne produce la versione stampabile. Ogni modifica alla pagina si
riflette nel PDF alla rigenerazione successiva, senza intervento manuale.

Uso:
    hugo --quiet --gc
    python tools/genera-pdf-psn.py            # italiano
    python tools/genera-pdf-psn.py --lang en  # inglese
"""
import argparse, datetime, hashlib, io, os, re, sys

from bs4 import BeautifulSoup
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLU, ROSSO, VERDE, GRIGIO = colors.HexColor("#0066CC"), colors.HexColor("#D9364F"), colors.HexColor("#1D9E75"), colors.HexColor("#6C757D")

CFG = {
    "it": dict(src="public/psn/index.html", out="static/pdf/psn-analisi-profili-sovranita-digitale.pdf",
               titolo="PSN — Analisi dei Profili di Sovranità Digitale",
               sotto="Perché il Polo Strategico Nazionale non garantisce la sovranità digitale",
               ente="Osservatorio Nazionale sulla Sovranità Digitale — progetto indipendente",
               nota=("Documento generato automaticamente dalla pagina osservatorio.mxmap.it/psn/. "
                     "Pagina e PDF hanno una sorgente unica: non possono divergere."),
               pag="Pagina %d"),
    "en": dict(src="public/en/psn/index.html", out="static/pdf/psn-digital-sovereignty-profile-analysis-en.pdf",
               titolo="PSN — Analysis of Digital Sovereignty Profiles",
               sotto="Why Italy's national cloud programme does not deliver digital sovereignty",
               ente="National Digital Sovereignty Observatory — an independent project",
               nota=("Generated automatically from osservatorio.mxmap.it/en/psn/. "
                     "Page and PDF share a single source and cannot diverge."),
               pag="Page %d"),
}


def stili():
    s = getSampleStyleSheet()
    def st(n, **kw):
        base = dict(fontName="Helvetica", fontSize=9.5, leading=13.5, spaceAfter=5, textColor=colors.HexColor("#111111"))
        base.update(kw)
        return ParagraphStyle(n, parent=s["Normal"], **base)
    return {
        "h1":   st("h1", fontName="Helvetica-Bold", fontSize=20, leading=24, spaceBefore=14, spaceAfter=8, textColor=BLU),
        "h2":   st("h2", fontName="Helvetica-Bold", fontSize=13, leading=16, spaceBefore=13, spaceAfter=5, textColor=BLU),
        "h3":   st("h3", fontName="Helvetica-Bold", fontSize=10.5, leading=14, spaceBefore=9, spaceAfter=3),
        "p":    st("p", alignment=TA_JUSTIFY),
        "li":   st("li", leftIndent=10, bulletIndent=3, alignment=TA_JUSTIFY, spaceAfter=3),
        "box":  st("box", fontSize=9, leading=12.5, leftIndent=6, rightIndent=6, spaceBefore=3, spaceAfter=3),
        "cell": st("cell", fontSize=7.4, leading=9.4, spaceAfter=0),
        "th":   st("th", fontName="Helvetica-Bold", fontSize=7.4, leading=9.4, spaceAfter=0, textColor=colors.white),
        "small":st("small", fontSize=7.6, leading=10, textColor=GRIGIO),
    }


def pulisci(el):
    """HTML di un nodo -> markup minimale accettato da reportlab."""
    h = el.decode_contents() if hasattr(el, "decode_contents") else str(el)
    h = re.sub(r"<svg.*?</svg>", "", h, flags=re.S)
    h = re.sub(r"</?(?:span|div|code|small|abbr)[^>]*>", "", h)
    h = re.sub(r"<a [^>]*href=\"(https?://[^\"]+)\"[^>]*>(.*?)</a>", r"\2 <font color='#0066CC'>[\1]</font>", h, flags=re.S)
    h = re.sub(r"<a [^>]*>(.*?)</a>", r"\1", h, flags=re.S)
    h = re.sub(r"</?(?:strong|b)>", lambda m: "<b>" if "/" not in m.group(0) else "</b>", h)
    h = re.sub(r"</?(?:em|i)>", lambda m: "<i>" if "/" not in m.group(0) else "</i>", h)
    h = re.sub(r"<br\s*/?>", "<br/>", h)
    h = re.sub(r"<(?!/?(?:b|i|br|font|super|sub)\b)[^>]*>", "", h)
    return re.sub(r"[ \t\n]+", " ", h).strip()


def tabella(tab, S, larghezza):
    righe, intest = [], []
    for th in tab.select("thead th"):
        intest.append(Paragraph(pulisci(th), S["th"]))
    if intest:
        righe.append(intest)
    ncol = len(intest) or max((len(tr.find_all(["td", "th"])) for tr in tab.select("tbody tr")), default=0)
    if not ncol:
        return None
    for tr in tab.select("tbody tr"):
        celle, span = [], []
        for td in tr.find_all(["td", "th"]):
            celle.append(Paragraph(pulisci(td), S["cell"]))
            span.append(int(td.get("colspan", 1)))
        while sum(span) < ncol:
            celle.append(Paragraph("", S["cell"])); span.append(1)
        righe.append(celle)
    if len(righe) < 2:
        return None
    w = [larghezza / ncol] * ncol
    t = Table(righe, colWidths=w, repeatRows=1 if intest else 0)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLU),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#BBBBBB")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F7F7")]),
    ]))
    return t


def riquadro(el, S, larghezza, colore):
    parti = [Paragraph(pulisci(x), S["box"]) for x in el.find_all(["p", "li"], recursive=True) if pulisci(x)]
    if not parti:
        return None
    t = Table([[parti]], colWidths=[larghezza])
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.9, colore),
        ("LINEBEFORE", (0, 0), (0, -1), 3.2, colore),
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FBFBFB")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def costruisci(lang):
    cfg = CFG[lang]
    src = os.path.join(ROOT, cfg["src"])
    if not os.path.exists(src):
        sys.exit("Manca %s — eseguire prima: hugo --quiet --gc" % cfg["src"])
    soup = BeautifulSoup(io.open(src, encoding="utf-8").read(), "lxml")
    # il contenuto sta nell'ultimo container-xxl: i primi sono intestazione e navigazione
    cand = [c for c in soup.select("div.container-xxl") if c.select("h2")]
    main = max(cand, key=lambda c: len(c.select("h2"))) if cand else soup.body
    for sel in ("nav", "header", "footer", ".cloudact-bar", ".callout.danger .callout-title svg"):
        for x in main.select(sel):
            x.decompose()

    S = stili()
    W = A4[0] - 30 * mm
    flow = [Paragraph(cfg["titolo"], S["h1"]),
            Paragraph("<b>%s</b>" % cfg["sotto"], S["p"]),
            Paragraph(cfg["ente"], S["small"]),
            Paragraph(datetime.date.today().strftime("%d.%m.%Y"), S["small"]),
            Spacer(1, 4 * mm),
            Paragraph("<i>%s</i>" % cfg["nota"], S["small"]),
            Spacer(1, 5 * mm)]

    visti = set()
    for el in main.find_all(["h2", "h3", "p", "ul", "ol", "table", "blockquote", "div"], recursive=True):
        if any(a in visti for a in (id(x) for x in el.parents)):
            continue
        cls = " ".join(el.get("class", []))
        if el.name == "div":
            if any(k in cls for k in ("callout", "alert", "info-box-custom")):
                colore = ROSSO if ("danger" in cls or "warning" in cls) else (VERDE if "success" in cls else BLU)
                r = riquadro(el, S, W, colore)
                if r:
                    flow += [Spacer(1, 2 * mm), r, Spacer(1, 2 * mm)]
                    visti.add(id(el))
            continue
        if el.name == "table":
            r = tabella(el, S, W)
            if r:
                flow += [Spacer(1, 2 * mm), r, Spacer(1, 2.5 * mm)]
            visti.add(id(el))
            continue
        if el.name in ("ul", "ol"):
            for i, li in enumerate(el.find_all("li", recursive=False), 1):
                txt = pulisci(li)
                if txt:
                    flow.append(Paragraph(txt, S["li"], bulletText="%d." % i if el.name == "ol" else "•"))
            visti.add(id(el))
            continue
        txt = pulisci(el)
        if not txt:
            continue
        if el.name == "h2":
            flow.append(KeepTogether([Paragraph(txt, S["h2"])]))
        elif el.name == "h3":
            flow.append(Paragraph(txt, S["h3"]))
        elif el.name == "blockquote":
            flow.append(Paragraph("<i>%s</i>" % txt, S["box"]))
        else:
            flow.append(Paragraph(txt, S["small"] if "small" in cls else S["p"]))

    out = os.path.join(ROOT, cfg["out"])
    os.makedirs(os.path.dirname(out), exist_ok=True)

    def pagina(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(GRIGIO)
        canvas.drawString(15 * mm, 10 * mm, cfg["titolo"])
        canvas.drawRightString(A4[0] - 15 * mm, 10 * mm, cfg["pag"] % doc.page)
        canvas.setStrokeColor(colors.HexColor("#DDDDDD"))
        canvas.line(15 * mm, 13 * mm, A4[0] - 15 * mm, 13 * mm)
        canvas.restoreState()

    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm,
                          topMargin=15 * mm, bottomMargin=18 * mm,
                          title=cfg["titolo"], author=cfg["ente"])
    doc.addPageTemplates([PageTemplate(id="std",
                                       frames=[Frame(15 * mm, 18 * mm, W, A4[1] - 33 * mm, id="f")],
                                       onPage=pagina)])
    n_flow = len(flow)
    doc.build(flow)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()
    print("%s  |  %d elementi  |  %d KB  |  sha256 %s…" % (cfg["out"], n_flow, os.path.getsize(out) // 1024, h[:16]))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="it", choices=["it", "en", "both"])
    a = ap.parse_args()
    for l in (["it", "en"] if a.lang == "both" else [a.lang]):
        costruisci(l)
