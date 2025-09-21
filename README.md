# 👑 Checkpoint 4: Jogo das Pedras - Programação Dinâmica

## Informações do Projeto

| Disciplina | Curso | Professor |
| :--- | :--- | :--- |
| `DYNAMIC PROGRAMMING 2025/2` | `ENGENHARIA DE SOFTWARE` | `Marcelo Amorim` |

---

## 👥 Integrantes 2ESR

- **RM 558385** — Alexia Ramalho
- **RM 559008** — Hellen Silva
- **RM 557397** — Lorenzo Acquesta
- **RM 558859** — Wendell dos Santos

---

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo implementar uma solução para o "Jogo das Pedras", um jogo de estratégia para dois jogadores. A missão é desenvolver uma função em Python capaz de determinar se o jogador da vez possui uma estratégia vencedora para um dado número de pedras, assumindo que ambos os jogadores jogam de forma ótima.

A solução foi desenvolvida utilizando conceitos de recursão e programação dinâmica, com duas abordagens distintas, conforme solicitado.

---

## 🚀 Solução Implementada

O problema foi resolvido com duas funções principais, representando as duas abordagens solicitadas no checkpoint. As implementações completas podem ser encontradas nos arquivos de código deste repositório.

### 1. Função Recursiva Pura

Esta versão implementa a lógica de forma direta. Para saber se `vence(n)` é verdade, ela chama recursivamente `vence(n-1)`, `vence(n-2)` e `vence(n-3)` para ver se alguma dessas posições é perdedora para o próximo jogador.

Apesar de ser simples, ela recalcula os mesmos valores várias vezes, tornando-se muito lenta para números maiores (por exemplo, `n > 35`).

### 2. Função Recursiva com Memoização

Esta versão otimizada utiliza **memoização** para resolver o problema de performance da função pura. Ela armazena os resultados já calculados em um cache para não precisar repeti-los. Com isso, a função se torna extremamente eficiente, capaz de encontrar a solução para milhares de pedras de forma quase instantânea.

---

## ⚙️ Como Executar o Código

1.  Certifique-se de ter o Python 3 instalado.
2.  Clone este repositório para a sua máquina local.
3.  Abra os arquivos de código (`.py` ou `.ipynb`) para ver as implementações.
4.  Execute o arquivo principal pelo terminal para ver os testes.
