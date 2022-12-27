try:
    import pickle # this is for saving cookies
    import sys # sys module 
    import os # os module 
    from selenium import webdriver # webdriver
    from selenium.webdriver import Chrome # chrome 
    from selenium.webdriver.common.keys import Keys # keys
    from selenium.webdriver.common.by import By # by
    from selenium.webdriver.support.ui import WebDriverWait # webdriverwait
    from selenium.webdriver.support import expected_conditions # expected conditions
    from selenium.common.exceptions import TimeoutException # time out exception
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC # options
    from selenium.webdriver.common.proxy import Proxy, ProxyType
    import time # time module 
    import re
    import json
    import random
    from multiprocessing.pool import ThreadPool, Pool
    import threading
    import concurrent.futures
    print("all modules are loaded!")
except ModuleNotFoundError as e:
    e = f"{e}".split("'")[1]
    print(f"please install the {e} module!")
class FaceBookNumber:
    face_numbers = []
    file_path = input("please put the numbers file path here:>").strip()
    with open(file_path,"r",encoding="utf-8") as f:
        numbers = [number for number in f.readlines()]
    with open("user_agent.txt","r",encoding="utf-8") as f:
        user_agent = [agent for agent in f.readlines()]
    def main(self,number):
        options = Options()
        #options.add_extension('vpn.crx')
        options.add_argument(f'user-agent={random.choice(self.user_agent)}')
        driver = webdriver.Chrome(executable_path=r"chromedriver.exe",options=options)
        driver.get("https://www.facebook.com/login/identify/")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="identify_email"]')))
        search_filed = driver.find_element(By.XPATH,'//*[@id="identify_email"]')
        search_button = driver.find_element(By.XPATH,'//*[@id="did_submit"]')
        search_filed.clear()
        search_filed.send_keys(number)
        search_button.click()
        time.sleep(2)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="identify_yourself_flow"]/div/div[2]/div[1]')))
            print(f"{number} Dosen't have a facebook account!")
        except Exception as e:
            print(f"{number} has a facebook account!")
            if number not in self.face_numbers:
                self.face_numbers.append(number)
    def run(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            executor.map(self.main,self.numbers)
        print("saving the numbers associated with a facbook account into final.txt")
        with open("final.txt","w",encoding="utf-8") as f:
            for item in self.face_numbers:
                f.write(item)
            f.close()
        print(f"Everything is done succefully!\n{len(self.face_numbers)} numbers saved successfully!")
if __name__ == "__main__":
    bot = FaceBookNumber()
    bot.run()
            

