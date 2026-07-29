# FACT PACK — Lo strato italiano: chi rivende, chi gestisce, chi controlla

**Stato: PARZIALE.** Il PSN è documentato su fonte primaria. L'elenco sistematico dei rivenditori
è ancora da chiudere sul catalogo ACN dei servizi qualificati (v. §5).
Compilato il 28 luglio 2026.

---

## 1. LA TESI DA VERIFICARE

Tesi di partenza: *«i partner italiani che rivendono cloud USA sono meri rivenditori: il sottostante
resta al 100% sotto gestione discrezionale dell'azienda statunitense e quindi sotto CLOUD Act.»*

**Esito della verifica: la tesi è VERA per una parte dello strato italiano, ma NON per tutto.**
Usarla indistintamente ci espone a una replica tecnica fondata. Serve una tassonomia.

---

## 2. TASSONOMIA — quattro modelli, quattro livelli di esposizione

| | Modello | Chi controlla il sottostante | Esposizione a giurisdizione USA |
|---|---|---|---|
| **A** | **Infrastruttura propria italiana/europea** (es. Aruba, Seeweb, Register, Irideos e altri operatori con data center e stack propri) | l'operatore italiano | **Nessuna** per via del fornitore. È la prova che l'alternativa esiste |
| **B** | **Operatore che gestisce e integra tecnologia hyperscaler, con custodia delle chiavi** (es. PSN — *Secure Public Cloud*) | infrastruttura del CSP, **chiavi fuori dal perimetro CSP** | **Mitigata tecnicamente**, non esclusa giuridicamente (v. §4) |
| **C** | **Regione hyperscaler in Italia con partner locale** (es. Google Cloud con TIM/Noovle; regioni Azure/AWS in Italia) | il fornitore statunitense (tecnologia e piano di controllo) | **Piena** |
| **D** | **Rivenditore / distributore / system integrator** (licenze e servizi gestiti su Microsoft 365, Azure, GCP, AWS) | il fornitore statunitense | **Piena** — lo strato italiano è **commerciale**, non tecnico |

**Il punto che regge in trasmissione**, e vale per C e D:
> Il rivenditore cambia **chi ti fattura**, non **chi ha il controllo**. Il contratto è italiano;
> il piano di controllo, gli aggiornamenti, l'accesso amministrativo e — salvo custodia esterna delle
> chiavi — la possibilità di decifrare restano del fornitore statunitense.

---

## 3. IL PSN USA OGNI HYPERSCALER — fonte primaria

**AFFERMAZIONE** — Il Polo Strategico Nazionale eroga servizi costruiti sulla tecnologia dei principali
CSP statunitensi. Lo dichiara il PSN stesso.

| Servizio PSN | CSP impiegati |
|---|---|
| Public Cloud PSN Managed | **Oracle**, **Google** |
| Hybrid Cloud | **Microsoft Azure** |
| Secure Public Cloud | **AWS**, **Microsoft Azure**, **Google Cloud** |

**VERBATIM (dal sito PSN)** — «These services, currently created in partnership with Oracle, Google,
Microsoft Azure, AWS, may also be provided with other Cloud Service Providers in the future.»

**Ubicazione** — «PSN Data Centers or Italian regions»; per il Secure Public Cloud: «provided by public
Cloud Service Providers in Italy».

**Ruolo del PSN** — gestore e integratore, non semplice rivenditore: «managed by personnel of Polo
Strategico Nazionale with logical-physical separation».

**FONTE** — `https://www.polostrategiconazionale.it/en/solutions/cloud-services-with-csp/`
**AFFIDABILITÀ — ALTA** (fonte primaria, il soggetto stesso).

**Rilievo per il documentario** — L'infrastruttura che si chiama *Polo Strategico **Nazionale***
è costruita, per esplicita ammissione, sulla tecnologia dei quattro grandi fornitori statunitensi.
Non è un'illazione: è la loro pagina istituzionale.

---

## 4. LA DIFESA DEL PSN — e come va trattata onestamente

Il PSN dichiara due mitigazioni tecniche serie, che **non possiamo ignorare**:

