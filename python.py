#calculadora simples#

numberOne = 0
numberTwo = 0
result = 0
operation = ""


print ("Bem-vindo a calculadora. \nAs operações válidas são: Adição (+), Subtração (-), Divisão (/) e Multiplicação (*). \nUse os simbolos para indicar qual operação deseja !")
operation = input("Digite a operação: ")
numberOne = int(input("digite o primeiro número: "))
numberTwo = int(input("digite o segundo número: "))

if operation == "+":
 result = numberOne + numberTwo
elif operation == "-":
 result = numberOne - numberTwo
elif operation == "/":
 result = numberOne / numberTwo
elif operation == "*":
 result = numberOne * numberTwo
else:
    result = "Operação Inválida"

print (str(numberOne) + "" + str(operation) + "" + str(numberTwo) + " = " + str(result))