from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('C:\chromedriver.exe')

driver.get('http://www.dbdbdeep.com/login/login_member.php')



sleep(0.5)
driver.find_element_by_name('id').send_keys('아이디')
sleep(0.5)
driver.find_element_by_name('pwd').send_keys('비밀번호')


driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/div[1]/a/div').click()

sleep(0.5)
driver.get('http://www.dbdbdeep.com/ma2/event/attend_event.php')