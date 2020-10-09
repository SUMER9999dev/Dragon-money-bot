"""
адресса Xpath к кнопкам и другим вещам 
обновлять нужно при изменение структуры сайта!
"""


class offsets(object):
    # классы
    money_class = 'money'

    # ставки
    auto_conclusion = '/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div[4]/label/div/input'
    bet = '/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/label/div/input'
    accept_btn = '/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/button'
    # значения кнопок
    accept_btn_text = '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div/button/div'
    # краш
    current_x = '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div'
