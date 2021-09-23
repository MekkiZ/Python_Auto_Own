from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#trouver ID non dynamique , statique test, endant le code avec un ID dynamique on trouve une erreur car les id dynamique changer a chaque recharge de la page


class FindByElement():
    def test(self):
        
        driver = webdriver.Chrome()
        driver.get('https://courses.letskodeit.com/practice')
        #time.sleep(3)
        #avec send_key() = on envoi la value dans un champs par exemple, selenium rempli le premier champs qu'il trouver, c'est problemaituqe , il faut vraiment un seul element pour selenium
        element1 = driver.find_element_by_name("enter-name")
        element2 = driver.find_element_by_id("name")
        element3 = driver.find_element_by_xpath("//input[@id='displayed-text']")
        element4 = driver.find_element_by_css_selector("button#openwindow")
        element5= driver.find_element_by_partial_link_text("SUPP")
        element6= driver.find_element_by_link_text("SUPPORT")
        element7= driver.find_element_by_class_name('displayed-class') # contrairement a scarppy on peuc mettre QU'UN element de class donc on eneleve 'inputs' et on laisse dispalyed..
        element8= driver.find_elements_by_tag_name('h1')
        element9= driver.find_element(By.XPATH,"/html//button[@id='mousehover']")
        element10=driver.find_elements_by_class_name("inputs")
        taille_liste_element10= len(element10)
        element11= driver.find_elements(By.TAG_NAME,"button")
        taille_liste_element11= len(element11)
        #attention au recherche avec tag_name, class°_name, car il y as souvent plusieur nom avec ces class et tag(a par exemple)
        if element1 is not None:
            print('on as trouver un element by name')
        else:
            print('nous avons rien trouvé')
        
        if element2 is not None:
            print("on as trouver un element id ")
        else:
            print('on as pas trouver')
        
        if element3 is not None:
            print('il as un Xpath avec ce chemain')
        else: 
            print("il n'y a spas de chemain avec ce Xpath")
        
        if element4 is not None:
            print('il as un css avec ce chemain')
        else:
            print("il n'y as pas de chemain avec ce css")
        
        if element5 is not None:
            print('il as un parce_link-text avec ce chemain')
        else:
            print("il n'y as pas de chemain avec ce parc_link-text")
        
        if element6 is not None:
            print('il as un link-text avec ce chemain')
        else:
            print("il n'y as pas de chemain avec ce PArc-link-text")
        
        if element7 is not None:
            print('il as un class-name avec ce chemain')
        else:
            print("il n'y as pas de chemain avec ce Pclass-name")
        
        for text in element8: # cette fonction sert a extriper le texte de l'élément, en l'occurence ici le titre de h1, car il prend le scrp comme un 'list' on fais alors une boucle
            if element8 is not None:
                print("il y as un tag et le titre de ce tag et" + text.text)
            else:
                print("il n'y as pas de titre")
        
        if element9 is not None:
            print('il as un avec la methode BY.XPATH, sur ce chemain XPATH')
        else:
            print("il n'y as pas de la methode BY.XPATH, sur ce chemain XPATH")

        if element10 is not None:
            print('il as de nombre d element :'+ str(taille_liste_element10))
        else:
            print("il n'y as pas de la methode BY.X sur ce chemain XPATH")
        
        if element11 is not None:
            print('il as de nombre d element :'+ str(taille_liste_element11))
        else:
            print("il n'y as pas de la methode BY.X sur ce chemain XPATH")

        






ff= FindByElement()
ff.test()
