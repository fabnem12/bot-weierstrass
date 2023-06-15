from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def availability(username, mdp, usageManuel = False):
    driver = webdriver.Chrome()
    driver.maximize_window()

    #on cherche la page de login
    driver.get("https://www.fmel.ch/fr/")
    
    #on ferme le pop-up
    #time.sleep(5)
    #test = [x for x in driver.find_elements(By.TAG_NAME, "button") if x.get_attribute("class") == "v-btn v-btn--is-elevated v-btn--fab v-btn--has-bg v-btn--round theme--light v-size--x-small"]
    #test[1].click()

    liensUp = driver.find_elements(By.CLASS_NAME, 'link')
    login = liensUp[2]
    login.click()

    #on est sur la page de login
    #on cherche le formulaire de connexion
    lienLoginForm = driver.find_elements(By.TAG_NAME, "a")[6]
    lienLoginForm.click()

    #on cherche les champs du formulaire pour les remplir
    inputForms = driver.find_elements(By.TAG_NAME, "input")
    usernameBtn, passwordBtn = inputForms[:2]
    usernameBtn.send_keys(username)
    passwordBtn.send_keys(mdp)

    time.sleep(5)

    trouveLoginButton = driver.find_elements(By.TAG_NAME, "button")
    loginButton = [x for x in trouveLoginButton if x.get_attribute("aria-label") == "Login"]
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    loginButton[0].click()

    time.sleep(5)

    liens = driver.find_elements(By.TAG_NAME, "a")
    lienReserver = liens[8]
    lienReserver.click()

    time.sleep(5)

    trouveBouton = driver.find_elements(By.TAG_NAME, "button")
    bouton = [x for x in trouveBouton if x.get_attribute("aria-label") == "Réserver"]
    bouton[0].click()

    time.sleep(5)

    trouveBouton = driver.find_elements(By.TAG_NAME, "button")
    bouton = [x for x in trouveBouton if x.get_attribute("aria-label") == "Tout voir"]
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    bouton[0].click()

    time.sleep(5)

    ret = not any("Pas de disponibilité actuellement" in x.text for x in driver.find_elements(By.TAG_NAME, "strong"))

    if not usageManuel:
        driver.close()
        return ret

if __name__ == "__main__":
    from constantes import userFMEL, mdpFMEL
    availability(userFMEL, mdpFMEL, True)