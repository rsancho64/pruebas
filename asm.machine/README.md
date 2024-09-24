---
title: ASM.MACHINE
author: RSA
date: \today
lang: ES
geometry:
  - a4paper
  - margin=2.5cm
  - heightrounded
header-includes: |
  \usepackage{fancyhdr}
  \pagestyle{fancy}
  \fancyhead[L]{\textbf{\leftmark}}
  \fancyhead[R]{\textbf{\rightmark}}
  \lfoot{}\cfoot{\thepage}\rfoot{}
numbersections: yes,
linestretch: 1.2
toccolor: Blue
bibliography: [X:/absolute/path/to/ref.bib]
csl: [X:/absolute/path/to/chicago-fullnote-bibliography.csl]
documentclass: article
toc: true
---



Emulación en python de una arquitectura convencional minima

## Elementos en la arquitectura:

- banco MA (en 0..10)
- banco MB (en 0..10)
- registro AC
- UAL: 

## Repertorio

|   tipo | forma         |
|-------:|:--------------|
| no @'s | `OP`          |
|  1 @'s | `OP D1`       |
|  2 @'s | `OP D1 D2`    |
|  3 @'s | `OP D1 D2 D3` |

| expresion         | semantica LP alto nivel |
|:------------------|:------------------------|
| `ADD  opdo1 opdo2` | `AC = opdo1 + opdo2`   |
| `ADD  opdo1`       | `AC += opdo1`          |
| `MOV  orig dest`   | `dest = orig`          |
| `READ dest`        | `dest = input()`       |
| `WRI  orig`        | `print(orig)`          |

## Programa Ejemplo

```asm:
READ M[0]
READ M[1]
ADD  M[0] M[1] // AC
STO  M[2]
WRI  M[3]
```

El programa python equivalente es [**este**](https://github.com/rsancho64/python101-curso24-25/blob/main/101.py)

## Etc

### pytopics to know

Una buena organización de [*"pythonitems"*](https://zetcode.com/all/#python)


