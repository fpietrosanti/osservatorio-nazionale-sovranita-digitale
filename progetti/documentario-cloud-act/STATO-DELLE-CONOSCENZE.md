# STATO DELLE CONOSCENZE — progetto documentario CLOUD Act

Aggiornato al 28 luglio 2026. Documento di controllo: separa ciò che è **verificato su fonte primaria**
da ciò che è **riportato da fonti secondarie** e da ciò che è **ancora aperto**.
Serve a decidere cosa può andare in onda e cosa no.

**Legenda affidabilità**
🟢 **A — CERTO**: fonte primaria letta direttamente. Utilizzabile in trasmissione.
🟡 **B — SOLIDO, DA CONFERMARE**: fonte secondaria affidabile o fonte primaria letta tramite intermediario. Utilizzabile con verifica finale.
🔴 **C — APERTO**: non verificato. **Non utilizzabile.**
⚫ **D — CONTRADDITTORIO**: le fonti confliggono. Da risolvere.

---

## 🟢 A — VERIFICATO SU FONTE PRIMARIA

### A1. Chi gestisce la posta delle istituzioni italiane
Interrogazione diretta dei record MX (dato pubblico, ripetibile da chiunque in cinque secondi).

| Dominio | Provider | |
|---|---|---|
| carabinieri.it | `smtp.google.com` | 🇺🇸 Google |
| poliziadistato.it | `mail.protection.outlook.com` | 🇺🇸 Microsoft |
| governo.it | `mail.protection.outlook.com` | 🇺🇸 Microsoft |
| istruzione.it | `mail.protection.outlook.com` | 🇺🇸 Microsoft |
| **acn.gov.it** | `mail.protection.outlook.com` | 🇺🇸 Microsoft |
| difesa.it | `mx.difesa.it` | 🇮🇹 propria |
| gdf.gov.it | `mercurio-e01.gdf.it` | 🇮🇹 propria |
| guardiacostiera.gov.it | `mail.guardiacostiera.gov.it` | 🇮🇹 propria |

**Come rifarlo**: `nslookup -type=MX carabinieri.it`
**⚠️ Limite da rispettare**: prova che la **posta istituzionale ordinaria** è gestita da quei fornitori.
NON prova nulla sulle reti operative/classificate, che sono separate. Non dire «Trump legge le indagini».

### A2. Il PSN è costruito sui quattro hyperscaler statunitensi
Dichiarazione del PSN stesso: «These services, currently created in partnership with **Oracle, Google,
Microsoft Azure, AWS**, may also be provided with other Cloud Service Providers in the future.»
Public Cloud PSN Managed → Oracle e Google · Hybrid Cloud → Azure · Secure Public Cloud → AWS, Azure, Google Cloud.
🔗 https://www.polostrategiconazionale.it/en/solutions/cloud-services-with-csp/

### A3. Le difese tecniche dichiarate dal PSN
«Encryption-key management **outside the CSP's control perimeter**» ·
«Confidential computing, **where activated**, makes it impossible for cloud service provider operators to
access even the data during processing».
**Da notare**: nella pagina non compare mai il CLOUD Act. E «where activated» è condizionale.

### A4. Microsoft gestisce già cloud «nazionali» operati da terzi
«National clouds are physical and logical network-isolated instances… **operated by local personnel**.»
«Microsoft is the technology provider, but **Microsoft doesn't operate the service**. 21Vianet independently
operates, provides, and manages the delivery of Microsoft cloud services… keep data within China.»
Esistono: **Microsoft Cloud for US Government** e **Azure/Office 365 operati da 21Vianet in Cina**.
🔗 https://learn.microsoft.com/en-us/partner-center/enroll/csp-national-clouds-overview

### A5. Che cosa chiede la campagna EUCS High+
Testo della lettera aperta del 10/06/2024 (estratto direttamente dal PDF): «High+ criteria» = **criteri di
immunità**; lo schema è **volontario**; «Cloud providers not meeting the High+ criteria will remain fully
able to offer their solutions to us **without any market distortion**»; «several non-EU providers are
progressively setting up corporate partnerships within the EU».
Destinatari: Stati membri, esperti ECCG, Commissione.
🔗 https://sovereignedge.eu/wp-content/uploads/2024/06/EUCS_OpenLetter_10June2024.pdf

