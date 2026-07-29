# DD ACN 21007/24 — analisi del TESTO PRIMARIO
## Esiste un requisito di immunità dalle leggi extraterritoriali e/o di controllo europeo del capitale?

**Data ricerca:** 29 luglio 2026
**Metodo:** download del PDF ufficiale da acn.gov.it, estrazione integrale del testo con `pypdf`, scansione lessicale esaustiva su tutte le 88 pagine (Regolamento + Allegati 1, 2, 3, 4), lettura integrale delle sezioni rilevanti.

---

## 0. Documento primario effettivamente letto

| Elemento | Valore |
|---|---|
| Titolo | *Regolamento per le infrastrutture digitali e per i servizi cloud per le pubbliche amministrazioni*, ai sensi dell'art. 33-septies, c. 4, DL 179/2012 |
| Atto di adozione | Decreto Direttoriale ACN n. 21007/24 del 27 giugno 2024 |
| File | `RegolamentoCloud.pdf` — PDF v1.7, **88 pagine**, 951.036 byte |
| URL | https://www.acn.gov.it/portale/documents/20119/111690/RegolamentoCloud.pdf/aa9b66a5-8c91-18de-d619-68f5c0c62e99?t=1719580455774 |
| Pagina indice | https://www.acn.gov.it/portale/cloud/documentazione-utile |
| Contenuto | Articolato (27 articoli, pp. 1–26) + **Allegato 1** (classificazione dati/servizi) + **Allegato 2** (livelli minimi infrastrutture, 30 pp.) + **Allegato 3** (caratteristiche di base servizi cloud, 27 pp.) + **Allegato 4** (requisiti adeguamento e qualificazione AC/QC 1-4 e AI 1-4, 8 pp.) |

**Nota metodologica decisiva:** tutti e quattro gli allegati sono contenuti nello STESSO file PDF. Non esistono allegati separati non letti. La scansione lessicale sotto riportata copre quindi il 100% del testo normativo primario.

### Scansione lessicale esaustiva (occorrenze su 326.143 caratteri = testo integrale)

