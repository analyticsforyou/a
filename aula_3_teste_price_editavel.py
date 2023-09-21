#pip install pandas no terminal do power shell

import pandas as pd

PV = 120000  # Valor do empréstimo
i = (1.07) ** (1/12) - 1  # Convertendo taxa anual para mensal
n = 120  # Tempo em meses
Juros = [0] * n  # Inicialização da lista de juros
Amort = [0] * n  # Inicialização da lista de amortização
Saldo = [0] * n  # Inicialização da lista de saldo devedor

# Cálculo do PMT
PMT = PV * (1 + i) ** n * i / (((1 + i) ** n) - 1)

# Criar um DataFrame pandas com os resultados
df = pd.DataFrame(columns=["Mês", "PMT", "Juros", "Amortização", "Saldo"])

Juros[0] = PV * i
Amort[0] = PMT - Juros[0]
Saldo[0] = PV - Amort[0]

for j in range(1, n):
    Juros[j] = i * Saldo[j - 1]
    Amort[j] = PMT - Juros[j]
    Saldo[j] = Saldo[j - 1] - Amort[j]

# Preencher o DataFrame com os resultados
df["Mês"] = range(1, n + 1)
df["PMT"] = round(PMT, 2)
df["Juros"] = [round(x, 2) for x in Juros]
df["Amortização"] = [round(x, 2) for x in Amort]
df["Saldo"] = [round(x, 2) for x in Saldo]

# Exibir a tabela
print(df)

# Agora você pode editar a tabela conforme necessário

