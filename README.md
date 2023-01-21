# BowBin
Una pipeline per la rilevazione di virus in dati metagenomici

## Tabella dei contenuti:
- [Descrizione](#descrizione)
- [Installazione](#installazione)
- [Requisiti](#requisiti)
- [Esecuzione di BowBin](#esecuzione-di-bowbin)
- [Spiegazione dell'output](#spiegazione-output)
- [File e cartelle](#file-e-cartelle)
- [Autori](#autori)

## Descrizione
BowBin è una pipeline progettata per la rilevazione di genomi virali in dati metagenomici.

BowBin riceve in input il file contenente i dati metagenomici e un insieme di genomi virali, divide i genomi virali in scaffolds, esegue Bowtie2 per allineare le reads metagenomiche con gli scaffolds e, grazie a Metabat2 e a vari scripts, genera la coverage table da cui è possibile osservare le specie di virus rilevati nei dati metagenomici, con il relativo numero di scaffolds. 

Inoltre la pipeline prevede un ulteriore step di binning. In questa fase, particolarmente utile quando il numero di genomi virali dati in input è molto elevato, vengono raggruppati gli scaffolds in bin. Il processo di binning prevede l'utilizzo di Binsanity o di vRhyme, entrambi i tool utilizzano la coverage table. 



## Installazione

## Requisiti

## Esecuzione di BowBin

## Spiegazione output

## File e cartelle

## Autori
[Alessando Aquino](https://github.com/AlessandroUnisa), [Nicolapio Gagliarde](https://github.com/GagliardeNicolapio/)