| Termine cercato | Occorrenze |
|---|---|
| `extraterrit*` (extraterritoriale/extraterritorialità) | **0** |
| `CLOUD Act` / `Cloud Act` | **0** |
| `nazionalità` | **0** |
| `sede legale` | **0** |
| `capogruppo` | **0** |
| `controllo societario` | **0** |
| `assetto proprietario` | **0** |
| `capitale` (sociale) | **0** |
| `azionar*` / `partecipazion*` | **0** |
| `paesi terzi` / `paese terzo` | **0** |
| `sovranità` | **0** |
| `immunità` | **0** |
| `cittadinanza` | **0** |
| `golden power` / `antimafia` | **0** |
| `PSN` / `Polo Strategico Nazionale` | **0** |
| `giurisdizion*` | 2 (entrambe = "autorità giurisdizionali legali" nel contesto contatti con forze dell'ordine, RS.CO-05) |
| `extra-UE` | **4** (tutte in PR.DS-01, All. 2 e All. 3 — vedi §3) |
| `localizzazione` | 8 |
| `chiavi` | 21 |

---

## 1. RISPOSTA SINTETICA

**NO.** Il Regolamento ACN 21007/24, letto integralmente in tutte le sue 88 pagine, **non contiene alcun requisito di immunità dalle legislazioni extraterritoriali extra-UE, né alcun requisito sulla nazionalità, sulla sede legale o sul controllo del capitale del fornitore o della sua capogruppo, a nessuno dei quattro livelli di qualificazione (QC1, QC2, QC3, QC4), né per i dati "strategici".**

L'unica misura che tocca il tema è una clausola **procedurale di notifica e autorizzazione** (PR.DS-01, requisito `_S`, applicabile solo ai dati strategici), che presuppone la legittimità dell'accesso extra-UE e lo subordina all'autorizzazione dell'amministrazione — l'esatto opposto di un divieto strutturale.

---

## 2. TABELLA AFFERMAZIONE | CITAZIONE | FONTE | AFFIDABILITÀ

### 2.1 — Requisiti su nazionalità / sede legale del fornitore o della capogruppo

| Campo | Contenuto |
|---|---|
| **AFFERMAZIONE** | **NON ESISTONO.** Nessun requisito di nazionalità o di sede legale del fornitore o della sua controllante, a nessun livello. |
| **DOVE AVREI DOVUTO TROVARLO** | Allegato 4 — le sezioni che elencano i requisiti di qualificazione: §2 (QC1), §3 (QC2), §4 (QC3), §5 (QC4). È l'unico luogo del Regolamento dove si elencano i requisiti soggettivi del fornitore. |
| **COSA HO EFFETTIVAMENTE LETTO** | I requisiti soggettivi si esauriscono in **certificazioni tecniche**. QC1 (All. 4, §2.3): «*un'autocertificazione che attesti la conformità allo standard ISO 9001 […]; la certificazione ISO/IEC 27001 […] con estensioni ISO/IEC 27017 e ISO/IEC 27018 […]. In alternativa […] la certificazione Cloud Security Alliance – Star Level 2*». QC2 (§3.2): autocertificazioni ISO 22301 e ISO 20000. QC3 (§4.2): certificazioni ISO 22301, ISO/IEC 20000, CSA STAR Level 2. QC4 (§5.1): nessuna ulteriore certificazione, solo 5 requisiti tecnici (HYOK, HSM dedicato, autonomia operativa, vetting personale). |
| **UNICO RIFERIMENTO GEOGRAFICO PRESENTE** | Riguarda **l'ente certificatore, non il fornitore**: All. 4, §2.3 (e identico in §4.2, §6.1, §8.2): «*le certificazioni devono essere emesse da ente certificatore accreditato da un organismo nazionale di accreditamento di un paese membro dell'unione europea ovvero beneficiario di un accordo di mutuo riconoscimento con l'organismo nazionale di accreditamento italiano*». Nota: l'IAF MLA include gli USA (ANAB), quindi neppure questo esclude soggetti extra-UE. |
| **FONTE** | DD ACN 21007/24, Allegato 4 «Requisiti per l'adeguamento e la qualificazione…», pp. 81–88 del PDF. URL: come sopra. Data: 27/06/2024. |
| **AFFIDABILITÀ** | **ALTA** — testo primario letto integralmente; ricerca lessicale su 0 occorrenze di `nazionalità`, `sede legale`, `capogruppo`. |

### 2.2 — Requisiti su controllo societario / del capitale

| Campo | Contenuto |
|---|---|
| **AFFERMAZIONE** | **NON ESISTONO.** Zero occorrenze di `capitale`, `azionariato`, `partecipazioni`, `controllo societario`, `assetto proprietario` in tutto il documento. |
| **DOVE AVREI DOVUTO TROVARLO** | Allegato 4 §5.1 (requisiti QC4, il livello massimo) — l'unico punto dove ci si aspetterebbe un requisito di "sovranità". |
| **COSA HO EFFETTIVAMENTE LETTO** | Il requisito QC4 più vicino al tema è di natura **operativa, non proprietaria**: All. 4, §5.1, PR.DS-01, punto **21_SS**: «*Il fornitore dei servizi cloud è autonomo nella fornitura del servizio cloud, disponendo di proprie capacità per operare l'infrastruttura fisica e logica sottostante. Per casi eccezionali e sulla base di documentate limitazioni di carattere tecnico, il fornitore dei servizi cloud può avvalersi di competenze di terze parti, assicurandone, ove possibile, la fungibilità.*» — Si tratta di autonomia *tecnico-operativa*, non di autonomia *giuridica dal controllo estero*. Un hyperscaler statunitense soddisfa questo requisito senza difficoltà. |
| **UNICA MENZIONE DI "CONTROLLO" SOCIETARIO** | Art. 15, c. 1: «*I servizi cloud per le pubbliche amministrazioni erogati da un soggetto pubblico, da società in house, ovvero, per espressa previsione normativa, da società a controllo pubblico, come definite nel decreto legislativo 19 agosto 2016, n. 175, sono sottoposti al processo di adeguamento.*» — Questa norma **distingue la procedura** (adeguamento AC vs qualificazione QC) in base alla natura pubblica del soggetto, **non impone** che i fornitori privati siano a controllo europeo. Anzi, l'art. 17 c. 1 dedica esplicitamente ai «*fornitori dei servizi cloud diversi da quelli di cui all'articolo 15, comma 1*» — cioè i privati, senza alcuna limitazione di nazionalità — i quattro livelli QC1–QC4. |
| **FONTE** | DD ACN 21007/24, artt. 15 e 17; Allegato 4 §5.1 (p. 85 PDF). |
| **AFFIDABILITÀ** | **ALTA** |

### 2.3 — Clausole su leggi extraterritoriali / CLOUD Act / accesso di autorità straniere

| Campo | Contenuto |
|---|---|
| **AFFERMAZIONE** | **NON esiste alcun requisito di immunità.** Esiste UNA SOLA clausola sul tema, di natura procedurale (notifica + autorizzazione), applicabile **solo ai dati strategici** e formulata in modo da **presupporre e ammettere** l'accesso extra-UE. |
| **CITAZIONE TESTUALE (servizi cloud)** | Allegato 3, §4.1.4, PR.DS-01, punto **15_S**: «*Con riferimento all'accesso ai dati da parte di entità extra-UE, il soggetto: a. segnala all'Agenzia per la cybersicurezza nazionale (ACN) e all'amministrazione ogni richiesta di accesso a dati o metadati da parte di entità extra-UE; b. fornisce accesso a dati dell'Amministrazione o metadati ad entità extra-UE solo a valle di un'autorizzazione esplicita da parte dell'amministrazione.*» |
| **CITAZIONE TESTUALE (infrastrutture)** | Allegato 2, §4.2.7, PR.DS-01, punto **6_S**: formulazione identica, riferita all'operatore di infrastruttura digitale. |
| **LETTURA CRITICA** | (a) È collocata nella **sezione 4** dell'Allegato 3, che ai sensi dell'art. 8 c. 2 lett. c) si applica **solo ai dati "strategici"**. Per dati ordinari e critici la clausola **non esiste affatto**. (b) È un obbligo di **trasparenza ex post**, non un divieto: la norma disciplina *come* si dà accesso a un'entità extra-UE, ammettendo implicitamente che ciò avvenga. (c) Non menziona mai il CLOUD Act, il FISA §702, l'Executive Order 12333 né alcuna legislazione estera. (d) Nulla dice su cosa accada se il fornitore è **giuridicamente obbligato** da un ordine straniero corredato da *gag order* — l'ipotesi centrale del CLOUD Act — che rende materialmente ineseguibili sia la segnalazione all'ACN sia la richiesta di autorizzazione all'amministrazione. |
| **CONFRONTO CON L'UNICA ALTRA MENZIONE ATTINENTE** | Art. 22, c. 5 dell'articolato (disciplina GDPR): «*In caso di trasferimento di dati personali al di fuori dello Spazio economico europeo, i responsabili del trattamento […] sono tenuti ad attenersi alle istruzioni delle amministrazioni impartite ai sensi dell'articolo 28, paragrafo 3, lettera a), del regolamento (UE) 2016/679 e a mettere a disposizione delle stesse ogni informazione necessaria per valutare l'effettività delle misure appropriate poste in essere ai sensi del capo V del regolamento (UE) 2016/679.*» — È un mero rinvio al GDPR, non un requisito di qualificazione. |
| **FONTE** | DD ACN 21007/24, Allegato 3 p. 78 PDF (25 di 27); Allegato 2 p. 44 PDF (21 di 30); art. 22 c. 5. |
| **AFFIDABILITÀ** | **ALTA** |

