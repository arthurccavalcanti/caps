# Empresas do Recife - CAPS
Projeto de análise de dados de empresas da cidade do Recife

### Integrantes
- Ramon Taffarel (PO)
- Jardel Simplicio (Scrum Master)
- Arthur Cavalcanti (Dev)
- Susan Capelo (Dev)
- Manoel Nascimento (Dev)

## 1. Visão Geral do Projeto (Os 3Cs)

* **Claro:** Este projeto visa analisar a base de dados de empresas registradas no município para gerar um diagnóstico claro e detalhado sobre o cenário econômico local. O objetivo é transformar dados brutos em insights que possam ser facilmente compreendidos e utilizados por gestores públicos.

* **Conciso:** Focaremos em responder a perguntas estratégicas sobre a distribuição geográfica, o crescimento temporal, a diversidade de setores e a longevidade das empresas. A análise será direta e orientada para gerar relatórios e dashboards objetivos.

* **Valor Definido:** O valor principal deste projeto é capacitar a gestão municipal a tomar decisões mais inteligentes e baseadas em evidências. Os insights permitirão a criação de políticas públicas mais eficazes, a otimização da alocação de recursos, o fomento a setores estratégicos e o planejamento urbano alinhado às vocações econômicas de cada bairro.

## 2. Priorização das Entregas

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
* **Análise 9 (Opcional, se dados disponíveis):** Investigar o porte das empresas (micro, pequena, média) e o nível de formalidade (existência de alvarás).

## 3. Implementação do Projeto

### Ferramentas Propostas
* **Linguagem de Programação:** Python
* **Bibliotecas de Análise:**
    * **Pandas:** Para manipulação, limpeza e análise estruturada dos dados.
    * **GeoPandas:** Para a análise e visualização de dados geográficos (distribuição por bairros).
    * **Matplotlib & Seaborn:** Para a criação de gráficos estáticos e visualizações de dados.
    * **Plotly:** Para a criação de gráficos interativos.
* **Ferramenta de BI (Business Intelligence):** Microsoft Power BI, Google Looker Studio ou Qlik Sense para a criação de dashboards interativos que permitirão aos gestores explorar os dados de forma autônoma.

### Técnicas de Análise
1.  **Limpeza e Tratamento de Dados:** Verificação de inconsistências, tratamento de valores ausentes e padronização das colunas `data_abertura_empresa`, `situacao_empresa` e `cnae`.
2.  **Análise Estatística Descritiva:** Uso de contagens, médias, medianas e distribuições para resumir as principais características da base de dados.
3.  **Análise Temporal:** Agrupamento de dados por ano e mês para analisar tendências e sazonalidades na abertura de empresas.
4.  **Análise Geoespacial:** Utilização de latitude e longitude (ou `nome_bairro`) para criar mapas de calor (heatmaps) que mostram a densidade empresarial no mapa do município.
5.  **Análise de Segmentação:** Agrupamento de empresas por CNAE (setor), bairro e situação para comparar seus perfis e dinâmicas.

## 4. Valores e Benefícios dos Insights Gerados

A conclusão deste projeto trará benefícios tangíveis e estratégicos para a gestão municipal:

| Insight Gerado | Benefício para a Gestão Municipal |
| :--- | :--- |
| **Mapa de Concentração Empresarial** | **Planejamento Urbano e Desenvolvimento Econômico:** Identificação de áreas que necessitam de incentivos fiscais e infraestrutura para atrair novos negócios e equilibrar o desenvolvimento. |
| **Série Histórica de Abertura de Empresas** | **Monitoramento da Saúde Econômica:** Permite avaliar o impacto de políticas e crises, servindo como um termômetro da confiança do empreendedor local. |
| **Análise Setorial (CNAE)** | **Fomento a Setores Estratégicos:** Base para a criação de programas de apoio e capacitação direcionados aos setores mais promissores ou mais vulneráveis da economia local. |
| **Longevidade e Taxa de Sobrevivência** | **Desenvolvimento de Políticas de Apoio:** Ajuda a entender os desafios enfrentados pelas empresas em seus primeiros anos, permitindo a criação de programas de mentoria e crédito para aumentar sua longevidade. |
| **Vocações Econômicas dos Bairros** | **Marketing Territorial e Alocação de Recursos:** Facilita a promoção de bairros para atrair investimentos específicos (ex: um "polo de tecnologia" ou uma "rota gastronômica") e otimiza a alocação de serviços públicos. |
| **Impacto de Políticas e Eventos** | **Avaliação de Políticas Públicas:** Fornece uma métrica clara para medir o sucesso (ou fracasso) de incentivos fiscais e programas de fomento, garantindo que o dinheiro público seja bem investido. |

Com este roteiro, o projeto está preparado para entregar valor de forma rápida e incremental, transformando dados em um ativo estratégico para o desenvolvimento econômico e social do município.
