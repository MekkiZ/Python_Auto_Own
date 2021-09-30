"""
en prenena un exempl on as une iconne pour recharger avec un icpne qui nous le montre, en cliquant sur un lien 
cela charge.

simuler un comporter humain, certian site internet bloque les robot, donc avoir des attente simule les comportement humain pour automatiser des commande.

Selnium propose differnete methode avec une attente.
il yas plusieur methode attente, explicite et implicite

implicite : c'est unand lelement nest aps due suite dispo, il dit webdriver dinterroger le dom apres uncertain temps, expl tout les 5 seocnde on fait un test pour linterroger, value rpar default est 0, une fois mit la methode implcite , il va attendre pour tester pour charger complement.
elle est asser pratique cette methode il veux verifier si tout la page est chatrger

explicite: c'est pour la personalisaiton, mettre des temps dattente dasn certain ligne de cocede, il ya s plusieur merthode: expl dasn expedia. voir pdf



"""


from selenium import webdriver
import time
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Own_Framwork_Scrapp import Scrapping # on apple la methode cree precdeement pour ma reeutiliser ici
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from Own_Framwork_Scrapp import ExplicitWaitType


#on as un erreur sasn mettre des temps attente car il faut un temps pour que l'erreur ne soit plus.


class CheckList():
    def AttentePY(self):
        driver= webdriver.Chrome()
        ulr="https://courses.letskodeit.com/practice"
        driver.get(ulr)
        driver.maximize_window()
        
        driver.implicitly_wait(10)#methode implicite, cette methode va attendre 10 seonce avant que la page soit charger et continuer le code, cette methode sapplique a tout les elements

        

        elemnt1= driver.find_element(By.XPATH,"//a[normalize-space()='Sign In']")
        elemnt1.click()
        

        emailField=  driver.find_element(By.XPATH,"//form[@role='form']//input[@id='email']")
        emailField.send_keys("gogogo@gmail.com")
        driver.quit()


class ExplicitWaitDemo2Expedia(): #code obselete, il faut trouver comment contourner le code sur chrome du moins


    def test(self):
        chrome_options = webdriver.ChromeOptions()
        
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(.5)
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        driver.get(baseUrl)
        driver.find_element_by_link_text("Flights").click()
        driver.find_element(By.LINK_TEXT, "One-way").click()
        driver.find_element(By.CLASS_NAME, "uitk-faux-input").send_keys("SFO")
        driver.find_element(By.LINK_TEXT, "Going to").send_keys("NYC")
        driver.find_element(By.LINK_TEXT,"Search")
        returnDate = driver.find_element(By.ID, "flight-returning")
        

        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()


        '''
        wait= WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, 
                                                                              ElementNotVisibleException, 
                                                                              ElementNotSelectableException]) # poll frequency, va delande rtout les seconde si lelement est presetn ou pas, on me tignor exception , pour mettre tout les excpetion qu'on veu ignorer.
        
        element=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Destination']")))
        element.click()
        #  alors ici on met dans notre on as beosinces ligne de code, on a cre notre variable notre variable avec un attente 10 on demande quil introge le dom tout les 10 seconde, on ignore les expection si il en fais face, on import les librairi sinon sa marchera spas, cette methode va attendre ensuite a lelement on va dire quil va dire quil atten en mettant une condition jusqua quil trouve, ce "//button[@aria-label='Destination']" jusqua quil soit clickable, il passe a la suite
        
        
        note perso : il faut babsolument comprendre comment contourner le captcha de lautomatisation du code.
        '''



