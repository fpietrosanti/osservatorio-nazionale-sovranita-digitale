# FACT PACK — EUCS High+, le certificazioni europee e la soluzione praticabile

Compilato il 28 luglio 2026. Fonti primarie: lettera aperta 10 giugno 2024 (testo estratto dal PDF),
sito della campagna eucshighplus.eu (letto via browser), documentazione Microsoft Learn.

---

## 1. LA SCALA DELLE SOLUZIONI — «metterle in fila»

Il dibattito è confuso perché cinque cose diverse vengono chiamate tutte «cloud sovrano».
Questa è la scala reale, dal meno al più protettivo.

| Livello | Modello | Esempi | Cosa protegge | Esposizione al CLOUD Act |
|---|---|---|---|---|
| **0** | Cloud globale USA | Azure, AWS, GCP standard | nulla di giurisdizionale | **Piena** |
| **1** | **Residenza del dato** in UE | «EU Data Boundary», region europee | la *geografia* | **Piena** — è il mito che il documentario demolisce |
| **2** | **Sovranità contrattuale** degli hyperscaler | AWS European Sovereign Cloud, Microsoft Cloud for Sovereignty, Google Assured Workloads | impegni contrattuali e operativi | **Piena**: la capogruppo resta statunitense. *«Contractual sovereignty ≠ legal sovereignty»* |
| **3** | **Cloud di fiducia**: tecnologia USA **in licenza**, operata da un'entità europea **indipendente** | **Bleu** (Orange + Capgemini su Azure), **S3NS** (Thales + Google) | la giurisdizione, se l'operatore è realmente autonomo | **Esclusa** se qualificato SecNumCloud |
| **4** | **Infrastruttura europea nativa** | OVHcloud, IONOS, Scaleway, Hetzner, Deutsche Telekom, Aruba, Seeweb | tutto | **Nessuna** |

**Il livello 3 è il punto politico decisivo**: dimostra che *non* si tratta di «cacciare Microsoft»,
ma di **cambiare chi opera il servizio**.

---

## 2. LA PROVA CHE IL LIVELLO 3 È GIÀ REALTÀ — e la fa Microsoft

**AFFERMAZIONE** — Microsoft gestisce già «national clouds»: istanze **isolate fisicamente e logicamente**,
confinate nei confini geografici di un paese e **operate da personale locale**. In Cina, Microsoft
**non opera il servizio**: lo opera un'azienda locale su licenza della tecnologia.

**VERBATIM (Microsoft Learn)**
> «National clouds are physical and logical network-isolated instances of Microsoft enterprise cloud
> services. The clouds are confined within the geographic borders of specific countries/regions and
> **operated by local personnel**.»

> «Microsoft is the technology provider, but **Microsoft doesn't operate the service**. 21Vianet
> independently operates, provides, and manages the delivery of Microsoft cloud services. By licensing
> Microsoft technologies, 21Vianet can offer Azure and Office 365 services and operate Azure and
> Office 365 datacenters that **keep data within China**. 21Vianet also provides subscription and
> billing services, and support.»

**I national cloud esistenti**: **Microsoft Cloud for US Government** (per il governo statunitense) e
**Azure/Office 365 operati da 21Vianet in Cina** (Shanghai Blue Cloud Technology Co.).

**FONTE** — `https://learn.microsoft.com/en-us/partner-center/enroll/csp-national-clouds-overview`
**AFFIDABILITÀ — ALTA** (documentazione ufficiale del fornitore).

### 🎯 Il punto che vale l'intero blocco del documentario

> Gli Stati Uniti hanno preteso un cloud operato secondo le proprie regole: Microsoft l'ha costruito.
> La Cina ha preteso un cloud operato da un'azienda cinese: Microsoft ha concesso la tecnologia in licenza
> e si è tirata fuori dalla gestione. La Francia l'ha preteso: sono nati Bleu e S3NS.
> **L'Italia non l'ha preteso. E infatti non ce l'ha.**
>
> Non è un problema tecnico né commerciale: è un problema di **domanda politica**.

**Cautela editoriale** — Non dire «Microsoft in Cina è sovrana per proteggere i cittadini cinesi»:
il modello cinese risponde a esigenze di controllo statale, non di tutela dei diritti. L'argomento corretto
è strettamente **strutturale**: *quando un governo lo impone come condizione di mercato, il modello si realizza*.

---

## 3. LE CERTIFICAZIONI EUROPEE — chi ha la clausola di immunità