### 2.4 — Requisiti su nazionalità / ubicazione del PERSONALE con accessi privilegiati

| Campo | Contenuto |
|---|---|
| **AFFERMAZIONE** | **NON ESISTE alcun requisito di nazionalità né di ubicazione del personale privilegiato.** Esiste solo un obbligo di **disclosure della metodologia di vetting** e dell'**elenco nominativo**, con diritto di veto dell'amministrazione — e solo al livello massimo QC4/AI4. |
| **CITAZIONE TESTUALE** | Allegato 4, §5.1 (QC4), PR.IP-11: «*1_SS. Il fornitore dei servizi cloud rende disponibile all'amministrazione la metodologia utilizzata per la verifica del personale (vetting process methodology) con accesso privilegiato al servizio cloud o ai dati dell'amministrazione. 2_SS. Il fornitore dei servizi cloud rende disponibile all'amministrazione l'elenco dei dipendenti con accesso privilegiato al servizio cloud o ai dati dell'amministrazione. L'amministrazione può richiedere unilateralmente la rimozione di uno o più dipendenti dal citato elenco e il fornitore dei servizi cloud provvede nel senso tempestivamente.*» (formulazione identica in §9.1 per le infrastrutture AI4, riferita all'«operatore di infrastrutture digitali») |
| **COSA MANCA** | Nessuna prescrizione che il personale con accesso privilegiato debba essere cittadino UE, risiedere nell'UE, o operare da territorio UE. Zero occorrenze di `cittadinanza`, `nulla osta`, `NOS`, `residenza` (in senso di requisito personale). Il vetting è **autodefinito dal fornitore**: l'ACN ne impone la trasparenza, non il contenuto. |
| **FONTE** | DD ACN 21007/24, Allegato 4 §5.1 (p. 86 PDF) e §9.1 (p. 88 PDF). |
| **AFFIDABILITÀ** | **ALTA** |

### 2.5 — Localizzazione dei dati

| Campo | Contenuto |
|---|---|
| **AFFERMAZIONE** | Esiste un requisito di localizzazione UE dei dati dell'amministrazione **già dal livello ordinario**, ma **con clausola di deroga generalizzata**. I metadata seguono un regime a tre gradini più permissivo. |
| **CITAZIONE (dati, livello ORDINARIO)** | Allegato 3, §2.4.7, PR.DS-01, **1_O**: «*I dati dell'amministrazione, ivi inclusi quelli deputati alla sicurezza (quali, a titolo esemplificativo, i sistemi di controllo degli accessi), sono trattati mediante infrastrutture localizzate sul territorio dell'Unione europea. **Salvo motivate e documentate ragioni di natura normativa o tecnica**, nelle citate infrastrutture sono ricomprese quelle deputate alle funzioni di: a. Business Continuity e Disaster Recovery, anche se esternalizzate […]; b. Content Delivery Network con distribuzione geografica globale.*» |
| **CITAZIONE (metadata, ORDINARIO)** | Ibid., **2_O**: «*Diversamente dal caso dei Metadata relativi al funzionamento del Servizio, che possono essere trattati mediante infrastrutture localizzate anche al di fuori del territorio dell'Unione europea, i Metadata relativi all'amministrazione sono trattati mediante infrastrutture localizzate sul territorio dell'Unione europea, **salvo motivate e documentate ragioni di natura normativa o tecnica**.*» E **3_O**: i metadata dell'amministrazione finalizzati a sicurezza informatica o resilienza «*possono essere trattati […] anche fuori del territorio europeo*». |
| **CITAZIONE (metadata, STRATEGICO)** | Allegato 3, §4.1.4, PR.DS-01, **17_S**: «*Nel caso di dati e di servizi strategici delle Amministrazioni, non trovano applicazione le previsioni del requisito di cui punto 2_O. Al riguardo, tutte le tipologie di metadata devono essere trattate mediante infrastrutture localizzate sul territorio dell'Unione europea, ad eccezione di quelli necessari all'erogazione dei servizi indicati al punto 1_O.*» |
| **TRASPARENZA SEDI** | All. 3, §4.1.4, **16_S** (solo strategici): «*Esiste un documento aggiornato che descrive da quali sedi e infrastrutture è erogato il servizio cloud. Il soggetto rende disponibile l'elenco all'amministrazione.*» |
| **LETTURA CRITICA** | La localizzazione UE è **territoriale, non giurisdizionale**. Un datacenter in Irlanda gestito da una controllata di una capogruppo USA soddisfa integralmente il requisito, pur restando nel perimetro soggettivo del CLOUD Act (che si applica *ratione personae* al provider, non *ratione loci* al dato). Il Regolamento non colma questo divario in nessun punto. |
| **FONTE** | DD ACN 21007/24, Allegato 3 pp. 62, 78 PDF; Allegato 2 pp. 43–44 PDF. |
| **AFFIDABILITÀ** | **ALTA** |

### 2.6 — Gestione delle CHIAVI crittografiche

| Campo | Contenuto |
|---|---|
| **AFFERMAZIONE** | Il regime delle chiavi è **graduato** e rappresenta il presidio tecnicamente più forte del Regolamento. Ma è un presidio **crittografico**, non giuridico, e il livello massimo (HYOK) è richiesto solo a QC4 — che non è obbligatorio per i dati strategici. |
| **ORDINARI (2_O ss.)** | All. 3, §2.4.7, PR.DS-01, **6_O**: «*Con riferimento alle chiavi crittografiche, **su richiesta dell'amministrazione**, il soggetto garantisce: a. la gestione autonoma da parte dell'amministrazione; b. la generazione di chiavi crittografiche segrete e private per uno scopo unico.*» (facoltativo, attivabile a richiesta) |
| **CRITICI** | All. 3, §3.2.7, PR.DS-01, **9_C**: «*Nel caso di dati e di servizi critici delle Amministrazioni, non trovano applicazione le previsioni del requisito di cui al punto 6_O. Con riferimento alle chiavi crittografiche, il soggetto **garantisce la gestione autonoma da parte dell'Amministrazione**…*» + **11_C**: «*Il servizio cloud supporta un meccanismo di cifratura di tipo **Bring Your Own Key (BYOK)**, che consente all'Amministrazione di generare autonomamente almeno la chiave principale di cifratura (root key), attraverso un HSM ospitato, alternativamente, presso: a. propria infrastruttura; b. infrastruttura messa a disposizione dal fornitore all'Amministrazione in modalità dedicata; c. infrastruttura di una terza parte scelta dall'Amministrazione.*» |
| **QC4 / AC4 (livello massimo)** | All. 4, §5.1, PR.DS-01, **18_SS**: «*Il servizio cloud supporta un meccanismo di cifratura di tipo **Hold Your Own Key (HYOK)**, che consente all'amministrazione la generazione e la gestione autonoma di tutte le chiavi di cifratura attraverso un HSM ospitato, alternativamente, presso: a. la propria infrastruttura; b. un'infrastruttura messa a disposizione dal fornitore all'amministrazione in modalità dedicata presso una terza parte scelta dall'amministrazione.*» + **19_SS**: «*È garantito l'accesso esclusivo da parte dell'amministrazione alle chiavi di cui al punto 1 e ai dati in chiaro dell'amministrazione.*» + **20_SS**: HSM dedicato. |
| **PUNTO CRITICO** | **HYOK (18_SS/19_SS) è requisito di QC4, non di QC3.** Ma ai sensi dell'art. 17 c. 4 lett. c) i dati strategici possono essere erogati anche da servizi **QC3**. Quindi un dato "strategico" può legittimamente stare su un servizio che offre solo **BYOK** (chiave root generata dall'amministrazione ma operata nell'ambiente del fornitore), non HYOK. |
| **FONTE** | DD ACN 21007/24, All. 3 pp. 62, 71–72 PDF; All. 4 §5.1 p. 85 PDF; art. 17 c. 4. |
| **AFFIDABILITÀ** | **ALTA** |

### 2.7 — Mappatura classi di dati → livelli richiesti (il punto decisivo)

| Campo | Contenuto |
|---|---|
| **AFFERMAZIONE** | Per i dati **STRATEGICI** il Regolamento **NON impone né il PSN né un fornitore a controllo europeo**. Impone soltanto la qualificazione **QC3 o QC4** (o l'adeguamento AC3/AC4 per i soggetti pubblici). |
| **CITAZIONE — classificazione** | Art. 3, c. 2: «*I dati e i servizi digitali delle amministrazioni […] sono classificati […] nelle seguenti tre classi: a) «ordinari», qualora la loro compromissione non determini i pregiudizi di cui alle lettere b) e c); b) «critici», se la loro compromissione può determinare un pregiudizio al mantenimento di funzioni rilevanti per la società, la salute, la sicurezza pubblica e il benessere economico e sociale del Paese; c) «strategici», se la loro compromissione può determinare un pregiudizio alla sicurezza nazionale.*» |
| **CITAZIONE — mappatura qualificazione** | **Art. 17, c. 4**: «*I dati e i servizi digitali classificati, ai sensi dell'articolo 3, quali: a) «ordinari» possono essere erogati tramite servizi cloud accreditati nell'ambito delle tipologie di cui al comma 1, lettere a), b), c) e d); b) «critici» possono essere erogati tramite servizi cloud accreditati nell'ambito delle tipologie di cui al comma 1, lettere b), c) e d); **c) «strategici» possono essere erogati tramite servizi cloud accreditati nell'ambito delle tipologie di cui al comma 1, lettere c) e d).***» → ordinari ≥ QC1; critici ≥ QC2; **strategici ≥ QC3**. |
| **CITAZIONE — caratteristiche** | Art. 8, c. 2: «*a) «ordinari», i servizi cloud […] devono rispettare i livelli minimi di cui alla sezione 2 dell'Allegato 3; b) «critici», […] sezioni 2 e 3 dell'Allegato 3; c) «strategici», […] sezioni 2, 3 e 4 dell'Allegato 3.*» |
| **CITAZIONE — cosa contiene QC3** | All. 4, §4.1: «*È richiesto il rispetto delle caratteristiche di qualità, di sicurezza, di performance e di scalabilità, di interoperabilità, di portabilità di cui all'Allegato 3 al presente Regolamento per i servizi cloud per le pubbliche amministrazioni che possono trattare dati e servizi classificati quali strategici…*»; §4.2: le tre certificazioni ISO/CSA già citate. **Nient'altro.** |
| **PSN** | La sigla «PSN» e l'espressione «Polo Strategico Nazionale» **non compaiono mai** nel testo del Regolamento (0 occorrenze). L'unico riferimento indiretto è nella definizione di infrastruttura digitale, art. 1: «*2. l'infrastruttura promossa dalla Presidenza del Consiglio dei ministri di cui all'articolo 33-septies, comma 1, del decreto-legge n. 179 del 2012*». **Nessun obbligo di ricorso.** |
| **CLAUSOLA DI RINVIO** | Art. 8, c. 3: «*I servizi cloud per le pubbliche amministrazioni che trattano dati ed erogano servizi digitali soggetti al decreto-legge n. 105 del 2019, rispettano altresì le prescrizioni in materia di cloud previste dal predetto decreto.*» (analogo art. 7, c. 4 per le infrastrutture). → Eventuali vincoli più stringenti per il Perimetro di Sicurezza Nazionale Cibernetica stanno **fuori** da questo Regolamento, nel DL 105/2019 e nei suoi DPCM attuativi. **Il Regolamento 21007/24 non li riproduce né li richiama nel dettaglio.** |
| **AFFIDABILITÀ** | **ALTA** |