### A6. I 62 sostenitori di EUCS High+
Iniziativa coordinata dall'ufficio di Bruxelles di **Airbus**. Italiani presenti: **Leonardo, Fincantieri,
Generali, Telecom Italia**. Presenti anche Banque de France, Crédit Agricole, Caisse des Dépôts, EDF,
OVHcloud, IONOS, Deutsche Telekom, Orange, Capgemini, Thales, Sopra Steria, Cigref, Beltug e altri.
🔗 https://eucshighplus.eu/
⚠️ Nell'elenco «Aruba» rimanda a **arubanetworks.com** (HPE, statunitense), **non** ad Aruba S.p.A. italiana.

### A7. Il regolamento ACN NON contiene alcuna clausola di immunità ✅ *(era C1, risolto)*
Letto il **testo primario integrale**: `RegolamentoCloud.pdf`, **88 pagine**, articolato (27 artt.) +
Allegati 1-4 — tutti nello stesso PDF, nessun allegato separato non letto. 326.143 caratteri analizzati.

**Scansione lessicale sull'intero testo — occorrenze:**
`extraterritoriale` **0** · `CLOUD Act` **0** · `nazionalità` **0** · `sede legale` **0** ·
`capogruppo` **0** · `capitale` **0** · `assetto proprietario` **0** · `paese terzo` **0** ·
`sovranità` **0** · `PSN`/`Polo Strategico Nazionale` **0**.

È **«ho letto il testo e il requisito non c'è»**, non «non sono riuscito a leggere il testo».

**Dove avrebbe dovuto trovarsi**: Allegato 4, §§2-5 (requisiti QC1-QC4). **Cosa c'è invece**: certificazioni
ISO (9001, 27001+27017/27018, 22301, 20000) e CSA STAR L2. L'unico requisito geografico riguarda *l'ente
certificatore*, non il fornitore — e ammette l'IAF MLA, che include **ANAB (USA)**.

**L'unica clausola sul tema** — PR.DS-01 15_S (All. 3, p. 78) / 6_S (All. 2, p. 44), **solo dati strategici**:
il fornitore «*segnala all'ACN e all'amministrazione ogni richiesta di accesso a dati o metadati da parte di
entità extra-UE*», con accesso «*solo a valle di un'autorizzazione esplicita*».
🎯 **È un obbligo procedurale che presuppone e ammette l'accesso extra-UE**, non un divieto strutturale.
Ed è **ineseguibile per costruzione**: un ordine CLOUD Act con *gag order* vieta giuridicamente al fornitore
proprio quella segnalazione. **La norma chiede una comunicazione che la legge americana proibisce.**

**Tre reperti ulteriori:**
1. Per i dati **strategici bastano QC3 o QC4** (art. 17 c. 4 lett. c). **Nessun obbligo di PSN** — mai nominato.
2. **HYOK + accesso esclusivo alle chiavi è requisito del solo QC4** (All. 4 §5.1, 18_SS/19_SS): un dato
   strategico può stare legittimamente su QC3 con il solo BYOK.
3. **Localizzazione UE derogabile** — «*salvo motivate e documentate ragioni di natura normativa o tecnica*»
   (PR.DS-01 1_O/2_O) — ed è **territoriale, non giurisdizionale**: un datacenter irlandese di controllata
   USA la soddisfa restando nel perimetro *ratione personae* del CLOUD Act.

**Confronto con SecNumCloud 3.2** (ANSSI, 8 marzo 2022, 55 pp., letto direttamente) — §19.6 «*Protection
vis-à-vis du droit extra-européen*», requisiti **cumulativi**: (a) sede statutaria + amministrazione centrale
+ stabilimento principale in UE; (b) capitale e diritti di voto extra-UE **≤24% individuale / ≤39%
collettivo**, diretti o indiretti, senza veto né nomina della maggioranza degli organi; (c) **impossibilità
tecnica** per società terza extra-UE di ottenere i dati; (d) autonomia d'esercizio o qualificazione a cascata
del subfornitore; (e) legami con governi stranieri come elemento di valutazione. Più §19.2.c: «*Les opérations
d'administration et de supervision du service doivent être réalisées depuis l'Union Européenne*».

