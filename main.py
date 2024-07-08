from functions import calc_price
from variables import price_list
from simple_screen import Screen_manager, cls, pause

if __name__ == "__main__":
    with Screen_manager as sc:
        cls()
        calc_price()
        pause(10000)