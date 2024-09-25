
# Exercício 5 - Inverter uma string sem usar funções prontas

def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

# Teste
texto = "Exemplo de string"
print(inverter_string(texto))
