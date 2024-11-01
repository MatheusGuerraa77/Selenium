from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 1- Utilização do WebDriver
browser = webdriver.Chrome()
browser.get('https://www.amazon.com.br')

# 2- Acessando elemento de pesquisa
elem = browser.find_element(By.ID, 'twotabsearchtextbox')
elem.send_keys('ps5')
elem.send_keys(Keys.ENTER)
time.sleep(2)

# 3- Encontrando os elementos de todos os resultados
element = browser.find_element(
    By.CSS_SELECTOR,
    'div.puis-card-container.s-card-container.s-overflow-hidden.aok-relative.puis-expand-height.puis-include-content-margin.puis.puis-v2lk1billfaou72dkme0sb0jkg6.s-latency-cf-section.puis-card-border'
)
time.sleep(2)
print(element)
time.sleep(2)