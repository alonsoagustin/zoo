from variables import price_list, total

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
    global total
    age = request_age()
    while age:
        for key,value in price_list.items():
            if age < value['edad']:
                value['contador'] += 1
                total += value['precio']
                break
        age = request_age()
    return summary_to_pay(price_list)

def summary_to_pay(price_list:dict):
    global total
    for key, value in price_list.items():
        subtotal = value['contador'] * value['precio']
        string = f'{value['contador']} entradas de {key}: ${subtotal:.2f}'
        if value['contador'] == 1:
            string = string.replace('entradas','entrada')
        print(string)
    print('-----------------')
    print(f'TOTAL: ${total:.2f}')

calc_price()