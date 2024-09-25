# Progetto Python - Implementazione personalizzata di un JSON Parser

Questo progetto è una versione personale di un Json Parser basato sulla sfida proposta dal sito [codingchallenges.fyi](https://codingchallenges.fyi/challenges/challenge-json-parser).

## Descrizione del progetto

Il progetto ha l'obiettivo di realizzare un'applicazione Python che verifica se un file Json è valido

### Versioni

Sono state implementate diverse versioni del progetto:

- **Branch `main`**:
  - al momento è aggiornato alla versione definitiva del progetto che implementa tutti gli step previsti dalla challenge
  
- **Branch `Step2`**:
  - In questo branch ho implementato lo step 1/2 della sfida, vale a dire ho validato i seguenti oggetti json (string keys e string values):
    - ‘{}’
    - {"key": "value"}

- **Branch `Step3`**:
  - In questo branch ho implementato lo step 3 della sfida, vale a dire ho validato i seguenti oggetti json (string, numeric, boolean e null values):
    - {
  "key1": true,
  "key2": false,
  "key3": null,
  "key4": "value",
  "key5": 101
}

- **Branch `Step4`**:
  - In questo branch ho implementato lo step 4 della sfida, vale a dire ho validato i seguenti oggetti json (object e array values):
    -   {
  "key": "value",
  "key-n": 101,
  "key-o": {},
  "key-l": []
}

- **Branch `Step5`**:
  - In questo branch ho implementato lo step 5 della sfida, vale a dire ho validato le casistiche della test suite http://www.json.org/JSON_checker/test.zip



## Utilizzo
```bash
python parser.py <test case> #eseguo i test uno alla volta fornendo una descrizione della problematica incontrata in caso di validazione fallita
python run_testS.py #eseguo la test suite riportando se il test ha avuto successo o no
```

### Prerequisiti
- Python 3.10


