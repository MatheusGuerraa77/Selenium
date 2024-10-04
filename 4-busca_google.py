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
print(f'Foram encontrados {results}')

# 6 - Retornando número de páginas
# Corrigindo a extração do número de resultados
try:
    qtd_results = int(results.split('Aproximadamente ')[1].split(' resultados')[0].replace('.', '').replace(',', ''))
    tot_pages = qtd_results / 10  # Você pode ajustar o valor dependendo da configuração
    print(f'Número de páginas: {int(tot_pages)}')
except Exception as e:
    print("Não foi possível calcular o número de páginas.", e)

browser.quit()
