import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Função para simular dados
def simulate_data(num_days):
    """
    Simula dados de energia gerada, carbono e pH da água para um período de num_days dias.
    """
    date_range = pd.date_range(start='2023-01-01', periods=num_days, freq='D')
    energy_generated = np.random.uniform(low=50, high=150, size=num_days)  # Energia em kWh
    carbon_content = np.random.uniform(low=0.1, high=5.0, size=num_days)  # Carbono em mg/L
    ph_level = np.random.uniform(low=6.0, high=8.5, size=num_days)  # pH da água

    data = pd.DataFrame({
        'date': date_range,
        'energy_generated': energy_generated,
        'carbon_content': carbon_content,
        'ph_level': ph_level
    })

    return data

# 2. Funções para filtrar e analisar os dados
def filter_data_by_date(data, start_date, end_date):
    """
    Filtra os dados para o período especificado.
    """
    filtered_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]
    return filtered_data

def analyze_energy_generation(data):
    """
    Analisa os dados para calcular a energia média gerada por algas.
    """
    avg_energy = data['energy_generated'].mean()
    return avg_energy

def analyze_carbon_levels(data):
    """
    Analisa os dados para calcular a média de carbono na água.
    """
    avg_carbon = data['carbon_content'].mean()
    return avg_carbon

def analyze_ph_levels(data):
    """
    Analisa os dados para calcular a média do pH da água.
    """
    avg_ph = data['ph_level'].mean()
    return avg_ph

# 3. Funções aninhadas para simplificar etapas complexas
def generate_insights(data, start_date, end_date):
    """
    Gera insights a partir dos dados simulados, filtrados e analisados.
    """
    filtered_data = filter_data_by_date(data, start_date, end_date)
    avg_energy = analyze_energy_generation(filtered_data)
    avg_carbon = analyze_carbon_levels(filtered_data)
    avg_ph = analyze_ph_levels(filtered_data)
    
    return avg_energy, avg_carbon, avg_ph

# Simulação de dados
num_days = 365  # Simular um ano de dados
data = simulate_data(num_days)

# Parâmetros de filtragem
start_date = '2023-01-01'
end_date = '2023-12-31'

# 4. Geração de insights
avg_energy, avg_carbon, avg_ph = generate_insights(data, start_date, end_date)
print(f"Média de Energia Gerada: {avg_energy:.2f} kWh")
print(f"Média de Carbono na Água: {avg_carbon:.2f} mg/L")
print(f"Média de pH da Água: {avg_ph:.2f}")

# 5. Visualização dos dados
def plot_data(data, columns, title, ylabels):
    """
    Gera gráficos a partir dos dados analisados.
    """
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Data')
    ax1.set_ylabel(ylabels[0], color=color)
    ax1.plot(data['date'], data[columns[0]], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  
    color = 'tab:blue'
    ax2.set_ylabel(ylabels[1], color=color)
    ax2.plot(data['date'], data[columns[1]], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  
    plt.title(title)
    plt.show()

    fig, ax1 = plt.subplots()

    color = 'tab:green'
    ax1.set_xlabel('Data')
    ax1.set_ylabel(ylabels[2], color=color)
    ax1.plot(data['date'], data[columns[2]], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  
    plt.title(title)
    plt.show()

filtered_data = filter_data_by_date(data, start_date, end_date)
plot_data(filtered_data, ['energy_generated', 'carbon_content', 'ph_level'],
          'Dados de Energia, Carbono e pH ao Longo do Tempo',
          ['Energia Gerada (kWh)', 'Carbono (mg/L)', 'pH'])

# Plots individuais
def plot_individual_data(data, column, title, ylabel):
    """
    Gera gráficos individuais para cada métrica analisada.
    """
    data.set_index('date')[column].plot(kind='line')
    plt.title(title)
    plt.xlabel('Data')
    plt.ylabel(ylabel)
    plt.show()

plot_individual_data(filtered_data, 'energy_generated', 'Energia Gerada por Algas ao Longo do Tempo', 'Energia Gerada (kWh)')
plot_individual_data(filtered_data, 'carbon_content', 'Nível de Carbono na Água ao Longo do Tempo', 'Carbono (mg/L)')
plot_individual_data(filtered_data, 'ph_level', 'Nível de pH da Água ao Longo do Tempo', 'pH')
