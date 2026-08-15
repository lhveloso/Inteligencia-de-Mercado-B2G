"""
Gera a base de dados de pratica do curso de SQL (mentoria-sql).

Tema: Inteligencia de Mercado B2G (a mesma area do projeto principal deste
repositorio), para que os exercicios fiquem proximos da realidade de quem
vai trabalhar como Analista de Inteligencia de Mercado.

Uso:
    python3 gerar_base.py

Gera dois artefatos em mentoria-sql/dados/:
    - editais_b2g.db     -> banco SQLite pronto para consultar (DB Browser,
                            DBeaver, VS Code SQLite extension, python etc.)
    - schema_seed.sql    -> mesmo conteudo em SQL puro (CREATE TABLE + INSERT),
                            portavel para PostgreSQL/MySQL/SQL Server com
                            pequenos ajustes de tipos.
"""
import random
import sqlite3
import os
from datetime import date, timedelta

random.seed(42)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "editais_b2g.db")
SQL_PATH = os.path.join(BASE_DIR, "schema_seed.sql")

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------
cur.executescript("""
CREATE TABLE portais (
    portal_id INTEGER PRIMARY KEY,
    nome_portal TEXT NOT NULL,
    tipo TEXT NOT NULL              -- 'Federal', 'Estadual', 'Privado'
);

CREATE TABLE orgaos (
    orgao_id INTEGER PRIMARY KEY,
    nome_orgao TEXT NOT NULL,
    esfera TEXT NOT NULL,           -- 'Federal', 'Estadual', 'Municipal'
    uf TEXT NOT NULL
);

CREATE TABLE vendedores (
    vendedor_id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    equipe TEXT NOT NULL            -- 'Lances A', 'Lances B', 'Lances C'
);

CREATE TABLE empresas_concorrentes (
    empresa_id INTEGER PRIMARY KEY,
    nome_empresa TEXT NOT NULL,
    segmento TEXT NOT NULL,
    uf TEXT NOT NULL
);

CREATE TABLE editais (
    edital_id INTEGER PRIMARY KEY,
    orgao_id INTEGER NOT NULL,
    portal_id INTEGER NOT NULL,
    vendedor_id INTEGER NOT NULL,
    categoria_produto TEXT NOT NULL,
    data_publicacao TEXT NOT NULL,
    data_abertura_propostas TEXT,
    data_disputa TEXT,
    valor_estimado REAL NOT NULL,
    status TEXT NOT NULL,           -- 'Vencido', 'Perdido', 'Em Disputa', 'Cancelado'
    FOREIGN KEY (orgao_id) REFERENCES orgaos(orgao_id),
    FOREIGN KEY (portal_id) REFERENCES portais(portal_id),
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(vendedor_id)
);

CREATE TABLE propostas (
    proposta_id INTEGER PRIMARY KEY,
    edital_id INTEGER NOT NULL,
    empresa_id INTEGER NOT NULL,
    valor_proposto REAL NOT NULL,
    vencedora INTEGER NOT NULL,     -- 0/1
    FOREIGN KEY (edital_id) REFERENCES editais(edital_id),
    FOREIGN KEY (empresa_id) REFERENCES empresas_concorrentes(empresa_id)
);
""")

# ---------------------------------------------------------------------------
# Dimensoes
# ---------------------------------------------------------------------------
portais = [
    (1, "Compras.gov.br", "Federal"),
    (2, "BLL Compras", "Privado"),
    (3, "BEC/SP", "Estadual"),
    (4, "Licitar Digital", "Privado"),
    (5, "ComprasBR", "Privado"),
    (6, "BBMNET", "Privado"),
]
cur.executemany("INSERT INTO portais VALUES (?,?,?)", portais)

ufs = ["SP", "RJ", "MG", "RS", "PR", "BA", "PE", "CE", "DF", "SC"]
orgaos_nomes = [
    "Prefeitura Municipal", "Secretaria de Saude", "Secretaria de Educacao",
    "Governo do Estado", "Ministerio da Gestao", "Hospital Universitario",
    "Instituto Federal", "Camara Municipal", "Tribunal de Justica",
    "Universidade Federal",
]
orgaos = []
oid = 1
for uf in ufs:
    for base in random.sample(orgaos_nomes, 4):
        esfera = "Federal" if "Federal" in base or "Ministerio" in base or "Tribunal" in base else (
            "Estadual" if "Estado" in base else "Municipal")
        orgaos.append((oid, f"{base} de {uf}-{oid:03d}", esfera, uf))
        oid += 1
cur.executemany("INSERT INTO orgaos VALUES (?,?,?,?)", orgaos)

