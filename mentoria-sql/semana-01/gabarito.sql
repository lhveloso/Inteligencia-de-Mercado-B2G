-- =============================================================
-- Semana 1 — Gabarito comentado
-- Só olhe depois de tentar em exercicios.sql
-- =============================================================

-- 1. Id, categoria e valor de todos os editais.
SELECT edital_id, categoria_produto, valor_estimado
FROM editais;

-- 2. Editais com status 'Vencido'.
SELECT edital_id, categoria_produto, valor_estimado
FROM editais
WHERE status = 'Vencido';

-- 3. Editais com valor_estimado > 500000.
SELECT edital_id, categoria_produto, valor_estimado
FROM editais
WHERE valor_estimado > 500000;

-- 4. Status 'Vencido' OU 'Em Disputa' — duas formas equivalentes.
SELECT edital_id, categoria_produto, status
FROM editais
WHERE status = 'Vencido' OR status = 'Em Disputa';

SELECT edital_id, categoria_produto, status
FROM editais
WHERE status IN ('Vencido', 'Em Disputa');
-- IN é preferível quando a lista cresce: mais legível que uma sequência de OR.

-- 5. 'TI e Software' com valor entre 100k e 300k.
SELECT edital_id, categoria_produto, valor_estimado
FROM editais
WHERE categoria_produto = 'TI e Software'
  AND valor_estimado BETWEEN 100000 AND 300000;
-- BETWEEN é INCLUSIVO nos dois extremos (equivale a >= 100000 AND <= 300000).

-- 6. Editais sem data de abertura de propostas.
SELECT edital_id, categoria_produto, status
FROM editais
WHERE data_abertura_propostas IS NULL;
-- NUNCA use "= NULL" — NULL não é igual a nada, nem a si mesmo.

-- 7. Categoria contendo "Hospitalar".
SELECT edital_id, categoria_produto
FROM editais
WHERE categoria_produto LIKE '%Hospitalar%';

-- 8. Top 10 maiores valores.
SELECT edital_id, categoria_produto, valor_estimado
FROM editais
ORDER BY valor_estimado DESC
LIMIT 10;

-- 9. 5 editais 'Perdido' de menor valor (as "perdas baratas").
SELECT edital_id, categoria_produto, valor_estimado
FROM editais
WHERE status = 'Perdido'
ORDER BY valor_estimado ASC
LIMIT 5;
-- Combina WHERE (filtra só 'Perdido') + ORDER BY ASC (menor primeiro) + LIMIT.

-- 10. Status distintos.
SELECT DISTINCT status
FROM editais;

-- 11. Combinações distintas de (categoria_produto, status).
SELECT DISTINCT categoria_produto, status
FROM editais
ORDER BY categoria_produto;

-- 12. DESAFIO.
SELECT edital_id, categoria_produto, valor_estimado
FROM editais
WHERE categoria_produto <> 'TI e Software'
  AND valor_estimado > 400000
ORDER BY valor_estimado DESC
LIMIT 5;

-- Ordem de execução lógica: primeiro o banco decide de qual tabela ler (FROM),
-- depois aplica o WHERE linha a linha (descartando o que não bate com os dois
-- filtros), só então monta as colunas do SELECT, ordena o que sobrou com
-- ORDER BY e, por último, corta para as 5 primeiras linhas com LIMIT.
-- Ou seja: LIMIT sempre age por ÚLTIMO, depois de tudo já filtrado e ordenado.
