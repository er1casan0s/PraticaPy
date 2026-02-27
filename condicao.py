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

