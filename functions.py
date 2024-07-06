def is_valid(user_response:str)->bool:
    try:
        number = int(user_response)
        if number < 0:
            raise ValueError(f"Usted ingresó una edad inválida: {user_response}")
        return True
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese una edad válida.")
        return False