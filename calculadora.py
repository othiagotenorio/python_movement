#calculadora simples#

while True:

    print ("Bem-vindo a calculadora. \nAs operações válidas são: Adição (+), Subtração (-), Divisão (/) e Multiplicação (*). \nUse os simbolos para indicar qual operação deseja !")
    operation = input("Digite a operação: ")
    numberOne = int(input("digite o primeiro número: "))
    numberTwo = int(input("digite o segundo número: "))
    result = 0

    # invés de colocar int(input("digite o numero tal...")), poderia fazer somente input e usar o codigo a seguir:

     #if not numberOne.isnumeric() or not numberTwo.isnumeric():
     #   print("Você precisa digitar um número !")
     #   continue

    if operation == "+":
        result = (numberOne + numberTwo)
    elif operation == "-":
        result = (numberOne - numberTwo)
    elif operation == "/":
        result = (numberOne / numberTwo)
    elif operation == "*":
        result = (numberOne * numberTwo)
    else:
        result = ("Operação inválida")
        

    print ("O resultado de " + str(numberOne) + "" + str(operation) + "" + str(numberTwo) + " = " + str(result))