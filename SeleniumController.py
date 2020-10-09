"""
контроллер для селениума
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Offsets import offsets
import time
import json
from ConfigReader import Reader


class Controller(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.cfg = Reader()
    
    def open_website(self, url: str) -> None:
        self.driver.get(url)
    
    def close_website(self) -> None:
        self.driver.close()
    
    def is_crash_opened(self) -> bool:
        try:
            self.driver.find_element_by_xpath(offsets.accept_btn)
        except:
            return False
        else:
            return True
    
    def type_auto_conclusion(self, new_value: float) -> None:
        auto_conclusion_input = self.driver.find_element_by_xpath(offsets.auto_conclusion)

        auto_conclusion_input.send_keys(str(new_value))

    def type_bet(self, new_value: float) -> None:
        bet_input = self.driver.find_element_by_xpath(offsets.bet)

        bet_input.send_keys(str(new_value))
    
    def clear_bet(self) -> None:
        bet_input = self.driver.find_element_by_xpath(offsets.bet)
        
        bet_input.clear()
    
    def send_bet(self) -> None:
        bet_button = self.driver.find_element_by_xpath(offsets.accept_btn)

        bet_button.click()
    
    def get_money(self) -> float:
        return float(self.driver.find_element_by_class_name(offsets.money_class).text.replace(',', ''))
    

    def is_current_end(self) -> bool:
        obj = self.get_current_x()
        time.sleep(0.5)
        obj_2 = self.get_current_x()
        if obj_2 == obj:
            time.sleep(0.7)
            return True
        return False
    

    def save_cookie(self) -> None:
        cookies = self.driver.get_cookies()

        cookies_str = json.dumps(cookies)

        with open('cookies.json', 'w') as writer:
            writer.write(cookies_str)
    

    def load_cookie(self) -> None:
        with open('cookies.json', 'r') as reader:
            saved_cookies = json.loads(reader.read())
            for cookie in saved_cookies:
                self.driver.add_cookie(cookie)


    def get_current_x(self) -> float:
        return float(self.driver.find_element_by_xpath(offsets.current_x).text.strip('x'))


    
    def is_can_send_bet(self) -> bool:
        if self.driver.find_element_by_xpath(offsets.accept_btn_text).text == 'Сделать ставку':
            return True
        else:
            return False

    def get_history(self) -> list:
        history = self.driver.find_element_by_class_name('history-buttons-cont')

        history_items = history.find_elements_by_class_name('item')

        history_integers = []

        for history_obj in history_items:
            history_integers.append(float(str(history_obj.text).strip('x')))

        while history_integers == []:
            history_integers = self.get_history()

        return history_integers
