from binary_operations import binary_addition, binary_subtraction, binary_multiplication, binary_division, twos_complement
from conversion import binary_to_decimal, binary_to_octal, binary_to_hexadecimal, decimal_to_binary, octal_to_binary, hex_to_binary

def main():
    while True:
        print("\nMenu-1 (Main Menu)")
        print("[1] Binary Operations")
        print("[2] Number System Conversion")
        print("[3] Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            binary_operations()
        elif choice == '2':
            conversion()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def binary_operations():
    while True:
        print("\nMenu-2 (Binary Operations)")
        print("[1] Division")
        print("[2] Multiplication")
        print("[3] Subtraction")
        print("[4] Addition")
        print("[5] 2's Complement")
        print("[6] Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            dividend = input("Enter the dividend (binary): ")
            divisor = input("Enter the divisor (binary): ")
            quotient = binary_division(dividend, divisor)
            print("Quotient:", quotient)
        
        elif choice == '2':
            num1 = input("Enter the first number (binary): ")
            num2 = input("Enter the second number (binary): ")
            result = binary_multiplication(num1, num2)
            print("Result:", result)

        elif choice == '3':
            minuend = input("Enter the minuend (binary): ")
            subtrahend = input("Enter the subtrahend (binary): ")
            difference = binary_subtraction(minuend, subtrahend)
            print("Difference:", difference)

        elif choice == '4':
            num1 = input("Enter the first number (binary): ")
            num2 = input("Enter the second number (binary): ")
            result = binary_addition(num1, num2)
            print("Result:", result)

        elif choice == '5':
            binary = input("Enter the binary: ")
            result = twos_complement(binary)
            print("Result:", result)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please enter a valid option.")

def conversion():
    while True:
        print("\nMenu-3 (Conversion)")
        print("[1] Binary to X")
        print("[2] Decimal to X")
        print("[3] Octal to X")
        print("[4] Hexa to X")
        print("[5] Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            binary = input("Enter the binary number: ")
            decimal = binary_to_decimal(binary)
            print("Decimal:", decimal)
            print("Octal:", binary_to_octal(binary))
            print("Hexadecimal:", binary_to_hexadecimal(binary))

        elif choice == '2':
            decimal = float(input("Enter the decimal number: "))  
            print("Binary:", decimal_to_binary(decimal))
            print("Octal:", binary_to_octal(decimal_to_binary(decimal)))
            print("Hexadecimal:", binary_to_hexadecimal(decimal_to_binary(decimal)))

        elif choice == '3':
            octal = input("Enter the octal number: ")
            print("Binary:", octal_to_binary(octal))
            print("Decimal:", binary_to_decimal(octal_to_binary(octal)))
            print("Hexadecimal:", binary_to_hexadecimal(octal_to_binary(octal)))

        elif choice == '4':
            hexadecimal = input("Enter the hexadecimal number: ")
            print("Binary:", hex_to_binary(hexadecimal))
            print("Decimal:", binary_to_decimal(hex_to_binary(hexadecimal)))
            print("Octal:", binary_to_octal(hex_to_binary(hexadecimal)))
            
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
