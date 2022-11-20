# pip install selenium
# pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Doviz():

    def __init__(self, doviz_tipi: str):
        self.doviz_tipi = doviz_tipi
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.icerik = str()
        self.driver.get("https://www.haberturk.com/")

    def getir(self):

        if self.doviz_tipi == "dolar":
            self.icerik = self.driver.find_element(By.CSS_SELECTOR, "a#dolar span:nth-child(2)").text
            self.driver.quit()

        elif self.doviz_tipi == "euro":
            self.icerik = self.driver.find_element(By.CSS_SELECTOR, "a#euro span:nth-child(2)").text
            self.driver.quit()

        elif self.doviz_tipi == "gram-altin":
            self.icerik = self.driver.find_element(By.CSS_SELECTOR, "a#gram-altin span:nth-child(2)").text
            self.driver.quit()

