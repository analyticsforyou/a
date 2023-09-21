#%%
import pandas as pd

#%%
PV = 120000  # Valor do empréstimo

#%%
i = (1.07) ** (1/12) - 1  # Taxa de juros mensal

#%%
n = 120  # Tempo em meses

#%%
# Calcula a amortização constante
Amort_constante = PV / n

#%%
# Inicializa as listas para armazenar os resultados
Saldo = [PV]
Juros = []
Amortizacao = []

#%%
# Calcula os valores de juros, amortização e saldo para cada mês
for mes in range(1, n + 1):
    juros = Saldo[mes - 1] * i
    amortizacao = Amort_constante
    saldo = Saldo[mes - 1] - amortizacao

    Juros.append(juros)
    Amortizacao.append(amortizacao)
    Saldo.append(saldo)
    
#%%
# Cria um DataFrame pandas com os resultados
df = pd.DataFrame({
    "Mes": range(1, n + 1),
    "Juros": Juros,
    "Amortizacao": Amortizacao,
    "Saldo": Saldo[:-1],  # Remove o último valor do saldo, que é zero
})

#%%
# Arredonda os valores para duas casas decimais
df = df.round(2)

#%%
# Exibe a tabela
print(df)

#%%
import matplotlib.pyplot as plt

# Extrai os valores de mês e juros do DataFrame
meses = df["Mes"]
juros = df["Juros"]
amortizacao = df["Amortizacao"]
saldo_contrato = df["Saldo"]

# Cria o gráfico de linha para os juros
plt.figure(figsize=(10, 6))  # Define o tamanho da figura (opcional)
plt.plot(meses, juros, marker='o', linestyle='-', color='b', label='Juros')

# Configurações do gráfico
plt.title('Gráfico de Juros ao longo do Tempo')
plt.xlabel('Mes')
plt.ylabel('Juros')
plt.grid(True)
plt.legend()

# Exibe o gráfico
plt.show()

# %%
#Total de juros pagos no contrato
Total_juros =  sum(juros)

# %%
# Extrai os valores de amort e saldo do DataFrame
amortizacao = df["Amortizacao"]
saldo_contrato = df["Saldo"]

# Cria o gráfico de linha
plt.figure(figsize=(10, 6))  # Define o tamanho da figura (opcional)
plt.plot(meses, saldo_contrato, marker='o', linestyle='-', color='b', label='Saldo SAC')

# Configurações do gráfico
plt.title('Gráfico de evolução do saldo do contrato no SAC')
plt.xlabel('Meses')
plt.ylabel('Saldo do Contrato')
plt.grid(True)
plt.legend()

# Exibe o gráfico
plt.show()

# %%
Total_juros =  sum(juros) 
Total_amortização =  sum(amortizacao) 
Total_pagto = Total_juros+Total_amortização 
print(Total_amortização) #Total de amortização pagos no contrato
print(Total_juros) #Total de juros pagos no contrato
print(Total_pagto) #Total a pagar no prazo do contrato


# %%