**VERBATIM** — «Encryption-key management **outside the CSP's control perimeter**»
**VERBATIM** — «Confidential computing, **where activated**, makes it impossible for cloud service provider
operators to access even the data during processing»

**Valutazione onesta.** Se implementata correttamente, la custodia delle chiavi fuori dal perimetro del
fornitore è una difesa reale: un ordine emesso ai sensi del CLOUD Act obbliga il provider a consegnare
ciò che ha in *possesso, custodia o controllo* — se il provider non può decifrare, consegna cifrato.
È l'approccio **tecnico** allo stesso problema che la Francia affronta per via **giuridica** con SecNumCloud.

**Ma restano tre riserve legittime, da porre come domande e non come accuse:**
1. **«Where activated»** — il confidential computing è dichiarato *condizionale*, non predefinito.
   Su quali servizi è attivo e su quali no?
2. **Piano di controllo** — la custodia delle chiavi protegge il *dato*; non cambia chi opera l'hypervisor,
   chi distribuisce gli aggiornamenti, chi ha accesso amministrativo all'infrastruttura.
3. **Nessun riferimento al CLOUD Act** — nella pagina non compare alcuna menzione della giurisdizione
   extra-UE o del CLOUD Act. La protezione è presentata in termini di sicurezza, non di giurisdizione.

⚠️ **Regola editoriale**: al PSN va chiesta risposta su questi tre punti *prima* della messa in onda.
Se rispondono, è materiale; se non rispondono, è materiale ugualmente.

---

## 5. IL DATO CHE REGGE MEGLIO DI TUTTI: 280 contro 12.700

Anche concedendo al PSN le sue protezioni **nella loro versione migliore**, esse coprono una frazione
minima della migrazione celebrata il 21 luglio 2026:

| Destinazione | Enti | Regime |
|---|---|---|
| **PSN** (misura PNRR 1.1) | **oltre 280** PA centrali, ASL e aziende ospedaliere | protezioni PSN (chiavi, confidential computing) |
| **«Cloud qualificati»** (misura PNRR 1.2) | **oltre 12.700** PA locali **e scuole** | qualificazione ACN — **senza** clausola di immunità nota (v. dossier 06) |

> Le tutele più forti riguardano **il 2% degli enti migrati**. Il restante 98% — compresi tutti gli
> istituti scolastici — è finito su cloud qualificati secondo un regime che, per quanto verificato
> finora, non prevede alcun requisito di immunità dalle leggi extra-UE.

**AFFIDABILITÀ — ALTA** sui numeri (dichiarazione governativa del 21/07/2026, dossier 06).
**DA VERIFICARE** l'assenza della clausola nel regime ACN sul testo del DD 21007/24 (dossier 06 §2.2).

---

## 6. DA FARE — l'elenco sistematico dei fornitori

L'elenco “dei rivenditori italiani” **non va costruito dai siti commerciali**: la fonte autorevole per il
contesto PA è il **catalogo ACN dei servizi cloud qualificati** (lead non verificato: ~2.285 voci).
Per ciascun servizio qualificato occorre determinare:

- [ ] fornitore contrattuale (ragione sociale italiana);
- [ ] **tecnologia sottostante** (infrastruttura propria? Azure/AWS/GCP/Oracle?);
- [ ] classificazione della voce secondo la tassonomia A/B/C/D del §2;
- [ ] classi di dati ammesse.

Solo così si ottiene un numero difendibile: *«su N servizi qualificati per la PA italiana, M poggiano su
tecnologia statunitense»*. **Finché quel conteggio non esiste, non si citano numeri sui rivenditori.**

Da verificare inoltre sul PSN: composizione societaria e quote (TIM, Leonardo, CDP Equity, Sogei),
e la notizia dell'ingresso di AWS nel PSN (fonte stampa: Startmag — da confermare su fonte primaria).

**Operatori con infrastruttura propria** (categoria A) da censire e verificare uno per uno: sono la prova
narrativa che l'alternativa italiana esiste, e senza di essi il documentario risulterebbe difensivo.
