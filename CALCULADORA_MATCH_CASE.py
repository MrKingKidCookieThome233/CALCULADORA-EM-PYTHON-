num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

match operacao:
    case "+":
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "*":
        res = num1 * num2
    case "/":
        if num2 != 0:
            res = num1 / num2
        else:
            res = "Erro: divisão por zero!"
    case _:
        res = "Operação inválida!"

print(f"Resultado é igual a {res}")