import random


def load(c):
    while True:
        try:
            if c.is_can_send_bet() and random.randint(1, 5) == 2:
                c.clear_bet()
                
                bet_value = c.get_money() / c.cfg.balance_divide_value()

                c.type_bet(int(bet_value))

                c.send_bet()
            else:
                time.sleep(3)
        except:
            pass
