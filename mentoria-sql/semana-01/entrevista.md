# Semana 1 — Perguntas de Entrevista

Pratique respondendo em voz alta, como se estivesse numa call. Depois confira com o gabarito no final.

### 1. (Conceitual) "Por que `WHERE coluna = NULL` nunca retorna resultado, mesmo que existam linhas com `NULL` naquela coluna?"

### 2. (Conceitual) "Qual a diferença entre `WHERE status = 'A' OR status = 'B' AND valor > 1000` e a mesma expressão com parênteses? Por que isso importa?"

### 3. (Resolva na tela) "Nossa base tem uma tabela `editais` com uma coluna `status`. Me escreva uma query que traga os 5 editais de maior valor estimado entre os que estão 'Em Disputa' agora — precisamos priorizar o time comercial."

### 4. (Conceitual) "Se eu pedir pra você trazer os 10 primeiros registros de uma tabela em SQL Server, qual sintaxe você usa? E se fosse PostgreSQL ou MySQL?"

### 5. (Raciocínio de negócio) "Você tem a tabela de editais com um campo `valor_estimado`. Como analista de inteligência de mercado, que tipo de filtro ou corte você sugeriria para identificar 'oportunidades de baixo valor mas alta chance de vitória' só olhando essa tabela hoje (sem JOIN ainda)? Não tem resposta única — quero ver seu raciocínio."

---

## Gabarito resumido

1. `NULL` representa "desconhecido/ausente". Em SQL, qualquer comparação (`=`, `<>`, etc.) envolvendo `NULL` retorna `NULL` (nem verdadeiro nem falso), e o `WHERE` só mantém linhas onde a condição é `TRUE`. Por isso é preciso usar `IS NULL` / `IS NOT NULL`, que são operadores especiais para esse caso.

2. `AND` tem precedência maior que `OR`. Sem parênteses, `status = 'A' OR status = 'B' AND valor > 1000` é lido como `status = 'A' OR (status = 'B' AND valor > 1000)` — ou seja, todo status 'A' entra, independente do valor. Isso pode gerar bugs silenciosos e é clássico de entrevista justamente por isso: escrever sem parênteses funciona, mas raramente é o que a pessoa queria dizer.

3.
```sql
SELECT edital_id, categoria_produto, valor_estimado
FROM editais
WHERE status = 'Em Disputa'
ORDER BY valor_estimado DESC
LIMIT 5;
```

4. SQL Server: `SELECT TOP 10 * FROM tabela;` (o `TOP` vem logo depois do `SELECT`, sem `ORDER BY` obrigatório, mas normalmente combinado com ele). PostgreSQL e MySQL: `SELECT * FROM tabela ORDER BY coluna LIMIT 10;` (o `LIMIT` vem no final). É um ótimo gancho pra mostrar que você entende que SQL tem um "núcleo" padrão (ANSI SQL) mas cada banco tem suas extensões.

5. Não existe resposta fechada — o que se avalia é o raciocínio: por exemplo, cruzar valor_estimado baixo/médio com histórico de concorrência baixa (isso vem nas próximas semanas, com JOIN), ou pelo menos citar que "com JOIN eu poderia ver quantos concorrentes historicamente disputam editais parecidos" mostra que você já está pensando no próximo passo mesmo sem ainda saber a sintaxe.
