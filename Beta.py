def beta_tactical_check(c):
    is_end = c.is_current_end()
    if is_end:
        history_obj = c.get_history()[0]
        return 5.4 <= history_obj and history_obj < 15


def load(c):
    while True:
        try:
            if c.is_can_send_bet() and beta_tactical_check(c):
                c.clear_bet()
                
                bet_value = c.get_money() / c.cfg.balance_divide_value()

                c.type_bet(int(bet_value))


                c.send_bet()
            else:
                time.sleep(3)
                
        except:
            pass
