from functions import calc_price, summary_to_pay,request_age
from variables import price_list
from simple_screen import Screen_manager, cls, pause

if __name__ == "__main__":
    with Screen_manager as sc:
        summary_to_pay()
        pause(10000)