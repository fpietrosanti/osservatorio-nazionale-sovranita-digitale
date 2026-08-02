# Fact pack 16 — Sovranità digitale in Germania, Austria, Svizzera, Paesi Bassi, Belgio, Lussemburgo

**Ricerca svolta**: 2 agosto 2026 · **Lingue di ricerca**: tedesco, olandese, francese, inglese
**Perimetro**: iniziative con *significatività positiva* — (A) migrazione a open source; (B) migrazione da
fornitori a controllo statunitense a controllo europeo. Più, obbligatoriamente, **i fallimenti e le marce
indietro**.

---

## 0. AVVERTENZA METODOLOGICA — LA SCALA USATA

Il progetto ha già una scala a cinque livelli (scheda `01-scala-sovranita.svg`), numerata **1-5**, non 0-4.
La uso in quella numerazione per evitare disallineamenti fra dossier:

| Liv. | Definizione (testo della scheda) | Esposizione al CLOUD Act |
|---|---|---|
| **5** | Infrastruttura europea nativa — fornitore, capitale, tecnologia e gestione europei | **esclusa** |
| **4** | Cloud di fiducia — tecnologia USA in licenza, società e personale locali operano | mitigata (forte) |
| **3** | Sovranità contrattuale e tecnica — clausole, cifratura, chiavi cliente | mitigata |
| **2** | Residenza del dato in UE — data center in Europa, fornitore soggetto a legge USA | **piena** |
| **1** | Cloud globale statunitense | **piena** |

Alla richiesta «livello 0-4» corrisponde quindi: 0→1, 1→2, 2→3, 3→4, 4→5.
**Il software open source auto-ospitato da un ente pubblico non è propriamente sul continuum del cloud**:
lo classifico **livello 5**, perché non c'è alcun aggancio giurisdizionale statunitense, ma segnalo dove
l'infrastruttura sottostante resta di un terzo.

### ⚠️ Sei trappole specifiche di quest'area, individuate durante la ricerca

