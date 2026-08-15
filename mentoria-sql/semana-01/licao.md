# Semana 1 — Fundamentos: SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, NULL

Base usada: `dados/editais_b2g.db`

Tabelas que vamos usar esta semana:
- `editais` (edital_id, orgao_id, portal_id, vendedor_id, categoria_produto, data_publicacao, data_abertura_propostas, data_disputa, valor_estimado, status)
- `orgaos` (orgao_id, nome_orgao, esfera, uf)
- `portais` (portal_id, nome_portal, tipo)

---

## 1. `SELECT` — escolhendo o que ver

```sql
SELECT edital_id, categoria_produto, valor_estimado
FROM editais;
```

`SELECT *` traz todas as colunas — útil para explorar, mas em entrevista **evite usar `*` na resposta final**: nomear as colunas mostra que você sabe exatamente o que está pedindo. É um detalhe pequeno que entrevistador de analista repara.

---

## 2. `WHERE` — filtrando linhas

`WHERE` filtra **antes** de qualquer agregação (isso importa muito lá na frente, na Semana 3, quando comparar com `HAVING`).

```sql
SELECT edital_id, valor_estimado, status
FROM editais
WHERE status = 'Vencido';
```

Operadores mais usados:

| Operador | Exemplo | O que faz |
|---|---|---|
| `=`, `<>` (ou `!=`) | `status = 'Vencido'` | igual / diferente |
| `>`, `<`, `>=`, `<=` | `valor_estimado > 100000` | comparação numérica |
| `AND` / `OR` | `status = 'Vencido' AND valor_estimado > 100000` | combinar condições |
| `BETWEEN` | `valor_estimado BETWEEN 50000 AND 200000` | intervalo (inclusive nos dois lados) |
| `IN` | `status IN ('Vencido', 'Em Disputa')` | pertence a uma lista |
| `LIKE` | `categoria_produto LIKE '%Hospitalar%'` | busca por padrão de texto (`%` = qualquer sequência) |

**Cuidado com precedência:** `AND` tem prioridade sobre `OR`. Se misturar os dois, use parênteses:

```sql
-- Errado (ambíguo pra quem lê, mesmo que funcione):
WHERE status = 'Vencido' OR status = 'Perdido' AND valor_estimado > 100000

-- Correto e claro:
WHERE status = 'Vencido' OR (status = 'Perdido' AND valor_estimado > 100000)
```

---

## 3. NULL — o valor que não é valor nenhum

Na nossa base, `editais.data_abertura_propostas` pode ser `NULL` (editais sem propostas registradas ainda — reflete a realidade: 8% dos editais estão assim).

**Regra de ouro:** `NULL` nunca é igual a nada, nem a outro `NULL`. Por isso:

```sql
-- ERRADO — nunca retorna linhas, mesmo que existam NULLs:
SELECT * FROM editais WHERE data_abertura_propostas = NULL;

-- CORRETO:
SELECT * FROM editais WHERE data_abertura_propostas IS NULL;
SELECT * FROM editais WHERE data_abertura_propostas IS NOT NULL;
```

Isso é pergunta certa de entrevista teórica: *"por que `WHERE coluna = NULL` não funciona?"*

---

## 4. `ORDER BY` — ordenando o resultado

```sql
SELECT edital_id, valor_estimado
FROM editais
ORDER BY valor_estimado DESC;   -- DESC = maior pro menor. ASC é o padrão (pode omitir).
```

Pode ordenar por múltiplas colunas — a segunda só desempata a primeira:

```sql
ORDER BY status ASC, valor_estimado DESC;
```

---

## 5. `LIMIT` — top N

```sql
SELECT edital_id, valor_estimado
FROM editais
ORDER BY valor_estimado DESC
LIMIT 10;   -- os 10 editais de maior valor estimado
```

> Nota de dialeto (vai cair em entrevista): `LIMIT` é SQLite/PostgreSQL/MySQL. Em **SQL Server** (que é o que você já usou no projeto da Copa do Mundo!) o equivalente é `SELECT TOP 10 ...`. Mesma ideia, sintaxe diferente — entrevistador gosta muito de perguntar "e se fosse outro banco?".

---

## 6. `DISTINCT` — removendo duplicatas

```sql
SELECT DISTINCT status
FROM editais;
```

Retorna cada valor único de `status` uma vez só. Se usar com mais de uma coluna, a combinação das colunas que precisa ser única:

```sql
SELECT DISTINCT categoria_produto, status
FROM editais;
```

---

## 7. Juntando tudo: ordem lógica de leitura de uma query

Uma dúvida comum de entrevista: "em que ordem o banco processa a query?"

```
FROM   -> de onde vêm os dados
WHERE  -> filtra linhas
SELECT -> escolhe/calcula colunas
ORDER BY -> ordena o resultado
LIMIT  -> corta o resultado
```

Repare que `WHERE` acontece **antes** de `SELECT` — por isso você não pode usar um "apelido" (alias) criado no `SELECT` dentro do `WHERE` na mesma query (em vários bancos, ao menos). Isso vai ficar mais claro na Semana 3 com `HAVING`.

---

## Agora vá para `exercicios.sql`

Tente resolver todos antes de olhar `gabarito.sql`. Quando terminar (ou travar), me chame no chat e resolvemos juntos, explicando o raciocínio.
