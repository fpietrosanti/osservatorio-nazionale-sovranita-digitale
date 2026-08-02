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

### A12. Il Data Privacy Framework **non copre** il CLOUD Act — e lo dice per iscritto ✅ *(era C6, risolto)*
È la replica standard dei fornitori: «col DPF il problema è risolto». Ora abbiamo la confutazione su fonte
primaria, e sta in tre reperti.

**1. Il DPF cede il passo, testualmente.** *DPF Principles*, Principio I.5(a), letto verbatim sul PDF del
Dipartimento del Commercio USA: «*Adherence to these Principles may be limited: (a) to the extent necessary
to comply with a **court order** or meet public interest, **law enforcement**, or national security
requirements…*»
🎯 Un mandato §2703 **è letteralmente** una di quelle cose. **Il DPF non limita il CLOUD Act: gli cede il
passo per iscritto.**

**2. Chi subisce un ordine CLOUD Act non ha accesso al tribunale del ricorso.** EO 14086, Sez. 4: una
*covered violation* è quella che «*arises from **signals intelligence activities***». Un ordine di procedura
penale non lo è → **niente DPRC**. Confermato indipendentemente da COM(2024) 451.

**3. La Commissione, certificando il DPF, non ha esaminato lo strumento.** COM(2024) 451 final (22 pp.,
letto integralmente): ricerca full-text → **0 occorrenze di «CLOUD Act»**, e testualmente «*the below
findings only concern developments in the area of **national security***».

**Il resto del quadro, tutto da fonte primaria:**
- **La Commissione aveva indicato dove si sarebbe rotto** (COM(2024) 451, conclusione, ottobre 2024):
  vigilare su rapporti PCLOB, modifiche alla 702, nomine PCLOB. **Tutti e tre sono poi saltati.**
  Contestualmente ha diradato le revisioni a **tre anni** — prossima nel **2027**.
- **PCLOB senza quorum dal 27 gennaio 2025**: prova materiale nel *Staff Report* del 25 settembre 2025,
  uscito come rapporto dello staff endorsato da **un solo** membro (Beth A. Williams).
- **Formula fissa di risposta al ricorrente** (EO 14086 §3(d)(i)(H)), verbatim: nessuna motivazione, e
  «*without confirming or denying*».
- **Latombe T-553/23** (respinto il 3/9/2025) con il limite decisivo: il Tribunale ha giudicato la situazione
  **al 10 luglio 2023**. Impugnazione depositata il 31/10/2025.
- **Trump v. Slaughter** (29 giugno 2026, 6-3) supera *Humphrey's Executor*; noyb ha chiesto il ritiro
  dell'adeguatezza lo stesso giorno, la Commissione «valuterà».
  ⚖️ **Esiste però una contro-analisi forte** (Christakis/Propp/Swire, IAPP, 8 luglio 2026) secondo cui la
  sentenza non travolge la DPRC. **Va citata per prima, non per ultima**: anticiparla ci rende inattaccabili.

⚠️ **Accessi falliti dichiarati**: eur-lex (decisione 2023/1795), curia, europarl, edpb.europa.eu, justice.gov,
federalregister.gov (l'EO è stato letto su *The American Presidency Project*). Il numero della causa d'appello
CGUE (C-703/25 P) e l'ECLI della sentenza Latombe sono **DA VERIFICARE**.
🔗 Il dossier `01b` elenca **18 URL primari** da aprire a mano.

### A13. ⚠️ L'asimmetria esiste, ma NON funziona come credevamo — tesi corretta ✅ *(era C7)*

**Tre assunti di partenza sono risultati SBAGLIATI e vanno abbandonati:**

❌ **«Il Buy American Act impedisce di comprare tecnologia europea».** Falso, e c'è la prova nel testo:
la **FAR 25.103(e)** contiene un'**esenzione esplicita per l'information technology che sia *commercial
product***. Inoltre il BAA copre solo *supplies* e materiali da costruzione, **non i servizi**. Il Berry
Amendment riguarda cibo, tessuti, calzature e bandiere.
🚨 **Se in TV diciamo «gli USA escludono per legge il software europeo», veniamo smentiti in cinque minuti.**

❌ **«FedRAMP impone la cittadinanza statunitense al personale».** Falso: l'ufficio FedRAMP ha scritto
«*there is no government-wide requirement on citizenship*». L'obbligo di dichiarare proprietà/controllo/
influenza straniera (**FOCI Declaration**, policy A2LA R311, in attuazione del §3612 del FedRAMP
Authorization Act) è imposto ai **3PAO — gli auditor**, non ai fornitori cloud. Il divieto esplicito su
cittadinanza e localizzazione esiste solo nel **DoD Cloud SRG** per i livelli IL4/IL5, cioè **solo Difesa**.
L'esclusione reale è la **somma di quattro strati**, nessuno dei quali dice «vietato agli europei».

❌ **«Il Documento 79 cinese ordina di rimuovere il software straniero».** Trappola documentata: **CSET
(Georgetown)** ha tradotto il documento SASAC n. 79/2022 e annota testualmente che «*the publicly available
version of Document 79 translated below does not mention anything about removing foreign software*». La
storia «Delete America» viene dal *Wall Street Journal* (7 marzo 2024), su **fonti anonime** e un documento
non copiabile.
✅ **Sostituirlo con la lista MIIT/CISEC del 26 dicembre 2023** — 18 CPU, 6 sistemi operativi, 11 database,
tutti cinesi: pubblica e verificabile.

**Quello che invece REGGE ed è più forte:**

🎯 **Priorità 1 da verificare a mano — potrebbe essere il fatto più forte dell'intero blocco**: contare sul
**FedRAMP Marketplace** quanti CSP con casa madre europea siano autorizzati. L'unico caso emerso è
**SAP NS2**, che è una controllata **statunitense** di SAP.
> Se confermato: **per vendere al governo americano un europeo deve diventare americano — esattamente ciò
> che l'Europa non chiede agli americani.** Questa è l'asimmetria vera, e non ha bisogno di leggi inventate.

**IPI**: attivato **una sola volta in tre anni** — Reg. esec. (UE) 2025/1197, 19 giugno 2025, contro la Cina,
dispositivi medici sopra 5 M€. **Mai contro gli USA, mai sul digitale.** L'FSR ha soglie da 250 M€,
inutilizzabile per un ente locale.
**CADA** (COM(2026) 502, 3 giugno 2026): introduce quattro livelli di sovranità e il Livello 3 richiede
«*personnel citizenship*» — **l'UE copia il meccanismo americano** — ma la preferenza europea è
dichiaratamente «*ancillary and not decisive*». Revisione delle direttive appalti slittata a settembre 2026.

⚖️ **Dato che contraddice la nostra tesi e va citato comunque**: Eurostat mostra un disavanzo UE di
**126,3 mld €** sui canoni di proprietà intellettuale, ma un **avanzo di 60,4 mld €** sui servizi di
telecomunicazione e informatica (effetto Irlanda). **Ometterlo sarebbe manipolatorio.**

**Tema scuola — il vuoto è la notizia:**
Non esiste **alcun dato pubblico** su quante scuole italiane usino Google o Microsoft. Nella misura 1.2 le
scuole sono conteggiate dentro le «oltre 12.700 PA locali e scuole»: **un target europeo certificato senza
che sia pubblico su quali infrastrutture siano finiti i dati degli studenti.**
→ FOIA al MIM + incrocio del catalogo ACN con gli avvisi PNRR: **sarebbe lo scoop del blocco**.

⚠️ **Il «lock-in di competenze» non regge come vorremmo**: nessuno studio empirico longitudinale reperito.
Esiste advocacy (FSFE, 2011) e letteratura sul lock-in *istituzionale* (LiMux/Monaco), che è altra cosa.
⚠️ **Due casi europei finiscono con un adeguamento, non con un'espulsione**: Paesi Bassi (SURF/SIVON
rinegoziano con Google) ed EDPS/Commissione. Il caso forte è il **Baden-Württemberg**, che ha davvero
rinunciato a M365 nelle scuole. Il «divieto dell'Assia 2019» fu **ritirato dopo tre settimane**, e nel
novembre 2025 l'HBDI avrebbe dichiarato M365 conforme — **verifica urgente**.

