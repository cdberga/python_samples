print("Vamos dividir dois números inseridos por você\n")
num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")

try:
    resultado = int(num1) / int(num2)
    print("O resultado é " + str(resultado))
except:
    print("Entrada é inválida. Favor inserir dois números, sendo o segundo diferente que zero")