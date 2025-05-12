#Estruturas Lógicas & Estruturas Condicionais:

#Exemplo 1:
idade = 18
tem_carteira = True
if idade >= 18 and tem_carteira:
# if idade >= 18 or tem_carteira:
 print("Pode dirigir.")
else:
 print("Não pode dirigir.")

#Exemplo 2:
nota = 7.5
frequencia = 50
if nota >= 7 and frequencia >= 75:
 print("Aprovado!")
elif nota >= 5 and frequencia >= 75:
 print("Recuperação.")
else:
 print("Reprovado.")

#Exemplo 3:
tem_cafe = False
if not tem_cafe:
 print("Precisamos fazer mais café!")
else:
 print("Já temos café suficiente.")

#Exemplo 4:
numero = int(input("Digite um número: "))
if numero > 0 or numero % 2 == 0:
 print("O número é positivo ou par")
else:
 print("O número não é positivo nem par")

