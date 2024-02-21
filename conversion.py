def binary_to_decimal(binary):
    integer_part, fractional_part = binary.split('.')
    decimal = 0
    
    # Convert integer part
    for digit in integer_part:
        decimal = decimal * 2 + int(digit)
    
    # Convert fractional part
    fractional_decimal = 0
    for i in range(len(fractional_part)):
        fractional_decimal += int(fractional_part[i]) * (2 ** -(i + 1))
    
    return decimal + fractional_decimal

def binary_to_octal(binary):
    integer_part, fractional_part = binary.split('.') if '.' in binary else (binary, '0')
    integer_decimal = 0
    fractional_decimal = 0
    octal_integer = ""
    octal_fractional = ""

    # Convert integer part to decimal
    for i in range(len(integer_part)):
        integer_decimal += int(integer_part[-i - 1]) * (2 ** i)

    # Convert fractional part to decimal
    for i in range(len(fractional_part)):
        fractional_decimal += int(fractional_part[i]) * (2 ** -(i + 1))

    # Convert integer decimal to octal
    while integer_decimal > 0:
        octal_integer = str(integer_decimal % 8) + octal_integer
        integer_decimal //= 8

    # Convert fractional decimal to octal
    for i in range(10):  # Consider maximum precision of 10 for fractional part
        fractional_decimal *= 8
        octal_fractional += str(int(fractional_decimal))
        fractional_decimal -= int(fractional_decimal)

    return octal_integer + '.' + octal_fractional

def binary_to_hexadecimal(binary):
    integer_part, fractional_part = binary.split('.') if '.' in binary else (binary, '0')
    integer_decimal = 0
    fractional_decimal = 0
    hexadecimal_integer = ""
    hexadecimal_fractional = ""

    # Convert integer part to decimal
    for i in range(len(integer_part)):
        integer_decimal += int(integer_part[-i - 1]) * (2 ** i)

    # Convert fractional part to decimal
    for i in range(len(fractional_part)):
        fractional_decimal += int(fractional_part[i]) * (2 ** -(i + 1))

    # Convert integer decimal to hexadecimal
    while integer_decimal > 0:
        remainder = integer_decimal % 16
        hexadecimal_integer = (str(remainder) if remainder < 10 else chr(remainder + 55)) + hexadecimal_integer
        integer_decimal //= 16

    # Convert fractional decimal to hexadecimal
    for i in range(10):  # Consider maximum precision of 10 for fractional part
        fractional_decimal *= 16
        digit = int(fractional_decimal)
        hexadecimal_fractional += (str(digit) if digit < 10 else chr(digit + 55))
        fractional_decimal -= digit

    return hexadecimal_integer + '.' + hexadecimal_fractional

def decimal_to_binary(decimal):
    binary = ""
    if decimal == 0:
        return "0"
    
    integer_part = abs(int(decimal))
    fractional_part = abs(decimal - integer_part)
    
    # Convert integer part to binary
    while integer_part > 0:
        binary = str(integer_part % 2) + binary
        integer_part //= 2
    
    # Add fractional part
    if fractional_part != 0:
        binary += "."
        precision = 10  # Maximum precision for the fractional part
        while fractional_part != 0 and precision > 0:
            fractional_part *= 2
            if fractional_part >= 1:
                binary += "1"
                fractional_part -= 1
            else:
                binary += "0"
            precision -= 1
    
    return binary

def octal_to_binary(octal):
    integer_part, fractional_part = octal.split('.') if '.' in octal else (octal, '0')
    integer_binary = ""
    fractional_binary = ""

    # Convert integer part to binary
    for digit in integer_part:
        binary_digit = bin(int(digit))[2:].zfill(3)
        integer_binary += binary_digit

    # Convert fractional part to binary
    if fractional_part != '0':
        fractional_binary += '.'
        for digit in fractional_part:
            binary_digit = bin(int(digit))[2:].zfill(3)
            fractional_binary += binary_digit

    return integer_binary + fractional_binary

def hex_to_binary(hexadecimal):
    hex_to_bin = {
        '0': "0000", '1': "0001", '2': "0010", '3': "0011",
        '4': "0100", '5': "0101", '6': "0110", '7': "0111",
        '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
        'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"
    }

    integer_part, fractional_part = hexadecimal.split('.') if '.' in hexadecimal else (hexadecimal, '0')
    integer_binary = ""
    fractional_binary = ""

    # Convert integer part to binary
    for digit in integer_part:
        integer_binary += hex_to_bin[digit]

    # Convert fractional part to binary
    if fractional_part != '0':
        fractional_binary += '.'
        for digit in fractional_part:
            fractional_binary += hex_to_bin[digit]

    return integer_binary + fractional_binary
