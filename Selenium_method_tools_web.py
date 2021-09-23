from selenium import webdriver
import time
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

class Browser():
    def test(self):

        driver=webdriver.Chrome()

        #windows maximize
        driver.maximize_window()

        #ouvertur de l'url
        get_url= driver.get('https://courses.letskodeit.com/practice')
    

        #prednre le titre de la page, savhant que title est un proprieter elle ne comporte pas de parenthese comme les methodes
        titre= driver.title
        print(f'le titre de la page est : {titre}')
    
        #L'url de la page
        currentUrl=driver.current_url
        print(f"Actuellement l'url de la page est {currentUrl}")
    
        #browser Refresh
        driver.refresh()
        print("browser refreshed 1st time")
        driver.get(driver.current_url)
        print('browser refreshed énd time')

        #ouvrire une nouvelle URL
        driver.get('https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text')

        #revenir en arrier dnas le navigateur
        driver.back()
        print("vous retourner en arriere dans l'historique")

        #naviger suivnat dans le navigateur
        driver.forward()
        print("une etape dn suivant dans le navigateur")

        #recuerer la page source
        pageSource=driver.page_source
        print(f'la page source du navigateur : {pageSource}')

     #quitter et close le navigateur
        driver.quit()
        #driver.close()


class ClickWeb(): # ce code sert a aller dans une page web cliquer sur sign in'login) trasnfere vers la page, ensuite renseigner auto les camps email et mpd, effacer le mdp puis remettre le mdp , et cliquer sur login
    def autoClick(self):
        Url1='https://courses.letskodeit.com/'
        driver=webdriver.Chrome()
        driver.get(Url1)
        driver.maximize_window()

        FindXpath= driver.find_element(By.XPATH,"//div[@id='navbar-inverse-collapse']/div//a[@href='/login']").click()
        # autre ecriture FindXpath.clcik()
        #Url2='https://courses.letskodeit.com/login'
        #driver.get(Url2)
        FindXpath2=driver.find_element(By.XPATH,"/html//input[@id='email']").send_keys("gggg@gmail.com")
        # autre ecriture FindXpath2.send_keys("gggg@gmail.com")
        if FindXpath2 == "gggg@gmail.com":
            print('le champs est bien renseigner')
        else:
            print("le champs n'est pas bien renseigner")
        
        time.sleep(5)
       
        FindXpath3=driver.find_element(By.XPATH,"/html//input[@id='password']").send_keys("koko") 
        # autre ecriture FindXpath3.send_keys("koko")
        time.sleep(5)
        
        FindXpath3=driver.find_element(By.XPATH,"/html//input[@id='password']").clear()
        time.sleep(5)
        
        FindXpath3=driver.find_element(By.XPATH,"/html//input[@id='password']").send_keys("koko")
        # autre ecriture FindXpath3.send_keys("koko")
        time.sleep(5)
       
        FindXpath4=driver.find_element(By.XPATH,"//input[@value='Login']").click()
        # autre ecriture FindXpath4.click()
        time.sleep(3)




Cw =ClickWeb()

Cw.autoClick()










        






