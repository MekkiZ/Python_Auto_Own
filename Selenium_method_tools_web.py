
from selenium import webdriver
import time
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Own_Framwork_Scrapp import Scrapping # on apple la methode cree precdeement pour ma reeutiliser ici
from selenium.webdriver import ActionChains








class Browser(): #quelques methode a faire sur une page web pour automatier le tout
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
        pageSource=driver.page_source#ceci est un proprrieter de webdriver
        print(f'la page source du navigateur : {pageSource}')

     #quitter et close le navigateur
        driver.quit()
        #driver.close()


class ClickWeb(): # ce code sert a aller dans une page web cliquer sur sign in'login) trasnfere vers la page, ensuite renseigner auto les champs email et mpd, effacer le mdp puis remettre le mdp , et cliquer sur login
    def autoClick(self):
        Url1='https://courses.letskodeit.com/'
        driver=webdriver.Chrome()
        driver.get(Url1)
        driver.maximize_window()
        #driver.implicitly_wait() ;  cela sert comme el time.sleep, sauf que ici selenium va attendre 10 seconde si ils ne trouee pas les element si il trouve pas il relance le code 10s etc etc, si je relance mon code le pagre se charge , il va attendre A0seconde il va relancer le code

        FindXpath= driver.find_element(By.XPATH,"//div[@id='navbar-inverse-collapse']/div//a[@href='/login']").click()
        # autre ecriture FindXpath.clcik()
        #Url2='https://courses.letskodeit.com/login'
        #driver.get(Url2)
        ecriture_mail="gggg@gmail.com"
        FindXpath2=driver.find_element(By.XPATH,"/html//input[@id='email']").send_keys(ecriture_mail)

        # autre ecriture FindXpath2.send_keys("gggg@gmail.com")
        
        if FindXpath2 == "gggg@gmail.com" : #le if ne marche trouver comment réussir ce code !!!!!!
            print('le champs est bien renseigner')
        else:
            print("le champs n'est pas bien renseigner")
        
        time.sleep(3)
       
        FindXpath3=driver.find_element(By.XPATH,"/html//input[@id='password']").send_keys("koko") 
        # autre ecriture FindXpath3.send_keys("koko")
        time.sleep(3)
        
        FindXpath3=driver.find_element(By.XPATH,"/html//input[@id='password']").clear()
        time.sleep(3)
        
        FindXpath3=driver.find_element(By.XPATH,"/html//input[@id='password']").send_keys("koko")
        # autre ecriture FindXpath3.send_keys("koko")
        time.sleep(3)
       
        FindXpath4=driver.find_element(By.XPATH,"//input[@value='Login']").click()
        # autre ecriture FindXpath4.click()
        time.sleep(3)