---

## 3. CONFRONTO PUNTUALE CON SecNumCloud 3.2 (ANSSI)

**Documento primario letto:** *Prestataires de services d'informatique en nuage (SecNumCloud) — référentiel d'exigences*, **Version 3.2 du 8 mars 2022**, ANSSI, 55 pagine.
**URL PDF:** https://cyber.gouv.fr/sites/default/files/document/secnumcloud-referentiel-exigences-v3.2.pdf
**Storico versioni (p. 2):** «*08/03/2022 — 3.2 — Version intégrant principalement des critères de protection vis-à-vis du droit extra-européen. Modifications apportées aux chapitres 1.3.1, 3.2, 3.3.2, 4, 5.3, 6.1, 7.1, 7.2, 8.1, 9.1, 9.5, 9.7, 10.2, 11.2.1, 11.5, 12.10, 12.13, 12.14, 17.1, 18.2.3, 19.1, **19.6**, Annexes 1 et 2.*»

### 3.1 — Il capitolo 19.6 «Protection vis-à-vis du droit extra-européen» (pp. 50–51)

| Lett. | Citazione testuale |
|---|---|
| **a)** | «*Le siège statutaire, administration centrale et principal établissement du prestataire doivent être établis au sein d'un État membre de l'Union Européenne.*» |
| **b)** | «*Le capital social et les droits de vote dans la société du prestataire ne doivent pas être, directement ou indirectement: — individuellement détenus à plus de 24%; — et collectivement détenus à plus de 39%; par des entités tierces possédant leur siège statutaire, administration centrale ou principal établissement au sein d'un État non membre de l'Union européenne.* […] *Ces entités tierces susmentionnées ne peuvent pas individuellement ou collectivement: — en vertu d'un contrat ou de clauses statutaires, disposer d'un droit de véto; — en vertu d'un contrat ou de clauses statutaires, désigner la majorité des membres des organes d'administration, de direction ou de surveillance du prestataire.*» |
| **c)** | «*En cas de recours par le prestataire […] aux services d'une société tierce — y compris un sous-traitant — possédant son siège statutaire, administration centrale ou principal établissement au sein d'un État non membre de l'Union Européenne ou appartenant ou étant contrôlée par une société tierce domiciliée en dehors l'Union Européenne, cette susdite société tierce **ne doit pas avoir la possibilité technique d'obtenir les données opérées au travers du service**.*» |
| **d)** | «*[…] toute société tierce à laquelle le prestataire recourt […] doit garantir au prestataire une **autonomie d'exploitation continue** […] ou doit être qualifié SecNumCloud.*» |
| **e)** | «*Le service fourni par le prestataire doit respecter la législation en vigueur en matière de droits fondamentaux et les valeurs de l'Union […]. Il peut être pris en considération pour l'appréciation de la conformité susmentionnée, le fait que **le prestataire entretienne des liens avec un gouvernement ou un organisme public étrangers**.*» |
| **f)** | «*Le prestataire doit informer formellement le commanditaire, et dans un délai d'un mois, de tout changement juridique, organisationnel ou technique pouvant avoir un impact sur la conformité de la prestation aux exigences du chapitre 19.6.*» |

