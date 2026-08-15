# Mentoria de SQL — Rumo às Entrevistas Técnicas (12 semanas)

**Aluno:** lhveloso
**Objetivo:** estar pronto(a) para entrevistas técnicas de **Analista de Inteligência de Mercado** em 12 semanas.
**Ritmo:** 6–10h/semana.
**Base de dados do curso:** `dados/editais_b2g.db` — um banco fictício, mas realista, no mesmo domínio do projeto [`Inteligência de Mercado B2G`](../README.md) deste repositório (editais públicos, portais, órgãos, concorrentes e propostas). Você pratica exatamente o tipo de pergunta que vai aparecer numa entrevista para essa vaga.

Como abrir a base:
- **DB Browser for SQLite** (grátis, interface simples) — abra `dados/editais_b2g.db` direto.
- **VS Code** com a extensão "SQLite" ou "SQLTools".
- **Python**: `sqlite3.connect("dados/editais_b2g.db")`.
- Se preferir treinar em SQL Server/PostgreSQL/MySQL (mais comum em entrevistas), use `dados/schema_seed.sql` como base e ajuste os tipos se necessário.

---

## Como o curso funciona

Cada semana tem uma pasta `semana-XX/` com:
1. `licao.md` — teoria explicada do zero, direto ao ponto, com exemplos rodando na base do curso.
2. `exercicios.sql` — de 8 a 12 exercícios progressivos (fácil → difícil), sempre em cima de casos de negócio reais de inteligência de mercado (ex: "qual portal tem o melhor lead time médio?").
3. `gabarito.sql` — soluções comentadas, só olhe depois de tentar.
4. `entrevista.md` — 3 a 5 perguntas típicas de entrevista relacionadas ao tópico da semana (conceituais + "resolva na tela").

Todo módulo termina com uma pergunta de "e se..." para forçar raciocínio, não decoreba.

---

## Roadmap

### Bloco 1 — Fundamentos (Semanas 1–3)
| Semana | Tópico | Foco de entrevista |
|---|---|---|
| 1 | `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`, NULL | Filtrar e explorar dados rapidamente |
| 2 | Operadores, `CASE WHEN`, funções de texto e data | Traduzir regra de negócio em SQL |
| 3 | Funções agregadas + `GROUP BY` + `HAVING` | A pergunta mais comum em entrevista de analista: "agrupe e compare" |

### Bloco 2 — Combinando dados (Semanas 4–6)
| Semana | Tópico | Foco de entrevista |
|---|---|---|
| 4 | `INNER JOIN`, `LEFT JOIN` | Juntar tabelas sem perder ou duplicar linhas |
| 5 | `RIGHT/FULL JOIN`, self join, múltiplos JOINs | Casos com 3+ tabelas, comparação dentro da mesma tabela |
| 6 | Subqueries (escalar, `IN`, correlacionada) e `UNION` | Perguntas "aninhadas" clássicas de entrevista |

### Bloco 3 — SQL de analista de verdade (Semanas 7–9)
| Semana | Tópico | Foco de entrevista |
|---|---|---|
| 7 | CTEs (`WITH`) e organização de queries complexas | Legibilidade e queries em etapas |
| 8 | Window Functions: `ROW_NUMBER`, `RANK`, `LAG`/`LEAD`, `SUM() OVER` | Top N por grupo, comparação com a média, tendência — tema mais cobrado em entrevistas de analista |
| 9 | Modelagem de dados: chaves, normalização, tipos, índices (visão de quem consome, não de DBA) | "Por que essa query está lenta?" |

### Bloco 4 — Reta final para entrevistas (Semanas 10–12)
| Semana | Tópico | Foco de entrevista |
|---|---|---|
| 10 | KPIs de inteligência de mercado em SQL: taxa de conversão, lead time, ticket médio, ranking de concorrentes | Estudo de caso completo, como os das entrevistas reais |
| 11 | Simulados cronometrados (estilo live coding) + perguntas teóricas rápidas (JOIN vs subquery, index, ACID, normalização) | Simulação de entrevista técnica |
| 12 | Revisão geral, pontos fracos, portfólio: transformar os exercícios em 2-3 queries de destaque para mostrar em entrevista/LinkedIn | Fechamento + storytelling técnico |

---

## Regras do jogo

1. **Você tenta primeiro, sempre.** Eu só mostro o gabarito depois que você tentar (ou travar de verdade).
2. **Sem decoreba.** Toda semana eu vou te perguntar "por quê", não só "o quê".
3. **Erro é dado.** Se você errar um exercício, isso me diz onde focar a próxima aula — não pule direto pro gabarito.
4. **Fale em voz alta o seu raciocínio** quando resolver um exercício comigo no chat — é exatamente isso que um entrevistador quer ouvir.
5. **A cada bloco fechado (a cada 3 semanas)**, fazemos uma revisão consolidada antes de avançar.

---

## Status

- [x] Semana 1 — Fundamentos (`SELECT`/`WHERE`/`ORDER BY`) — **material pronto, comece por aqui**
- [ ] Semana 2
- [ ] Semana 3
- [ ] Semana 4
- [ ] Semana 5
- [ ] Semana 6
- [ ] Semana 7
- [ ] Semana 8
- [ ] Semana 9
- [ ] Semana 10
- [ ] Semana 11
- [ ] Semana 12

> As próximas semanas são criadas sob demanda, conforme o progresso — assim o conteúdo se ajusta ao seu ritmo real em vez de despejar 12 semanas de material de uma vez.
