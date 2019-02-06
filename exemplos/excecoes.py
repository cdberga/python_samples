print("Vamos dividir dois números inseridos por você\n")
num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")

try:
    resultado = int(num1) / int(num2)
    print("O resultado é " + str(resultado))
except ZeroDivisionError:
    print("O segundo número não pode ser zero.")
except ValueError:
    print("Você deve inserir 2 números.")