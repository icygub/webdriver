#! python3

import webbrowser, pyperclip
from selenium import webdriver

"""
Currently working on transpostal
"""
driver = webdriver.Chrome()

driver.get('http://www.transpostal.com.br/v3/')
usuario_elem = driver.find_element_by_name('usr')
usuario_elem.send_keys('username here')
senha_elem = driver.find_element_by_name('pwd')
senha_elem.send_keys('password here')
senha_elem.submit()

por_dest_elem = driver.find_element_by_name('imgDest')
por_dest_elem.click()

destinario_elem = driver.find_element_by_name('txtNomeDest')
destinario_elem.send_keys(pyperclip.paste())
destinario_elem.submit()

objeto_href = driver.find_element_by_tag_name('a')
objeto_href.click()
"""
try:
    objeto_href_two = driver.find_element_by_tag_name('a')
    print('Still on the first page')
except:
    print('Out of the first page')
"""

last_button_elem = driver.find_element_by_css_selector('btCorreio')
last_button_elem.click()

#res = requests.get('http://www.example.com')
#print(res.text[0:])
#webbrowser.open('http://www.transpostal.com.br/v3/')
