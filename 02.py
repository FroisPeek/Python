#questao 1
from math import pow
print("Programa para calcular o volume de uma esfera.")
print("-"*70)
raio = float(input("Informe o raio da esfera: ")) #o usuario vai informar o valor do raio
equacao = (4/3) * pow(raio, 3) #equacao utilizada para a solucao
print(f"O volume da esfera: {equacao:.2f} centimetros cubicos")



#questao 2
print("Media dos valores impar e par.")
print("-" * 70)
ctp = 0  # contador dos numeros pares
cti = 0  # contador dos numeros impares
soma_par = 0  # somador dos pares
soma_impar = 0  # somador dos impares
print("[0] para sair do programa.")
while True:  #estrutura de repetica
    num = int(input("Informe o numero: "))
    if num == 0:  #se o numeor for = 0
        break  #finaliza o programa

    if num % 2 == 0:  #se o resto do numero ao ser dividido por 2 for = 0
        print("valor par")
        print("-" * 30)
        ctp += 1  #soma 1 ao contador par
        soma_par += num  #soma o numero aos numeros pares
    else:  # senao
        print("Valor impar")
        print("-" * 30)
        cti += 1  # soma 1 ao contador impar
        soma_impar += num  #soma o numero aos numero impares

if ctp > 0:  #se o contador for maior q 0, vai ser possivel a divisao
    mediap = soma_par / ctp
    print(f"A media aritmetica dos números par: {mediap:.2f}")
else:
    print("nenhum número par foi digitado.")

if cti > 0:  #se o contador for maior q 0, vai ser possivel a divisao
    mediai = soma_impar / cti
    print(f"A media aritmetica dos números impar: {mediai:.2f}")
else:
    print("nenhum número impar foi digitado.")