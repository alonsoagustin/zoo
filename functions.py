from variables import price_list, total
from simple_screen import cls, Print, locate, Input

def request_age():
    while True:
        try: 
            locate(0,0)
            user_response = Input("Ingrese una edad: ")
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
        cls()
        age = request_age()
    return summary_to_pay(price_list)

def summary_to_pay(price_list:dict):
    global total
    y = 2
    cls()
    title = "Resumen"
    locate(1,1)
    Print(title)
    for key, value in price_list.items():
        subtotal = value['contador'] * value['precio']
        string = f'{value['contador']:02d} entradas de {key:.<20s}: ${subtotal:05.2f}'
        locate(1,y)
        Print(string)
        y += 1
    line = '-'
    locate(1,6)
    Print(line * 43)
    locate(1,7)
    Print(f'TOTAL: ${total:.2f}')