vendedores = [
    (1, "Ana Ferreira", "Lances A"),
    (2, "Bruno Castro", "Lances A"),
    (3, "Camila Duarte", "Lances B"),
    (4, "Diego Martins", "Lances B"),
    (5, "Elaine Souza", "Lances C"),
    (6, "Felipe Rocha", "Lances C"),
]
cur.executemany("INSERT INTO vendedores VALUES (?,?,?)", vendedores)

segmentos = ["Material Hospitalar", "Material de Escritorio", "TI e Software",
             "Equipamentos de Laboratorio", "Mobiliario", "Limpeza e Higiene"]
empresas_base = [
    "Nortex", "Vitalmed", "SulSupply", "Governa Tech", "PublicaMax",
    "AlfaDist", "Bemol Corp", "Reta Suprimentos", "OrionGov", "Delta B2G",
    "Ceara Insumos", "Planalto Comercio", "Zenith Materiais", "Litoral Sup",
    "Cerrado Distribuidora",
]
empresas = []
eid = 1
for nome in empresas_base:
    for suf in ["", " Filial"]:
        empresas.append((eid, f"{nome}{suf}", random.choice(segmentos), random.choice(ufs)))
        eid += 1
cur.executemany("INSERT INTO empresas_concorrentes VALUES (?,?,?,?)", empresas)

# nossa empresa entra como concorrente id 999 conceitualmente (vencedora = nossa proposta)
NOSSA_EMPRESA_ID = 999
empresas.append((NOSSA_EMPRESA_ID, "Nossa Empresa (Cliente)", "Diversos", "SP"))
cur.execute("INSERT INTO empresas_concorrentes VALUES (?,?,?,?)", empresas[-1])

# ---------------------------------------------------------------------------
# Fatos: editais + propostas
# ---------------------------------------------------------------------------
categorias = segmentos
status_opcoes = ["Vencido", "Perdido", "Em Disputa", "Cancelado"]
status_pesos = [0.35, 0.40, 0.15, 0.10]

start_date = date(2024, 1, 1)

editais_rows = []
propostas_rows = []
edital_id = 1
proposta_id = 1

for _ in range(600):
    orgao_id = random.choice(orgaos)[0]
    portal_id = random.choice(portais)[0]
    vendedor_id = random.choice(vendedores)[0]
    categoria = random.choice(categorias)

    pub_offset = random.randint(0, 545)
    data_publicacao = start_date + timedelta(days=pub_offset)
    abertura = data_publicacao + timedelta(days=random.randint(5, 20))
    disputa = abertura + timedelta(days=random.randint(1, 15))

    valor_estimado = round(random.uniform(15000, 850000), 2)
    status = random.choices(status_opcoes, weights=status_pesos, k=1)[0]

    # ~8% dos editais ainda nao tem propostas registradas (edge case p/ LEFT JOIN)
    tem_propostas = random.random() > 0.08

    editais_rows.append((
        edital_id, orgao_id, portal_id, vendedor_id, categoria,
        data_publicacao.isoformat(),
        abertura.isoformat() if tem_propostas else None,
        disputa.isoformat() if status != "Em Disputa" else None,
        valor_estimado, status,
    ))

    if tem_propostas:
        n_concorrentes = random.randint(0, 5)
        concorrentes_sorteados = random.sample(empresas[:-1], n_concorrentes)

        valor_nossa_proposta = round(valor_estimado * random.uniform(0.75, 0.99), 2)
        somos_vencedores = 1 if status == "Vencido" else 0
        propostas_rows.append((
            proposta_id, edital_id, NOSSA_EMPRESA_ID, valor_nossa_proposta, somos_vencedores
        ))
        proposta_id += 1

        for emp in concorrentes_sorteados:
            valor_conc = round(valor_estimado * random.uniform(0.70, 1.05), 2)
            venceu_conc = 1 if (status == "Perdido" and emp == concorrentes_sorteados[0]) else 0
            propostas_rows.append((
                proposta_id, edital_id, emp[0], valor_conc, venceu_conc
            ))
            proposta_id += 1

    edital_id += 1

cur.executemany("INSERT INTO editais VALUES (?,?,?,?,?,?,?,?,?,?)", editais_rows)
cur.executemany("INSERT INTO propostas VALUES (?,?,?,?,?)", propostas_rows)

conn.commit()

# ---------------------------------------------------------------------------
# Exportar tambem como .sql puro (schema + seed) para uso fora do SQLite
# ---------------------------------------------------------------------------
with open(SQL_PATH, "w", encoding="utf-8") as f:
    for line in conn.iterdump():
        f.write(f"{line}\n")

conn.close()

print(f"OK -> {DB_PATH}")
print(f"OK -> {SQL_PATH}")
print(f"Orgaos: {len(orgaos)} | Empresas: {len(empresas)} | Editais: {len(editais_rows)} | Propostas: {len(propostas_rows)}")
