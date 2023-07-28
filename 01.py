"""
questao 1:

print("Área lateral de um cilindro reto") #mensagem padrao
raio = float(input("Valor do raio do cilindo: ")) #para o usuario informar o valor do raio
altura = float(input("Valor da altura do cilindo: ")) #para o usuario informar o valor da altura
al = 2 * raio * altura #formula para calcular
print(f"A área lateral do cilindo é: {al}") #mensagem mostrando o resulatado
"""


"""
questao 2:

print("Informe dois valores para colocar em ordem crescente.") #dando um comando para o usuario
x = int(input("Digite um valor: ")) # usado para o usuario informar o primeiro valor
y = int(input("Digite outro valor: ")) # para informar o segundo valor
if x > y: #se x for maior que y aparece as mensagens abaixo
    print(f"O valor {x} é maior que {y}.")
    print(f"{x}>{y}")
elif x < y: #se y for maior que x aparece as mensagem abaixo
    print(f"O valor {y} é maior que {x}.")
    print(f"{y}>{x}")
else: #se os valores forem iguais aparece a mensagem abaixo
    print("Os dois valores sao iguais.")
    print(f"{x}={y}")
"""

"""
questao 3: 

ct = 0 #atribui um valor a ct = contador
soma = 0 #atribui um valor a soma
media = 0 #atribui um valor a media 
print("Digite [0] para sair do programa.") #mensagem que informa qual botao apertar para sair do comando
while True: # estrutura de repeticao
    x = int(input("Informe um valor: ")) #pede para o programa informar os valores
    if x == 0: # se for = 0
        break # finaliza o programa
    else: # senao 
        ct = ct + 1 # adiciona 1 ao contador
        soma = soma + x #a soma dos valores informados
        media = soma / ct # media dos valores informados
print(f"A quantidade de valores digitados foram: {ct}") #mensagem que informa a quantidade de valores
print(f"A soma dos valores: {soma}") #mensagem que informa a soma desses valores
print(f"A média aritmética: {media}") #mensagem que informa a media
"""

