class StatueDesElements(): # Ce code sert a ouvire page google, cliquer sur jaccepte des mention legal, puis ecrier un ecrito sur la bar de recherche et ensuite envoyer cela
    
    def statue(self):
        driver=webdriver.Chrome()
        Lur=driver.get("https://www.google.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        
        time.sleep(3)
        #on va essayer de clqiuer sur le accpter de la page de popup qui vien a l'ouverture d ela page

        pop_1= driver.find_element_by_id("L2AGLb").click()
        #time.sleep(3)

        elementFirst=driver.find_element_by_xpath("//input[@role='combobox']")
        bouton_sub=driver.find_element_by_name('btnK')
        element1_etat=elementFirst.is_enabled()
        print("L'etat de l'élément est :" + str(element1_etat))
        elementFirst.send_keys('letskodeit')
        time.sleep(3)
        elementFirst.submit()

    

        #element1_etat=elementFirst.is_enabled()
        #print("L'etat de l'élément est :" + str(element1_etat))
       
        #elementFirst=driver.find_element(By.XPATH,"//input[@title='Rechercher']")
        #element1_etat=elementFirst.is_enabled() # il renvoi a true mm false
        #print("L'etat de l'élément est :" + str(element1_etat))
        
        """
        on fais la meme chose quand on as plusieur input biensur on change les ID ou le XPath de chaqu'un 


        elementSecond=driver.find_element(By.XPATH,"//input[@title='Rechercher']")
        element2_etat=elementSecond.is_enabled()
        print("L'etat de l'élément est :" + str(element2_etat))

        elementThird=driver.find_element(By.XPATH,"//input[@title='Rechercher']")
        element3_etat=elementThird.is_enabled()
        print("L'etat de l'élément est :" + str(element3_etat))
        
        
        """

class CheckBox():
    
    def cocher(self):
        driver=webdriver.Chrome()
        get_url="https://courses.letskodeit.com/practice"
        driver.implicitly_wait(5)
        driver.get(get_url)

        ElementBox = driver.find_element_by_xpath("//input[@id='bmwradio']").click()
        ElementBoxS= driver.find_element_by_xpath("//input[@id='bmwradio']").is_selected()# vrai si il est selection , faux si il n'est pas selectionner, cette methode sert a sa
        
        time.sleep(3)

        ElementBox2= driver.find_element_by_xpath("//input[@id='hondaradio']").click()
        
        print('les boutton bmw radion est selctionner : ' + str(ElementBoxS)) # vrai si il est selection , faux si il n'est pas selectionner, cette methode sert a sa
        #print('les boutton bmw radion est selctionner : ' + ElementBox2.is_selected())
        
        time.sleep(5)
    




class CheckList():
    def listCheck(self):
        driver= webdriver.Chrome()
        ulr="https://courses.letskodeit.com/practice"
        driver.get(ulr)
        driver.maximize_window()
        driver.implicitly_wait(5)
        
        elementRadio= driver.find_elements(By.XPATH,"//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(elementRadio) #on calcule ici sa taille 
        print(f"la taile de al lsite est : {str(size)}")

        for boutton in elementRadio:        #fair une boucle pour verifier le nom d'elemeent d'une liste, les selectionner chcun
            Selectionner = boutton.is_selected()
            print(f'{str(boutton)}')
            
            if not Selectionner:
                boutton.click()
                print(f'{str(boutton)}')
                time.sleep(2)



class SelectList():
    def choisir(self):

        driver= webdriver.Chrome()
        g_url="https://courses.letskodeit.com/practice"
        driver.get(g_url)
        element1= driver.find_element_by_id('carselect')# on choisie avec le id par exemple la div qui englobe le tout et on utilise apres SELECT()
        sel=Select(element1)#select seet a selectionner les element de differente maniere
        
        #selectionner la propositiond e la liste par sa "value"
        
        l1=sel.select_by_value('benz')
        print("Tu as choisi : " + str(l1))
        time.sleep(3)

        #selectionner Honda par son index expl : [0,1,2,3....]
        l2=sel.select_by_index("2")

        print("Tu as choisie : " +str(l2))
        time.sleep(3)


        #Selectionner BMW par "visile text"
        l3=sel.select_by_visible_text('BMW')

        print("tu as choisi : " +str(l3) )
        time.sleep(3)

        
#faire ici le hidden show avec pratice.com et reouvrire la page experia juste apres icci:














class ElementHidden():
    def voirElement(self):
        driver= webdriver.Chrome()
        get_URL="https://www.expedia.fr/"
        driver.get(get_URL)
        step1=driver.find_element_by_xpath("//button[normalize-space()='1 chambre, 2 voyageurs']").click()
        time.sleep(3)
        step2 = driver.find_element_by_xpath("//button[normalize-space()='Ajouter une autre chambre']")
        
        step2bis=step2.is_displayed()# cette focntion sert a savoir si cela est afficher ou pas , il renvoi true ou false come selected etc..
        print('le text est il visible ?'  + str(step2bis))
        time.sleep(3)
        
        step2ter = driver.find_element_by_xpath("//button[normalize-space()='Ajouter une autre chambre']").click()
        visibleStep2ter= step2ter.is_displayed()
        print('est il visible : ' +str(visibleStep2ter))
        time.sleep(3)
        driver.quit()



class TextGet():#essayer de faire cette focntiona avec le partiel link, et avec d'autre trvailler cette focntion plus en pronfondeur
    def TextRecup(self):
        driver=webdriver.Chrome()
        get_UrL="https://courses.letskodeit.com/practice"
        driver.get(get_UrL)
        driver.maximize_window()
        driver.implicitly_wait(10)

        txt1= driver.find_element_by_id("opentab")
        get_title= txt1.text
        print("le titre de l'élément est : " + get_title)
        time.sleep(1)
        driver.quit()


class GetAttribu():
    def scrapperAttribu(self):
        driver= webdriver.Chrome()
        get_uRl="https://courses.letskodeit.com/practice"
        driver.get(get_uRl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        attri=driver.find_element_by_id('mousehover')
        fo=attri.get_attribute("class")#recupere la valeur de l attribu class par exemple

        print("l'altribu est ' : " + str(fo))
        time.sleep(1)
        driver.quit()





class UnsingScrapper():# cette focntion est pour tester le fichier meth_creaation...
    def test(self):
        driver= webdriver.Chrome()
        get_uRl="https://courses.letskodeit.com/practice"
        driver.get(get_uRl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw= Scrapping(driver)

        textField=hw.Getelement("name")
        textField.send_keys('koki')
        time.sleep(2)

        textField2= hw.Getelement("//input[@id='name']", "xpath")
        textField2.clear()
        driver.quit()


class UnsingScrapper():# cette focntion est pour tester le fichier meth_creaation...
    def test(self):
     
        get_uRl="https://courses.letskodeit.com/practice"   
        driver= webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw= Scrapping(driver)
        driver.get(get_uRl)

        elementR= hw.isElementPresent("name", By.ID)
        print(str(elementR))

        elementR2= hw.elementPresentceCheck(By.XPATH, "/html//input[@id='name']")#on recueille le nombre delemnet an une liste 0 aucun plus de 1 element trouver




 #faire ici le cours 46 selinum  utiliser la postion format pour rempler les {0, 1 , 2 , 3 , 4} par un text exmpl : xxxxx.format("xxxxx", "xxxx","xxxx"...)





class CalendarChose():
    def datechose(self):
        driver= webdriver.Chrome()
        get_url="https://www.expedia.fr/"
        driver.get(get_url)
        driver.implicitly_wait(5)

        driver.find_element(By.XPATH,"//span[normalize-space()='Vols']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//span[normalize-space()='Aller simple']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[normalize-space()='13 oct.']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[@aria-label='29 oct. 2021']").click()
        time.sleep(3)

    def test2(self):
        driver= webdriver.Chrome()
        get_url="https://www.expedia.fr/"
        driver.get(get_url)
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,"//span[normalize-space()='Vols']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//span[normalize-space()='Aller simple']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[normalize-space()='14 oct.']").click()
        allValidates=driver.find_elements(By.XPATH,"//button[@class='uitk-date-picker-day uitk-new-date-picker-day']")
        time.sleep(3)
        for date in allValidates: # voici le resultat pour chercher un date avec un if
            
            ju=driver.find_element(By.XPATH,"//button[@aria-label='28 oct. 2021']")
            
            if date == ju:
                ju.click()
                print("__________")
                break # pour sprtire de la boucle
        time.sleep(3)




#auto-suggestion sur un formulaire avec des suggestion 

class Auto_Sugg():
    
    
    def suggestionChose(self):
        driver= webdriver.Chrome()
        get_url="https://www.southwest.com/"
        driver.get(get_url)
        driver.implicitly_wait(5)
        el=driver.find_element(By.XPATH,"//input[@id='LandingAirBookingSearchForm_originationAirportCode']")
        el.click()
        time.sleep(3)
        el.send_keys('Los angeles')
        time.sleep(3)
        el1=driver.find_element(By.XPATH,"//button[@aria-label='Los Angeles Area Airports - Burbank, CA - BUR']")
        el1.click()
        time.sleep(3)
        driver.quit()




#execution de commande JAVASCRIPT

class JavaScriptExecution():
    def test(self):
       
        driver=webdriver.Chrome()
        get_url="https://courses.letskodeit.com/practice"
        driver.implicitly_wait(5)
        driver.get(get_url)
        driver.execute_script("window.location= 'https://courses.letskodeit.com/practice'; ")

        element= driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")
        height = driver.execute_script("return window.innerHeight;")#pour savoir la taille de la fenetre
        width = driver.execute_script("return window.innerWidth;")#pour savoir la taille de la fenetre
        print("Height: " + str(height))
        print("Width: " + str(width))
        time.sleep(5)



class Scroller():
    def test(self):
        driver=webdriver.Chrome()
        get_url="https://courses.letskodeit.com/practice"
        driver.implicitly_wait(5)
        driver.get(get_url)

        #scroll down 
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(3)

        #scroll up
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(3)

        #scroll jussqu'au un eement

        element= driver.find_element(By.ID,'mousehover')
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-150);")#on rmonte de 150px car element jjsute audessu sera cacher par la bar nav
        time.sleep(3)
        #Native Way To Scroll Element Into View
        driver.execute_script("window.scrollBy(0,-1000);")# on descend tout en abs
        location=element.location_once_scrolled_into_view  #on as deja un element on cree cette variable  avec into.. on  a mettre la position del apage  une fois que sa etait scroller
        print("location"+str(location))
        driver.execute_script("window.scrollBy(0,-150);")


#iFram  


class Window1(): # alors ici jidentifier la fenetre parent avce un variable , apres je trouve le bouton pour trouver la fentre, ensuite jai deux fenetre ouverte, je strpck les deux fenetre dasn une autre variabler je parcour par un list des deux fente pour identifier qui n'est pas le fentre parent, une fois identifier je vais chercehr le champs search pour effectuer une recherhc, enfin je termin en fermer la fenetre je quitte la boucle et je revien sur la fentree parrent , la premier fenetre que mon robot avaiqouvert
    def fenetre(self):
        driver=webdriver.Chrome()
        get_url="https://courses.letskodeit.com/practice"
        driver.implicitly_wait(5)
        driver.get(get_url)
        #
        #trouver la fenetre parent ( window main)
        PArent= driver.current_window_handle # sa va nour envoi lidentifier que selinium vien douvrire
        print('parrent hnadles')

        #trouver louverture d ela page avec le boutton et clicquer
        driver.find_element(By.ID,'openwindow').click()
        time.sleep(3)

        #trouver trouver ce qui fere, laba on doit soccuper apres le clikc pour ouvire la fenetre
        handles= driver.window_handles # ici on va avoir tout la liste des fenetre ouverte avec selenium

        #switch to winbdow and search course,  pour afficher ces fenetre on va fia reun boucle for

        for handle in handles:
            print("handle: " + handle)
            if handle not in PArent:
                driver.switch_to_window(handle) # ici on utilise la methode on lui apsse la fenetre et on lui met la fenetre en question
                print('switched to window : ' + handle)
                search = driver.find_element(By.XPATH,"//form[@id='search']//input[@id='search']")
                search.send_keys("python")
                time.sleep(3)
                driver.close() # juste fermer la fenetre 
                break
        #switch  back up th parent handle
        driver.switch_to_window(PArent)
        driver.find_element(By.ID,'name').send_keys('Test Succesful')

        


class Ifram():
    def test(self):
        driver=webdriver.Chrome()
        get_url="https://courses.letskodeit.com/practice"
        driver.implicitly_wait(5)
        driver.get(get_url)
        #scroll down 
        driver.execute_script("window.scrollBy(0,1000);")

        #SWitch to fram using Id
        #driver.switch_to.frame("courses-iframe")

        #switch to frame using name

        #switch to fram using numbers , ici si on tombe sur un ifram san id sans rien on utilise le snombre, par identifier par le snumero comme un index dans liste
        driver.switch_to_frame(0)
        time.sleep(3)
        
        #search course
        sB= driver.find_element(By.XPATH,"//input[@placeholder='Search Course']")
        sB.send_keys("python")
        time.sleep(3)

        #Switch back to rhe parent handle frame
        driver.switch_to.default_content() # on revien au parent, default contet n revien parent, ifram est formecement contenu dans un page mere
        driver.execute_script("window.scrollBy(0,-1000);") # ons croll pour bine montrer quon est a la fenetre parent
        time.sleep(3)
        driver.find_element(By.ID,'name').send_keys('toto')
        time.sleep(3)


class AlertePop():
    def test(self):
        driver=webdriver.Chrome()
        get_url="https://courses.letskodeit.com/practice"
        driver.implicitly_wait(5)
        driver.get(get_url)
        ko=driver.find_element(By.ID,"name").send_keys("miklar")
        driver.find_element(By.ID,"alertbtn").click() 
        time.sleep(3)
        #il va fallori apssrr sur le popup m    int, maintn on utilis eune methode pour  ue slenium sai identifer les pop up javascript, comme ca:
        alert1= driver.switch_to_alert()
        alert1.accept()
        time.sleep(3)
        driver.find_element(By.ID,"confirmbtn").click()
        time.sleep(2)
        alert2= driver.switch_to_alert
        alert2.dismiss()



class DrangAndDrop():
    def test(self):
        driver=webdriver.Chrome()
        get_url="https://jqueryui.com/droppable/"
        driver.implicitly_wait(5)
        driver.get(get_url)

        driver.switch_to_frame(0)# si on fia sun aspect avec chrompath, il  yas un iframe, on prend les xPATH des deux fenetre pour le drag and drop 

        fromElement= driver.find_element(By.ID,'draggable')
        toElement= driver.find_element(By.ID,'droppable')
        time.sleep(2)
        try:
            action=ActionChains(driver)
            #1re facon de faire:
            #action.drag_and_drop(fromElement, toElement).perform()# perform() is used to compile and execute the actions class. Use the different methods under the actions class to perform various operations like click(), drag and drop and so on.
            # des fosi sa ne marche pas 
            # facon 2: 
            action.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print('drag and drop elmeent succesful')
            time.sleep(3)
        except:
            print('drag and drop failed on element')


class Slider():
    def test(self):
        driver=webdriver.Chrome()
        get_url="https://jqueryui.com/slider/"
        driver.implicitly_wait(5)
        driver.get(get_url)

        driver.switch_to_frame(0)

        element= driver.find_element(By.XPATH,"//div[@id='slider']//span")
        time.sleep(3)
        try:
            action=ActionChains(driver)
            action.drag_and_drop_by_offset(element, 100, 0).perform()# ceci est de gauche a droit, si on aurais voulais faire de droit a gauche on auirais fait (XXXX, 0, 100), ne pa soublie .perform() sinn cela ne marche pas , il receuil lelement il fau tun perform pour lappliquer
            print("sliding element Succedful")
            time.sleep(3)
        except:
            print("Slinding failed on element")




















        






