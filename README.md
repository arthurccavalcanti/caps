# Empresas do Recife - CAPS
Projeto de análise de dados de empresas da cidade do Recife
Trello: https://trello.com/invite/b/68c0b61fd803f00ccc8d5ba2/ATTIeb3fd7596947223b0c918f0dde559be849B8B4FE/caps-fds

### Integrantes
- Ramon Taffarel (PO)
- Jardel Simplicio (Scrum Master)
- Arthur Cavalcanti (Dev)
- Susan Capelo (Dev)
- Manoel Nascimento (Dev)
- Paulo Nery (Dev)

## 1. Visão Geral (3Cs)

* **Claro:** Este projeto visa analisar a base de dados de empresas registradas no município para gerar um diagnóstico claro e detalhado sobre o cenário econômico local para gestores públicos.

* **Conciso:** Focaremos em responder a perguntas estratégicas sobre a distribuição geográfica, o crescimento temporal, a diversidade de setores e a longevidade das empresas. A análise será direta e orientada para gerar relatórios e dashboards objetivos.

* **Valor Definido:** O valor principal deste projeto é capacitar a gestão municipal a tomar decisões mais inteligentes e baseadas em evidências. Os insights permitirão a criação de políticas públicas mais eficazes, a otimização da alocação de recursos, o fomento a setores estratégicos e o planejamento urbano alinhado às vocações econômicas de cada bairro.

## 2. Implementação

### Ferramentas Propostas
* Python
* **Bibliotecas de Análise:**
    * **Pandas:** Para manipulação, limpeza e análise estruturada dos dados.
    * **GeoPandas:** Para a análise e visualização de dados geográficos (distribuição por bairros).
    * **Matplotlib & Seaborn:** Para a criação de gráficos estáticos e visualizações de dados.
    * **Plotly:** Para a criação de gráficos interativos.
* **Ferramenta de BI (Business Intelligence):** Microsoft Power BI para a criação de dashboards interativos que permitirão aos gestores explorar os dados de forma autônoma.

### Técnicas de Análise
1.  **Limpeza e Tratamento de Dados:** Verificação de inconsistências, tratamento de valores ausentes e padronização das colunas `data_abertura_empresa`, `situacao_empresa` e `cnae`.
2.  **Análise Estatística Descritiva:** Uso de contagens, médias, medianas e distribuições para resumir as principais características da base de dados.
3.  **Análise Temporal:** Agrupamento de dados por ano e mês para analisar tendências e sazonalidades na abertura de empresas.
4.  **Análise Geoespacial:** Utilização de latitude e longitude (ou `nome_bairro`) para criar mapas de calor (heatmaps) que mostram a densidade empresarial no mapa do município.
5.  **Análise de Segmentação:** Agrupamento de empresas por CNAE (setor), bairro e situação para comparar seus perfis e dinâmicas.

## 4. Valores e Benefícios dos Insights Gerados

| Insight Gerado | Benefício para a Gestão Municipal |
| :--- | :--- |
| **Mapa de Concentração Empresarial** | **Planejamento Urbano e Desenvolvimento Econômico:** Identificação de áreas que necessitam de incentivos fiscais e infraestrutura para atrair novos negócios e equilibrar o desenvolvimento. |
| **Série Histórica de Abertura de Empresas** | **Monitoramento da Saúde Econômica:** Permite avaliar o impacto de políticas e crises, servindo como um termômetro da confiança do empreendedor local. |
| **Análise Setorial (CNAE)** | **Fomento a Setores Estratégicos:** Base para a criação de programas de apoio e capacitação direcionados aos setores mais promissores ou mais vulneráveis da economia local. |
| **Longevidade e Taxa de Sobrevivência** | **Desenvolvimento de Políticas de Apoio:** Ajuda a entender os desafios enfrentados pelas empresas em seus primeiros anos, permitindo a criação de programas de mentoria e crédito para aumentar sua longevidade. |
| **Vocações Econômicas dos Bairros** | **Marketing Territorial e Alocação de Recursos:** Facilita a promoção de bairros para atrair investimentos específicos (ex: um "polo de tecnologia" ou uma "rota gastronômica") e otimiza a alocação de serviços públicos. |
| **Impacto de Políticas e Eventos** | **Avaliação de Políticas Públicas:** Fornece uma métrica clara para medir o sucesso (ou fracasso) de incentivos fiscais e programas de fomento, garantindo que o dinheiro público seja bem investido. |

---
## 1.Distribuição Geográfica Desigual

Agrupamento da base de dados pela coluna nome_bairro e contagem do número de CNPJs únicos para cada bairro.

**Visualização Geográfica**: Criar um mapa de calor (heatmap) sobre o mapa do município. Áreas com cores mais "quentes" indicarão alta concentração de empresas.

