from binary_operations import twos_complement
from conversion import binary_to_decimal

def signed_binary_to_decimal(binary):
    # Check if the number is negative
    if binary[0] == '1':
        # Convert the remaining binary digits to decimal and subtract 1 to get the two's complement
        decimal = -binary_to_decimal(twos_complement(binary[1:]))
    elif binary[0] == '0':
        # Convert binary to decimal for positive numbers
        decimal = binary_to_decimal(binary)
    else:
        print("Invalid binary number!")
    return decimal

def signed_binary_to_octal(binary):
    integer_part, fractional_part = binary.split('.') if '.' in binary else (binary, '0')
    integer_decimal = 0
    fractional_decimal = 0
    octal_integer = ""
    octal_fractional = ""

    # Check if the number is negative (leftmost digit is 1)
    is_negative = False
    if binary[0] == '1':
        is_negative = True

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

    answer = octal_integer + '.' + octal_fractional
    if is_negative:
        answer = '7' + answer
    return answer

def signed_binary_to_hexadecimal(binary):
    integer_part, fractional_part = binary.split('.') if '.' in binary else (binary, '0')
    integer_decimal = 0
    fractional_decimal = 0
    hexadecimal_integer = ""
    hexadecimal_fractional = ""

    # Check if the number is negative (leftmost digit is 1)
    is_negative = False
    if binary[0] == '1':
        is_negative = True
    

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

    answer = hexadecimal_integer + '.' + hexadecimal_fractional
    if is_negative:
        answer = 'F' + answer

    return answer

def signed_decimal_to_binary(x):
    binary = []

    # Convert to string if it's not already
    x = str(x)

    # check if negative
    if '-' in x:
        is_negative = True
        x = x.replace('-', '')
    else:
        is_negative = False

    # checking for radix
    if '.' in x:
        whole = int(x[:x.index('.')])
        frac = float(x) - whole

        temp_whole = []

        # conversion
        while True:
            temp_whole.append('1' if int(whole) % 2 != 0 else '0')

            whole = whole // 2
            if whole == 0:
                temp_whole.reverse()
                for i in temp_whole:
                    binary.append(i)
                break

        binary.append('.')
        decimal_count = 0

        while True:
            if frac * 2 >= 1:
                binary.append('1')
                frac = frac * 2 - 1

            else:
                binary.append('0')
                frac = frac * 2

            decimal_count += 1
            if frac == 0 or decimal_count == 9:
                break

    # conversion without radix
    else:
        x = int(x)
        while True:
            binary.append('1' if int(x) % 2 != 0 else '0')

            x = x // 2
            if x == 0:
                binary.reverse()
                break

    binary = ''.join(binary)

    # padding
    if '.' in binary:
        while len(binary[:binary.index('.')]) % 4 != 0:
            binary = '0' + binary

    else:
        while len(binary) % 4 != 0:
            binary = '0' + binary

    if is_negative:
        binary = twos_complement(binary)
        binary = '1111' + binary

    return binary

def signed_octal_to_binary(octal):
    binary = ""
    
    # Check if the number is negative (leftmost digit is 7)
    is_negative = False
    if octal[0] == '7':
        is_negative = True

    # Remove the negative sign if present
    if is_negative:
        octal = octal[1:]

    # Split into integer and fractional parts
    parts = octal.split('.')
    integer_part = parts[0]
    fractional_part = parts[1] if len(parts) > 1 else ""

    # Convert each octal digit of the integer part to binary
    for digit in integer_part:
        # Convert octal digit to binary
        binary_digit = ""
        octal_digit = int(digit)

        # Convert octal digit to binary manually
        for i in range(3):
            binary_digit = str(octal_digit % 2) + binary_digit
            octal_digit //= 2

        binary += binary_digit

    # If there's a fractional part, handle it
    if fractional_part:
        binary += "."

        # Convert each octal digit of the fractional part to binary
        for digit in fractional_part:
            # Convert octal digit to binary
            binary_digit = ""
            octal_digit = int(digit)

            # Convert octal digit to binary manually
            for i in range(3):
                binary_digit = str(octal_digit % 2) + binary_digit
                octal_digit //= 2

            binary += binary_digit

    # If the number was negative, prepend three '1's to the binary
    if is_negative:
        binary = '111' + binary

    return binary

def signed_hex_to_binary(hexadecimal):
    binary = ""
    
    # Check if the number is negative (leftmost digit is F)
    is_negative = False
    if hexadecimal[0] == 'F':
        is_negative = True

    # Remove the negative sign if present
    if is_negative:
        hexadecimal = hexadecimal[1:]

    # Define a dictionary to map hexadecimal digits to their binary representation
    hex_to_binary = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    # Split into integer and fractional parts
    parts = hexadecimal.split('.')
    integer_part = parts[0]
    fractional_part = parts[1] if len(parts) > 1 else ""

    # Convert each hexadecimal digit of the integer part to binary
    for digit in integer_part:
        binary += hex_to_binary[digit]

    # If there's a fractional part, handle it
    if fractional_part:
        binary += "."

        # Convert each hexadecimal digit of the fractional part to binary
        for digit in fractional_part:
            binary += hex_to_binary[digit]

    # If the number was negative, prepend four '1's to the binary
    if is_negative:
        binary = '1111' + binary

    return binary