### A14. L'EUCS **non esiste ancora** — contraddizione D1 risolta ✅
**Prova decisiva, fonte primaria istituzionale**: nella proposta **COM(2026) 502 final** (*Cloud and AI
Development Act*, Bruxelles 3.6.2026) la Commissione scrive che ENISA sta sviluppando l'EUCS «*which has
**not yet been adopted***» e che «*work will resume*».
👉 **Nessun atto giuridico, non in vigore, zero certificati emessi.**

1. **Nessun livello High contiene requisiti di sovranità**: rimossi il 22 marzo 2024, **mai reintrodotti**.
   Il CADA formalizza il principio opposto: «*cybersecurity must be distinguished from sovereignty
   requirements*» e «*Certification under the Cybersecurity Act… is not suited for addressing sovereignty
   concerns*».
2. **«High+» non è mai stato un livello formale**: il Cybersecurity Act (Reg. 2019/881, art. 52) ne prevede
   tre. Era l'**etichetta negoziale** dei criteri di immunità.
3. **La sovranità è rinata altrove**: i *Union assurance levels* 1-4 del CADA (art. 16 + All. II). Il
   **livello 4** è nella sostanza l'High+ mancato — stabilimento UE, personale cittadino UE, nessun controllo
   di paese terzo, supporto tecnico solo dall'UE, SBOM, separazione effettiva capogruppo/controllate extra-UE.
   ⚠️ Ma vincola **gli appalti pubblici**, non il mercato, ed è **ancora una proposta in codecisione**.

🚨 **Su sota.io**: la pagina è stata riletta e **nella versione online oggi afferma l'opposto** di quanto
riportato in precedenza — «*Even EUCS High does not currently mandate that cloud providers be EU-incorporated
or EU-controlled*». Contiene inoltre una colonna «EUCS Status (2026)» per singoli fornitori che è
**inesistente**. **Confermato: non usare quelle tabelle come fonte.**

### A15. 🔄 L'Italia ha chiesto la sovranità — e l'ha co-scritta. Narrativa da rovesciare
**«L'Italia non ha chiesto la sovranità» è FALSO.** Va corretto ovunque.

- **Luglio 2021** — l'Italia è **coautrice con Francia, Germania e Spagna** del non-paper che aggiungeva
  **immunità dal diritto straniero** e localizzazione UE al livello «high» dell'EUCS. Prova indiretta ma
  solida: esiste un documento olandese il cui *titolo* la nomina — «*Opinion of the Netherlands on the
  non-paper by **DE, ES, FR and IT** on the EUCS requirements for immunity from non-EU laws*» (citato due
  volte nel cepInput 8/2025). Fonte sull'autoria: Kenneth Propp, Cross-Border Data Forum, 13.9.2022 —
  **fonte ostile ai requisiti, che nondimeno attesta la paternità italiana**.
- **Dicembre 2022** — l'Italia **non firma** il non-paper contrario degli undici Stati (DK, EE, FI, EL, IE,
  LV, LT, PL, SK, SE, NL).
