from conversion import binary_to_decimal, binary_to_octal, binary_to_hexadecimal, \
    decimal_to_binary, octal_to_binary, hex_to_binary

def binary_addition(binary1, binary2):
    # Convert binary numbers to decimal
    decimal1 = binary_to_decimal(binary1)
    decimal2 = binary_to_decimal(binary2)

    # Add decimals
    result_decimal = decimal1 + decimal2

    # Convert decimal result back to binary
    result_binary = decimal_to_binary(result_decimal)

    return result_binary

def binary_subtraction(binary1, binary2):
    # Convert binary numbers to decimal
    decimal1 = binary_to_decimal(binary1)
    decimal2 = binary_to_decimal(binary2)

    # Subtract decimals
    result_decimal = decimal1 - decimal2

    # Convert decimal result back to binary
    result_binary = decimal_to_binary(result_decimal)

    return result_binary

def binary_multiplication(binary1, binary2):
    # Convert binary numbers to decimal
    decimal1 = binary_to_decimal(binary1)
    decimal2 = binary_to_decimal(binary2)

    # Multiply decimals
    result_decimal = decimal1 * decimal2

    # Convert decimal result back to binary
    result_binary = decimal_to_binary(result_decimal)

    return result_binary

def binary_division(binary1, binary2):
    # Convert binary numbers to decimal
    decimal1 = binary_to_decimal(binary1)
    decimal2 = binary_to_decimal(binary2)

    # Check for division by zero
    if decimal2 == 0:
        return "Division by zero error"

    # Divide decimals
    result_decimal = decimal1 / decimal2

    # Convert decimal result back to binary
    result_binary = decimal_to_binary(result_decimal)

    return result_binary

def twos_complement(binary):
    integer, fractional = binary.split('.') if '.' in binary else (binary, '0')

    # Invert bits
    inverted = ''.join(['1' if bit == '0' else '0' for bit in integer + fractional])

    # Add one
    result = bin(int(inverted, 2) + 1)[2:]

    # Adjust length if necessary
    if len(result) < len(inverted):
        result = '0' * (len(inverted) - len(result)) + result

    # Insert decimal point
    index = len(result) - len(fractional)
    result = result[:index] + '.' + result[index:]

    return result