### 3.2 — Il capitolo 19.2 «Localisation des données» (p. 49)

«*a) Le prestataire doit documenter et communiquer au commanditaire la localisation du stockage et du traitement des données de ce dernier. b) Le prestataire doit stocker et traiter les données du commanditaire au sein de l'Union Européenne. **c) Les opérations d'administration et de supervision du service doivent être réalisées depuis l'Union Européenne.** d) Le prestataire doit stocker et traiter les données techniques (identités des bénéficiaires et des administrateurs de l'infrastructure technique, données manipulées par le Software Defined Network, journaux de l'infrastructure technique, annuaire, certificats, configuration des accès, etc.) au sein de l'Union Européenne. e) Le prestataire peut réaliser des opérations de support aux commanditaires depuis un État hors de l'Union Européenne. Il doit documenter la liste des opérations […] et les mécanismes permettant d'en assurer le contrôle d'accès et la supervision depuis l'Union Européenne.*»

### 3.3 — Tabella comparativa

| Requisito | **SecNumCloud 3.2 (ANSSI)** | **DD ACN 21007/24** |
|---|---|---|
| Sede statutaria + amministrazione centrale + stabilimento principale in UE | **SÌ** — §19.6.a, obbligo assoluto | **NO** — assente (0 occorrenze di "sede legale") |
| Tetto al capitale extra-UE | **SÌ** — §19.6.b: 24% individuale / 39% collettivo, diretto o indiretto | **NO** — assente (0 occorrenze di "capitale") |
| Divieto di diritto di veto / nomina maggioranza organi da parte di entità extra-UE | **SÌ** — §19.6.b | **NO** — assente |
| Impossibilità **tecnica** per società terza extra-UE di ottenere i dati | **SÌ** — §19.6.c (obbligo di risultato) | **NO** — il corrispondente 15_S/6_S impone solo *segnalazione + autorizzazione*, ammettendo l'accesso |
| Autonomia d'esercizio (o subfornitore a sua volta qualificato) | **SÌ** — §19.6.d, con definizione vincolante ("almeno due società terze alternative") | **PARZIALE** — All. 4 §5.1 punto 21_SS, solo a QC4, autonomia *tecnica* con deroga per "casi eccezionali", nessun obbligo di qualificazione a cascata sul subfornitore extra-UE |
| Legami con governi/organismi pubblici stranieri come elemento di valutazione | **SÌ** — §19.6.e | **NO** — assente |
| Notifica di variazioni societarie rilevanti (1 mese) | **SÌ** — §19.6.f | **NO** — assente (l'art. 16 c. 7 impone notifica di "modifiche sostanziali" solo tecniche/di caratteristiche) |
| **Amministrazione e supervisione del servizio operate dall'UE** | **SÌ** — §19.2.c, obbligo | **NO** — nessun requisito sull'ubicazione degli operatori |
| Dati tecnici (identità, log, directory, certificati, config accessi) in UE | **SÌ** — §19.2.d | **PARZIALE/DEROGABILE** — All. 3 PR.DS-01 2_O e 3_O ammettono metadata fuori UE "salvo motivate e documentate ragioni di natura normativa o tecnica" e per finalità di sicurezza/resilienza |
| Localizzazione dati clienti in UE | **SÌ** — §19.2.b, secco | **SÌ ma derogabile** — All. 3 PR.DS-01 1_O, con clausola "salvo motivate e documentate ragioni" |
| Controllo chiavi dal cliente | Presidio distribuito nel referenziale (cap. 10) | **PIÙ ESPLICITO** — BYOK a livello critico, HYOK + accesso esclusivo a QC4 |

**Sintesi del confronto:** SecNumCloud 3.2 costruisce l'immunità con **tre leve cumulative** — soggettiva (sede + capitale + governance), tecnica (impossibilità tecnica di accesso da parte di società extra-UE) e operativa (amministrazione dall'UE). Il Regolamento ACN 21007/24 usa **solo la leva tecnica, in forma attenuata** (BYOK/HYOK, localizzazione derogabile) e sostituisce la leva soggettiva con una leva **procedurale** (segnalazione + autorizzazione). La leva soggettiva — la sola che neutralizza il CLOUD Act, che opera *ratione personae* sul provider — è **integralmente assente** dal testo italiano.