- **15-16 aprile 2024, ECCG** — l'ACN rappresenta l'Italia; il voto sulla proposta belga che rimuove la
  sovranità è rinviato. Il **17 aprile Butti**, su *La Verità*: la proposta «*permetterebbe ai fornitori…
  anche quelli che operano sotto la giurisdizione di governi esterni all'UE, di essere certificati come
  sicuri*»; e «*altri paesi invece, tra cui l'Italia, hanno sollecitato l'adozione di standard più elevati
  e rigorosi*».
- **ACN, Relazione annuale al Parlamento**: lo schema dovrà «*contemperare le esigenze di mercato con le
  istanze di autonomia e di non dipendenza da tecnologie extra-UE*».
- **Fronte opposto italiano**: **AmCham Italy** firmataria nel maggio 2024 della dichiarazione per adottare
  l'EUCS **senza** sovranità.
- ✅ **Risolve il dubbio di A6**: **Aruba S.p.A. è firmataria certa** della lettera del **10 aprile 2024**
  con TIM (fonte Reuters). ⚠️ È una lettera **diversa** da quella del 10 giugno 2024 di eucshighplus.eu:
  per quest'ultima l'ambiguità «Aruba / arubanetworks» **resta valida**.

> **🎯 LA TESI CORRETTA, ed è più forte di quella sbagliata:**
> Il divario non è fra l'Italia e le sue parole. È **fra ciò che l'Italia ha chiesto a Bruxelles e ciò che
> ha scritto in casa propria**. Per cinque anni ha premuto per la clausola di immunità a livello europeo e
> ha perso. Negli stessi anni **non l'ha mai introdotta nel proprio schema nazionale** — l'unico strumento
> che non dipendeva dal voto di nessun altro. E ora, con il CADA, la decisione torna agli Stati membri via
> valutazione di rischio (art. 29): **quella valutazione non è ancora stata fatta.**

⚠️ **Coalizione dei dodici (dic. 2023)**: **l'elenco non esiste in fonte pubblica**. L'EUISS cita «twelve
Member States» senza nominarne alcuno tranne i Paesi Bassi. **L'esclusione dell'Italia è una deduzione
solida, non un fatto accertato** — va detto così in onda.

**Non pubblici**: il non-paper 2021, i verbali ECCG, le istruzioni di posizione ad ACN, l'elenco dei dodici.
**Due strade a maggior rendimento**: (1) **accesso agli atti al Consiglio** (Reg. 1049/2001) per il non-paper
DE/ES/FR/IT; (2) la **relazione del Governo ex art. 6 l. 234/2012** su COM(2026) 502 — atto parlamentare
pubblico che contiene la posizione negoziale italiana.

### A16. 🎯 Zero fornitori cloud europei sono autorizzati FedRAMP ✅ *(era C9, risolto)*
Verificato direttamente sull'elenco pubblico del FedRAMP Marketplace (`marketplace.fedramp.gov`,
endpoint dati `/marketplace/products/__data.json`, **684 prodotti**, 511 certificati — letto il 29/07/2026).

**Ricerca per nome — tutti ASSENTI:**
`OVHcloud` · `IONOS` · `Deutsche Telekom` / `T-Systems` · `Scaleway` · `Hetzner` · `Exoscale` ·
`Stackit` · `CloudFerro` · `Cloud Temple` · `Oodrive` · `Docaposte` · `Outscale` · `Aruba S.p.A.` ·
`Orange Business` · `Telefónica` · `Capgemini` · `Sopra Steria` · `Bleu` · `S3NS` · `Infomaniak` ·
`Nextcloud` · `Proton`

**I gruppi europei presenti ci sono tutti tramite una società statunitense costituita apposta:**
- **SAP** → *SAP National Security Services Inc. (SAP NS2)*
- **Siemens** → *Siemens Government Technologies* (che veicola anche *Mendix Cloud for Government*)
- **Software AG** → *Software AG Government Solutions*
- **Darktrace** (UK) → *Darktrace Federal Inc.*
- **Ericsson** (SE) → *Ericsson – NetCloud Federal*

> **Per vendere al governo americano un europeo deve prima diventare americano.
> È esattamente ciò che l'Europa non chiede agli americani.**

⚠️ **Falsi positivi da non ripetere**: la ricerca testuale grezza segnala «Atos» dentro *Kratos* ed
«Eviden» dentro *evidence*. **Nessuno dei due è presente.** E le occorrenze di «Aruba» sono
**Aruba Networks (HPE, statunitense)**, non Aruba S.p.A. — conferma l'avvertenza di A6.

### A17. Le scuole: il dato ce l'abbiamo già, ed è il peggiore del dataset ✅ *(era C10, non serve FOIA)*
Dai dati dell'Osservatorio, il cluster **Istruzione** è quello con la **quota extra-UE più alta di tutta
la Pubblica Amministrazione italiana**:

| Cluster | Enti | Quota extra-UE | Provider dominante |
|---|---|---|---|
| **Istruzione** | **8.403** | **77,7%** | **Google Workspace** |
| PA Centrale | 52 | 63,5% | Microsoft 365 |
| Sanità | 234 | 59,4% | Microsoft 365 |

**8.403 istituti = il 37% di tutti gli enti misurati.** È il cluster più grande, ed è quello messo peggio.

⚠️ **Precisione obbligatoria**: il dato misura il **dominio di posta istituzionale** degli istituti
registrati in IndicePA. È prova diretta della piattaforma adottata dalla scuola, **non** una misura di
quanti studenti usino quotidianamente un applicativo. Il FOIA al Ministero **non serve più**.

