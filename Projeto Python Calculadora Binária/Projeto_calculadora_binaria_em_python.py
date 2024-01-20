def main_menu():
    print("*** Calculadora Binária ***\n")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair\n")
    choice = input("Escolha a opção (1/2/3/4/5):")
    return int(choice)

def get_binary_input():
    binary_input = input("Entre com o número binário :")
    if not set(binary_input).issubset({'0', '1'}):
        print("Entrada Inválida. Apenas número binário. (0 e 1) são autorizados.")
        return None
    return int(binary_input, 2)

def binary_addition(num1, num2):
    return bin(num1 + num2)[2:]

def binary_subtraction(num1, num2):
    return bin(num1 - num2)[2:]

def binary_multiplication(num1, num2):
    return bin(num1 * num2)[2:]

def binary_division(num1, num2):
    if num2 == 0:
        return "Não se pode dividir por zero!"
    quotient = num1 // num2
    remainder = num1 % num2
    return bin(quotient)[2:] + "." + binary_division_helper(remainder, num2, [])

def binary_division_helper(dividend, divisor, remainders):
    if dividend == 0 or divisor in remainders:
        return "".join([str(i) for i in remainders])
    dividend *= 2
    if dividend >= divisor:
        remainders.append(1)
        dividend -= divisor
    else:
        remainders.append(0)
    return binary_division_helper(dividend, divisor, remainders)

while True:
    choice = main_menu()
    if choice == 5:
        print("Saindo do Programa, Até Logo!")
        break

    num1 = get_binary_input()
    if num1 is None:
        continue

    num2 = get_binary_input()
    if num2 is None:
        continue

    if choice == 1:
        result = binary_addition(num1, num2)
    elif choice == 2:
        result = binary_subtraction(num1, num2)
    elif choice == 3:
        result = binary_multiplication(num1, num2)
    elif choice == 4:
        result = binary_division(num1, num2)

    print(f"Resultado: {result}\n")