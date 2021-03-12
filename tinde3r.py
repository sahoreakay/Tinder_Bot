from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from random import random
from secret import username as un
from secret import password as pw


class tindrbot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get('https://tinder.com/')
        time.sleep(3)
        cookie_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        cookie_btn.click()
        try:
            login_btn1 = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
            login_btn1.click()

        except Exception:
            login_btn2 = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div/main/div/div/div/div[3]/div[2]/div/button[2]')
            login_btn2.click()
        time.sleep(4)

        try:
            login_fb = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
            login_fb.click()
        except Exception:
            more_opt = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/button')
            more_opt.click()
            login_fb = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
            login_fb.click()
        base_window = self.driver.window_handles[0]
        time.sleep(3)
        self.driver.switch_to_window(self.driver.window_handles[1])
        fb_email = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_email.send_keys(un)
        fb_pass = self.driver.find_element_by_xpath('//*[@id="pass"]')
        fb_pass.send_keys(pw)
        fb_login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        fb_login.click()
        time.sleep(15)
        conform_login = self.driver.find_element_by_xpath(
            '//*[@id="platformDialogForm"]/div[3]/div/table/tbody/tr/td[2]/button[2]')
        conform_login.click()
        self.driver.switch_to_window(base_window)

        time.sleep(10)
        enable_loc = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
        enable_loc.click()
        notfic_rej = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
        notfic_rej.click()

    def like(self):
        right_swipe = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        right_swipe.click()
        time.sleep(1)

    def dislike(self):
        left_swipe = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
        left_swipe.click()

    def superlike_popup(self):
        no_thank = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/button[2]')
        no_thank.click()

    def autoswipe(self):
        no_of_likes, no_of_dislikes = 0, 0
        while True:
            rand = random()

            time.sleep(0.5)
            try:
                if(rand < 0.75):
                    self.like()
                    no_of_likes = no_of_likes + 1
                else:
                    self.dislike()
                    no_of_dislikes = no_of_dislikes + 1
            except Exception:
                try:
                    self.superlike_popup()
                except Exception:
                    self.addscrn_popup()
                except Exception:
                    self.match_popup()
                except Exception:
                    time.sleep(10)

            print('{} is th present number of likes'.format(no_of_likes))
            print('{} is the present number of dislikes'.format(no_of_dislikes))

    def addscrn_popup(self):
        not_intrested = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        not_intrested.click()

    def match_popup(self):
        cross = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]')
        cross.click()

    def automsg(self):
        match_list = self.driver.find_element_by_xpath(
            '//*[@id="match-tab"]')
        match_list.click()
        while(True):
            # match_list=self.driver.find_element_by_xpath('//*[@id="match-tab"]')
            # match_list.click()
            rand = random()
            match = self.driver.find_element_by_class_name('matchListItem')
            match.click()
            time.sleep(3)
            chat = self.driver.find_element_by_xpath(
                '//*[@id="chat-text-area"]')
            if(rand <= 0.33):
                chat.send_keys('hey there!!!!\n')
            elif(rand > 0.33 and rand <= 0.66):
                chat.send_keys('yo whats up?!!!!\n')
            else:
                chat.send_keys('holaa!!!!!\n')

            # send=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
            # send.click()

            time.sleep(5)
            # match_list = self.driver.find_element_by_xpath(
            #     '//*[@id="match-tab"]')
            match_list.click()
            time.sleep(5)


bot = tindrbot()
bot.login()
time.sleep(10)
bot.autoswipe()
bot.automsg()

#
# right_swipe=driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
# right_swipe.click()
#
# not_intrested=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]/span')
