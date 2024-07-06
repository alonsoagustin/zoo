from variables import price_list

def request_age():
    while True:
        try:
            user_response = input("Ingrese una edad: ")
            if user_response == "":
                return False
            else:
                return is_valid(user_response)
        except Exception as e:
            print(f" Error inesperado: {e}")

def is_valid(user_response:str)->bool:
    try:
        number = int(user_response)
        if number < 0:
            raise ValueError(f"Usted ingresó una edad inválida: {user_response}")
        return number
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese una edad válida.")
        return False

def calc_price():
    age = request_age()
    total = 0
    while age:
        for key,value in price_list.items():
            if age < value['edad']:
                value['contador'] += 1
                total += value['precio']
                break
        age = request_age()
    return None