> **ANSSI aziona tre leve: societaria, tecnica e operativa. ACN aziona solo quella tecnica in forma
> attenuata e sostituisce quella societaria con una procedurale. La leva societaria — la sola che
> neutralizzi il CLOUD Act — è integralmente assente.**

🔗 https://www.acn.gov.it/portale/cloud/regolamento-cloud-per-la-pa · 🔗 https://cyber.gouv.fr/
⚠️ **Limite dichiarato**: il catalogo `catalogocloud.acn.gov.it` restituisce una pagina di login del Portale
Fornitori e va aperto a mano (non incide sulla risposta: i requisiti sono nell'Allegato 4, letto per intero).
Nessuna determinazione successiva modificativa rinvenuta — affidabilità MEDIA su questo punto specifico.

### A8. 🔥 La gara del cloud di Stato fu vinta da Aruba e Fastweb — non dalla cordata che gestisce il PSN
**AFFIDABILITÀ ALTA** — Corte dei conti, Delib. 30/2024/G (7 febbraio 2024), p. 16, testuale:
«*il 22 giugno 2022 la gara è stata aggiudicata al RTI costituito da **Aruba e Fastweb** (mandataria);
il **7 luglio 2022**, il RTI promotore ha esercitato il **diritto di prelazione** previsto dalla procedura
di gara. Pertanto, la realizzazione e la gestione del PSN sono state affidate all'operatore economico
costituito dal raggruppamento **Sogei, Leonardo, C.D.P Equity e Tim**.*»
L'offerta vincente aveva uno sconto medio del **39,19%**.

**Il contenzioso** — TAR Lazio n. 4338/2023 dichiarò **inammissibile l'offerta del RTI TIM** per due difetti
fisici: distanza minima di 500 km fra le due region (rispettata solo sulla direttrice Pomezia–Santo Stefano
Ticino, **513 km**) e rischio sismico di **Pomezia, passata da zona 3 a 2B**. Il **Consiglio di Stato,
Sez. V, 24 ottobre 2023, n. 9210** ha confermato accertando **l'illegittimo esercizio della prelazione**;
la Corte dei conti registra che l'Amministrazione voleva impugnare anche l'accertamento, nella motivazione,
«*addirittura di un "affidamento diretto" della concessione*».
Il raggruppamento ha però **continuato a gestire il PSN**: per le opere PNRR l'art. 125 c.p.a. (richiamato
dall'art. 48 c. 4 d.l. 77/2021) esclude subentro e inefficacia del contratto — il rimedio è solo risarcitorio.
**Risarcimenti richiesti: Fastweb € 551.938.000 · Aruba € 27.126.000 · totale € 579.064.000.**

⚠️ **CONTRO-ARGOMENTO OBBLIGATORIO**: il diritto di prelazione del promotore era **previsto ex ante dalla
lex specialis** (art. 183 c. 15 d.lgs. 50/2016) e noto a tutti i concorrenti. Non fu un espediente
sopravvenuto. Il contro-contro-argomento è che il Consiglio di Stato ha accertato illegittimo *quell'esercizio*.
🔴 **DA VERIFICARE, priorità alta**: l'esito finale della domanda risarcitoria (giustizia-amministrativa.it)
e i testi integrali di TAR Lazio 4338/2023 e Cons. Stato Sez. V 9210/2023.

### A9. Il denaro non è tracciabile — ed è un'assenza documentata, non una supposizione
Scaricati i dataset ufficiali del DTD: **22.162 candidature finanziate** sulla misura 1.2 per
**€ 1.343.231.660**, venti colonne, **nessun campo fornitore**. Verifica diretta e riproducibile.
**Tre cause strutturali documentate**: (1) erogazione a *lump sum*, che elimina la rendicontazione delle
fatture; (2) il DTD si dichiara per iscritto «*estraneo al rapporto*» tra amministrazione e concessionario;
(3) **10.947 scuole e 10.887 comuni** sono stazioni appaltanti autonome.

> **La conclusione sostenibile non è «miliardi finiti in America» — non ne abbiamo la prova. È: l'Italia ha
> speso 1,9 miliardi per la sovranità digitale costruendo un sistema in cui è impossibile sapere quanta parte
> di quel denaro abbia comprato tecnologia sovrana. L'opacità è il fatto verificabile.**

⚠️ Due punti da chiarire col DTD: il totale di € 1,343 mld **eccede la dotazione di 1.000 mln**, e manca la
legenda ufficiale degli stati `E`/`R`/`A`.

### A10. Composizione del catalogo ACN — Google è il primo fornitore del cloud della PA italiana
Catalogo scaricato e analizzato (**2.107 schede, 826 fornitori**): **Google Cloud Italy è il primo fornitore
con 59 servizi qualificati**. Il PSN vende sei servizi denominati alla lettera «*Secure Public Cloud Amazon
Web Services / Microsoft / Google*».
⚖️ **Contro-fatto onesto da riportare**: i **nove servizi di livello massimo (QC4)** sono tutti e soli
nativi PSN. **Sulla fascia dei dati strategici la linea tiene.** Va detto.

### A11. Non solo non esiste un vincolo a comprare europeo: la legge vieta di discriminare gli USA
**Art. 69 d.lgs. 36/2023** obbliga a trattare gli operatori statunitensi **non meno favorevolmente**, in
quanto firmatari dell'Accordo sugli appalti pubblici dell'OMC. L'**IPI (Reg. UE 2022/1031)** è per
costruzione **inapplicabile ai firmatari dell'AAP**: è strutturalmente cieco proprio verso il maggiore
fornitore extra-UE.

> 🔑 **Perché questo rafforza la tesi invece di indebolirla**: non si *può* escludere Microsoft per legge —
> e infatti la Francia non l'ha fatto. Ha scritto un **requisito di sicurezza** che un fornitore soggetto a
> legge extra-UE non può soddisfare se non ristrutturandosi. **La via della certificazione non è una
> preferenza: è l'unica porta compatibile con il diritto degli appalti.**

---

## 🟡 B — SOLIDO, DA CONFERMARE PRIMA DELLA MESSA IN ONDA

### B1. La dichiarazione di Butti del 21 luglio 2026
75% raggiunto · oltre 13.000 PA · 1,9 miliardi PNRR · oltre 280 PA centrali/ASL su PSN · oltre 12.700 PA
locali **e scuole** su «cloud qualificati» · oltre 135.000 servizi.
Verbatim: «Con questo risultato **l'Italia si pone tra i Paesi europei più avanzati nella protezione dei
dati della pubblica amministrazione**.»
**Non usa mai l'espressione «sovranità digitale»**: parla di sicurezza e protezione dei dati.
🔗 https://www.key4biz.it/pnrr-butti-oltre-13mila-pa-in-cloud-75-centrati-obiettivi-ue/581879/
**Da fare**: recuperare il comunicato **primario** del Dipartimento per la trasformazione digitale
(innovazione.gov.it / governo.it). Il lancio è d'agenzia (Adnkronos), non l'atto originale.

### B2. La citazione del Senato francese
Scambio Wattebled/Carniaux del 10/06/2025, **sotto giuramento**, con richiamo alle pene per falsa
testimonianza. Risposta integrale: «Non, je ne peux pas le garantir, **mais, encore une fois, cela ne s'est
encore jamais produit**.» Ripresa nel rapporto del Senato n. 830 dell'8 luglio 2025.
🔗 https://www.senat.fr/compte-rendu-commissions/20250609/ce_commande_publique.html
🔗 Video ufficiale: https://videos.senat.fr/commission.COPU
**Da fare**: ricontrollare l'**audio del video** contro il resoconto scritto prima della messa in onda
(il *compte rendu* è un resoconto rivisto, non una trascrizione stenografica).

### B3. SecNumCloud 3.2 contiene la clausola di immunità
Richiede immunità dalle legislazioni extraterritoriali + **controllo europeo del capitale** + personale
operativo europeo. Unico schema nazionale che esclude *strutturalmente* il CLOUD Act.
Qualificati a metà 2026: **OVHcloud**; **S3NS** (fine 2025, 30 servizi, roadmap a 150). **Bleu** in corso.
🔗 https://www.erpimplementation.eu/en/erp-sovereign-cloud-europe-secnumcloud-hds-bsi-c5-2026/
**Da fare**: citare l'articolo/sezione sul **referenziale ANSSI originale**, non su fonte secondaria.
🔗 Riferimento primario da aprire: https://cyber.gouv.fr/ (sezione SecNumCloud)

### B4. Il lobbying tech a Bruxelles
€151 mln/anno (da €113 mln nel 2023) · top 10 = €49 mln, 7 su 10 statunitensi · Meta €10M, Microsoft €7M,
Apple €7M, Amazon €7M, Google €4,5M · **890 lobbisti** a tempo pieno · **437 badge permanenti** al PE
(su 720 deputati) · 378 incontri istituzionali nel primo semestre 2025 (~3 al giorno).
Fonte: Corporate Europe Observatory / LobbyControl su Registro trasparenza UE.
**⚠️ Sono sottostime**: il registro dichiara fasce, le analisi usano il limite inferiore.
**⚠️ CEO e LobbyControl sono ONG di advocacy**: dichiararlo.
🔗 Registro trasparenza UE: https://transparency-register.europa.eu/

### B5. La rimozione dei requisiti di sovranità dall'EUCS
22 marzo 2024: la terza bozza rimuove i requisiti di sovranità, sparisce il livello «High+».
Pressione **convergente**: industria USA + governo USA (via TTC/USTR) + **una coalizione di dodici Stati
membri guidata dai Paesi Bassi**. Fonte più autorevole: **EUISS** (istituto di studi strategici ufficiale UE).
Prova documentale più forte: comunicato **ITI**, *«ITI Urges EU Lawmakers to Drop Sovereignty Requirements
in Final EUCS»*.
**⚠️ Non dire «la lobby americana ha cancellato la regola»**: dodici governi europei hanno spinto nella
stessa direzione. La versione corretta è più scomoda, non meno.

### B6. Investimenti annunciati in Italia
Microsoft €4,3 mld (2 ottobre 2024, con incontro Brad Smith–Meloni tracciato su governo.it) ·
AWS €1,2 mld (novembre 2024, con accesso alla procedura per le infrastrutture strategiche nazionali) ·
Google $900M dal 2020 (region Milano e Torino con TIM) · Equinix €4 mld 2026-2033.
**⚠️ Cifre in conflitto tra fonti**: Microsoft €4,3 vs €10 mld; AWS €1,2 vs €2 mld. Da chiudere.

---

## ⚫ D — CONTRADDIZIONI DA RISOLVERE

### D1. Stato reale dei livelli EUCS (🔴 bloccante)
- **EUISS** (dossier 04): i requisiti di sovranità furono **rimossi** il 22/03/2024.
- **sota.io** (2026): il livello **High** *include* proprietà europea, personale UE per accessi privilegiati
  e giurisdizione esclusivamente UE; i fornitori con capogruppo USA **non** possono qualificarsi.
Non possono essere entrambe vere.
🚨 **sota.io è un fornitore commerciale che elenca sé stesso tra i qualificabili**: conflitto d'interesse.
🔗 https://sota.io/blog/eucs-cloud-assurance-levels-which-providers-qualify-eu-sovereignty-2026
🔗 **Fonte da consultare per dirimere**: https://www.enisa.europa.eu/ (schema EUCS)
*(approfondimento in corso — dossier 10)*

---

## 🔴 C — APERTO: NON UTILIZZABILE FINCHÉ NON VERIFICATO

| # | Domanda aperta | Perché è importante | Dove cercare |
|---|---|---|---|
| ~~C1~~ | ~~Il Regolamento ACN contiene una clausola di immunità?~~ | ✅ **RISOLTO — vedi A7. Risposta: NO**, verificato sul testo integrale | — |
| **C2** | Come si è espressa **l'Italia** nel negoziato ECCG sui criteri High+? Era tra i dodici Stati che ne chiesero la rimozione? | È l'informazione politicamente più pesante dell'intero progetto | Atti ECCG, posizioni ufficiali del Governo, eventuale accesso agli atti |
| ~~C3~~ | ~~Quanto denaro PNRR è finito a fornitori USA?~~ | ✅ **RISOLTO — vedi A9. Non è tracciabile, e l'assenza è documentata** | — |
| ~~C4~~ | ~~Quanti servizi qualificati ACN poggiano su tecnologia USA?~~ | ✅ **RISOLTO — vedi A10.** Catalogo analizzato: 2.107 schede, 826 fornitori | — |
| **C5** | Esito finale della domanda risarcitoria Fastweb/Aruba (€ 579 mln richiesti) | Se lo Stato è stato condannato, è spesa pubblica causata dalla prelazione illegittima | giustizia-amministrativa.it; testi integrali TAR Lazio 4338/2023 e Cons. Stato 9210/2023 |
| **C6** | Tenuta del **Data Privacy Framework** e stato del PCLOB | È la replica standard: «col DPF il problema è risolto». Senza risposta siamo scoperti | Decisione di adeguatezza 10/07/2023, causa Latombe, EDPB |
| **C7** | Asimmetria USA/Cina/UE e lock-in scolastico | Due atti interi del documentario | FedRAMP, Buy American Act, IPI Reg. 2022/1031, decisioni Garanti privacy UE su scuole |
| **C8** | **Aruba S.p.A.** è tra i firmatari EUCS High+? | Il link nell'elenco punta a HPE Aruba Networks | Verifica diretta presso la campagna |

*(C1 → A7 · C3 → A9 · C4 → A10, risolti. C2, C6, C7 hanno approfondimenti in corso — dossier 10, 01b, 05)*

---

## ERRORI DA NON COMMETTERE (registro delle trappole già individuate)

1. **Il 46% non è una quota del 75%.** Sono universi diversi: il 46% misura la posta elettronica, il 75%
   la migrazione al cloud. Dire «di quel 75%, il 46% è americano» è indifendibile.
   Formulazione corretta: *«Il Governo dichiara. Noi abbiamo misurato.»*
2. **CLOUD Act ≠ FISA 702.** Per spiare un funzionario straniero lo strumento pertinente è la **702**
   (bersagli non-americani all'estero), non il CLOUD Act, che è procedura penale. Citarne uno solo ci
   espone a smentita da parte di un giurista.
3. **Non tutti i partner italiani sono «meri rivenditori».** Vero per system integrator e region
   hyperscaler; falso per operatori con infrastruttura propria (Aruba, Seeweb…) e per il PSN, che dichiara
   custodia delle chiavi. Servono le quattro categorie del dossier 07.
4. **Non dire «Butti ha rivendicato la sovranità digitale»**: non l'ha detto. Ha detto «protezione dei dati».
5. **Non accusare di ipocrisia** Leonardo, TIM, Fincantieri e Generali per aver firmato la lettera High+:
   chiedere che uno standard esista è compatibile con l'operare secondo le regole vigenti.
6. **Non tagliare** l'inciso «ma, ancora una volta, ciò non si è ancora mai verificato»: mandarlo in onda
   integralmente è ciò che rende la citazione inattaccabile.
7. **Non presentare il modello cinese come tutela dei diritti**: risponde a esigenze di controllo statale.
   L'argomento corretto è solo strutturale — *quando un governo lo impone, il modello si realizza*.
8. **Non confondere base d'asta e spesa effettiva.** I «2,7 miliardi» del PSN **non sono soldi che lo Stato
   versa**: sono il tetto di valore della concessione, cioè il fatturato potenziale massimo generabile in
   tredici anni vendendo servizi alle PA. La Corte dei conti segnala che è *l'errore giornalistico più
   frequente su questo dossier*. Farlo in TV significa regalare la replica.
9. **Non dire che la prelazione fu un espediente**: era prevista dal bando e nota a tutti prima delle offerte.
   Il fatto è un altro, ed è più forte: **il Consiglio di Stato ha accertato che quell'esercizio fu illegittimo**.
10. **Non dire che gli americani hanno il livello massimo di qualificazione**: i nove servizi QC4 sono tutti
    e soli nativi PSN. Dirlo rafforza la nostra credibilità sul resto.
