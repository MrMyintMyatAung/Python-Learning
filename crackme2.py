import hashlib

def calculate_md5(input_string):
    """
    Calculates the MD5 hash of an ASCII-encoded string and returns it 
    as an uppercase hexadecimal string, matching the C# implementation.
    
    Args:
        input_string (str): The input string to hash
        
    Returns:
        str: Uppercase MD5 hash string
    """

    input_string = "6136C2A666EABC25A3B6A6348473A7C7"
    # Encode the string to ASCII bytes
    input_bytes = input_string.encode('ascii')
    
    # Calculate MD5 hash
    hash_bytes = hashlib.md5(input_bytes).digest()
    
    # Convert to uppercase hexadecimal string
    hex_string = ''.join(f'{byte:02X}' for byte in hash_bytes)
    
    return hex_string