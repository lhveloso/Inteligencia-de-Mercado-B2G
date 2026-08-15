-- =============================================================
-- Semana 1 — Exercícios: SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, NULL
-- Base: dados/editais_b2g.db
-- Tente resolver cada um ANTES de olhar o gabarito.sql
-- =============================================================

-- 1. Liste o id, a categoria do produto e o valor estimado de todos os editais.
--    (sem usar SELECT *)


-- 2. Liste todos os editais com status 'Vencido', mostrando id, categoria e valor_estimado.


-- 3. Liste os editais com valor_estimado maior que 500.000.


-- 4. Liste os editais cujo status seja 'Vencido' OU 'Em Disputa'
--    (resolva de duas formas: uma com OR, outra com IN).


-- 5. Liste os editais da categoria 'TI e Software' com valor_estimado
--    entre 100.000 e 300.000 (use BETWEEN).


-- 6. Quantos e quais editais ainda não têm data de abertura de propostas registrada?
--    (dica: NULL)


-- 7. Liste todos os editais cuja categoria_produto contenha a palavra "Hospitalar"
--    em qualquer parte do nome (use LIKE).


-- 8. Liste os 10 editais de MAIOR valor_estimado, ordenados do maior para o menor,
--    mostrando id, categoria e valor.


-- 9. Liste os 5 editais 'Perdido' de MENOR valor_estimado — ou seja, as perdas
--    "baratas" que a empresa deveria ter vencido fácil.
--    (pense: quais cláusulas você precisa combinar aqui?)


-- 10. Quais são todos os status distintos que aparecem na tabela editais?


-- 11. Quais são todas as combinações distintas de (categoria_produto, status)
--     que existem na base? Ordene por categoria_produto.


-- 12. DESAFIO — "e se...":
--     Liste os editais que NÃO são da categoria 'TI e Software' E que têm
--     valor_estimado acima de 400.000, ordenados por valor_estimado decrescente,
--     mostrando apenas os 5 primeiros.
--     Escreva a query e, em uma frase, explique em que ordem o banco
--     processa essas cláusulas (WHERE, ORDER BY, LIMIT) para chegar no resultado.
