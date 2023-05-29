# import webdriver
import selenium
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




#starts chrome web driver and opens the initial login page
driver = webdriver.Chrome()  
driver.get("https://login.urbe.edu/login")  
time.sleep(3) #waits 3 secs for the website to load properly

#find ID for username and password textBoxes
login = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password") 

#Credentials input
loginUser = str(input("Ingrese su usuario: "))
loginPassword = str(input("Ingrese su contraseña: "))

#Login   
login.send_keys(loginUser)
password.send_keys(loginPassword)
password.send_keys(Keys.RETURN) 

#opens Pregrado page
driver.get("https://login.urbe.edu/classroom?server=0")

#Clicks on programacion III course
time.sleep(3)
prog3 = driver.find_element(By.XPATH, '//*[@id="frontpage-category-combo"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/a')
prog3.click()

#Clicks on chat button
time.sleep(3)
chat = driver.find_element(By.XPATH, '//*[@id="module-20199"]/div/div[1]/div/div[1]/div/div[2]/div[2]/a')
chat.click()

#Joins the chat
time.sleep(3)
entrar = driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div[1]/div[2]/div/section/div[2]/div[1]/div/div[1]/a')
entrar.click()

#Reopens the chat in a new tab
time.sleep(3)
driver.get("https://pregrado.ead.urbe.edu/mod/chat/gui_ajax/index.php?id=633")
textBox = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/table/tbody/tr/td/div/div[1]/span[1]/input')
 
# "." message iteration each 90 seconds
while True:
    
    textBox.click()
    textBox.send_keys(".")
    textBox.send_keys(Keys.RETURN) 
    time.sleep(90)





