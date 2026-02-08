import secrets

def generate_api_token(length=32):
    """
    Generates a secure random API token.
    Args:
        length (int): Length of the token.
    Returns:
        str: The generated token.
    """
    return secrets.token_hex(length)