### A18. Come funziona davvero il protezionismo americano — non per divieto, ma per stratificazione
Censiti **25 strumenti**: **7 mordono direttamente sul cloud, 5 indirettamente, 13 no.** Il conteggio onesto
rende la mappa incontestabile.

**Ciò che NON regge (e va detto noi per primi):**
- **FAR 25.103(e)** — esenzione espressa per l'IT commerciale (base: §535(a) Consolidated Appropriations
  Act 2004). Il Buy American Act **non** blocca il software europeo.
- **15 CFR §7.4** — la lista dei *foreign adversaries* è **tassativa**: Cina, Cuba, Iran, Corea del Nord,
  Russia, regime Maduro. Le regole ICTS **non si applicano agli europei**.
- 🚨 **41 U.S.C. §1323 contiene un divieto espresso**: «*Nothing in this section shall be construed… to
  authorize the issuance of an exclusion or removal order **based solely on the fact of foreign
  ownership**.*» **È il contro-argomento più forte contro la nostra tesi: va citato per primo.**
  Non la distrugge — la costringe a essere precisa.

**Ciò che regge, ed è il meccanismo vero:**
- **32 CFR §117.11(d)** (FOCI) — *Voting Trust* e *Proxy Agreement* impongono alla capogruppo estera di
  **cedere l'esercizio del controllo societario a cittadini statunitensi con nulla osta**. È il cuore.
  *(SAP NS2 come applicazione concreta: la qualificazione «Proxy Agreement» viene da fonti secondarie,
  perché gli accordi FOCI non sono pubblici — MEDIA.)*
- **DFARS 252.239-7010(b)(3)** (gen. 2023) — dati governativi da mantenere negli Stati Uniti.
- **DoD Cloud SRG** — *US persons* per IL4/IL5, cittadinanza + clearance SECRET per IL6.
  ⚠️ **La riga più importante è anche la meno documentata**: confermata da cinque fonti indipendenti ma
  **il PDF originale non è mai stato letto**. È il primo documento da aprire a mano.
- **CMMC** (DFARS 252.204-7021, efficace 10/11/2025) — estende i requisiti cloud all'intera filiera privata
  della difesa: sposta la barriera dal cliente pubblico ai fornitori.

**⚠️ DUE CORREZIONI CHE CAMBIANO LA SCENEGGIATURA:**
1. **La barriera FedRAMP NON è il costo: è la *sponsorship* di agenzia.** FedRAMP 20x sta abbassando costi
   e tempi **di proposito** (Fase 3 nel Q3-Q4 2026). **Se il documentario poggia sul costo, è smentito entro
   un anno.** Sponsorship, cittadinanza e controllo societario invece non si abbassano.
   *(Nota: la base legale FedRAMP, 44 U.S.C. §§3607-3616, ha una sunset al 23 dicembre 2027.)*
2. **Nel 2025-2026 gli USA NON hanno introdotto alcuna restrizione verso i fornitori europei.** Anzi: EO
   14275 e il *Revolutionary FAR Overhaul* vanno in direzione **deregolatoria**, e l'*America First
   Investment Policy* (21/02/2025) **favorisce** gli investitori alleati. Le novità restrittive riguardano
   la Cina. **Va detto in voce**: gli Stati Uniti non hanno chiuso agli europei perché non ne hanno
   bisogno — l'effetto è già prodotto dallo strato costruito fra il 2011 e il 2019.

⚠️ **Limiti**: `ecfr.gov` e `federalregister.gov` reindirizzano (302) e non sono stati leggibili;
`uscode.house.gov` irraggiungibile. Ripiego su Cornell LII e govinfo XML, con le righe interessate
degradate a MEDIA. 20 URL da aprire a mano elencati nel dossier 11.

### A19. 🎬 LE QUATTRO VOCI AL SENATO FRANCESE — sei anni, tre aziende, un solo «no»
La segnalazione «anche AWS e Google risposero» era **vera**, ma riferita a **un'altra commissione**.
Entrambe le cose stanno in piedi:

- **Commissione 2025** (rapporto n° 830): il dossier 02 aveva ragione. Tomo I integrale scaricato ed
  estratte le tre liste ufficiali: la `LISTE DES CONTRIBUTIONS ÉCRITES` contiene **solo Microsoft France**
  fra gli hyperscaler. AWS e Google non compaiono né lì né fra le persone audite.
- **Commissione 2019** — *commission d'enquête sur la souveraineté numérique*, rapporto n° 7 (2019-2020):
  **tutti e tre furono auditi sotto giuramento.**
  - **Google France** (Benoît Tabaka) — 17 luglio 2019
  - **Microsoft** (Marc Mossé, Mathieu Coulaud) — 18 luglio 2019
  - **AWS France** (Julien Groues, DG; Stéphan Hadinger, CTO) — **3 settembre 2019**, 16h15-16h50

La domanda del presidente Montaugé ad AWS era **più ampia** di quella del 2025, perché nominava le
controllate: «*Pouvez-vous nous assurer qu'Amazon, **ou ses filiales**, ne permet pas et ne permettra pas
aux autorités américaines de prendre connaissance des données de nos concitoyens…?*»

**Nessuno dei tre rispose sì o no.** AWS smontò «i miti» sul CLOUD Act e concluse «*nous appliquons la
loi*». Google affermò che «*ces dispositions ne sont pas entrées en vigueur, en l'absence de conclusion des
accords bilatéraux*». ⚠️ **CORREZIONE (v. A27)**: qui era stato scritto «giuridicamente scorretto» in modo
troppo netto. La verifica sul verbatim ampio mostra che **il dubbio resta**: non è falsa testimonianza.

