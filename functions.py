from variables import price_list, total
from simple_screen import cls, Print, locate, Input

def request_age():
    while True:
        try: 
            locate(0,8)
            user_response = Input("Ingrese una edad: ")
            if user_response == "":
                user_response = "Saliendo del programa"
                locate(0,8)
                Print(user_response)
                return False
            else:
                cls()
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
        break
    return age

def summary_to_pay():
    global total, price_list
    cls()
    age = True
    while age:
        y = 1
        title = " RESUMEN DE COMPRA" 
        locate(0,0)
        Print(title)
        for key, value in price_list.items():
            subtotal = value['contador'] * value['precio']
            string = f'{key:.<20s} {value['precio']:05.2f} ..... {value['contador']:02d} ..... €{subtotal:05.2f}'
            locate(0,y)
            Print(string)
            y += 1
        line = '-'
        locate(0,5)
        Print(line * 43)
        locate(0,6)
        Print(f'TOTAL: €{total:05.2f}')
        age = calc_price()