
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

def AcharElemento(driver, pPath):
    '''
    Recupera elemento baseado em endereço XPath relativo ou absoluto
    Inclui rotina de Wait ou espera, caso o elemento ainda não tenha sido carregado pelo browser.
    Retorna erro "ElementoNaoEncontrado" para caso o elemento não esteja disponível no momento.
    
    Parametros:
    -----------
    pPath : string
        Caminho relativo ou absoluto para o elemento na página desejado.

    Retorno:
        Objeto
            Caso o elemento seja encontrado retorna o mesmo
        String
            Caso não seja encontrado retorna o string 'ElementoNaoEncontrado'

    Forma de usar:
    --------------
    var = AcharElemento([Caminho do Elemento])
    Em seguida cabe um var.click() ou var.text de acordo com o tipo de objeto ou elemento recuperado.

    Obs.: O ChromeDriver deve estar carregado antecipadamente

    '''
    sElem = ''
    nDelay = 5
    try:
        wait = WebDriverWait(
            driver, 
            nDelay, 
            poll_frequency=1, 
            ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException]
        )
        wait.until(
            EC.presence_of_element_located((By.XPATH, pPath))
        )
        sElem = driver.find_element_by_xpath(pPath)
    except NoSuchElementException:
        return 'ElementoNaoEncontrado'
    return sElem

