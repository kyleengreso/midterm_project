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

# Example usage:
hexadecimal_input = "FFF.AB"
binary_output = signed_hex_to_binary(hexadecimal_input)
print("Binary representation:", binary_output)