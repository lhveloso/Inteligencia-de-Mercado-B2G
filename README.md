# Mapeamento e Inteligência Competitiva B2G (Editais Públicos)

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-ETL-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-DataViz-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Dashboard-E34F26?style=for-the-badge&logo=html5&logoColor=white)

## Visão Geral do Projeto
Este projeto consiste na construção de um pipeline de **Data Analytics & Inteligência de Mercado B2G (Business to Government)**. O objetivo principal foi transformar dados brutos e desorganizados de monitoramento de editais públicos em um **Dashboard Executivo Interativo**, permitindo otimizar a tomada de decisão comercial e o dimensionamento da equipe de lances.

---

## Arquitetura e Engenharia do Projeto

```text
[Entrada: CSV Bruto]
        │
        ▼
[Estágio 1: ETL & Limpeza (Python / Pandas)]
   ├── Remoção de colunas nulas/fantasma
   ├── Tratamento de duplicidades (Produtos)
   ├── Normalização de grafias de portais
   └── Ajuste de datas & tratamento de outliers no Lead Time
        │
        ▼
[Estágio 2: Exportação de Dados Tratados]
   └── Generates: 'base_editais_tratada.csv'
        │
        ▼
[Estágio 3: Dashboard Interativo Front-end]
   └── Single-file HTML5 + CSS3 + Chart.js (Tema Claro / Escuro + Filtros)
