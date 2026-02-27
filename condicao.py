#https://www.programiz.com/python-programming/online-compiler/
#EXEMPLOS DE CONDIÇÂO

nome = input("Digite seu nome: ")
if len(nome) >= 5: #len() -> mostrar tamanho da string
    print("Seu nome é grande, ele possui mais de 20 letras")
print(f"Seu nome {len(nome)} caracteres.")

#EXEMPLOS IF-SE e ELSE-SENAO
numero = int(input("Digite um número: "))
if numero %2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
 
#EXEMPLOS DE IF-ELSE-IF
nota = float(input("DIGITE SUA NOTA: "))
if nota <= 10 and nota >7:
    print("PASSOU!")
else:
    if nota == 7:
        print("Pode melhorar.")
    else:
        print("Recuperação.")


#EXEMPLO IF-ELIF-ELSE
nota1 = float(input("Digite sua nota: "))

if nota1 <= 10 and nota1 >7:
    print("PASSOU. VERY GOOD!")
elif nota1 == 7:
    print("Vamos estudar né")
else:
    if nota1 < 6.9 and nota1 >= 2:
        print("iiih, foi para a recuperação.")
    else:
        print("REPROVOU!")

#EXEMPLO IDADE

idade = int(input("Digite sua idade: "))

if idade >= 16 and idade <= 69:
    print("Faixa permitida.")
else:
    print("Fora de faixa.")