**Oportunidade**: 
- Identificar "desertos comerciais" — bairros com alta densidade populacional mas baixa oferta de serviços e comércios. Essas são áreas com alto potencial para novos empreendimentos.
- Planejamento Urbano: Direcionar investimentos em infraestrutura (transporte público, internet, segurança) para as áreas com menor densidade empresarial, incentivando a descentralização econômica.
- Incentivos Fiscais: Criar programas de isenção ou redução de impostos (como IPTU ou ISS) para empresas que se instalarem nessas áreas carentes, gerando empregos locais e reduzindo o deslocamento da população.

---
## 2. Chegada de Empreendimentos por Ano e Impacto de Crises

**Visualização Temporal**: Criar um gráfico de linhas ou de barras com o tempo (ano) no eixo X e a contagem de novas empresas no eixo Y. Marque no gráfico os anos de eventos importantes (ex: início da pandemia em 2020).

**Oportunidade**: 
- Medir a resiliência da economia local.
- Validar a eficácia de programas de estímulo econômico. 
- Previsão de necessidades/crises futuras com base em dados temporais.

---
## 3. Desigualdade por Setor (CNAE) e Sobrevivência por Setor

**Análise de Setor**: Agrupar os dados pela coluna desc_atividade ou nome_grupo e contar o número de empresas. Criar um gráfico de barras horizontais para mostrar os setores dominantes.

**Análise de Longevidade**:
- Calcular a "idade" das empresas ativas (situacao_empresa == 'ATIVA') subtraindo a data atual da data_abertura_empresa.
- Calcular o "tempo de vida" das empresas fechadas subtraindo a data_encerramento da data_abertura_empresa.
- Calcular a idade/tempo de vida médio para cada setor (desc_atividade).
- Criar um gráfico de barras comparando a longevidade média entre os setores.

**Oportunidade**: Identificar os setores que são a "espinha dorsal" da economia local (grande volume e alta longevidade) e os setores que são "frágeis" (alta taxa de fechamento precoce).

**Fomento Inteligente**: Em vez de políticas genéricas, a gestão pode criar programas específicos: para setores frágeis, oferecer consultoria de gestão e acesso a crédito; para setores fortes, oferecer apoio para expansão e exportação.

**Desenvolvimento de Talentos**: Alinhar os cursos de capacitação técnica oferecidos pela prefeitura com as necessidades dos setores mais resilientes e em crescimento, aumentando a empregabilidade.

---
## Priorização das Entregas

Para garantir agilidade e entrega de valor contínua, o projeto será dividido em três fases prioritárias:

### Fase 1: Diagnóstico Fundamental do Ecossistema Empresarial
* **Análise 1: Distribuição Geográfica Desigual:** Mapear a concentração de empresas por bairro para identificar polos econômicos e áreas com menor densidade empresarial.
* **Análise 2: Chegada de Empreendimentos por Ano:** Criar uma linha do tempo do número de empresas abertas para visualizar tendências de crescimento, estagnação ou queda.
* **Análise 3: Desigualdade por Setor (CNAE):** Quantificar a predominância dos setores econômicos (ex: serviços, comércio, indústria) no município.

### Fase 2: Aprofundamento no Perfil e Dinâmica das Empresas
* **Análise 4: Tempo de Atividade Médio:** Calcular a idade média das empresas ativas para entender a maturidade do ambiente de negócios.
* **Análise 5: Relação entre Atividades e Bairros:** Cruzar dados de CNAE com localização para identificar "vocação econômica" dos bairros (ex: polos gastronômicos, áreas industriais, centros comerciais).
* **Análise 6: Impacto de Grandes Eventos ou Crises:** Analisar o impacto de eventos macroeconômicos (como a pandemia de 2020) no ritmo de abertura de novas empresas.

### Fase 3: Análises Estratégicas e Preditivas
* **Análise 7: Sobrevivência por Setor:** Comparar a longevidade de empresas entre diferentes setores para identificar os mais resilientes e os que necessitam de maior apoio.
* **Análise 8: Impacto de Políticas Públicas:** Correlacionar a abertura de empresas de setores específicos (ex: tecnologia) com a implementação de políticas de incentivo (ex: Porto Digital).

---
## Protótipo no Figma

Você pode visualizar o protótipo do projeto diretamente no Figma através do link abaixo:

[🔗 Acessar protótipo no Figma](https://www.figma.com/design/wNX8CAKAYyzrUxeO2DHyJm/FDS?node-id=4-6488&t=aF1eegjzoOfXfpnE-1)

---
## Bug Tracker
[🔗 Acessar Bug Tracker](https://docs.google.com/document/d/1hN_d5-Roq8JewAP6yDAeJkOeVa656AMSWeRj0CBevdk/edit?tab=t.0)

## Streamcast link
[🔗 Acessar Streamcast](https://youtu.be/tY55M1ke62M)
