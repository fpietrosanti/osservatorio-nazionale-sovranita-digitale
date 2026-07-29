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
| **C1** | Il Regolamento ACN (**DD 21007/24**) contiene una clausola di immunità dalle leggi extra-UE? | È il perno dell'atto politico: «la Francia l'ha scritta, l'Italia no». Finora ho letto solo pagine-vetrina | 🔗 https://www.acn.gov.it/portale/cloud/regolamento-cloud-per-la-pa — serve il **testo del decreto e degli allegati** |
| **C2** | Come si è espressa **l'Italia** nel negoziato ECCG sui criteri High+? Era tra i dodici Stati che ne chiesero la rimozione? | È l'informazione politicamente più pesante dell'intero progetto | Atti ECCG, posizioni ufficiali del Governo, eventuale accesso agli atti |
| **C3** | Quanto denaro PNRR è finito a fornitori statunitensi? | Se non è tracciabile, **l'impossibilità di tracciarlo è essa stessa la notizia** | Contratti Consip, accordi quadro, rendicontazione misure 1.1 e 1.2, Corte dei conti |
| **C4** | Quanti dei servizi qualificati ACN poggiano su tecnologia USA? | Serve per dire «su N servizi qualificati, M sono su tecnologia statunitense». Senza il conteggio, niente numeri | Catalogo ACN dei servizi qualificati (*lead non confermato: ~2.285 voci*) |
| **C5** | Composizione e quote societarie del PSN; ingresso di AWS nel PSN | Base fattuale del blocco PSN | Atti di aggiudicazione, visure, comunicati |
| **C6** | Tenuta del **Data Privacy Framework** e stato del PCLOB | È la replica standard: «col DPF il problema è risolto». Senza risposta siamo scoperti | Decisione di adeguatezza 10/07/2023, causa Latombe, EDPB |
| **C7** | Asimmetria USA/Cina/UE e lock-in scolastico | Due atti interi del documentario | FedRAMP, Buy American Act, IPI Reg. 2022/1031, decisioni Garanti privacy UE su scuole |
| **C8** | **Aruba S.p.A.** è tra i firmatari EUCS High+? | Il link nell'elenco punta a HPE Aruba Networks | Verifica diretta presso la campagna |

*(C1, C2, C3, C6, C7 hanno approfondimenti in corso — dossier 09, 10, 03, 01b, 05)*

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