> 🎯 **Il «No, je ne peux pas le garantir» di Carniaux (10 giugno 2025) è il primo «no» esplicito in sei
> anni.** Il dossier 12 contiene il verbatim integrale delle quattro voci con traduzione e un **blocco di
> montaggio a quattro voci**: è materiale da mandare in onda affiancato.

### A20. 🔥 Il CTO di AWS ha enunciato lui stesso, sotto giuramento, la dottrina che oggi lo smentisce
**3 settembre 2019**, Stéphan Hadinger, CTO di AWS France, davanti al Senato francese:
«*une société non américaine sera aussi soumise au Cloud Act si elle a […] **une filiale ou des employés
sur le territoire américain***» — citando il DOJ (Richard Downing) per cui «*la plupart des grands
fournisseurs de cloud américains ou non américains étaient soumis à la juridiction des États-Unis*».

È **il principio che rende non immune l'AWS European Sovereign Cloud**, enunciato da AWS stessa.

### A21. Nitro: cosa dice davvero l'audit — e cosa esclude
Rapporto **NCC Group** letto per intero. Quattro limiti dichiarati dall'auditor stesso:
1. È **pagato da AWS**;
2. è una ***design review* senza test**: l'auditor dichiara di non poter attestare che l'implementazione
   corrisponda al progetto;
3. mette **fuori perimetro** il piano di controllo EC2, l'hypervisor, il firmware e le Nitro Card;
4. 🎯 riga decisiva: fornisce «*no assurance with regards to any future chosen or **compelled** technical
   changes*» — l'auditor **esclude espressamente** la garanzia contro modifiche tecniche **imposte**.
   Che è esattamente lo scenario CLOUD Act.

Contrappeso indipendente, non pagato da AWS — **Trail of Bits**: «*you must completely trust AWS*».

### A22. Il test giuridico, risolto su fonte primaria DOJ
Scaricato il **white paper DOJ 2019** (dava 403 nel dossier 01, oggi risponde 200). La **FAQ n° 25** pone
letteralmente la nostra domanda e risponde: «*The analysis remains the same **regardless of corporate
structure** […] Whether a company exercises sufficient control over data held by a subsidiary is a
**fact-dependent inquiry***.»

**Verdetto sulla tesi Amazon: regge nella sostanza, ma va corretta in due punti.**
- ❌ Dire «è una controllata, **quindi** soggetta al CLOUD Act» è **troppo netto**: il DOJ dice
  *fact-dependent*, e **non è stata trovata né letta alcuna sentenza** che applichi il §2713 a una
  controllata estera con personalità giuridica distinta.
- ✅ La **difesa crittografica di AWS** (chiavi in *external key store*) è **tecnicamente valida per il
  dato a riposo** e va riconosciuta.
- ⚖️ **AWS non ha mai preteso di essere immune** dal CLOUD Act. L'equivoco è **commerciale**, e sta tutto
  nella parola «sovereign».

⚠️ **Lacune**: catena di controllo azionaria **non letta su visura** (handelsregister.de a pagamento);
**nessuna giurisprudenza letta**. 14 URL primari da aprire a mano nel dossier 12.

### A23. ⚡ UN VETTORE NUOVO: non l'accesso ai dati, ma la REVOCA del servizio e dell'identità
Distinto dal CLOUD Act e da tenere separato in tutto il racconto. Qui non si tratta di **leggere** i dati,
ma di **spegnere** l'accesso di una persona ai propri strumenti digitali.

**Il fondamento è nel testo presidenziale.** EO 14203 §3, letto verbatim: vieta «*the provision of funds,
goods, or **services***» a un soggetto designato. La parola «servizi» è nell'ordine esecutivo: non serve
interpretazione.

**E le aziende lo hanno messo per iscritto.** Facebook, 28 dicembre 2017 (caso Kadyrov): «*Facebook has a
**legal obligation** to disable these accounts.*» Ammissione scritta dell'obbligo, con otto anni d'anticipo.
**Microsoft è già stata multata** (~3,3 M$, aprile 2023, OFAC+BIS) per aver fornito servizi a *blocked
persons*: non un'azienda che sceglie, ma **una recidiva sotto vigilanza**.

### A24. 🎯 I DUE CASI SOLIDI SONO CITTADINI EUROPEI — e non sono quelli che si citano di solito
🚨 **Il caso Karim Khan è il PIÙ FRAGILE del dossier, non il più forte.** La fonte è AP (Molly Quell,
15 maggio 2025): «*Microsoft, for example, cancelled Khan's email address… **ICC staffers said***» —
funzionari **anonimi**, nessun documento. Brad Smith ha smentito il 4 giugno 2025. **Ma la smentita nega
la cessazione dei servizi alla Corte come organizzazione, non la disconnessione dell'account individuale:
le due affermazioni possono essere entrambe vere.** Da maneggiare con estrema cautela.

**I due casi incontestabili:**

1. **Beti Hohler**, giudice slovena — marzo 2026, verbatim:
   > «*My Apple ID, iCloud, Amazon, Airbnb, PayPal, and other accounts have all been blocked or cancelled.
   > **These cancellations happened overnight without advance warning.***»
   **Nessuna azienda l'ha mai contestato.**
2. **Nicolas Guillou**, giudice francese — documentato in un **atto parlamentare francese** (interrogazione
   11576 Lachaud, 9 dicembre 2025) **con risposta ufficiale del Governo** del 10 febbraio 2026, in cui la
   Francia si dichiara «*favorable à l'activation du règlement de blocage*».
   **È la migliore fonte documentale dell'intero dossier.**

### A25. L'asimmetria fra denaro e dati — è il fatto analitico più forte
Per i **fondi** bloccati la legge americana prescrive conto fruttifero, interessi, *audit trail* e
restituzione in caso di delisting. Per i **dati**: **nulla**. Nessuna regola su conservazione,
esportabilità o restituzione. **L'assenza di disciplina è essa stessa il risultato.**