**T-16.1 — «Schleswig-Holstein è passata a Linux».** *È falso al momento.* L'80% riguarda **LibreOffice**
(la suite d'ufficio). Il sistema operativo Linux è ancora in **fase pilota**, con rollout previsto nel 2026.
La stampa internazionale (e i titoli tedeschi) confondono sistematicamente le due cose. Vedi caso 1.

**T-16.2 — «Le postazioni di Schleswig-Holstein sono 30.000 / 25.000 / 60.000».** Circolano tutte e tre.
25.000 = postazioni IT su cui LibreOffice fu installato nel 2024 · 30.000 = cifra usata nei titoli 2024 ·
60.000 = **dipendenti** del «Konzern Schleswig-Holstein», non postazioni. Non usare le tre come sinonimi.

**T-16.3 — «La Svizzera ha reso obbligatorio l'open source con l'EMBAG».** *È falso.* L'art. 9 EMBAG
obbliga a **pubblicare il codice sorgente del software che l'amministrazione sviluppa o fa sviluppare**.
Non obbliga a *usare* software libero. Vedi caso 9, con il verbatim.

**T-16.4 — «Clarence / S3NS / Proximus sono cloud sovrani europei».** Girano su **Google Distributed
Cloud Hosted** e su **Azure Local**. Sono *livello 4* (cloud di fiducia), non livello 5. Il comunicato del
governo lussemburghese, letto integralmente, **non nomina mai Google**. Vedi casi 12-13.

**T-16.5 — «openDesk ha 100.000 postazioni».** La cifra è di ZenDiS, ripresa da terzi, e convive con
«più di 80.000» della stessa fonte a poche settimane di distanza. Inoltre «postazioni equipaggiate»
≠ «postazioni che hanno dismesso Microsoft»: il **Ministero federale del digitale** che commissiona
openDesk lo sta testando su **oltre 80 postazioni**. Vedi caso 3.

**T-16.6 — L'errore simmetrico: non raccontare solo i successi.** In quest'area i due fatti più duri sono
che **il governo federale tedesco ha speso 481,4 milioni di euro in licenze Microsoft nel 2025** (+75,6%
in due anni) e che **la Confederazione svizzera ha completato il rollout di Microsoft 365 su ~54.000
postazioni a dicembre 2025**. Entrambi nello stesso periodo della retorica sulla sovranità. Casi 6 e 10.

---

# PARTE I — GERMANIA

## Caso 1 — Schleswig-Holstein: la migrazione più avanzata d'Europa (e cosa è davvero)

| Campo | Contenuto |
|---|---|
| **NOME** | Schleswig-Holstein, «Digitale Souveränität / Linux +1» |
| **PAESE** | 🇩🇪 Germania (Land) |
| **TIPO** | Migrazione a open source (A) |
| **STATO** | **In corso — parzialmente concluso.** LibreOffice e posta: concluso all'80%. Linux come SO: **pilota**. |
| **AFFIDABILITÀ** | **ALTA** — comunicato ufficiale del Land letto direttamente + pagina di progetto ufficiale + verifica critica su heise |
| **LIVELLO** | **5** (software libero, infrastruttura del Land / Dataport) |

**COSA È STATO FATTO**
- **LibreOffice**: installato come suite standard su tutte le postazioni IT del Land dal 2024. Al 4 dicembre
  2025, «circa l'80%» delle postazioni **fuori dall'amministrazione fiscale** ha Microsoft Office
  disinstallato o in corso di disinstallazione. Il restante 20% dipende ancora da MS Office per procedure
  specialistiche; percorsi di adeguamento definiti «per i prossimi mesi», amministrazione fiscale inclusa.
- **Posta e calendario**: migrazione a **Open-Xchange** completata a ottobre 2025 — **circa 44.000 caselle**
  e **oltre 110 milioni di voci di calendario/email** trasferite.
- **Nuove licenze Microsoft**: scese a **«meno del 10%»** del totale (esclusa la fiscalità).
- **Nextcloud** sostituirà SharePoint gradualmente; **telefonia** open source (Kamailio/Asterisk/RTPengine)
  in fase di allestimento; **directory** (sostituzione di Active Directory) in fase di test.
- **Linux come sistema operativo**: 🔴 **ancora pilota.** La pagina ufficiale del progetto elenca «+1 Linux
  Workplace» come pilastro in cui si stanno «selezionando distribuzione e concetti di rollout». Il 2026 è
  descritto come l'anno di modernizzazione dei sistemi verticali *per creare i presupposti* del rollout.

**NUMERI E DATE**
- Risparmio già conseguito: **oltre 15 milioni di euro** in costi di licenza.
- Investimento una tantum a bilancio 2026: **9 milioni di euro**.
- Ministro competente (CDS, Chef der Staatskanzlei): **Dirk Schrödter** (CDU).
- Comunicato: **4 dicembre 2025**.

**LE DIFFICOLTÀ — da riportare, sono la parte più utile**
- **Settembre 2025**: la Procura generale e i presidenti dei tribunali del Land scrivono al ministro
  avvertendo di una **«massiva compromissione dei tribunali»**.
- Schrödter ammette l'errore, verbatim: *«Avremmo forse dovuto sottolineare fin dall'inizio che le
  interfacce hanno un aspetto diverso e i pulsanti si trovano in posizioni differenti.»*
- Contromisure adottate: materiali formativi, piattaforme di scambio, *migration manager* dedicati.
- Bilancio di heise (6 gennaio 2026): **«Open Source ist praxistauglich trotz Umstellungsproblemen»** —
  praticabile, *nonostante* i problemi di transizione. È la formulazione onesta.

**FONTI**
- 🔗 https://www.schleswig-holstein.de/DE/landesregierung/ministerien-behoerden/I/Presse/PI/2025/cds/251204_cds_open-source — **tedesco**, comunicato ufficiale del Land, 4/12/2025
- 🔗 https://www.schleswig-holstein.de/DE/landesregierung/themen/digitalisierung/linux-plus1/Projekt — **tedesco**, pagina di progetto (i sei pilastri e il loro stato)
- 🔗 https://www.heise.de/news/Schleswig-Holstein-Open-Source-ist-praxistauglich-trotz-Umstellungsproblemen-11131005.html — **tedesco**, 6/1/2026 (critiche della magistratura, ammissione del ministro)

> ⚠️ **Da non dire**: «Schleswig-Holstein ha sostituito Windows con Linux». Non ancora.
> **Da dire**: «Schleswig-Holstein ha tolto Microsoft Office a otto postazioni su dieci e ha spostato
> quarantaquattromila caselle di posta fuori da Microsoft. Il sistema operativo è il prossimo passo,
> non è ancora fatto.»

---

## Caso 2 — Dataport «Phoenix»: il fallimento da 90 milioni certificato dalla Corte dei conti 🔴

| Campo | Contenuto |
|---|---|
| **NOME** | Programma **Phoenix** / dPhoenixSuite — Dataport |
| **PAESE** | 🇩🇪 Germania (sei Länder del Nord + un'associazione comunale) |
| **TIPO** | Migrazione a open source (A) |
| **STATO** | 🔴 **FALLITO.** Progetto chiuso a ottobre 2024. Fallimento accertato dalla Corte dei conti di Amburgo nel Jahresbericht 2026. |
| **AFFIDABILITÀ** | **ALTA** — rapporto della *Rechnungshof der Freien und Hansestadt Hamburg*, pubblicato il 17/2/2026, pp. 75-81 |
| **LIVELLO** | — (progetto cessato) |

**COSA È SUCCESSO**
Dataport — il fornitore IT pubblico in *house* di sei Länder del Nord (fra cui Amburgo, Schleswig-Holstein,
Brema, Meclemburgo-Pomerania Anteriore) — avvia nel **2019, di propria iniziativa**, il programma Phoenix:
una postazione di lavoro amministrativa interamente open source (Nextcloud, Matrix, Jitsi, Collabora, UCS)
come alternativa a Microsoft 365. Nel 2022 la **Schleswig-Holstein abbandona Phoenix** per ritardi e concetti
di sicurezza insufficienti. A metà 2024 il consiglio di amministrazione constata che ai costi accumulati
**non corrisponde alcuna prospettiva di ricavo**. **Ottobre 2024: progetto chiuso.**

**NUMERI E DATE**
- Costi accumulati alla chiusura: **circa 140 milioni di euro**.
- Perdita: **circa 90 milioni di euro** complessivi, di cui **circa 30 milioni nel solo 2024**.
- Svalutazione contabile per Phoenix: **36,5 milioni di euro**.
- Risultato d'esercizio Dataport 2024: **-28,9 milioni**; quota di capitale proprio scesa al **9,9%**.
- Rapporto: **Jahresbericht 2026** della Rechnungshof di Amburgo, presentato il **16/2/2026**,
  pubblicato il **17/2/2026**, sei pagine dedicate (pp. 75-81).

**I RILIEVI DELLA CORTE — verbatim/parafrasi stretta**
- Phoenix **«non è stato pianificato in modo economico fin dall'inizio sulla base di assunzioni realistiche»**;
  costi e rischi sottostimati.
- Informazione al consiglio di amministrazione **«zögerlich und verspätet»** (esitante e tardiva).
- Controllo interno e gestione del rischio insufficienti; documentazione lacunosa.
- Contratti stipulati con terzi per prestazioni che Dataport non era in grado di erogare.
- Ammissione dell'amministratore delegato **Johann Bizer**, verbatim: **«Wir haben den Aufwand
  unterschätzt»** — riferito allo sforzo di integrare produttori diversi su un'unica piattaforma.

**IL SEGUITO — che cambia il senso del caso**
Le tecnologie sviluppate in Phoenix **costituiscono oggi la base essenziale di openDesk**, gestito da ZenDiS
per conto del Ministero dell'Interno federale. E il **Baden-Württemberg**, che usava dPhoenixSuite per il
posto di lavoro digitale dei docenti, dall'estate 2025 lo esegue **su openDesk** (caso 5).

**LA CRITICA PRECEDENTE, CHE AVEVA VISTO GIUSTO**
Già il **6 giugno 2023** la **Free Software Foundation Europe** pubblicava *«dPhoenix on the road to
failure?»*: il codice della suite integrata **non era ottenibile da Dataport su richiesta**; solo i
componenti sottostanti erano liberi, mentre **integrazione e glue code restavano proprietari**. La FSFE
parlava esplicitamente di **«open-washing»**, di confusione su quale progetto fosse basato su quale, e di
responsabilità non chiare. Chiedeva la pubblicazione del codice su openCoDE entro fine 2023.

**FONTI**
- 🔗 https://taz.de/Versemmeltes-Open-Source-Projekt/!6157121/ — **tedesco**, taz, 25/2/2026
- 🔗 https://www.golem.de/news/rechnungshof-jahresbericht-managementfehler-und-dubiose-beschluesse-bei-dataport-phoenix-2602-205486.html — **tedesco**, Golem
- 🔗 https://www.hamburg.de/resource/blob/1136702/a5078d4727385985f43b3420b2c698a2/jahresbericht-2026-pdf-data.pdf — **tedesco**, Jahresbericht 2026 integrale (fonte primaria, pp. 75-81) 🔴 *da leggere in originale prima della messa in onda*
- 🔗 https://fsfe.org/news/2023/news-20230606-01.en.html — **inglese**, FSFE, 6/6/2023

> 🎯 **Perché questo caso vale più di dieci successi**: dimostra che il fallimento di una migrazione open
> source non è mai «il software non funziona». È **governance, stima dei costi e integrazione**. E che il
> codice prodotto **non è andato perduto**: è diventato openDesk, che oggi gira su decine di migliaia di
> postazioni. È l'unica storia dell'area che contiene insieme il fallimento e il riscatto.

---

## Caso 3 — ZenDiS e openDesk: l'alternativa federale tedesca a Microsoft 365

| Campo | Contenuto |
|---|---|
| **NOME** | **ZenDiS GmbH** (Zentrum für Digitale Souveränität der Öffentlichen Verwaltung) · prodotti **openDesk** e **openCode** |
| **PAESE** | 🇩🇪 Germania (federale) |
| **TIPO** | Migrazione a open source (A) |
| **STATO** | **In corso.** Prodotto in produzione, adozione reale in crescita ma **frammentata fra pilota e produzione**. Obiettivo dichiarato: alternativa disponibile all'amministrazione federale entro **ottobre 2028**. |
| **AFFIDABILITÀ** | **MEDIA sulle cifre di adozione** (fonte unica, autodichiarata, incoerente) · **ALTA su natura, proprietà e cronologia** |
| **LIVELLO** | **5** (stack interamente libero, ospitabile in casa) |

**COS'È**
GmbH di diritto tedesco fondata a **dicembre 2022** su iniziativa del **Ministero federale dell'Interno
(BMI)**, sede a **Bochum**. **Azionista unico: la Repubblica Federale di Germania**. L'ingresso dei Länder
era previsto fin dall'origine ma **non si è ancora perfezionato**: al 2026 **Turingia e Schleswig-Holstein**
sono in procedura di adesione; Baden-Württemberg, Berlino, Renania Settentrionale-Vestfalia e Sassonia
hanno dichiarato l'intenzione.
- **openDesk**: suite d'ufficio e collaborazione che integra **Nextcloud, Collabora Online, Element/Matrix,
  XWiki, OpenProject, Jitsi Meet** — presentata come «alternativa digitalmente sovrana a Microsoft 365».
  Sviluppo assunto da ZenDiS a **gennaio 2024**. Versione corrente **1.17.1** (31/7/2026).
- **openCode**: piattaforma GitLab per lo scambio di codice fra amministrazioni.

**NUMERI E DATE — con il conflitto dichiarato**
- ⚫ **«100.000 postazioni amministrative equipaggiate con openDesk»** (ZenDiS, 2026) — **contro**
  «più di 80.000 postazioni migrate con successo» (ZenDiS, stesso periodo). ⚠️ **Le due cifre non sono
  riconciliate su fonte primaria.** Usare la forma *«fra ottanta e centomila postazioni, secondo il
  gestore»*, mai una cifra secca.
- **Robert Koch-Institut**: circa **7.000 utenti**.
- **Baden-Württemberg**: circa **60.000 docenti** (caso 5) — è verosimilmente il blocco maggiore.
- **BMDS** (Ministero federale del digitale e della modernizzazione dello Stato), *committente del prodotto*:
  lo sta testando su **oltre 80 postazioni** (aprile 2026). 🔴 **Il dato più imbarazzante e più onesto
  dell'intero dossier.**
- **Deutsche Rentenversicherung Bund** e **Bundesagentur für Arbeit**: in test dall'inizio 2026 — ma
  **come postazione di emergenza** (*Notfallarbeitsplatz*) nel progetto CKKI, concluso con bilancio
  positivo il 21/7/2026. **Non è adozione ordinaria**: è continuità operativa in caso di crisi.
- **Obiettivo dichiarato**: alternativa digitalmente sovrana disponibile all'amministrazione federale
  entro **ottobre 2028**.

**LE TURBOLENZE — da non omettere**
- **Aprile 2025**: la CTO **Jutta Horstmann** viene rimossa inaspettatamente.
- **Novembre 2025**: **Pamela Krosta-Hartl** nominata nuova CEO.
- **15 aprile 2026**: il consiglio di sorveglianza avvia un **processo di riorientamento strategico**, con
  **Dr. Stefan Groß-Selbeck** (ex CEO di Xing, ex capo di eBay Germania) come consulente esterno; l'obiettivo
  dichiarato include **ridurre il ruolo di ZenDiS come fornitore IT** e aprire un programma di partner
  commerciali. Il programma di partnership era già stato **rinviato** al Q1 2026.

**FONTI**
- 🔗 https://www.zendis.de/ e https://opendesk.eu/ — **tedesco/inglese**, gestore
- 🔗 https://bmds.bund.de/aktuelles/pressemitteilungen/detail/bund-stellt-zendis-strategisch-neu-auf — **tedesco**, BMDS, 15/4/2026 (le «oltre 80 postazioni» del ministero)
- 🔗 https://bmds.bund.de/themen/digitale-souveraenitaet/digitale-souveraenitaet-in-der-oeffentlichen-verwaltung/souveraener-arbeitsplatz — **tedesco**, obiettivo ottobre 2028
- 🔗 https://www.deutsche-rentenversicherung.de/Bund/DE/Presse/Pressemitteilungen/pressemitteilungen_aktuell/2026/2026-07-21-ckki-zendis-opendesk — **tedesco**, 21/7/2026, progetto CKKI
- 🔗 https://de.wikipedia.org/wiki/Zentrum_für_Digitale_Souveränität_der_Öffentlichen_Verwaltung — **tedesco**, cronologia societaria 🟡 *fonte terziaria, da confermare sui comunicati BMI*
- 🔗 https://dserver.bundestag.de/btd/21/055/2105502.pdf — **tedesco**, Bundestag Drucksache 21/5502 (22/4/2026), risposta del Governo su openDesk 🔴 **PDF non estraibile automaticamente — da aprire a mano. È la fonte primaria che scioglierebbe il conflitto sulle cifre.**

---

## Caso 4 — Bundeswehr: BwMessenger su Matrix, oltre 100.000 utenti

| Campo | Contenuto |
|---|---|
| **NOME** | **BwMessenger** (e **BundesMessenger** per le altre amministrazioni) |
| **PAESE** | 🇩🇪 Germania |
| **TIPO** | Migrazione a open source (A) + sostituzione di servizi USA (B) |
| **STATO** | ✅ **CONCLUSO E IN PRODUZIONE** dal novembre 2020. È la migrazione open source **più consolidata** di tutta l'area. |
| **AFFIDABILITÀ** | **MEDIA-ALTA** — la cifra utenti viene dal fornitore (Element/New Vector) e da BWI, non da una fonte parlamentare |
| **LIVELLO** | **5** — protocollo aperto, client open source, server auto-ospitato dalla società IT della Bundeswehr |

**COSA È STATO FATTO**
Messenger basato sul protocollo aperto **Matrix**, con client derivato da **Element**, sviluppato e operato
da **BWI GmbH**, la società IT interna della Bundeswehr. Sostituisce **BwChat**, che era un pilota basato sul
servizio proprietario *stashcat*. È lo standard unico di messaggistica per militari e civili della Difesa.

**NUMERI E DATE**
- **Dicembre 2019**: avvio sviluppo · **aprile 2020**: pilota esteso a **30.000 dispositivi** ·
  **novembre 2020**: lancio completo.
- **Luglio 2021**: certificazione **BSI** per comunicazioni classificate **VS-NfD**.
- **Dicembre 2023**: lancio di **BundesMessenger** per le altre amministrazioni federali.
- Utilizzo dichiarato: **oltre 100.000 persone**, su base quotidiana.

**FONTI**
- 🔗 https://element.io/de/case-studies/bundeswehr — **tedesco**, case study del fornitore ⚠️ *fonte di parte*
- 🔗 https://www.bwi.de/magazin/artikel/open-source-matrix-ist-einheitlicher-messenger-standard-fuer-die-bundeswehr — **tedesco**, BWI
- 🔗 https://messenger.bwi.de/bwmessenger — **tedesco**, pagina di prodotto

> 🎯 **Perché è forte per il film**: è **la Difesa tedesca** — l'ente che più di ogni altro potrebbe
> giustificare l'acquisto del prodotto commerciale «migliore» — che si è costruito il proprio strumento
> su un protocollo aperto e lo ha fatto **certificare per il materiale classificato**. Ed è **concluso**,
> non annunciato. È il gemello tedesco di `difesa.it` che gestisce la propria posta (Atto 6).

---

## Caso 5 — Baden-Württemberg: circa 60.000 docenti su openDesk

| Campo | Contenuto |
|---|---|
| **NOME** | **Digitaler Arbeitsplatz für Lehrkräfte (DAP)**, piattaforma **SCHULE@BW** |
| **PAESE** | 🇩🇪 Germania (Land Baden-Württemberg) |
| **TIPO** | Migrazione a open source (A) |
| **STATO** | ✅ **IN PRODUZIONE** dal 2024, migrato da dPhoenixSuite a openDesk **dall'estate 2025** |
| **AFFIDABILITÀ** | **ALTA** — comunicato del Ministero della cultura del Land, 19/9/2025, letto direttamente |
| **LIVELLO** | **5** |

**COSA È STATO FATTO**
Posto di lavoro digitale per i docenti del Land: casella, calendario, contatti, attività, archiviazione,
collaborazione. Costruito **con Dataport, govdigital, Univention, Open-Xchange, Nextcloud, Collabora**;
dall'estate 2025 eseguito **sulla base di openDesk**, in cooperazione con **ZenDiS**.

**NUMERI E DATE**
- **Circa 60.000 insegnanti** usano il DAP; in distribuzione dal **2024**.
- Passaggio dPhoenixSuite → openDesk: **estate 2025**; comunicato del **19 settembre 2025**.
- Il comunicato sottolinea che per i docenti **gli indirizzi email non cambiano** e i componenti restano gli
  stessi: la migrazione è **quasi impercettibile all'utente**.
- Nessuna cifra di costo pubblicata.
- Citazione della Segretaria di Stato **Sandra Boser** (MdL): con openDesk e ZenDiS «facciamo un ulteriore
  passo verso maggiore sovranità digitale e quindi maggiore indipendenza».

**FONTE**
- 🔗 https://km.baden-wuerttemberg.de/de/service/pressemitteilung/pid/digitaler-arbeitsplatz-fuer-lehrkraefte-wird-nun-mit-opendesk-umgesetzt — **tedesco**, Kultusministerium BW, 19/9/2025

> 🎯 **Aggancio diretto al film.** Il registro delle trappole (n. 15) dice già: *«non dire che l'Assia ha
> vietato Microsoft nelle scuole; il caso solido è il Baden-Württemberg»*. **Questo è il seguito di quel
> caso**: il Land che disse no a Microsoft 365 nelle scuole non si è fermato al divieto — **ha costruito
> l'alternativa e la fa girare su sessantamila docenti da due anni.** È esattamente la prova che manca
> all'Atto 10.

---

## Caso 6 — 🔴 IL CONTRO-FATTO: la Germania spende ogni anno di più in Microsoft

| Campo | Contenuto |
|---|---|
| **NOME** | Spesa del Bund per licenze Microsoft |
| **PAESE** | 🇩🇪 Germania (federale) |
| **TIPO** | ⚫ **Contro-fatto** — misura la distanza fra retorica e bilancio |
| **STATO** | **Fatto accertato**, risposta scritta del Governo federale |
| **AFFIDABILITÀ** | **ALTA** — risposta del Governo a interrogazione scritta della deputata **Rebecca Lenhard** (Bündnis 90/Die Grünen), portavoce per la politica digitale |
| **LIVELLO** | **1-2** |

**I NUMERI**

| Anno | Spesa del Bund in licenze Microsoft |
|---|---|
| 2023 | **274,1 milioni €** |
| 2024 | **347,7 milioni €** |
| 2025 | **481,4 milioni €** |

**+75,6% in due anni.** Quasi mezzo miliardo di euro in un anno solo per l'amministrazione **federale**:
heise segnala che **il Governo federale non dispone di dati attendibili su Länder e comuni** — la cifra
complessiva tedesca è quindi **ignota**, esattamente come in Italia (cfr. A9, l'opacità come fatto
verificabile).

**La reazione**: Lenhard — «le cifre presentate mostrano una tendenza pericolosa» — osserva che con quelle
somme si sarebbero potute finanziare soluzioni open source ed alternative europee. La **Open Source Business
Alliance** ha intitolato il proprio comunicato: *«Quasi mezzo miliardo di euro per licenze Microsoft: i
soldi mancano per la modernizzazione dello Stato»*.

**FONTI**
- 🔗 https://www.heise.de/en/background/Microsoft-Dependency-Federal-Government-Pays-near-500-Million-Euros-in-One-Year-11171050.html — **inglese/tedesco**, heise
- 🔗 https://osb-alliance.de/pressemitteilungen/fast-eine-halbe-milliarde-euro-fuer-microsoft-lizenzen-geld-fehlt-fuer-die-modernisierung-des-staates — **tedesco**, OSBA
- 🔴 **Da recuperare**: il testo integrale della risposta governativa all'interrogazione Lenhard, su dip.bundestag.de

---

## Caso 7 — LiMux, Monaco di Baviera: il fallimento — e la marcia indietro sulla marcia indietro

| Campo | Contenuto |
|---|---|
| **NOME** | **LiMux** → ritorno a Windows → **nuovo ritorno all'open source** |
| **PAESE** | 🇩🇪 Germania (città di Monaco) |
| **TIPO** | Migrazione a open source (A) |
| **STATO** | 🔴 **FALLITO nel 2017** · 🟡 **RIAVVIATO come indirizzo politico nel 2026 — annunciato, non realizzato** |
| **AFFIDABILITÀ** | **ALTA** sui fatti 2006-2017 · **MEDIA** sull'attuazione 2026 (è un contratto di coalizione, non un atto amministrativo) |
| **LIVELLO** | 5 (2006-2017) → 1-2 (2017-2026) → indirizzo verso 5 (2026-) |

**LA CRONOLOGIA**
- **2006**: Monaco avvia LiMux, distribuzione Linux basata su Ubuntu, per sostituire Windows.
- **Picco**: **14.800 desktop** effettivamente in esercizio su LiMux.
- **2016**: perizia di **Accenture** commissionata dal Comune. ⚠️ **La perizia raccomandava di introdurre un
  client Windows *in aggiunta* a LiMux — non di eliminarlo.** Il consiglio comunale fece qualcosa di
  **più radicale** di ciò che il consulente aveva proposto.
- **23 novembre 2017**: il consiglio comunale, con la maggioranza della grande coalizione **SPD-CSU**,
  delibera la fine di Linux come client. Migrazione a Windows **entro fine 2020**, su **circa 29.000
  computer** dell'amministrazione municipale.
- **13 maggio 2026**: la nuova coalizione «Mango» (Verdi/Rosa Liste, SPD, FDP/Freie Wähler), per la
  legislatura **2026-2032**, inserisce nel contratto di coalizione che **l'open source diventa il caso
  normale** per gli acquisti software comunali e che **«il software finanziato con il gettito fiscale deve
  essere messo a disposizione della collettività»** (Public Money, Public Code). L'**Open Source Program
  Office** fondato a inizio 2024 viene rafforzato come unità centrale di indirizzo; la FDP guiderà il nuovo
  dipartimento digitale.

**I COSTI DEL RITORNO A WINDOWS**
- **86,1 milioni €** stimati per i sei anni successivi, di cui **49,3 milioni** per il solo posto di lavoro
  IT unificato basato su Windows.
- **Oltre 89 milioni €** includendo i 3,1 milioni di spesa dei singoli dipartimenti.
- I Verdi stimavano potenzialmente **centinaia di milioni** includendo il passaggio da LibreOffice a MS Office.

**PERCHÉ FALLÌ — la risposta contro-intuitiva**
- Un sondaggio interno rilevò che **il 68,6% dei dipendenti era soddisfatto della funzionalità del software**,
  ma **solo il 32% della struttura organizzativa**.
- Il problema accertato fu la **«doppia gestione»** (IT centralizzata vs dipartimenti autonomi), non Linux.
- ⚠️ **Il conflitto d'interessi da nominare, ma con cautela**: Accenture è stata premiata **nove volte** da
  Microsoft come *«Geschäftspartner des Jahres»* e commercializza prodotti Microsoft nel mondo tramite la
  joint venture **Avanade**. 🟡 **Formulazione corretta**: il fatto è documentabile; l'inferenza che la
  perizia fosse per questo di parte **non lo è** — e la perizia, letta, **non chiedeva di eliminare LiMux**.
  Dire il fatto, non l'accusa.
- 🟡 **Il contesto che va detto perché la contro-parte lo dirà**: nel 2016 Microsoft ha trasferito la propria
  sede tedesca a Monaco. 🔴 **Correlazione temporale, non nesso causale accertato. Non presentarlo come
  causa.** *(La singola fonte consultata non lo riporta: verificare prima di usarlo, o ometterlo.)*

**FONTI**
- 🔗 https://www.heise.de/news/Endgueltiges-Aus-fuer-LiMux-Muenchener-Stadtrat-setzt-den-Pinguin-vor-die-Tuer-3900439.html — **tedesco**, heise, 23/11/2017
- 🔗 https://u-labs.de/portal/warum-limux-scheiterte/ — **tedesco**, analisi del sondaggio interno e della perizia Accenture 🟡 *fonte secondaria*
- 🔗 https://vergabeblog.de/2017-12-12/muenchen-limux-aus-endgueltig-besiegelt/ — **tedesco**
- 🔗 https://www.heise.de/en/news/Munich-s-IT-transition-Open-Source-is-the-default-for-the-new-coalition-11292449.html — **inglese**, heise, 13/5/2026

> 🎯 **Il modo giusto di raccontarlo, e non è quello che ci si aspetta.**
> Non «LiMux fallì perché Linux non funzionava»: i dipendenti erano soddisfatti del software a due terzi.
> Non «LiMux fu ucciso da Microsoft»: la perizia chiedeva di *aggiungere* Windows, il consiglio comunale
> decise di *togliere* Linux.
> **La formulazione difendibile è: una migrazione tecnica riuscita può essere disfatta da un cambio di
> maggioranza politica e da una struttura organizzativa mai risolta.** Il che rende il caso ancora più utile:
> mostra che **la sovranità digitale è reversibile** — e che nove anni dopo, sempre a Monaco, si può tornare
> indietro dal ritorno indietro. **Nulla è definitivo, in nessuna delle due direzioni.**

---

## Caso 8 — Sovereign Tech Agency: la Germania finanzia l'infrastruttura aperta del mondo

| Campo | Contenuto |
|---|---|
| **NOME** | **Sovereign Tech Fund** → **Sovereign Tech Agency** |
| **PAESE** | 🇩🇪 Germania (federale) |
| **TIPO** | Sostegno all'open source (A) — non una migrazione |
| **STATO** | ✅ **OPERATIVA E IN EROGAZIONE** dal 2022 |
| **AFFIDABILITÀ** | **MEDIA-ALTA** — cifre da fonti terziarie e giornalistiche; il sito ufficiale ha restituito 403 in fase di verifica |
| **LIVELLO** | n/a (strumento di finanziamento) |

**COS'È**
Struttura pubblica tedesca che **finanzia la manutenzione dell'infrastruttura software libera critica** —
non prodotti nuovi, ma le fondamenta che tutti usano e nessuno paga. È una **filiale di SPRIND**, l'agenzia
federale per le innovazioni dirompenti, su incarico del Ministero federale dell'economia (BMWK).
Direzione: **Adriana Groh** e **Luisa von Beust** (co-CEO), **Fiona Krakenbürger** (CTO).

**NUMERI E DATE**
- Bilancio: **13 mln € (2022)** · **~22 mln € (2023)** · **fino a 16 mln € (2024)** · **~17 mln € (2025)**.
  ⚫ Le fonti divergono sul 2025: una riporta *«quasi 29 milioni disponibili per il 2025»* comprensivi di
  altre voci. **Non usare una cifra secca per il 2025.**
- Investito complessivamente: **circa 23,5 milioni €** in **circa 60 tecnologie critiche** (dato 2025);
  oltre **40 progetti** finanziati ad aprile 2025.
- Progetti finanziati (esempi con importo): **KDE 1.285.200 €** (erogati 2026-2027) · **Prossimo/Rustls
  1.436.729 €** · **Python Package Index 1.056.672 €** · **GNOME ~1.000.000 €** · **Sequoia PGP 900.000 €** ·
  **OpenJS Foundation 874.940 €** · **coreutils 99.060 €**. Fra i beneficiari anche **Log4j, Samba, GNOME**.
- **Il dato che conta**: sono state presentate **oltre 500 proposte** per un fabbisogno dichiarato di
  **circa 114 milioni di euro**. **La domanda vale cinque volte l'offerta.**

**FONTI**
- 🔗 https://en.wikipedia.org/wiki/Sovereign_Tech_Agency — **inglese** 🟡 *terziaria*
- 🔗 https://www.heise.de/en/news/Budget-2025-Bundestag-increases-funding-for-the-Sovereign-Tech-Fund-9979095.html — **inglese**
- 🔗 https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/document/funding-open-source-case-study-sovereign-tech-fund — **inglese**, caso studio della Commissione
- 🔗 https://www.sovereign.tech/ — sito ufficiale ⚠️ *403 in fetch automatico, aprire a mano*

---

## Caso 9 — STACKIT (Gruppo Schwarz): il candidato hyperscaler tedesco

| Campo | Contenuto |
|---|---|
| **NOME** | **STACKIT** — Schwarz Digits, Gruppo Schwarz (Lidl/Kaufland) |
| **PAESE** | 🇩🇪 Germania |
| **TIPO** | Fornitore a controllo europeo (B) |
| **STATO** | ✅ **IN PRODUZIONE**, in forte espansione. Aggiudicatario di gare pubbliche europee. |
| **AFFIDABILITÀ** | **MEDIA-ALTA** — l'aggiudicazione della Commissione è certa e datata; le cifre di scala vengono da fonti settoriali |
| **LIVELLO** | **5** — capitale, sede, tecnologia e gestione tedeschi. È il caso più chiaramente di livello 5 dell'area. |

**COSA È STATO FATTO**
- Infrastruttura in **Germania e Austria**: oltre **23.000 server**, **30 petabyte** di storage dichiarati.
  Fatturato esterno della divisione cloud: **1,9 miliardi €**.
- **Ottobre 2024**: partnership con **SAP** annunciata al congresso DSAG di Lipsia — i clienti SAP possono
  spostare l'intero ERP su STACKIT via *RISE with SAP*.
- Il **Governo federale tedesco** investe circa **250 milioni €** in una piattaforma IA basata su STACKIT.
- **Aprile 2026**: selezionato dalla **Commissione europea** fra i quattro fornitori della gara da
  **180 milioni €** per il cloud sovrano delle istituzioni UE — riconosciuto **SEAL-3** («Digital
  Resilience»: immune da interruzioni della catena di fornitura da parte di terzi extra-UE).
- **23 aprile 2026**: il **Governo dei Paesi Bassi** firma con STACKIT un **accordo quadro**
  (*raamovereenkomst*) — vedi caso 15.
- **Campus cloud di Bad Friedrichshall**: 20 ettari, fino a 5.000 addetti.

**FONTI**
- 🔗 https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_en — **inglese**, Commissione europea, 17/4/2026
- 🔗 https://dsag.de/presse/dsag-begruesst-cloud-partnerschaft-zwischen-sap-und-schwarz-gruppe-zu-stackit/ — **tedesco**, DSAG
- 🔗 https://european.cloud/provider/stackit/ — **inglese** 🟡 *directory settoriale*

---

# PARTE II — AUSTRIA

## Caso 10 — Bundesheer: 16.000 postazioni militari su LibreOffice

| Campo | Contenuto |
|---|---|
| **NOME** | **Österreichisches Bundesheer** — migrazione a LibreOffice |
| **PAESE** | 🇦🇹 Austria |
| **TIPO** | Migrazione a open source (A) |
| **STATO** | **In corso, decisione conclusa e attuazione avviata** (annuncio pubblico settembre 2025) |
| **AFFIDABILITÀ** | **MEDIA-ALTA** — dichiarazioni dirette di un responsabile del Bundesheer riprese da inside-it, derStandard, Linux-Magazin. 🔴 *Manca un atto ufficiale del Ministero della difesa letto in originale.* |
| **LIVELLO** | **5** |

**COSA È STATO FATTO**
L'esercito austriaco sostituisce Microsoft Office con **LibreOffice** su **circa 16.000 postazioni**.
La motivazione dichiarata **non è il risparmio** sulle 16.000 licenze, ma **la sovranità digitale**.

**CRONOLOGIA DICHIARATA**
- **2020**: decisione di cercare alternative alla suite Microsoft.
- **2021**: processo decisionale concluso.
- **2022**: pianificazione di dettaglio.
- **2023**: incarico a **un'azienda tedesca** per sviluppo e supporto.
- **Settembre 2025**: annuncio pubblico della migrazione.

**FONTI**
- 🔗 https://www.inside-it.ch/osterreichische-armee-mustert-microsoft-office-aus-20250923 — **tedesco**, 23/9/2025
- 🔗 https://www.derstandard.at/story/3000000288311/microsoft-wird-ausgemustert-bundesheer-wechselt-zu-libreoffice — **tedesco**
- 🔗 https://www.linux-magazin.de/news/oesterreich-bundesheer-setzt-auf-libreoffice/ — **tedesco**

> 🎯 **Il parallelo con la Bundeswehr (caso 4) e con `difesa.it` (Atto 6) è la struttura narrativa più
> economica di tutto questo dossier**: tre eserciti europei — tedesco, austriaco, italiano — che scelgono
> autonomia là dove le amministrazioni civili scelgono comodità.

---

## Caso 11 — Ministero dell'economia austriaco: via SharePoint, arriva Nextcloud

| Campo | Contenuto |
|---|---|
| **NOME** | **BMWET** (Bundesministerium für Wirtschaft, Energie und Tourismus) → Nextcloud |
| **PAESE** | 🇦🇹 Austria |
| **TIPO** | Migrazione a open source (A) |
| **STATO** | **In corso** — dismissione di Microsoft SharePoint prevista nel **primo trimestre 2026** |
| **AFFIDABILITÀ** | **DA VERIFICARE** — 🔴 la notizia circola su fonti secondarie di settore; non ho trovato un comunicato del ministero |
| **LIVELLO** | **5** |

**CONTESTO ISTITUZIONALE AUSTRIACO**
- Esiste un **«Erster Fortschrittsbericht Digitale Souveränität»** depositato in Parlamento (XXVIII leg.,
  documento SONS/20, maggio 2026): è **la fonte primaria austriaca da leggere per intero**. Il fetch
  automatico ne ha estratto solo la struttura (obiettivi: riduzione della dipendenza da infrastrutture
  digitali straniere, migrazione a open source, controllo dei dati pubblici; migrazioni citate: LibreOffice,
  Nextcloud, ecosistemi Linux lato server).
- **Autunno 2025**: su iniziativa del Segretario di Stato alla digitalizzazione **Alexander Pröll**, vertice
  a Vienna con la Commissaria **Henna Virkkunen** e rappresentanti di tutti gli Stati membri sulla sovranità
  digitale.

**FONTI**
- 🔗 https://www.parlament.gv.at/dokument/XXVIII/SONS/20/imfname_1761074.pdf — **tedesco**, fonte primaria 🔴 **da leggere a mano: il PDF non è estraibile automaticamente**
- 🔗 https://www.mrak.at/digitale-souveranitat-wird-jetzt-europaweit-zum-regierungsprogramm/ — **tedesco** 🟡 *secondaria*

---

# PARTE III — SVIZZERA

## Caso 12 — EMBAG: la legge che *non* obbliga a usare l'open source ⚠️

| Campo | Contenuto |
|---|---|
| **NOME** | **EMBAG** — *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben*, **art. 9** |
| **PAESE** | 🇨🇭 Svizzera |
| **TIPO** | Obbligo di trasparenza del codice (A, parziale) |
| **STATO** | ✅ **IN VIGORE dal 1° gennaio 2024**; ambito **esteso alle unità decentralizzate dal 1° maggio 2025** |
| **AFFIDABILITÀ** | **ALTA sul testo** (verbatim di art. 9 cpv. 1 reperito) · 🔴 *fedlex.admin.ch richiede JavaScript: il testo consolidato va aperto a mano prima della messa in onda* |
| **LIVELLO** | n/a (norma, non infrastruttura) |

**IL TESTO — verbatim, tedesco**
> *«Die diesem Gesetz unterstehenden Bundesbehörden legen den Quellcode von Software offen, die sie zur
> Erfüllung ihrer Aufgaben entwickeln oder entwickeln lassen, es sei denn die Rechte Dritter oder
> sicherheitsrelevante Gründe würden dies ausschliessen oder einschränken.»*

**LA PORTATA REALE — e la trappola**
🚨 **L'art. 9 impone di PUBBLICARE il codice sorgente del software che l'amministrazione sviluppa o fa
sviluppare. NON impone di USARE software open source.** È un obbligo di trasparenza sul software *prodotto*,
non un vincolo di approvvigionamento sul software *acquistato*. Eccezioni: diritti di terzi, ragioni di
sicurezza.
La Cancelleria federale ha prodotto una guida strategica e checklist operative per l'attuazione. Il
principio viene ora invocato per estensione anche a livello cantonale (mozione del PS per il Canton Zurigo
«analogamente all'art. 9 EMBAG»).

**FONTI**
- 🔗 https://parldigi.ch/de/embag/ — **tedesco**, Parlamentarische Gruppe Digitale Nachhaltigkeit (verbatim art. 9)
- 🔗 https://www.fedlex.admin.ch/ — **tedesco/francese/italiano**, testo di legge consolidato 🔴 **da aprire a mano**
- 🔗 https://www.netzwoche.ch/news/2025-04-03/open-source-grundsatz-gilt-bald-auch-fuer-dezentrale-bundesverwaltung — **tedesco**, estensione dal 1/5/2025

> ⚠️ **Da non dire in nessun caso**: «la Svizzera ha reso obbligatorio l'open source nella pubblica
> amministrazione». È l'errore più comune sulla stampa internazionale e ci farebbe smontare in dieci secondi
> dal caso 13, che segue.

---

## Caso 13 — 🔴 IL CONTRO-FATTO SVIZZERO: 54.000 postazioni su Microsoft 365, e cloud federale agli hyperscaler

| Campo | Contenuto |
|---|---|
| **NOME** | **Microsoft 365 nella Bundesverwaltung** + **«Public Clouds Bund»** |
| **PAESE** | 🇨🇭 Svizzera (Confederazione) |
| **TIPO** | ⚫ **Contro-fatto** — il Paese con la legge sull'open source è anche quello che ha appena finito di mettere l'amministrazione su Microsoft 365 |
| **STATO** | ✅ **CONCLUSO** — rollout M365 completato a **metà dicembre 2025** |
| **AFFIDABILITÀ** | **ALTA** su cifre e date (comunicato admin.ch, ripreso da Netzwoche/SRF) — 🔴 *il comunicato admin.ch ha restituito 403 al fetch: riaprirlo a mano* |
| **LIVELLO** | **1-2** |

**I FATTI**
- **24 giugno 2021**: nell'appalto «Public Clouds Bund» la Confederazione aggiudica a **AWS, IBM, Microsoft,
  Oracle** e all'hyperscaler cinese **Alibaba**. Accordo quadro **fino a 110 milioni di franchi su 5 anni**.
  Contratti firmati a **settembre 2022**. **Google escluso**: ricorre al Tribunale amministrativo federale il
  13/7/2021, si vede negare l'effetto sospensivo in ottobre 2021, **ritira il ricorso** a novembre 2021.
  I fornitori cloud svizzeri lamentarono che il bando li escludesse di fatto; l'**Incaricato federale della
  protezione dei dati (EDÖB)** formulò raccomandazioni **recepite solo in parte**.
- **Ottobre 2024**: inizia il rollout di **Microsoft 365** nell'amministrazione federale.
- **Metà dicembre 2025**: rollout **completato**. **Circa 54.000 postazioni** equipaggiate.
- La Cancelleria federale, per rispondere alle critiche, avvia il **«Proof of Concept BOSS»**
  (*Büroautomation durch Einsatz von Open-Source-Software*). **Esiti dello studio di fattibilità attesi a
  metà 2026** — attorno al **15 agosto 2026** secondo le ultime indicazioni.

**LE CRITICHE INTERNE — e sono di peso**
- Il **Capo dell'esercito, Thomas Süssli**, chiede pubblicamente una **strategia di uscita** da Microsoft 365,
  parlando di **«erhebliche Schwächung der digitalen Souveränität»** (rilevante indebolimento della sovranità
  digitale).
- Verdetto della NZZ am Sonntag sul lavoro di verifica delle alternative: **«Prüfung von
  Microsoft-Alternativen harzt»** — l'esame procede a rilento.

**FONTI**
- 🔗 https://www.admin.ch/de/newnsb/frKHCNmrngH8I3vO8ip7o — **tedesco**, comunicato ufficiale 🔴 *403 in fetch, aprire a mano*
- 🔗 https://www.netzwoche.ch/news/2023-02-15/bund-fuehrt-microsoft-365-definitiv-ein — **tedesco**
- 🔗 https://www.inside-it.ch/public-cloud-der-bund-hat-vertraege-mit-hyperscalern-unterzeichnet-20220927 — **tedesco**, firma contratti 27/9/2022
- 🔗 https://www.inside-it.ch/de/post/public-coud-bund-google-zieht-beschwerde-zurueck-20211112 — **tedesco**, ritiro ricorso Google
- 🔗 https://www.nzz.ch/schweiz/erhebliche-schwaechung-der-digitalen-souveraenitaet-armeechef-suessli-ist-mit-seiner-warnung-vor-microsoft-nicht-allein-ld.1909897 — **tedesco**, NZZ
- 🔗 https://www.bk.admin.ch/de/public-clouds-bund-2 — **tedesco**, Cancelleria federale

---

## Caso 14 — 🔥 Il Comando Cyber dell'esercito svizzero lascia Microsoft 365 per openDesk — citando il CLOUD Act

| Campo | Contenuto |
|---|---|
| **NOME** | **Kommando Cyber**, Esercito svizzero → **openDesk** |
| **PAESE** | 🇨🇭 Svizzera |
| **TIPO** | Migrazione a open source (A) + uscita da fornitore USA (B) |
| **STATO** | 🟡 **ANNUNCIATO / in avvio.** Partenza **autunno 2026** per il personale con «identità particolarmente protetta». **Non ancora realizzato.** |
| **AFFIDABILITÀ** | **MEDIA** — dichiarazioni del comandante riprese dalla stampa svizzera. 🔴 *Manca un documento ufficiale del DDPS letto in originale.* |
| **LIVELLO** | **5** |

**COSA È STATO ANNUNCIATO**
Il **Kommando Cyber** dell'esercito svizzero — **circa 800 professionisti a tempo pieno** e **circa 13.000
militi** — sostituisce Microsoft 365 con **openDesk**, la soluzione open source **tedesca** (caso 3).
Avvio in autunno 2026 per il personale con identità particolarmente protetta.

**LA MOTIVAZIONE — verbatim del comandante, Divisionär Simon Müller**
> *«Microsoft 365 è una soluzione molto buona, ma per un'armata come la nostra, che ha esigenze più elevate
> di riservatezza, disponibilità e integrità dei dati, non è adatta.»*

Le ragioni riportate: rischio di accesso ai dati da parte di **autorità e servizi statunitensi**, e il
timore di un **«kill switch» digitale**. La stampa svizzera collega esplicitamente la decisione al
**CLOUD Act**.

**FONTI**
- 🔗 https://www.watson.ch/wirtschaft/digital/546681426-schweizer-armee-setzt-auf-europaeische-software-statt-microsoft — **tedesco**
- 🔗 https://www.bluewin.ch/de/digital/warum-die-schweizer-armee-microsoft-den-stecker-zieht-li.3526829 — **tedesco**
- 🔗 https://www.nzz.ch/schweiz/erhebliche-schwaechung-der-digitalen-souveraenitaet-armeechef-suessli-ist-mit-seiner-warnung-vor-microsoft-nicht-allein-ld.1909897 — **tedesco**, NZZ

> 🎯 **È il singolo reperto più utile dell'intero fact pack per l'apertura del film.**
> Un **comando cyber militare europeo** dichiara pubblicamente che Microsoft 365 non è adatto alle proprie
> esigenze di riservatezza — e lo dice **cinque mesi dopo** che la stessa Confederazione ha finito di
> installare Microsoft 365 su 54.000 postazioni civili. Le due cose convivono nello stesso Stato, nello
> stesso anno. **La contraddizione non va risolta: va mostrata.**
> ⚠️ **Cautela obbligatoria**: è **annunciato**, non fatto. Dire «ha deciso di uscire», mai «è uscito».

---

# PARTE IV — PAESI BASSI

## Caso 15 — Il Parlamento olandese preme il freno: otto mozioni contro l'IT americana

| Campo | Contenuto |
|---|---|
| **NOME** | Le «cloudmoties» della Tweede Kamer |
| **PAESE** | 🇳🇱 Paesi Bassi |
| **TIPO** | Indirizzo politico verso fornitori europei (B) |
| **STATO** | ✅ **APPROVATE** — ma sono mozioni di indirizzo, non atti vincolanti. Il Governo le aveva **sconsigliate**. |
| **AFFIDABILITÀ** | **ALTA** sul fatto e sulla data · **MEDIA** sull'elenco puntuale delle otto |
| **LIVELLO** | indirizzo verso 4-5 |

**COSA È SUCCESSO**
- **13 marzo 2025**: dibattito plenario sulle **«Migraties van overheids-ICT naar het buitenland»**.
- **18 marzo 2025**: la Tweede Kamer approva **tutte e otto** le mozioni presentate. Il Segretario di Stato
  le aveva **sconsigliate** in aula.

**IL CONTENUTO (principali)**
1. Mozione **Barbara Kathmann** (GroenLinks-PvdA): impedire **migrazioni ICT non necessarie** verso i colossi
   tecnologici statunitensi.
2. Costituzione di una **rijkscloud** — infrastruttura cloud dello Stato **interamente sotto gestione
   olandese** — per i dati critici.
3. Sulla decisione di **SIDN** (il registro del dominio `.nl`) di spostare parte dell'infrastruttura **su AWS**:
   la catena DNS deve restare ospitata nei Paesi Bassi.
4. **Analisi di rischio e strategie di uscita per tutti i servizi cloud** dei colossi statunitensi.
5. Clausole nei contratti cloud a tutela di sovranità, continuità e protezione dei dati.
6. Rafforzamento di capacità e competenze interne all'amministrazione.
- **Successivamente**, mozione **Thijssen/Bruyning** (36 574, nn. 5 e 17): **almeno il 30% dei servizi di
  archiviazione cloud su suolo olandese/europeo entro il 2029**. ⚠️ Registrata come *«aangenomen en
  ontraden»* — **approvata, e sconsigliata dal Governo**.
- **18 dicembre 2025**: il Governo deposita la **«Visie Digitale autonomie en soevereiniteit van de
  overheid»** (doc. 2025D53291). 🔴 *Da leggere integralmente: è la fonte primaria olandese.*

**FONTI**
- 🔗 https://www.tweedekamer.nl/kamerstukken/plenaire_verslagen/kamer_in_het_kort/migraties-van-overheids-ict-naar-het-buitenland — **olandese**
- 🔗 https://zoek.officielebekendmakingen.nl/kst-26643-1427.html — **olandese**, atti ufficiali
- 🔗 https://www.tweedekamer.nl/kamerstukken/detail?id=2025D53291&did=2025D53291 — **olandese**, Visie, 18/12/2025 🔴 *da scaricare*
- 🔗 https://www.computable.nl/2025/03/18/ruim-baan-voor-eu-cloud-nu-tweede-kamer-op-stopknop-drukt/ — **olandese**, 18/3/2025

---

## Caso 16 — Lo Stato olandese sostituisce la postazione Microsoft: ~78.000 postazioni

| Campo | Contenuto |
|---|---|
| **NOME** | **Soevereine digitale werkplek** del Rijk |
| **PAESE** | 🇳🇱 Paesi Bassi |
| **TIPO** | Migrazione a open source (A) |
| **STATO** | 🟡 **ANNUNCIATO — sostituzione «stapsgewijs», componente per componente.** Primi utenti pilota. |
| **AFFIDABILITÀ** | **MEDIA** — lettera del ministro alla commissione parlamentare (23 giugno), letta tramite fonte secondaria 🔴 *recuperare la lettera originale* |
| **LIVELLO** | indirizzo verso **5** |

**COSA È STATO DECISO**
Il ministro **Heerma** annuncia in **lettera alla commissione permanente Affari digitali della Tweede Kamer
(23 giugno)** la sostituzione **graduale** della postazione di lavoro Microsoft dei dipendenti pubblici con
componenti **sovrani e open source**, mantenuti sotto controllo pubblico diretto.

**NUMERI, CAUTELE E CRITICITÀ**
- Perimetro: **circa 78.000 postazioni** presso i due principali fornitori ICT dello Stato.
- Modalità: **non** una sostituzione simultanea, ma **componente per componente**, partendo da gruppi di test.
- ⚠️ **Governance frammentata**: tre fornitori in parallelo — **DICTU, SSC-ICT, DUO**.
- ⚠️ **La Corte dei conti olandese** rileva rischi di continuità non risolti: tempi di ripristino garantiti a
  **16 ore** per guasti ordinari, **assenti** per crisi maggiori.

**FONTE**
- 🔗 https://www.floh.solutions/kennis/nieuws/rijk-vervangt-microsoft-werkplek-soevereine-digitale-werkplek — **olandese** 🟡 *secondaria; la lettera parlamentare è la fonte da recuperare*

---

## Caso 17 — Il Governo olandese firma con un fornitore tedesco (STACKIT)

| Campo | Contenuto |
|---|---|
| **NOME** | Accordo quadro Stato olandese – **STACKIT** |
| **PAESE** | 🇳🇱 Paesi Bassi (fornitore 🇩🇪) |
| **TIPO** | **Cambio di controllo: da fornitori USA a fornitore europeo (B)** |
| **STATO** | ✅ **FIRMATO** il 23 aprile 2026 — ⚠️ **ma l'adesione è facoltativa** |
| **AFFIDABILITÀ** | **ALTA** — annuncio ministeriale ripreso dalla NOS |
| **LIVELLO** | **5** |

**COSA PREVEDE**
**Raamovereenkomst** (accordo quadro) con **STACKIT** (Gruppo Schwarz, Germania), annunciato dal ministro
**van Weel** (Giustizia e Sicurezza) e dalla Segretaria di Stato **Willemijn Aerdts** (Economia digitale e
sovranità). Scopo dichiarato: **abbassare la soglia** perché i ministeri passino al cloud europeo.
- Archiviazione dei dati **esclusivamente nello Spazio economico europeo**.
- **Clausole risolutive** se il fornitore passa sotto **controllo extra-SEE**. 🎯 *È il requisito societario
  che manca al Regolamento ACN italiano (cfr. A7).*

⚠️ **LA CAUTELA DECISIVA — verbatim, olandese**:
> *«Overheidsorganisaties mogen zelf bepalen in hoeverre zij gebruikmaken van de diensten en zijn niet
> verplicht om over te stappen.»*
> *(Le amministrazioni decidono da sé in che misura usare i servizi e non sono obbligate a passare.)*

**Non è una migrazione: è un canale d'acquisto reso disponibile.** Va detto così.

**FONTE**
- 🔗 https://nos.nl/artikel/2611744-overheid-neemt-duitse-cloudleverancier-in-de-arm-wil-minder-afhankelijk-zijn-van-de-vs — **olandese**, NOS, 23/4/2026

---

## Caso 18 — Amsterdam: indipendenza dalle Big Tech americane entro il 2035

| Campo | Contenuto |
|---|---|
| **NOME** | Piano di autonomia digitale del Comune di **Amsterdam** |
| **PAESE** | 🇳🇱 Paesi Bassi |
| **TIPO** | Cambio di controllo (B) + open source (A) |
| **STATO** | 🟡 **ANNUNCIATO**, con scadenze e percentuali. Primo pilota nel 2026. |
| **AFFIDABILITÀ** | **ALTA** sul contenuto del piano (NOS, 3/2/2026) · **DA VERIFICARE** l'atto deliberativo comunale |
| **LIVELLO** | indirizzo verso 5 |

**LE TRE FASI**
1. **Dal 2026**: primo pilota di ambiente di lavoro su software non statunitense.
2. **Entro il 2031**: **almeno il 30%** del cloud comunale presso fornitori europei.
3. **Entro il 2035**: **nessuna informazione sensibile dei residenti di Amsterdam** su servizi cloud
   statunitensi.

**LA MOTIVAZIONE — verbatim dell'assessore Scholtes (delega ICT)**
> *«Se Trump impone sanzioni ai Paesi Bassi, dovremmo interrompere i servizi.»*
Cita come precedente le **sanzioni statunitensi contro i magistrati della Corte penale internazionale
dell'Aia**.

**FONTE**
- 🔗 https://nos.nl/artikel/2600808-amsterdam-wil-in-2035-onafhankelijk-zijn-van-amerikaanse-techbedrijven — **olandese**, NOS, 3/2/2026

> 🎯 **Il precedente CPI è materiale d'oro e già in linea con il dossier 13** (*interruzione servizi e
> identità digitale*). Un comune europeo motiva la propria politica IT citando **un caso reale di
> interruzione di servizio per ragioni politiche avvenuto sul proprio territorio**. Non è un'ipotesi: è
> successo all'Aia.

---

## Caso 19 — SURF: Nextcloud per università e ricerca

| Campo | Contenuto |
|---|---|
| **NOME** | **SURF** (cooperativa ICT di università e istituti di ricerca) — pilota **Nextcloud** |
| **PAESE** | 🇳🇱 Paesi Bassi |
| **TIPO** | Migrazione a open source (A) |
| **STATO** | 🟡 **PILOTA in corso**, aprile-dicembre 2026 |
| **AFFIDABILITÀ** | **MEDIA** |
| **LIVELLO** | **5** |

**COSA**: SURF offre agli istituti di istruzione e ricerca **Nextcloud** come alternativa aperta e sovrana
alle applicazioni Microsoft 365 (videoscrittura, condivisione documenti, integrazione posta, riunioni online).
**NUMERI**: pilota da **aprile a dicembre 2026**; reclutamento di **circa 2.000** fra docenti, ricercatori e
personale. Partecipa fra le altre **ArtEZ University of the Arts**. La cooperativa **SIVON** (scuole) lavora
su servizi analoghi.

**FONTI**
- 🔗 https://www.security.nl/posting/914382/SURF+biedt+onderwijsinstellingen+Nextcloud+voor+digitale+soevereiniteit — **olandese**
- 🔗 https://www.ru.nl/medewerkers/actuele-themas/digitale-soevereiniteit-nextcloud-pilot — **olandese**, Radboud
- 🔗 https://www.cursor.tue.nl/en/news/2025/november/week-4/surf-seeks-testers-for-a-microsoft-alternative — **inglese/olandese**, TU Eindhoven

---

# PARTE V — BELGIO E LUSSEMBURGO

## Caso 20 — ⚠️ Clarence: il «primo cloud sovrano europeo» gira su Google

| Campo | Contenuto |
|---|---|
| **NOME** | **Clarence SA** — joint venture **LuxConnect** (60%) / **Proximus Luxembourg** (40%) |
| **PAESE** | 🇱🇺 Lussemburgo (con 🇧🇪) |
| **TIPO** | Cambio di controllo operativo (B) — **non** open source |
| **STATO** | ✅ **OPERATIVO.** Partnership con il Governo lussemburghese firmata il **23 gennaio 2025**; adottato dalla **CSSF** (dicembre 2024); nel consorzio aggiudicatario della gara UE (aprile 2026). |
| **AFFIDABILITÀ** | **ALTA** sui fatti · 🔴 **La descrizione della tecnologia richiede una verifica finale sul contratto, non sui comunicati** |
| **LIVELLO** | **4 — cloud di fiducia. NON livello 5.** |

**COSA È**
Cloud **«disconnesso»** (*air-gapped*), installato in **due data center Tier IV di LuxConnect** in Lussemburgo,
gestito localmente e isolato da internet e da terzi. **LuxConnect è al 100% dello Stato lussemburghese.**
Il Governo ha firmato per l'uso da parte del **CTIE** (Centro delle tecnologie dello Stato), che «supervisiona
direttamente» la gestione tecnica e operativa dell'infrastruttura.

🚨 **IL PUNTO CHE CAMBIA LA CLASSIFICAZIONE**
La piattaforma è costruita su **Google Distributed Cloud Hosted**. È stata presentata pubblicamente il
**25 ottobre 2023** in occasione del **Google Distributed Cloud Launch Event**. Esiste un collegamento
controllato («airgap») con Google **per gli aggiornamenti**, e ogni aggiornamento è **ispezionato dai team
lussemburghesi** prima dell'applicazione.

🔴 **REPERTO DA VERIFICARE E, SE CONFERMATO, DA USARE**: il comunicato ufficiale del Governo lussemburghese
del 23/1/2025, letto integralmente, **non nomina mai Google**. Parla di «controllo totale dei dati»,
«autonomia operativa completa», «sovranità indefettibile». La tecnologia sottostante compare sui materiali
di LuxConnect e Proximus, non su quelli del Governo.
⚠️ **Formulazione corretta**: *il comunicato governativo non menziona il fornitore della tecnologia*.
**Non** «il Governo lo ha nascosto» — è un'inferenza sull'intenzione che non possiamo dimostrare.

**FONTI**
- 🔗 https://mindigital.gouvernement.lu/en/actualites.gouvernement2024+en+actualites+toutes_actualites+communiques+2025+01-janvier+23-obertin-clarence-cloud.html — **inglese/francese**, Ministero della digitalizzazione, 23/1/2025
- 🔗 https://www.luxconnect.lu/clarence/ e https://clarence-cloud.com/en/solution/ — **inglese**, gestore (tecnologia Google Distributed Cloud Hosted)
- 🔗 https://www.cssf.lu/en/2024/12/the-cssf-adopts-clarence-to-develop-artificial-intelligence-with-full-sovereignty-a-major-breakthrough-for-the-financial-sector/ — **inglese**, autorità di vigilanza finanziaria, dicembre 2024
- 🔗 https://delano.lu/article/new-made-in-luxembourg-cloud-c — **inglese**

---

## Caso 21 — Proximus (Belgio): sovrano con Microsoft *e* con Google, contemporaneamente

| Campo | Contenuto |
|---|---|
| **NOME** | **Proximus NXT** — offerte «sovereign cloud» |
| **PAESE** | 🇧🇪 Belgio (+ 🇱🇺) |
| **TIPO** | Cambio di controllo operativo (B) |
| **STATO** | ✅ **Operativo / in espansione** |
| **AFFIDABILITÀ** | **ALTA** — comunicati societari datati |
| **LIVELLO** | **4** (entrambe le linee) |

**COSA HA FATTO**
Proximus — operatore telecom belga a partecipazione pubblica — offre **due** cloud «sovrani», entrambi
costruiti su tecnologia statunitense in licenza:
- **Con Google Cloud**: accordo **quinquennale** per servizi cloud sovrani in Belgio e Lussemburgo, basato su
  **Google Distributed Cloud Hosted** («disconnected sovereign cloud») per governi, imprese regolate e
  organizzazioni internazionali.
- **Con Microsoft** (maggio 2026): rafforzamento della partnership strategica, basato su **Azure Local
  disconnected operations** — ambienti cloud autonomi, disconnettibili temporaneamente o permanentemente dal
  cloud pubblico, mantenendo i servizi essenziali di Azure.

**FONTI**
- 🔗 https://www.proximus.com/news/2026/202605-microsoft-proximus-nxt-reinforce-strategic-partnership.html — **inglese**, maggio 2026
- 🔗 https://www.proximusnxt.lu/en/proximus-and-google-cloud-deliver-sovereign-cloud-services-belgium-and-luxembourg — **inglese**
- 🔗 https://www.datacenterdynamics.com/en/news/proximus-group-partners-with-google-for-sovereign-cloud-offerings-in-belgium-and-luxembourg/ — **inglese**

> 🎯 **Questo caso vale come *definizione operativa* di «sovranità di facciata» — ma con onestà.**
> Lo stesso operatore vende «cloud sovrano» su tecnologia Google **e** su tecnologia Microsoft.
> ⚖️ **Il contro-argomento va dato**: nel modello *disconnected/air-gapped*, la separazione tecnica è reale e
> l'operatore è europeo — è il **livello 4** della nostra scala, cioè **il modello 21Vianet applicato in
> Europa**, che il film già presenta come prova che «si può fare». Non è finzione. **Semplicemente non è il
> livello 5**, e i canoni di licenza continuano a uscire verso gli Stati Uniti. **È l'esempio perfetto per
> mostrare al pubblico la differenza fra i due gradini.**

---

## Caso 22 — La gara UE da 180 milioni: come l'Europa ha classificato sé stessa

| Campo | Contenuto |
|---|---|
| **NOME** | **Cloud Sovereignty Framework / SEAL** — gara della Commissione europea |
| **PAESE** | 🇪🇺 (aggiudicatari 🇱🇺🇫🇷🇩🇪🇧🇪) |
| **TIPO** | Cambio di controllo (B) — **è il primo appalto in cui la sovranità è criterio di aggiudicazione misurato** |
| **STATO** | ✅ **AGGIUDICATA** il 17 aprile 2026 |
| **AFFIDABILITÀ** | **ALTA** — comunicati della Commissione, datati |
| **LIVELLO** | vedi sotto |

**LA SCALA SEAL** (Sovereignty Effectiveness Assurance Levels), da **SEAL-0** (assenza totale di sovranità) a
**SEAL-4** (catena di fornitura interamente UE, **dai chip al software**). Otto obiettivi: strategici,
giuridici, operativi, ambientali, trasparenza della catena di fornitura, apertura tecnologica, sicurezza,
conformità al diritto UE. Soglia di ammissione: **SEAL-2** (*Data Sovereignty*).

**I QUATTRO AGGIUDICATARI — 180 milioni €, sei anni**

| Aggiudicatario | Composizione | SEAL |
|---|---|---|
| Consorzio **Post Telecom** 🇱🇺 | + OVHcloud 🇫🇷, Clever Cloud 🇫🇷 | **SEAL-3** |
| **STACKIT** 🇩🇪 | Gruppo Schwarz | **SEAL-3** |
| **Scaleway** 🇫🇷 | Gruppo Iliad | **SEAL-3** |
| Consorzio **Proximus** 🇧🇪 | + **S3NS** (Thales/Google), **Clarence**, **Mistral** | **SEAL-2** |

**LA CRITICA — da riportare**
**CISPE** (associazione di 38 fornitori cloud europei) contesta il quadro: riconoscere S3NS come sovrana
«sebbene sfrutti la tecnologia cloud di Google» è **«chiaramente un'autolesione»** (*self-harm*).
**La replica di S3NS, da dare**: è un'entità francese **interamente controllata da Thales**, con dipendenti
europei in Francia, infrastrutture **fisicamente segregate** e operazioni condotte **esclusivamente da
personale S3NS**.

🚨 **IL PUNTO STRUTTURALE, ED È NOSTRO**: **nessun aggiudicatario ha raggiunto SEAL-4.** Il livello che
richiede una catena di fornitura interamente europea **dai chip al software** esiste sulla carta e **non è
stato raggiunto da nessuno** nel primo appalto in cui la Commissione ha misurato la sovranità.

**FONTI**
- 🔗 https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_en — **inglese**, Commissione europea, 17/4/2026
- 🔗 https://commission.europa.eu/news-and-media/news/sovereign-cloud-framework-explained-2026-06-01_en — **inglese**, spiegazione del quadro SEAL, 1/6/2026
- 🔗 https://commission.europa.eu/news-and-media/news/commission-moves-forward-cloud-sovereignty-eur-180-million-tender-2025-10-10_en — **inglese**, bando, 10/10/2025
- 🔗 https://www.theregister.com/2026/04/20/europe_picks_4_sovereign_cloud/ — **inglese**, 20/4/2026 (critica CISPE + replica S3NS)

> ⚠️ **Segnalazione utile**: la piattaforma belga **BeLibre** ha pubblicato *«L'Europa misura la sovranità
> digitale. Perché non pubblica i risultati?»* (21/4/2026) — i **punteggi SEAL analitici** dei singoli
> partecipanti non sono stati resi pubblici.
> 🔗 https://belibre.be/nl/soevereiniteit/2026-04-21-europese-soevereine-cloud/ — **olandese**

---

## Caso 23 — Belgio: iniziative in fase iniziale

| Campo | Contenuto |
|---|---|
| **NOME** | Ecosistema belga della sovranità digitale (**BeLibre**, **OSBA belga**, **Smals Research**) |
| **PAESE** | 🇧🇪 Belgio |
| **TIPO** | Indirizzo / advocacy (A) |
| **STATO** | 🟡 **Iniziale.** Nessuna migrazione federale belga con numeri accertati rinvenuta. |
| **AFFIDABILITÀ** | **DA VERIFICARE** |
| **LIVELLO** | n/a |

**COSA C'È**
- **7 maggio 2026**: evento **«Advancing Digital Sovereignty Initiatives in Belgium»** organizzato da BeLibre —
  temi: software open source, ruolo di organizzazioni e imprese, ostacoli incontrati.
- **Christopher Peeters** guida la costituzione di una **Open Source Business Alliance belga**.
- **Smals Research** (centro di ricerca dell'IT della sicurezza sociale belga) ha una linea di lavoro
  dedicata alla sovranità digitale.
- Sul piano operativo, il contributo belga di rilievo è **Proximus** (casi 21-22).

🔴 **LACUNA DICHIARATA**: **non ho trovato una decisione del governo federale belga di migrazione a open
source o a fornitori europei con numeri verificabili.** Se serve al film, va cercata direttamente su
`bosa.belgium.be` (Servizio pubblico federale Strategia e Supporto) e negli atti della Camera.

**FONTI**
- 🔗 https://data-en-maatschappij.ai/publicaties/verslag-advancing-digital-sovereignty-initiatives-in-belgium — **olandese**
- 🔗 https://www.smalsresearch.be/digitale-soevereiniteit/ — **olandese**
- 🔗 https://belibre.be/ — **olandese/francese**

---

# QUADRO DI SINTESI

## Tabella comparativa — dove sta ciascuno

| # | Caso | Paese | Tipo | Stato | Numeri chiave | Liv. |
|---|---|---|---|---|---|---|
| 1 | Schleswig-Holstein | 🇩🇪 | A | **in corso** (LibreOffice ~concluso, Linux pilota) | ~80% postazioni · 44.000 caselle · 15 mln € risparmiati | 5 |
| 2 | **Dataport Phoenix** | 🇩🇪 | A | 🔴 **fallito** (ott. 2024) | 140 mln € spesi · **90 mln € persi** | — |
| 3 | ZenDiS / openDesk | 🇩🇪 | A | in corso | 80-100.000 postazioni ⚫ · BMDS: 80 | 5 |
| 4 | **BwMessenger** | 🇩🇪 | A+B | ✅ **concluso** (2020) | **>100.000 utenti** · VS-NfD | 5 |
| 5 | **BW, docenti** | 🇩🇪 | A | ✅ **in produzione** (2024) | **~60.000 docenti** | 5 |
| 6 | **Spesa Microsoft del Bund** | 🇩🇪 | ⚫ contro-fatto | accertato | **481,4 mln € (2025), +75,6% in 2 anni** | 1-2 |
| 7 | **LiMux Monaco** | 🇩🇪 | A | 🔴 **fallito** (2017) → riavviato (2026) | 14.800 desktop · **86-89 mln €** per tornare a Windows | 5→1→? |
| 8 | Sovereign Tech Agency | 🇩🇪 | A | operativa | ~23,5 mln € su ~60 tecnologie · **domanda 114 mln €** | n/a |
| 9 | STACKIT | 🇩🇪 | B | operativo | 23.000 server · 1,9 mld € · **SEAL-3** | 5 |
| 10 | **Bundesheer** | 🇦🇹 | A | in corso | **16.000 postazioni** | 5 |
| 11 | BMWET → Nextcloud | 🇦🇹 | A | in corso | SharePoint dismesso Q1 2026 | 5 |
| 12 | **EMBAG art. 9** | 🇨🇭 | A (parziale) | ✅ in vigore 1/1/2024 | ⚠️ **pubblicare ≠ usare** | n/a |
| 13 | **M365 + Public Clouds Bund** | 🇨🇭 | ⚫ contro-fatto | ✅ concluso dic. 2025 | **54.000 postazioni** · 110 mln CHF a AWS/IBM/MS/Oracle/Alibaba | 1-2 |
| 14 | **Kommando Cyber → openDesk** | 🇨🇭 | A+B | 🟡 **annunciato** (autunno 2026) | 800 prof. + 13.000 militi | 5 |
| 15 | Otto mozioni | 🇳🇱 | B | ✅ approvate 18/3/2025 | +30% cloud UE entro 2029 | → 4-5 |
| 16 | Postazione sovrana del Rijk | 🇳🇱 | A | 🟡 annunciato | **~78.000 postazioni** | → 5 |
| 17 | **Rijk ↔ STACKIT** | 🇳🇱 | **B** | ✅ firmato 23/4/2026 | ⚠️ **adesione facoltativa** | 5 |
| 18 | **Amsterdam 2035** | 🇳🇱 | A+B | 🟡 annunciato | 30% entro 2031 · 100% dati sensibili entro 2035 | → 5 |
| 19 | SURF Nextcloud | 🇳🇱 | A | 🟡 pilota | ~2.000 partecipanti | 5 |
| 20 | **Clarence** | 🇱🇺 | B | ✅ operativo | ⚠️ **Google Distributed Cloud Hosted** | **4** |
| 21 | Proximus sovereign | 🇧🇪 | B | operativo | Google **e** Microsoft, in parallelo | **4** |
| 22 | **Gara UE 180 mln** | 🇪🇺 | B | ✅ aggiudicata 17/4/2026 | 3× SEAL-3, 1× SEAL-2 · **0× SEAL-4** | 4-5 |
| 23 | Ecosistema belga | 🇧🇪 | A | iniziale | — | n/a |

## Le cinque conclusioni che reggono

**1. L'unica migrazione conclusa e su larga scala non è un ministero: è un esercito.**
BwMessenger, oltre 100.000 utenti, dal 2020, certificato per il materiale classificato. E l'esercito
austriaco lo segue su LibreOffice (16.000 postazioni), e il comando cyber svizzero su openDesk. **Tre
eserciti europei si tolgono dalla dipendenza mentre le amministrazioni civili la aumentano.**

**2. Ogni Paese di quest'area contiene contemporaneamente la migrazione e il suo contrario.**
La Germania costruisce openDesk e nel 2025 spende **481 milioni** in licenze Microsoft. La Svizzera scrive
l'EMBAG e nel dicembre 2025 finisce di installare Microsoft 365 su **54.000 postazioni**. Non sono
incoerenze da spiegare: **sono il fatto principale**.

**3. La sovranità digitale è reversibile — in entrambe le direzioni.**
Monaco: pioniera (2006), disfatta (2017, ~89 mln € per tornare indietro), ricostituita come indirizzo
politico (2026). Nessun risultato è acquisito. È l'argomento più onesto che il film possa fare, ed è anche
il più scomodo per chi promette che «basta decidere».

**4. Quando una migrazione open source fallisce, non fallisce il software.**
Phoenix: 90 milioni persi per pianificazione irrealistica, controllo interno assente, integrazione
sottostimata — parole della **Corte dei conti**, non di un critico. Monaco: **il 68,6% dei dipendenti era
soddisfatto del software**, il 32% dell'organizzazione. **Il punto di rottura è sempre la governance.**

**5. Il «cloud sovrano» europeo, nella sua forma oggi prevalente, è tecnologia americana operata da europei.**
Clarence, S3NS, Proximus-Azure: **livello 4**, non 5. Non è finzione — la separazione è reale, ed è il
modello che il film già cita come prova che si può fare. Ma **nessuno degli aggiudicatari della gara europea
ha raggiunto SEAL-4**, il livello con catena di fornitura interamente UE. **L'Europa ha definito il livello
massimo di sovranità e non l'ha raggiunto nemmeno una volta nel primo appalto in cui l'ha misurato.**

## 🔴 Da verificare prima della messa in onda

| # | Cosa | Dove |
|---|---|---|
| V1 | **Cifre openDesk** (80.000 vs 100.000): fonte primaria | Bundestag Drucksache **21/5502** (22/4/2026), PDF da aprire a mano |
| V2 | Testo integrale del rilievo su Phoenix | **Jahresbericht 2026** Rechnungshof Hamburg, **pp. 75-81** |
| V3 | Testo consolidato **art. 9 EMBAG** | fedlex.admin.ch (richiede JavaScript) |
| V4 | **Erster Fortschrittsbericht Digitale Souveränität** austriaco | parlament.gv.at, XXVIII/SONS/20 |
| V5 | Lettera del ministro Heerma alla Tweede Kamer (23 giugno) | tweedekamer.nl |
| V6 | **Visie Digitale autonomie** (18/12/2025) | doc. 2025D53291 |
| V7 | Comunicato admin.ch sul completamento M365 (403 in fetch) | admin.ch |
| V8 | Risposta governativa all'interrogazione **Lenhard** (spesa Microsoft) | dip.bundestag.de |
| V9 | Atto ufficiale del **DDPS** sul Kommando Cyber → openDesk | vbs.admin.ch |
| V10 | Esiste una decisione **federale belga** con numeri? | bosa.belgium.be, atti della Camera |
| V11 | Trasferimento sede Microsoft a Monaco nel 2016: confermare o **omettere** | — |

---

# IPOTESI DI INSERIMENTO NEL DOCUMENTARIO

## ① Kommando Cyber svizzero → **ATTO 0 — LA PROVA** (0:00-1:30) o **ATTO 5-BIS**

**Funzione narrativa: la conferma esterna, da un soggetto insospettabile.**
L'Atto 0 apre con i record MX italiani: un fatto tecnico che chiunque può ripetere. Il rischio è che il
pubblico legga tutto il film come una polemica italiana. **Una singola frase svizzera lo disinnesca:**

> *Nell'autunno del 2026 il Comando Cyber dell'esercito svizzero smetterà di usare Microsoft 365.
> Il suo comandante ha detto perché: «Microsoft 365 è una soluzione molto buona, ma per un'armata come la
> nostra, che ha esigenze più elevate di riservatezza, disponibilità e integrità dei dati, non è adatta.»*

**Perché funziona**: non è un attivista, non è un concorrente, non è un politico. È **un militare neutrale
che dice la stessa cosa che diciamo noi, e la dice prima di noi.** In alternativa sta benissimo in **Atto
5-BIS** (*Non è un'ipotesi: è già successo*), dove il timore del *kill switch* trova un soggetto istituzionale
che lo dichiara.
⚠️ **Vincolo**: è annunciato, non fatto. La frase deve dire **«smetterà»**, mai «ha smesso».

## ② Baden-Württemberg, 60.000 docenti → **ATTO 10 — I FIGLI** (17:00-18:00)

**Funzione narrativa: la prova che si può fare, esattamente dove il film dice che non si fa.**
L'Atto 10 è quello sulla scuola, il più emotivo e il più esposto all'obiezione *«e allora cosa dovremmo
fare, tornare alla carta?»*. Il registro delle trappole (n. 15) già indica il Baden-Württemberg come **il
caso solido**. Ma finora è solo il caso di **un divieto**. **Questo è il seguito:**

> *Il Land tedesco che disse no a Microsoft nelle scuole non si è fermato al divieto.
> Ha costruito l'alternativa. Da due anni ci lavorano sessantamila insegnanti.
> E il giorno del passaggio non è cambiato nemmeno il loro indirizzo email.*

**Perché funziona**: chiude la domanda con un numero, una data e un dettaglio concreto (gli indirizzi che non
cambiano) che rende il tutto **fisicamente immaginabile**. Trasforma l'Atto 10 da denuncia a dimostrazione,
senza aggiungere trenta secondi.

## ③ Monaco, l'arco intero → **ATTO 6 — LA SVOLTA: ERA UNA SCELTA** (10:30-11:45)

**Funzione narrativa: il contro-esempio che vaccina il film.**
L'Atto 6 dice: *«Si poteva fare. Qualcuno l'ha fatto. Non è un destino tecnologico: è una decisione.»*
È vero, ed è il punto giusto — ma è **unilaterale**, e uno spettatore informato pensa subito «e Monaco?».
**Meglio dirlo noi:**

> *Monaco di Baviera l'aveva fatto. Quattordicimilaottocento computer su Linux, dal 2006.
> Nel 2017 un cambio di maggioranza in consiglio comunale l'ha disfatto: ottantasei milioni di euro
> per tornare a Windows. Il sondaggio interno diceva che il settanta per cento dei dipendenti era
> soddisfatto del software. Insoddisfatto dell'organizzazione, non del software.
> Nel maggio del 2026 la nuova coalizione ha rimesso l'open source come regola.
> **Se è una decisione, allora si può decidere anche il contrario. Ed è già successo.**

**Perché funziona**: è l'inserimento che **aumenta** la credibilità del film invece di diluirla — la stessa
logica del contro-fatto QC4 (trappola 10) e dell'inciso *«ma ciò non si è ancora mai verificato»* (trappola 6).
Un documentario che cita LiMux **prima** che glielo obiettino non può più essere accusato di aver scelto
solo i successi. E la frase finale rafforza la tesi dell'Atto 6 anziché indebolirla.

## ④ Il contro-fatto della spesa tedesca → **ATTO 7 — LO STATO CERTIFICA, E NON SA** (11:45-14:00)

**Funzione narrativa: dato di scala, e la prova che l'opacità italiana non è un'anomalia italiana.**
L'Atto 7 poggia su A9: 1,343 miliardi tracciati senza **nessun campo fornitore**, l'opacità come fatto
verificabile. La replica prevedibile è *«è un problema della burocrazia italiana»*. **Non lo è:**

> *In Germania la domanda è stata fatta in Parlamento. La risposta c'è:
> duecentosettantaquattro milioni nel 2023, trecentoquarantasette nel 2024,
> **quattrocentottantuno milioni nel 2025.** Solo licenze Microsoft. Solo il governo federale.
> Per i Länder e i comuni — testuale — **il governo federale non ha cifre attendibili.**
> La Germania sa quanto spende lo Stato centrale, e non sa quanto spende il Paese.
> **L'Italia non sa nemmeno la prima cosa.**

**Perché funziona**: è **comparativo e quantificato**, chiude la scappatoia dell'eccezionalismo, e regge un
grafico a tre barre di quattro secondi. Ed è a costo narrativo quasi nullo: tre numeri e una data.

## ⑤ Clarence / SEAL-4 → **ATTO 11 — LA VIA D'USCITA** (18:00-20:00)

**Funzione narrativa: dare corpo alla distinzione fra i due gradini della scala — che la
«CORREZIONE APERTA» del documento di stato chiede esplicitamente di introdurre.**
Lo `STATO DELLE CONOSCENZE` registra che l'Atto 11 presenta **una sola** via d'uscita (il livello 4, cloud di
fiducia) e ne manca un'altra, il livello 5. Il Benelux fornisce **entrambe le facce in un unico blocco di
venti secondi**, con nomi e date:

> *In Lussemburgo lo Stato ha il suo cloud sovrano. Si chiama Clarence, i data center sono dello Stato,
> lo gestiscono tecnici lussemburghesi, ed è staccato da internet. **Dentro c'è tecnologia Google.**
> Non è un trucco: è il modello che funziona, ed è lo stesso della Cina e della Francia.
> Ma nell'aprile del 2026 la Commissione europea ha misurato per la prima volta la sovranità dei suoi
> fornitori, su una scala da zero a quattro.
> **Nessuno dei vincitori ha raggiunto il quattro.**
> Il quattro richiede una catena europea dai chip al software. Esiste sulla carta.
> **E nel primo appalto in cui l'Europa l'ha misurato, non l'ha raggiunto nessuno.**

**Perché funziona**: (a) rende **visiva e non teorica** la differenza fra livello 4 e livello 5, che il
progetto ha già in scheda ma non in sceneggiatura; (b) **evita il trionfalismo** proprio nell'atto conclusivo,
che è dove il rischio è massimo; (c) la chiusura *«non l'ha raggiunto nessuno»* è del tutto coerente con il
finale fattuale — non prescrittivo — che la CORREZIONE APERTA raccomanda.
⚠️ **Vincolo**: dire **«dentro c'è tecnologia Google»**, non «è Google». Il comunicato del Governo
lussemburghese non nomina Google: riportare che **non lo nomina**, non che lo abbia nascosto.

---

*Fine fact pack 16. Ricerca svolta il 2 agosto 2026. Ventitré casi, di cui due fallimenti documentati e due
contro-fatti. Undici verifiche aperte elencate sopra.*