| Schema | Paese | Immunità da leggi extra-UE | Note |
|---|---|---|---|
| **SecNumCloud 3.2** (ANSSI) | 🇫🇷 Francia | **SÌ** — immunità dalle legislazioni extraterritoriali + **controllo europeo del capitale**; residenza dati in Francia/SEE; personale operativo europeo | L'unico schema nazionale che **esclude strutturalmente** il CLOUD Act |
| **HDS** | 🇫🇷 Francia | obbligatorio per i dati sanitari; certificazione triennale con audit annuali | Distinto da SecNumCloud |
| **BSI C5** | 🇩🇪 Germania | **NO** (catalogo di requisiti, attestazioni «Testate» di auditor indipendenti) | Oltre 100 attestazioni; standard cloud più diffuso in Europa dopo ISO 27001 |
| **EUCS Basic / Substantial / High** | 🇪🇺 UE | **contestato — v. §5** | In via di adozione nel 2026 |
| **Qualificazione ACN** | 🇮🇹 Italia | **non risulta** (v. dossier 06 — **DA VERIFICARE sul DD 21007/24**) | |

**Qualificati SecNumCloud (metà 2026)**: **OVHcloud** (SAP HANA su VMware, SNC Cloud Platform);
**S3NS/PREMI3NS** (qualificazione ottenuta **fine 2025**, 30 servizi con roadmap a 150).
**Bleu** (Orange/Capgemini su Azure) ha richiesto la qualificazione nel 2025-2026, **non ancora ottenuta**
alla data della fonte.

**FONTE** — erpimplementation.eu (analisi comparativa, luglio 2026). **AFFIDABILITÀ — MEDIA-ALTA**
(fonte secondaria specializzata; i requisiti SecNumCloud vanno citati sul referenziale ANSSI prima della TV).

---

## 4. EUCS HIGH+ — che cosa è davvero

**«High+» = i criteri di immunità.** Testuale dalla lettera aperta: le deliberazioni sull'EUCS
«concern notably the inclusion of **immunity criteria ("High+ criteria")**».

Non è un livello tecnico superiore: è **il livello che aggiunge la protezione giuridica** —
lo stesso contenuto che la Francia ha già in SecNumCloud, portato a norma europea.

### La lettera aperta del 10 giugno 2024 — gli argomenti (verbatim)

> «As Cloud users, we need voluntary High+ criteria to make informed and free choices and foster
> our competitiveness.»

> «EUCS being a **voluntary** certification scheme, we will remain, as European Cloud users, able to
> freely choose our Cloud suppliers. **Cloud providers not meeting the High+ criteria will remain fully
> able to offer their solutions to us without any market distortion.**»

> «Gaia-X Level 3 standards, which mirror High+ criteria, were developed on the basis of joint
> provider/user demand — they are already implemented and have not provoked any such distortion.
> We note with interest that **several non-EU providers are progressively setting up corporate
> partnerships within the EU**.»

> «A multitude of potential national standards would **fragment the EU market**… The inclusion of High+
> criteria will therefore reinforce the EU digital single market.»

**Destinatari**: Stati membri, esperti ECCG, Commissione europea.

**🔑 Perché questi argomenti sono forti** — La richiesta arriva in larga parte da **utenti**, non da
fornitori europei che difendono il proprio mercato; ed è **volontaria**, quindi non esclude nessuno.
Questo disinnesca in partenza l'accusa di protezionismo, che è la replica standard dell'industria USA.

---

## 5. ⚠️ CONTRADDIZIONE TRA FONTI DA RISOLVERE PRIMA DELLA MESSA IN ONDA

- Il **dossier 04** (fonte: EUISS, istituto ufficiale UE) documenta che **il 22 marzo 2024 i requisiti di
  sovranità furono rimossi** dalla terza bozza EUCS, e che il livello «High+» sparì.
- La fonte **sota.io** (2026) descrive invece un livello **High** che *già include* proprietà europea,
  personale UE per gli accessi privilegiati e giurisdizione esclusivamente UE, e afferma che i fornitori
  con capogruppo statunitense **non possono** qualificarsi.

**Le due cose non possono essere entrambe vere.** Possibili spiegazioni: reintroduzione successiva dei
requisiti; oppure la fonte sota.io descrive uno stato desiderato/non aggiornato.

🚨 **sota.io è un fornitore commerciale che nella propria tabella elenca sé stesso tra i qualificabili**:
conflitto d'interesse dichiarato. **Non usare quella tabella come fonte.**

**DA FARE (bloccante)**: verificare sul **testo ENISA** lo stato reale dei requisiti nella versione
adottata/in adozione dell'EUCS 2026.