E il **Regolamento di blocco UE non è stato attivato** a 17 mesi dall'EO, nonostante due risoluzioni del
Parlamento europeo (9 luglio e 11 settembre 2025) e la richiesta di Spagna, Slovenia e Francia.

**Italia**: esistono designati reali (23 agosto 2024, EO 14024 — Fagima Fresatrici S.p.A., Idronaut S.r.l.
e quattro persone fisiche), ma **nessun effetto digitale documentato**. ⚠️ **Il rischio per un ente
pubblico italiano è dichiarato TEORICO**: va detto così.

### A26. ⚠️ SEI CORREZIONI — casi che circolano e che NON reggono
1. **Bensouda (2020) non perse servizi digitali**, solo bancari. **Il precedente digitale del 2020 non esiste.**
2. **A Moraes non è stato tolto Gmail**: la stampa brasiliana descriveva ipotesi. Ed è stato **delistato il
   12 dicembre 2025**.
3. **L'interruzione Microsoft in Russia (2024) ha base giuridica EUROPEA, non americana.** Usarla come prova
   del potere USA è **smentibile in dieci secondi**.
4. **Huawei è Entity List/BIS**, non OFAC/IEEPA: strumenti diversi, non cumulabili nel racconto.
5. **X/Starlink 2024 è il fenomeno OPPOSTO** — uno Stato che interdice un'azienda. Citarlo come conferma
   **dimostra la tesi della controparte**.
6. **L'impegno Microsoft del 30 aprile 2025** copre gli ordini di sospendere le «*cloud operations in
   Europe*» e **non menziona mai le sanzioni individuali**: copre lo scenario mai accaduto, non quello
   già accaduto tre volte.

🔴 **DA VERIFICARE A MANO, priorità 1**: nel **febbraio 2026 Microsoft si sarebbe scusata con la *Business
and Trade Committee* dei Comuni**, chiedendo la correzione del verbale dopo che un dirigente aveva
attribuito alla CPI — «*not Microsoft*» — la disattivazione della posta di Khan. Riportato in modo
concorde ma **la fonte non è stata aperta** (The Register blocca i bot): **serve il verbale parlamentare
originale**. La voce sulla presunta minaccia di Microsoft alla Corte è marcata DA VERIFICARE: **se la
fonte primaria olandese non si trova, quel punto va eliminato dal film.**
Bloccati anche `federalregister.gov` ed `ecfr.gov`: 31 CFR Part 528 e la **General License D-2** non letti
in originale — la clausola di esclusione dei *blocked persons* nella D-2 dirime il contro-argomento
«esistono licenze per i servizi essenziali». 25 URL da aprire a mano nel dossier 13.

### A27. Il caso Tabaka risolto: imprecisione con effetto fuorviante, **non** falsa testimonianza
Letti integralmente il resoconto ufficiale della commissione 2019 (189.384 caratteri) e il **rapporto n° 7
tomo I** (570.803 caratteri). Tre reperti:

1. **La domanda riguardava inequivocabilmente il §2713.** Il presidente Montaugé lo definisce lui stesso:
   «*le Cloud Act permet aux autorités américaines de disposer des données que vous stockez, **quel que soit
   le lieu de stockage***». Non nomina mai gli accordi bilaterali. Nomina invece **Airbus Defence and Space
   e Atos** come clienti a rischio.
2. **Il verbatim ampio consente due letture.** L'antecedente grammaticale di «*ces dispositions*» è la frase
   precedente sulla relazione bilaterale — quindi **l'ipotesi della definizione ristretta regge**, ed è la
   stessa che Google metterà per iscritto nel white paper 2022 (v. A28). **Ma una frase resta irriducibile**:
   «*quand bien même le Cloud Act entrerait en vigueur et obligerait Google à communiquer les données de ses
   clients*». **Il dubbio resta, e va dichiarato.**
3. **La smentita migliore è del Senato stesso, e non accusa nessuno.** «Tabaka» ricorre **0 volte** nel
   rapporto finale. Ma il riquadro didascalico sul CLOUD Act scrive: «*Il vise principalement à réaffirmer
   le droit […] la communication de toutes données stockées, même à l'étranger. **Il prévoit aussi, et
   indépendamment**, la conclusion d'accords bilatéraux*». **La parola «indépendamment» è del Senato francese.**

**PRIORITÀ 1**: ascoltare il **video ufficiale del 17/07/2019** — il *compte rendu* è rivisto, non stenografico.
**Bonus (nota 180 del rapporto)**: sei giorni prima, **OVH** rispose alla stessa domanda — ed è l'unica
risposta **strutturale** anziché procedurale. Il contrasto è materiale da montaggio.

### A28. Google smonta il mito della geografia — per iscritto, in un proprio documento
**Google Cloud Whitepaper, «Government Requests for Cloud Customer Data», febbraio 2022**, pag. 5, verbatim:
> «*the CLOUD Act clarifies that the U.S. government can compel production of data where the data is under
> the "possession, custody, or control" of a provider subject to US jurisdiction, **regardless of where that
> data is physically stored**. In other words, **data localization requirements do not impact whether a
> cloud provider may have to disclose data** in response to a government request.*»

E ammette la coercibilità: offre cifratura che tiene i dati illeggibili «*even if Google is compelled to
turn over the data*». **La difesa è tecnica, non giuridica.**
Pag. 6: definisce «CLOUD Act request» **in senso stretto** (solo accordi bilaterali con governi stranieri
qualificati), escludendo espressamente le «*U.S. request*» sui poteri preesistenti — cioè proprio il
meccanismo che conta. È la chiave di lettura di A27.
La procedura in quattro passi è tutta condizionata da «*unless prohibited by law*»: **stesso schema e stesso
limite della clausola italiana PR.DS-01** (A7).