---

## 4. AVVERTENZE E LIMITI DELLA RICERCA

**Cosa ho letto integralmente (affidabilità ALTA):**
- DD ACN 21007/24 e i suoi quattro allegati — testo completo, 88 pagine, estratto e analizzato.
- SecNumCloud 3.2 (8 marzo 2022) — testo completo, 55 pagine.

**Cosa NON ho potuto verificare direttamente (segnalato come DA VERIFICARE):**

| Elemento | Stato | Nota |
|---|---|---|
| **Catalogo dei servizi cloud qualificati** | **NON LETTO** | `https://catalogocloud.acn.gov.it/` restituisce una pagina di login del "Portale Fornitori ACN"; il contenuto pubblico non è estraibile via fetch automatico. **DA VERIFICARE MANUALMENTE.** Non incide però sulla risposta: la domanda riguarda i *requisiti*, che sono nell'Allegato 4, letto integralmente. |
| **Determinazioni successive al 27/06/2024 che modifichino il Regolamento** | **NON RINVENUTE** | La pagina ACN "Documentazione utile" elenca come «Precedente quadro normativo» i DD 29/2023, 5489/2023, 20610/2023, 2927/2024 — tutti **anteriori** e superati dal 21007/24. Non ho trovato atti modificativi successivi pubblicati su acn.gov.it. **Affidabilità: MEDIA** — verificare periodicamente la pagina documentazione-utile e la Gazzetta/albo ACN. |
| **DPCM attuativi del DL 105/2019 (Perimetro)** | **FUORI PERIMETRO** | Art. 7 c. 4 e art. 8 c. 3 del Regolamento vi rinviano. Eventuali requisiti soggettivi più stringenti per il PSNC starebbero lì, **non** nel Regolamento cloud. Da approfondire in una ricerca separata. |
| **Esistenza di una versione SecNumCloud 3.2.a** | **DA VERIFICARE** | Il PDF ufficiale scaricato da cyber.gouv.fr riporta in frontespizio «Version 3.2 du 8 mars 2022». Alcune fonti secondarie parlano di una «3.2.a». Il contenuto del §19.6 citato è quello del file ufficiale ANSSI. |