---

## 6. CHI SPINGE PER EUCS HIGH+ — i sostenitori (62 organizzazioni)

Iniziativa coordinata dall'ufficio di Bruxelles di **Airbus** (`eucshighplus.eu`).

**Difesa e aerospazio** — Airbus, Dassault Aviation, MBDA, Saab, Kongsberg, Navantia, **Leonardo**,
**Fincantieri**, ASD (associazione europea aerospazio e difesa), Oesia Group, SPAC
**Banche, assicurazioni, servizi pubblici** — **Banque de France**, Crédit Agricole, Caisse des Dépôts,
**Generali**, France Assureurs, Groupe La Poste, Post Luxembourg, MSA, EDF, Veolia, Saint-Gobain,
Air France-KLM, SCK CEN
**Operatori cloud e telco europei** — OVHcloud, IONOS, Deutsche Telekom, Orange, Proximus, A1, Stackit,
Cloud Temple, CloudFerro, Clarence, Oodrive, Docaposte, Deep, TDF, Tuxis, OpenNebula, Klarrio
**IT e industria** — Capgemini, Thales, Sopra Steria, Eviden, Dassault Systèmes, **Telecom Italia (TIM)**,
Secunet, HarfangLab, SiPearl, Cybernetica, Alter
**Associazioni di utenti** — Cigref (FR), Beltug (BE), CIO Platform Netherlands, CESIN, Dutch Cloud
Community, European Digital SME Alliance, European Champions Alliance

**FONTE** — `https://eucshighplus.eu/` (letto il 28/07/2026). **AFFIDABILITÀ — ALTA** (elenco pubblicato
dalla campagna stessa). **Copertura stampa**: EUNews e Euractiv, luglio 2024 («Defence industry wants
data localisation and contractual guarantees in EU cloud scheme»).

⚠️ **Attenzione**: nell'elenco compare «Aruba» ma il collegamento punta ad **arubanetworks.com**
(HPE Aruba Networks, statunitense), **non** ad Aruba S.p.A. italiana. **Non attribuire la firma ad Aruba
S.p.A. senza verifica diretta.**

---

## 7. 🇮🇹 LA SCOPERTA ITALIANA

**Quattro grandi imprese italiane hanno sostenuto la richiesta di criteri di immunità europei:
Leonardo, Fincantieri, Generali e Telecom Italia (TIM).**

E **Leonardo e TIM sono azionisti del Polo Strategico Nazionale**.

**Il contrasto, formulato in modo corretto e difendibile:**
> L'industria italiana ha chiesto a Bruxelles che esista uno standard europeo di immunità dalle leggi
> extra-UE. Lo schema di qualificazione con cui l'Italia certifica il cloud della propria Pubblica
> Amministrazione, per quanto verificato, quella clausola non la prevede.

⚠️ **Non trasformarlo in accusa di ipocrisia.** Sostenere che uno standard *debba esistere* è
perfettamente compatibile con l'operare oggi secondo le regole vigenti. Il fatto rilevante e sufficiente è
un altro: **la domanda di immunità esiste, e viene dall'industria italiana stessa; manca la risposta
normativa italiana.** Va inoltre chiesto conto a Leonardo e TIM in fase di intervista — è materiale
giornalistico, non un «gotcha».

---

## 8. LA TESI FINALE, IN UNA RIGA

> Non bisogna smettere di usare Microsoft: bisogna smettere di **lasciarla operare**.
> Il modello esiste, ha un nome tecnico (*cloud di fiducia*), una certificazione che lo misura
> (**SecNumCloud 3.2**, in prospettiva **EUCS High+**), ed è già stato realizzato — negli Stati Uniti,
> in Cina e in Francia. In Italia manca la richiesta politica di realizzarlo.

---

## 9. DA FARE

- [ ] **Bloccante**: stato reale dei requisiti di sovranità nell'EUCS adottato 2026 (testo ENISA) — §5.
- [ ] Citazione puntuale del requisito di immunità nel referenziale **SecNumCloud 3.2** (ANSSI).
- [ ] Verifica del DD 21007/24 italiano (dossier 06 §2.2).
- [ ] Stato aggiornato della qualificazione **Bleu**; perimetro dei 30 servizi **S3NS**.
- [ ] Verifica diretta se **Aruba S.p.A.** sia tra i firmatari (§6).
- [ ] Posizione ufficiale del **Governo italiano** nel voto/negoziato ECCG sull'EUCS: l'Italia come si è
      espressa sui criteri High+? È l'informazione politicamente più rilevante ancora mancante.
