# Guess The ampionship

Guess the campionship è un gioco in python in cui bisona indovinare a quale campionato appartiene una squadra di calcio (dati aggiornati a settembre 2024)

## Requisiti per giocare

Per giocare è necessario avere python e il modulo tkinter installato, successivamente eseguire il file Main.py

## Main.py

Questo file è il cuore del gioco, al suo interno viene gestita la finestra, il cronometro e l'estrazione di squadre e campionati

## InfoSquadre.py

Questo file permette di scorrere l'intera lista delle squadre, per verificare che le immagini e dati inseriti sono corretti

## Cartella Dati

Nella cartella dati sono presenti tutti i dati necessari per l'essecuozione del programma, tra cui la lista dei campionati, delle squadre  con tutti i collegamenti alle immagini e  delle piccole configurazioni della finestra di gioco

## Cartella Img

Nella cartella Img sono presenti tutte le immagini di cui il programma ha bisogno, suddivise i cartelle

Le immagini devono rispettare delle dimensioni precise: 

- 300x300 le immagini delle squadre (consigliato il Plug-in Bipm di Gimp)
- 250x250 le immagini dei campionati (consigliato il Plug-in Bipm di Gimp)

# Moduli utilizzati

## tkinter

Il modulo tkinter crea la finestra ed è fondamentale per creare tutti gli elementi a schermo

## threading e time

Questi 2 moduli permettono di creare un cronometro tramite il modulo time e di eseguirlo in un secondo thread tramite il modulo threading, in modo che possa essere esuito in simultanea con il resto del programma

## functools

Dalla functools importiamo la partial che ci premette di passare di parametri alla funzione che richiamiamo quando premiamio i pulsanti per scegliere il copionato corretto

## random

Il modulo random è un altro modulo importante per il funzionamento del programma, visot che premette di estrarre in modo casuale una squadra e 2 campionati prima di mostrarli a schermo

# Come Giocare

Il gioco è molto semplice:

Una volta eseguito il programma verrà mostrato il logo di una squadra di calcio, bisognarà indovinare in quale campionato gioca scegliendo tra i 3 loghi mostrati.

Per rispondere si hanno a disposizione 10 secondi, se non si risponde inn tempo verrà considerato errore.

In caso di errore o di tempo scaduto la partita terminarà e bisognerà ricominciare la partita da capo, invece in caso di risposta esatta si otterà 1 punto

# Campionati presenti:

- PremierLeague (Inghilterra)

- Championship (Inghilterra)

- Eredivise (Olanda)

- Bundesliga2 (Germania)

- Bundesliga (Germania)

- LaLiga (Spagna)

- LaLiga2 (Spagna)

- LeagueofIreland (Irlanda)

- LigaPortugal (Portogallo)

- MLS (USA)

- MLSNextPro (USA)

- SerieA (Italia)

- SerieB (Italia)

- Ligue1 (Francia)

- Ligue2 (Francia)

# Eseguire il Progrmma

Per eseguire il programma è sufficiente eseguire il launcher relativa al prorio sistema operativo
