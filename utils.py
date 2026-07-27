import re

def validate_email(email: str) -> bool:
    """
    Verifica si una cadena de texto tiene la estructura básica de un correo electrónico válido.
    Retorna True si contiene '@' y un dominio válido, False en caso contrario.
    """
    if not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email.strip()))
