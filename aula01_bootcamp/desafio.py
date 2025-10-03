PADRAO_BONUS = 1000

# 1) novo usuario
nome_usuario = input("Digite o seu nome: ")

# 2) Usuário valor do seu salário
salario_usuario = float(input("Digite o seu salario: "))

# 3) Bônus recebido
bonus_usuario = float(input("Digite o seu bonus: "))

# 4) Valor do bônus final

valor_do_bonus = PADRAO_BONUS + salario_usuario * bonus_usuario

# 5) Mensagem personalizada incluindo o nome do usuário e o valor do bonus
print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")