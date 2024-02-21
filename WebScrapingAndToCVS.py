from selenium import webdriver
#Para que clickee el verify you are human
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By #Para usar by y encontrar elementos dentro del html
from selenium.webdriver.support.ui import Select #Para importar el metodo select que nos ayudara a escoger un elente dentro de una lista
#from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

import time
url ="https://www.adamchoi.co.uk/teamgoals/detailed"

#Cambiar el modo es el predeterminado no hace efecto
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled') #No detecta que sea un bot
options.add_argument('--no-first-run') #Evita la ejecuion de ciertas tareas que se realizan la primera vez que se abre chrome
#options.add_argument('--no-sandbox') #Desabilita el modo sandbox que es el que separa los procesos del chrome del sistema. No hacer a menos que sea necesario
options.add_argument('--disable-notifications') #Bloquear las notificaciones de chrome
options.add_argument('--ignore-certificate-errors') #Ignora los errores de certificados
options.add_argument('--enable-logging')#No nos muestre nada en la terminal
driver = webdriver.Chrome(options=options)
driver.get(url)
#Para que clickee el verify you are human
#WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='Widget containing a Cloudflare security challenge']")))
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label.ctp-checkbox-label"))).click()

# Seleccionar el boton de partidos mediante el xpath
all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
dropdown = Select(driver.find_element(By.ID, 'country'))

#Click en el boton seleccionado
time.sleep(2)
all_matches_button.click()
time.sleep(2)
dropdown.select_by_visible_text('Ecuador')
time.sleep(2)
#Encontrar todos los elementos con el TAG tr
matches = driver.find_elements(By.TAG_NAME, 'tr')
partidos = [] #Crear una lista vacia
for match in matches: #Agregar todos los datos encontrados en el TAG tr en la lista
    partidos.append((match.text))#Se los agrega con el metodo append
driver.quit()#Cerrar el driver para no consumir memoria
df = pd.DataFrame({'partidos':partidos})#Crear una lista del tipo dataframe usando la lista anterior
print(df)#Imprimir la lista df
df.to_csv('partidos.csv', index=False)#convertir el dataframe a un archivo csv para que este almecene los datos. (Excel)


#chtml = driver.page_source
#with open('document.html', 'w', encoding='utf-8') as file:
 #  file.write(chtml)