---

## 5. RISPOSTA SECCA

# **NO.**

Il **Decreto Direttoriale ACN n. 21007/24 del 27 giugno 2024** — letto integralmente nel suo articolato e in tutti e quattro gli allegati, 88 pagine — **NON contiene**:

- ❌ alcun requisito di **immunità dalle legislazioni extraterritoriali extra-UE**; le parole «extraterritoriale», «CLOUD Act», «paese terzo», «giurisdizione straniera» **non compaiono mai**;
- ❌ alcun requisito sulla **nazionalità o sede legale** del fornitore o della sua capogruppo (0 occorrenze di «nazionalità», «sede legale», «capogruppo»);
- ❌ alcun requisito sul **controllo del capitale** (0 occorrenze di «capitale», «azionariato», «assetto proprietario»);
- ❌ alcun requisito sulla **nazionalità o ubicazione del personale** con accessi privilegiati;
- ❌ alcun obbligo di ricorso al **PSN** o a un **fornitore a controllo europeo** per i dati **strategici** (art. 17 c. 4 lett. c: bastano QC3 o QC4).

**Contiene invece**, come unico presidio sul tema, la clausola PR.DS-01 15_S (All. 3) / 6_S (All. 2), che per i soli dati strategici impone di *segnalare* le richieste di accesso extra-UE e di dare accesso *solo previa autorizzazione dell'amministrazione* — un obbligo procedurale che presuppone e ammette l'accesso extra-UE, e che è per costruzione ineseguibile a fronte di un ordine CLOUD Act corredato da *gag order*.

