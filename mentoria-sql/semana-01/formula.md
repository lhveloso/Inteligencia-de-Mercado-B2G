# Semana 1 — Fórmula mestre (cola rápida)

Decore o molde, depois pratique **variando os espaços em branco** — é assim que ele vira reflexo em vez de decoreba fixa. Cada exercício de `exercicios.sql` cabe nesse mesmo molde.

```sql
SELECT <colunas que eu quero ver>
FROM <tabela>
WHERE <coluna> = '<valor>'                 -- filtro (remova a linha se não precisar filtrar)
ORDER BY <coluna_de_ordenação> ASC|DESC    -- ASC = menor→maior | DESC = maior→menor
LIMIT <N>;                                 -- SQL Server: TOP N logo depois do SELECT
```

## Variações do mesmo molde

| Pedido | filtro (WHERE) | ordenação | N |
|---|---|---|---|
| "os 5 'Em Disputa' de maior valor" | `status = 'Em Disputa'` | `valor_estimado DESC` | `5` |
| "os 3 'Cancelado' de menor valor" | `status = 'Cancelado'` | `valor_estimado ASC` | `3` |
| "todos os 'Vencido' da categoria TI" | `status = 'Vencido' AND categoria_produto = 'TI e Software'` | `valor_estimado DESC` | (sem LIMIT = todos) |
| "os 10 editais mais antigos" | (sem filtro) | `data_publicacao ASC` | `10` |

## Quando o molde muda

- **Mais de um filtro?** Encadeia com `AND` / `OR` dentro do `WHERE` (lembre dos parênteses quando misturar os dois — Lição 1, seção 2).
- **Filtro é "está numa lista"?** Troca `WHERE coluna = 'x'` por `WHERE coluna IN ('x', 'y', 'z')`.
- **Filtro é "contém um texto"?** Troca por `WHERE coluna LIKE '%texto%'`.
- **Filtro é "é vazio/nulo"?** Nunca `= NULL` — sempre `IS NULL` / `IS NOT NULL`.
- **Sem `WHERE` nenhum?** Tudo bem, é opcional — a fórmula funciona sem essa linha.
- **Sem `LIMIT`?** Também opcional — traz todas as linhas que passaram no filtro.

## Regra de ordem que nunca muda

```
FROM → WHERE → SELECT → ORDER BY → LIMIT
```

O banco sempre filtra antes de ordenar, e sempre ordena antes de cortar (`LIMIT`/`TOP`). Isso explica por que trocar a ordem das cláusulas no texto da query dá erro de sintaxe, mas a *lógica* de processamento sempre segue essa sequência.
