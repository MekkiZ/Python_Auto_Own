from selenium import webdriver
import time
import os
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

import selenium

class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html
    def test(self):
        driverLocation = "/Users/gatsfreecs/Documents/VSCODE/Python_Stage_cours/libs/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        # Open the provided URL
        driver.get("http://www.letskodeit.com")
        time.sleep() # quand on as un problème il faut seulement rajouter cette action afin d'eviter un shut down, avec un import TIME
        driver.quit()
        
    




ff = RunChromeTests()
ff.test()


