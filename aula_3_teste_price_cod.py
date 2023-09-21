print("Sistem de amortização PRICE")

PV = 120000  # Valor do empréstimo
i = (1.07) ** (1/12) - 1  # Convertendo taxa anual para mensal
n = 120  # Tempo em meses
Juros = [0] * n  # Inicialização da lista de juros
Amort = [0] * n  # Inicialização da lista de amortização
Saldo = [0] * n  # Inicialização da lista de saldo devedor

# Cálculo do PMT
PMT = PV * (1 + i) ** n * i / (((1 + i) ** n) - 1)

print("PMT:", round(PMT, 2))

Juros[0] = PV * i
Amort[0] = PMT - Juros[0]
Saldo[0] = PV - Amort[0]

for j in range(1, n):
    Juros[j] = i * Saldo[j - 1]
    Amort[j] = PMT - Juros[j]
    Saldo[j] = Saldo[j - 1] - Amort[j]

# Criar uma lista de listas para resultados
Price = list(zip(range(1, n + 1), [round(PMT, 2)] * n, [round(x, 2) for x in Juros], [round(x, 2) for x in Amort], [round(x, 2) for x in Saldo]))

for row in Price:
    print("Mês:", row[0], "PMT:", row[1], "Juros:", row[2], "Amortização:", row[3], "Saldo:", row[4])
