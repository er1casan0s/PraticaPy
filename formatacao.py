#EXEMPLO 1 -CONVERSÃO DE CHAVES DENTRO DO PRINT
estatura = float(input("Digite sua altura: "))
estatura = estatura * 100

print(f"Sua altura é de: {estatura} cm")
print("Sua altura é de: ",estatura, "cm")

#EXEMPLO 2 - CONVERSÃO DE CHAVES DENTRO DE UMA VARIAVEL
nome = input("Digite seu nome: ")
idade = 29

#MODELO USANDO FORMAT
texto = "Meu nome é {} e tenho {} anos.".format(nome,idade)
#MODELO USANDO %
texto1 = "Meu nome é %s e tenho %d anos." % (nome,idade)

print(texto)
print(texto1)
