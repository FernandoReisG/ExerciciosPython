
# Exercício 3 - Cálculo de faturamento diário

import json

# Exemplo de faturamento diário em JSON
faturamento = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612}
]

# Filtrar os dias com faturamento
faturamento_diario = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

# Calcular o menor e maior valor de faturamento
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

# Calcular a média mensal
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Contar os dias com faturamento superior à média mensal
dias_acima_da_media = len([valor for valor in faturamento_diario if valor > media_mensal])

# Exibir os resultados
print(f"Menor faturamento: R$ {menor_faturamento}")
print(f"Maior faturamento: R$ {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
