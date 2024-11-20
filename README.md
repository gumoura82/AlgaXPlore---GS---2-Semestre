# Simulador de Dados de Energia e Qualidade da Água com Algas - AlgaXPlore

As algas desempenham um papel crucial na absorção de CO2 da atmosfera durante a fotossíntese, ajudando a reduzir os gases de efeito estufa e combatendo as mudanças climáticas. Embora não removam diretamente o CO2 da camada de ozônio, elas contribuem para o equilíbrio atmosférico e, no passado, ajudaram na formação da camada de ozônio, que protege a Terra da radiação ultravioleta. O projeto AlgaXPlore busca explorar esse potencial, utilizando algas para gerar energia sustentável e melhorar a qualidade da água, promovendo um futuro mais ecológico. Esta parte do projeto simula e analisa dados relacionados à geração de energia por algas, conteúdo de carbono e níveis de pH da água em um período de tempo. Ele é projetado para fornecer insights sobre energia sustentável e qualidade da água, com visualizações e análises estatísticas.

## Funcionalidades

1. **Simulação de Dados**  
   - Gera dados fictícios de energia gerada, carbono na água e níveis de pH ao longo de um período especificado.  
   
2. **Filtragem de Dados por Data**  
   - Filtra os dados simulados com base em intervalos de datas fornecidos pelo usuário.

3. **Análise Estatística**  
   - Calcula as médias de:
     - Energia gerada (kWh)
     - Conteúdo de carbono (mg/L)
     - Níveis de pH da água

4. **Geração de Insights**  
   - Combina filtragem e análise para oferecer uma visão simplificada dos dados.

5. **Visualização**  
   - Gráficos combinados e individuais para exibir:
     - Energia gerada ao longo do tempo.
     - Conteúdo de carbono.
     - Níveis de pH.


## Requisitos

- **Python** 3.8+
- Bibliotecas necessárias (instale usando `pip install`):
  - `pandas`
  - `matplotlib`
  - `numpy`

## Estrutura do Código

1. **Simulação de Dados**  
   - `simulate_data(num_days)`: Gera um DataFrame com dados simulados para energia, carbono e pH.

2. **Filtragem de Dados**  
   - `filter_data_by_date(data, start_date, end_date)`: Filtra os dados com base nas datas fornecidas.

3. **Análise de Dados**  
   - `analyze_energy_generation(data)`: Calcula a média de energia gerada.  
   - `analyze_carbon_levels(data)`: Calcula a média de carbono na água.  
   - `analyze_ph_levels(data)`: Calcula a média de pH.  

4. **Insights Automatizados**  
   - `generate_insights(data, start_date, end_date)`: Fornece os valores médios de energia, carbono e pH para o período especificado.

5. **Visualização**  
   - `plot_data(data, columns, title, ylabels)`: Gráficos combinados para energia, carbono e pH.  
   - `plot_individual_data(data, column, title, ylabel)`: Gráficos individuais por métrica.

## Como Usar

1. Clone o repositório ou copie o código para um arquivo Python local.  
2. Certifique-se de instalar todas as dependências com:
   ```bash
   pip install pandas matplotlib numpy
3. Edite o número de dias ou o intervalo de datas conforme necessário:
   ```
   num_days = 365  # Simular um ano de dados
   start_date = '2023-01-01'
   end_date = '2023-12-31'
   ```
4. Execute o arquivo


## Nomes

Nome: Gustavo Oliveira de Moura RM: 555827
Nome: Lynn Bueno Rosa RM: 551102





