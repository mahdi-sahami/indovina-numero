#  Indovina Numero

**Indovina Numero** è un gioco da riga di comando sviluppato in **Python**, progettato con un approccio professionale basato su **Object-Oriented Programming (OOP)** e sui principi di progettazione **SOLID** e **SCO (Separation of Concerns)**.

Questo progetto fa parte del mio portfolio e rappresenta il mio modo di scrivere codice: strutturato, leggibile, manutenibile e pronto per essere esteso — anche quando il problema da risolvere è semplice.

---

##  Descrizione del Progetto

In *Indovina Numero*, il computer cerca di indovinare il numero che l’utente ha scelto mentalmente all’interno di un intervallo definito.

###  Come funziona il gioco

1. L’utente sceglie un numero tra un intervallo (default: 0 – 100).
2. Il sistema genera un tentativo di previsione.
3. Dopo ogni tentativo, l’utente indica se:

   * `is` → il numero è corretto
   * `upper` → il numero scelto è più alto
   * `lower` → il numero scelto è più basso
4. Il sistema aggiorna dinamicamente il range possibile.
5. Il gioco termina quando il numero viene indovinato.

L’intervallo viene modificato progressivamente per evitare ripetizioni e garantire coerenza logica.

---

##  Struttura del Progetto

Tutto il codice si trova nella cartella `src/`:

```
src/
│
├── __init__.py
├── main.py
├── models.py
├── constants.py
├── choices.py
```

###  models.py

Contiene la classe `Game`, cuore dell’applicazione.
Qui viene gestita:

* La logica del gioco
* Lo stato interno
* L’aggiornamento dinamico del range
* La generazione del numero casuale
* Il controllo di fine partita

La classe utilizza proprietà (`@property`) per proteggere e controllare l’accesso allo stato interno.

---

###  constants.py

Contiene le costanti di configurazione:

* `UPPER_LIMIT_DEFAULT`
* `LOWER_LIMIT_DEFAULT`

Questo evita valori hard-coded e migliora la manutenibilità.

---

###  choices.py

Definisce l’enum `UserInputChoices` utilizzando `StrEnum`.

Vantaggi:

* Nessuna stringa “magica”
* Maggiore sicurezza
* Validazione pulita dell’input
* Centralizzazione delle scelte utente

---

###  main.py

Gestisce esclusivamente:

* Interazione con l’utente
* Input/output
* Avvio del ciclo di gioco

La logica di business è completamente separata dall’interfaccia.

---

##  Principi di Progettazione Applicati

###  Object-Oriented Programming (OOP)

Il progetto è costruito attorno alla classe `Game`, che incapsula:

* Stato interno
* Comportamenti
* Responsabilità specifiche

L’incapsulamento garantisce controllo e coerenza.

---

### SOLID Principles

**S — Single Responsibility Principle**
Ogni modulo ha una responsabilità chiara:

* Logica → `models.py`
* Input → `choices.py`
* Configurazione → `constants.py`
* Interfaccia → `main.py`

**O — Open/Closed Principle**
La struttura consente estensioni (es. nuova strategia di guessing) senza modificare il core esistente.

**L — Liskov Substitution Principle**
La progettazione permette estensioni future mantenendo la coerenza comportamentale.

**I — Interface Segregation Principle**
Responsabilità ben separate, nessuna interfaccia sovraccarica.

**D — Dependency Inversion Principle**
Le dipendenze sono modularizzate e separabili.

---

###  SCO – Separation of Concerns

Il progetto separa chiaramente:

* Logica di dominio
* Configurazione
* Interazione utente
* Gestione delle scelte

Questo rende il codice:

* Più leggibile
* Più testabile
* Più estendibile
* Più professionale

---

##  Come eseguire il progetto

Clona il repository:

```bash
git clone <repository-url>
```

Entra nella cartella:

```bash
cd indovina-numero/src
```

Esegui il gioco:

```bash
python main.py
```

---

##  Possibili Estensioni Future

La struttura è già pronta per:

* Implementare una strategia di ricerca binaria
* Aggiungere test unitari (pytest)
* Integrare logging strutturato
* Creare una GUI (Tkinter / PyQt)
* Trasformarlo in una web app (Flask / FastAPI)
* Applicare dependency injection più avanzata

---

##  Perché questo progetto conta

L’obiettivo non era semplicemente creare un gioco funzionante.

L’obiettivo era dimostrare:

* Capacità di progettazione
* Attenzione ai dettagli
* Pensiero architetturale
* Scrittura di codice pulito
* Applicazione concreta di principi di ingegneria del software

Anche un problema semplice può essere risolto con mentalità professionale.

---

##  Stack Tecnologico

* Python 3
* OOP
* Enum
* Architettura modulare
* SOLID Principles
* Separation of Concerns

---

##  Conclusione

**Indovina Numero** rappresenta il mio approccio allo sviluppo software:

Struttura.
Chiarezza.
Qualità.
Scalabilità.

Non è solo un gioco.
È un esempio concreto di come progetto e costruisco software.

Grazie per aver dedicato tempo alla
