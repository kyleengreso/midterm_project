from signed_conversion import signed_binary_to_decimal, signed_decimal_to_binary

def signed_binary_addition(binary1, binary2):
    # Convert binary numbers to decimals
    decimal1 = signed_binary_to_decimal(binary1)
    decimal2 = signed_binary_to_decimal(binary2)

    result_decimal = decimal1 + decimal2

    # Convert result back to signed binary

    return signed_decimal_to_binary(result_decimal)

def signed_binary_subtraction(binary1, binary2):
    # Convert binary numbers to decimals
    decimal1 = signed_binary_to_decimal(binary1)
    decimal2 = signed_binary_to_decimal(binary2)

    result_decimal = decimal1 - decimal2

    # Convert result back to signed binary
    return signed_decimal_to_binary(result_decimal)

def signed_binary_multiplication(binary1, binary2):
    # Convert binary numbers to decimals
    decimal1 = signed_binary_to_decimal(binary1)
    decimal2 = signed_binary_to_decimal(binary2)

    result_decimal = decimal1 * decimal2

    # Convert result back to signed binary
    return signed_decimal_to_binary(result_decimal)

def signed_binary_division(binary1, binary2):
    # Convert binary numbers to decimals
    decimal1 = signed_binary_to_decimal(binary1)
    decimal2 = signed_binary_to_decimal(binary2)

    if decimal2 == 0:
        raise ValueError("Division by zero error")

    result_decimal = decimal1 / decimal2

    # Convert result back to signed binary
    return signed_decimal_to_binary(result_decimal)

