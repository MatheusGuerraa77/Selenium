from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# 1 - Termo de pesquisa
term = input('Digite o que deseja pesquisar:\n')

# 2 - Iniciando o Driver
browser = webdriver.Chrome()
browser.get('https://www.google.com.br/')

# 3 - Encontrando o elemento
elem = browser.find_element(
    By.XPATH,
    "//textarea[@aria-label]"
    )

# 4 - Enviando termo para pesquisa
elem.send_keys(term)
elem.send_keys(Keys.ENTER)

# 5 - Retornando a quantidade de registros
time.sleep(2)
results = browser.find_element(By.ID, 'result-stats').text
print(f'foram encontrados {results}')

browser.quit()