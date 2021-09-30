from typing import Type
from selenium.webdriver.common.by import By
from selenium import webdriver
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys



class Scrapping():
    def __init__(self, driver) -> None:
        self.driver=driver
    
    def getBytype(self, TypeChose): # on cree une donction pour localiser le type delement sur la page WEB
        TypeChose= TypeChose.lower() # on utilise lower pour tout mettre ne minuscule
        # icic on va faire des if et elif etc pour pourvoir etre sur de choisir le bon element dans la apge web
        if TypeChose=="id":
            return By.ID
        elif TypeChose=="xpath":
            return By.XPATH
        elif TypeChose == "link text":
            return By.LINK_TEXT
        elif TypeChose == "partial link text":
            return By.PARTIAL_LINK_TEXT
        elif TypeChose == "name":
            return By.NAME
        elif TypeChose == "tag name":
            return By.TAG_NAME
        elif TypeChose == "class name":
            return By.CLASS_NAME
        elif TypeChose == "css selector":
            return By.CSS_SELECTOR
        else:
            print(f"le type : {TypeChose}, n'est pas pris en compte")
        return False
        
        
    
    def Getelement(self, locator, TypeChose="id"): # ceci va identifier lelement en question , on va metter id a tyechose, come si je ne precise pas je sais que cest par default

        elment =None # pour la vider au demarage

        try:
            
            TypeChose= TypeChose.lower() #je vais sa sur typechose, carje veux tester si j'ai bien recu un typechose ( soit id soit xpath dans notre exempl)
            thebyType= self.getBytype(TypeChose)# ma methode precedent pour identifier par quel type delement attirbu je vaux faire une recherche
            element= self.driver.find_element(thebyType,locator)#ensuite jappel mon element, auquel je passe les paremetre ici 
            print('element trouver')
        except:
            print("elment pas trouver attention")
        return element

    def isElementPresent(self,locator, thebyType):# on lui passe un self et un autre paramet si lelement est present ou pa avant de faire apple au emthode getelement etc. on test si un elment exsite
        #element= None ; on supprime cette ligne car on en as pas besoin car on test direct notre element
        
        try:
            element= self.driver.find_element(thebyType,locator)
            if element is not None: #si element si il a etait rempli par qeuqleu chose
                print('element toruver')
                return True
            else:
                print("elment pas trouver attention")
                return False
        except:
            print("elment pas trouver attention")
        return False
        #on cree une methode qui montre si lelement existe ou pas a lequels on place le self , on colle avec leutre code car il est similaire, on va chercher avec cela une liste de nombre on va extraire tout une liste delement , si il envoi zero resultat rien trouver, si il as au moin 1 resultat cest quola trouver un element
        # on calcule apres la longuer du nombre delement
    def elementPresentceCheck(self,thebyType, locator):
        try:
            elementList= self.driver.find_elements(thebyType, locator) # attention icic c'est elementSSSSS
            if len(elementList) > 0: #si la list delement est superieru a zero on as docn localisezr plusieur element on return TRUE
                print('element toruver')
                return True
            else:
                print("elment pas trouver attention")
                return False
        except:
            print("elment pas trouver attention.....")
            return False


class ExplicitWaitType(): 
    def __init__(self, driver) -> None:
        self.driver = driver
        self.hw=Scrapping(driver)

    def waitforElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        
        element= None
        try:
            byType= self.hw.getBytype(locatorType)
            print("attendre un maximum de :: "+str(timeout) +":: les secondes pour les element pour etre clickable" )
            
            wait= WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, 
                                                                              ElementNotVisibleException, 
                                                                              ElementNotSelectableException]) # poll frequency, va delande rtout les seconde si lelement est presetn ou pas, on me tignor exception , pour mettre tout les excpetion qu'on veu ignorer.
        
            element=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Destination']")))

            print("les elements apparaise sur la page")
        
        except:
            print("les element apparaise sur la ppage ( parti :execption)")
            print_stack()






