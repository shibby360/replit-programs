from bs4 import BeautifulSoup
from selenium import webdriver # manipulate page
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait as wait
 
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
driver = webdriver.Chrome(options=option)

driver.get('https://weather.com/weather/today/l/49a1ea9b381d94596eac5bad60bfcc5dc8ba92dfe552968853c4dbbf18777719?unit=m')
driver.implicitly_wait(2)
soup = BeautifulSoup(driver.page_source, 'html.parser')
temp = driver.find_element_by_css_selector('.CurrentConditions--tempValue--3a50n')
print('Its ' + temp.text + 'C in Pleasanton')
driver.get('https://weather.com/weather/today/l/49a1ea9b381d94596eac5bad60bfcc5dc8ba92dfe552968853c4dbbf18777719?unit=e')
driver.implicitly_wait(2)
soup = BeautifulSoup(driver.page_source, 'html.parser')
temp = driver.find_element_by_css_selector('.CurrentConditions--tempValue--3a50n')
print('Its ' + temp.text + 'F in Pleasanton')