**È dunque strutturalmente e qualitativamente diverso dal SecNumCloud 3.2 francese**, il cui §19.6 impone sede statutaria in UE, tetti al capitale extra-UE (24%/39%), divieto di veto/nomina da parte di entità extra-UE e impossibilità tecnica di accesso da parte di società terze extra-UE.

---

## 6. URL DEI DOCUMENTI PRIMARI DA APRIRE MANUALMENTE

**Verificati e scaricati (funzionanti al 29/07/2026):**

1. **Regolamento ACN 21007/24 completo (articolato + Allegati 1-4) — IL TESTO OPERATIVO**
   https://www.acn.gov.it/portale/documents/20119/111690/RegolamentoCloud.pdf/aa9b66a5-8c91-18de-d619-68f5c0c62e99?t=1719580455774
   (alias breve: https://www.acn.gov.it/portale/documents/d/guest/regolamentocloud)

2. **SecNumCloud 3.2 — référentiel d'exigences ANSSI (§19.2 e §19.6, pp. 49-51)**
   https://cyber.gouv.fr/sites/default/files/document/secnumcloud-referentiel-exigences-v3.2.pdf

3. **ACN — Documentazione utile cloud (pagina indice di tutti gli atti)**
   https://www.acn.gov.it/portale/cloud/documentazione-utile

4. **ACN — Evoluzione della normativa (schema di raccordo con il quadro precedente)**
   https://www.acn.gov.it/portale/documents/20119/111690/Evoluzione_Normativa_28_06_v3.pdf/18b3faa9-b199-6603-07ab-8c58b83ac0b0?t=1719580935736

**Da aprire manualmente perché non accessibili via fetch automatico:**

5. **Catalogo ACN infrastrutture e servizi cloud qualificati** (login/JS — verificare l'elenco effettivo dei servizi QC1-QC4 e i rispettivi fornitori)
   https://catalogocloud.acn.gov.it/

6. **ACN — Qualificazione dei servizi cloud (pagina istituzionale)**
   https://www.acn.gov.it/portale/qualificazione-cloud
   https://www.acn.gov.it/portale/faq/cloud

7. **ANSSI — elenco dei prestatori qualificati SecNumCloud** (per il confronto sul numero e la natura dei fornitori ammessi)
   https://cyber.gouv.fr/produits-services-qualifies

**Quadro normativo precedente (superato dal 21007/24, utile solo per ricostruzione storica):**

8. DD ACN n. 29 del 02/01/2023 — https://www.acn.gov.it/portale/documents/20119/63628/DecretodirettorialeQualificazioneServiziCloud2genn23DEFsigned.pdf/66ab88a0-2908-db0b-da03-a12767feb9da?t=1702644057383
9. DD ACN n. 5489 del 08/02/2023 — https://www.acn.gov.it/portale/documents/20119/56212/DeterminazioneCloud__20230208_def_signed.pdf/79998186-b4a4-ce86-aeed-33a4a53fbac4?t=1710164603287
10. DD n. 20610 del 28/07/2023 — https://www.acn.gov.it/portale/documents/20119/63628/Decreto+20610_2023.pdf/05c2aea2-3224-261c-138b-f30e8cf1f583?t=1710157536592
11. DD n. 2927 del 30/01/2024 — https://www.acn.gov.it/portale/documents/20119/63628/Decreto_2927_2024.pdf/97e300eb-d094-48f1-28e9-276666dcd897?t=1710164647146
12. Determinazione ACN n. 307 del 18/01/2022, Allegato 1 — https://assets.innovazione.gov.it/1642754054-all1det307acn.pdf
13. Determinazione ACN n. 306 del 18/01/2022 — https://assets.innovazione.gov.it/1642693979-det_306_cloud_modclass_20220118.pdf