### A29. Google, la FISA 702 e la scuola italiana
**Google ammette la FISA 702 in un documento destinato alle scuole** — white paper *Workspace for
Education*, agosto 2021: «*To the extent Google LLC may receive targeted requests […] under Downstream 702,
we **carefully review** each request*». **Non dice che rifiuterebbe.**

**Nessuna audizione di Google in un parlamento europeo dopo il 2019** (verificato sulle liste ufficiali 2025).

**S3NS**: qualificazione ANSSI del **17 dicembre 2025** — prima volta IaaS+PaaS+CaaS insieme (non «30
servizi»: correggere il dossier 08). S3NS oggi si dichiara «*fully owned by Thales*» mentre nel 2022 si
parlava di Google in minoranza: **forchetta 0%-24% da chiudere**. Non intacca la tesi, perché SecNumCloud
§19.6 fissa il tetto proprio al 24%.

> **LA TENSIONE, ed è l'argomento più forte del film a favore della regolazione.**
> Google ha **la posizione dichiarativa più debole** e **il rimedio strutturale più avanzato**.
> La spiegazione non è ipocrisia: **S3NS esiste perché la Francia ha scritto il §19.6.**
> Un fatto scomodo per noi diventa la prova che **la regola funziona**.

**Scuola** — esiti effettivi, tutti diversi: **Danimarca** ordine ai 53 comuni (non sanzione a Google) ·
**Paesi Bassi** adeguamento (**è il contro-argomento più forte di Google**) · **Germania** cautelare chiuso
da transazione (OVG NRW 19 B 417/22) · **Italia: nessun provvedimento, a fronte di 8.403 istituti.**
E **nemmeno Google pubblica dati di diffusione in Italia**: la misurazione dell'Osservatorio resta
**l'unica fonte esistente**.

---

## 🟡 B — SOLIDO, DA CONFERMARE PRIMA DELLA MESSA IN ONDA

### B1. La dichiarazione di Butti del 21 luglio 2026
75% raggiunto · oltre 13.000 PA · 1,9 miliardi PNRR · oltre 280 PA centrali/ASL su PSN · oltre 12.700 PA
locali **e scuole** su «cloud qualificati» · oltre 135.000 servizi.
Verbatim: «Con questo risultato **l'Italia si pone tra i Paesi europei più avanzati nella protezione dei
dati della pubblica amministrazione**.»
**Non usa mai l'espressione «sovranità digitale»**: parla di sicurezza e protezione dei dati.
🔗 https://www.key4biz.it/pnrr-butti-oltre-13mila-pa-in-cloud-75-centrati-obiettivi-ue/581879/
✅ **DECISO — si procede sul lancio d'agenzia.** Rischio residuo messo a verbale: la fonte è Adnkronos,
non l'atto originale del Dipartimento. Il virgolettato è stato ripreso in pari data da più testate in modo
concorde, quindi la citazione è solida; ma **in trasmissione va attribuita all'agenzia**, non presentata
come comunicato ufficiale. Se il comunicato primario emergesse, si aggiorna l'attribuzione.

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

## ⚫ D — CONTRADDIZIONI ✅ RISOLTE

### D1. Stato reale dei livelli EUCS (🔴 bloccante)
- **EUISS** (dossier 04): i requisiti di sovranità furono **rimossi** il 22/03/2024.
- **sota.io** (2026): il livello **High** *include* proprietà europea, personale UE per accessi privilegiati
  e giurisdizione esclusivamente UE; i fornitori con capogruppo USA **non** possono qualificarsi.
Non possono essere entrambe vere.
🚨 **sota.io è un fornitore commerciale che elenca sé stesso tra i qualificabili**: conflitto d'interesse.
🔗 https://sota.io/blog/eucs-cloud-assurance-levels-which-providers-qualify-eu-sovereignty-2026
🔗 **Fonte da consultare per dirimere**: https://www.enisa.europa.eu/ (schema EUCS)
✅ **RISOLTA — vedi A14: ha ragione EUISS. L'EUCS non è ancora stato adottato e nessun livello contiene requisiti di sovranità.** La pagina sota.io, riletta, oggi afferma essa stessa l'opposto di quanto le era stato attribuito.

---

## 🔴 C — APERTO: NON UTILIZZABILE FINCHÉ NON VERIFICATO

