
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    res = num1 + num2
elif operacao == "-":
    res = num1 - num2
elif operacao == "*":
    res = num1 * num2
elif operacao == "/":
    res = num1 / num2

print("Resultado:", res)