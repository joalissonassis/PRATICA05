import datetime

def calcular_idade_em_dias(ano_nascimento):
    hoje = datetime.date.today()
    nascimento = datetime.date(ano_nascimento, 1, 1)  # Assume que nasceu em 1º de janeiro
    idade_dias = (hoje - nascimento).days
    return idade_dias

# Input do usuário
try:
    ano_nasc = int(input("Digite o ano de nascimento: "))
    idade_em_dias = calcular_idade_em_dias(ano_nasc)
    print(f"Sua idade aproximada em dias é: {idade_em_dias} dias")
except ValueError:
    print("Por favor, digite um ano válido.")