| # | Domanda aperta | Perché è importante | Dove cercare |
|---|---|---|---|
| ~~C1~~ | ~~Il Regolamento ACN contiene una clausola di immunità?~~ | ✅ **RISOLTO — vedi A7. Risposta: NO**, verificato sul testo integrale | — |
| ~~C2~~ | ~~Come si è espressa l'Italia in sede ECCG?~~ | ✅ **RISOLTO — vedi A15. Ha co-scritto i criteri di immunità e ha perso** | — |
| ~~C3~~ | ~~Quanto denaro PNRR è finito a fornitori USA?~~ | ✅ **RISOLTO — vedi A9. Non è tracciabile, e l'assenza è documentata** | — |
| ~~C4~~ | ~~Quanti servizi qualificati ACN poggiano su tecnologia USA?~~ | ✅ **RISOLTO — vedi A10.** Catalogo analizzato: 2.107 schede, 826 fornitori | — |
| ~~C5~~ | ~~Esito causa Fastweb/Aruba~~ | 🗂️ **Vicenda esclusa dal film** (irregolarità negli appalti, non sovranità; l'offerta Aruba-Fastweb non è dimostrabilmente più sovrana). Resta nel dossier | — |
| ~~C6~~ | ~~Tenuta del Data Privacy Framework?~~ | ✅ **RISOLTO — vedi A12. Il DPF non copre il CLOUD Act e lo dice per iscritto** | — |
| ~~C7~~ | ~~Asimmetria USA/Cina/UE e scuola~~ | ✅ **RISOLTO — vedi A13, con tre assunti di partenza CORRETTI** | — |
| ~~C9~~ | ~~Fornitori cloud europei autorizzati FedRAMP?~~ | ✅ **RISOLTO — vedi A16. Zero.** | — |
| ~~C10~~ | ~~Dati delle scuole italiane?~~ | ✅ **RISOLTO — vedi A17. Istruzione 77,7%, il peggiore del dataset** | — |
| **C8** | **Aruba S.p.A.** è tra i firmatari EUCS High+? | Il link nell'elenco punta a HPE Aruba Networks | ✅ **parzialmente risolto in A15**: è firmataria certa della lettera del 10/04/2024; per quella del 10/06/2024 l'ambiguità resta |
| **C11** | Testo originale del **DoD Cloud SRG** | È la riga più importante del blocco asimmetria e non è mai stata letta in originale | PDF su `dl.dod.cyber.mil` — apertura manuale |
| **C12** | **Comune italiano** con videosorveglianza (o AI di riconoscimento) su AWS/Google/Microsoft | Servirebbe per il filone «Trump vede anche chi passa per strada». ⚠️ **Attenzione**: in Italia vige una moratoria sul riconoscimento facciale in luoghi pubblici — da verificare stato e portata prima di impostare la narrativa | Delibere comunali, bandi, provvedimenti del Garante |

*(Risolti: C1 → A7 · C2 → A15 · C3 → A9 · C4 → A10 · C6 → A12 · C7 → A13. Restano C5, C8, C9, C10 — tutte verifiche manuali su fonti non automatizzabili.)*

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
11. **Non dire «il Buy American Act esclude il software europeo»**: la FAR 25.103(e) esenta l'IT commerciale
    e il BAA non copre i servizi. È l'errore che ci farebbe smontare più in fretta di tutti.
12. **Non dire «FedRAMP impone la cittadinanza americana»**: l'obbligo FOCI riguarda gli **auditor 3PAO**,
    non i fornitori cloud. Il divieto su cittadinanza esiste solo nel DoD Cloud SRG, cioè solo per la Difesa.
13. **Non citare il «Documento 79» cinese come ordine di rimuovere il software straniero**: la versione
    pubblica tradotta da CSET non lo dice. Usare invece la lista MIIT/CISEC del 26 dicembre 2023.
14. **Non omettere l'avanzo di 60,4 mld € sui servizi informatici** quando si cita il disavanzo di 126,3 mld
    sui canoni IP: ometterlo è manipolatorio, e la contro-parte lo sa.
15. **Non dire che l'Assia ha vietato Microsoft nelle scuole**: quel divieto fu ritirato dopo tre settimane.
    Il caso solido è il **Baden-Württemberg**.
16. **🔴 LA PIÙ IMPORTANTE — non dire «l'Italia non ha chiesto la sovranità»**: è falso. L'ha **co-scritta**
    nel 2021 con Francia, Germania e Spagna, non ha firmato il non-paper contrario nel 2022, e nell'aprile
    2024 il Sottosegretario ha pubblicamente contestato la rimozione. Il divario vero è **fra ciò che
    l'Italia ha chiesto a Bruxelles e ciò che ha scritto in casa propria**. Chi ha seguito il dossier lo sa,
    e la formulazione sbagliata ci farebbe passare per disinformati.
17. **Non affermare che l'Italia era tra i dodici Stati che chiesero la rimozione**: quell'elenco **non
    esiste in fonte pubblica**. È una deduzione, e va detta come tale.
18. **Non dire «è una controllata europea, quindi è soggetta al CLOUD Act»**: il DOJ qualifica la
    questione come *fact-dependent* e non esiste giurisprudenza nota che lo affermi. La formulazione
    corretta è che **la struttura societaria non muta di per sé l'analisi** — lo dice il DOJ — e che
    **AWS non ha mai sostenuto di essere immune**. L'equivoco sta nella parola «sovereign».
19. **Riconoscere che la cifratura con chiavi esterne di AWS è una difesa tecnicamente valida** per il
    dato a riposo. Negarlo ci fa perdere il contraddittorio su un punto in cui hanno ragione.
20. **VIETATO dire «Google ha mentito»** sull'audizione del 2019: il verbatim consente due letture e il
    dubbio resta. Formulazione corretta: **«Google usa una definizione di CLOUD Act che esclude proprio il
    meccanismo che conta»** — e la smentita si fa citando **il Senato francese**, che scrive «*et
    indépendamment*» senza accusare nessuno.
21. **Non dire che la Danimarca «ha vietato Google nelle scuole»**: l'autorità ha ordinato ai **53 comuni**
    di adeguarsi, non ha sanzionato Google.
22. **Non dire che la Germania ha vietato Google/Microsoft nelle scuole**: il procedimento OVG NRW era
    **cautelare** e si è chiuso con una **transazione**.
23. **Citare l'esito olandese anche se ci contraddice**: nei Paesi Bassi si è arrivati a un **adeguamento**,
    non a un divieto. È il contro-argomento più forte di Google e va anticipato.
24. **Non dire che l'EUCS «sta per essere adottato»**: al giugno 2026 la Commissione stessa scrive che
    «*non è ancora stato adottato*». Zero certificati emessi.
