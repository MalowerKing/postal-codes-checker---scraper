#A little amount of imports ;0
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import re
import pandas as pd

#Webdriver configuration
WEBDRIVER_LOCATION = "C:\\Users\macie\\OneDrive\\Dokumenty\\project\\chromedriver_win32\\chromedriver.exe"
options = Options()
options.add_argument('--headless=new')
service = ChromeService(executable_path=WEBDRIVER_LOCATION)
driver = webdriver.Chrome(service=service, options=options)

#Data scraping function
def dataScraping (page):
    #Get page to scapre
    driver.get('https://docelu.pl/kody-pocztowe/{page}'.format(page=page))
    postalCodes = []
    try:
        #Wait till content is rendered.
        elem = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'codes-table'))
        )
        #Find And return Content
        postalCodesRows = driver.find_elements(By.CLASS_NAME, 'row') #Scrape Row
        for row in postalCodesRows: #Itarate over cells in a row
            #Add to the table
            postalCodes.append(row.find_elements(By.CSS_SELECTOR, 'html body div#container div#main.f div.content div.codes-table div.row div.cell')) 
        return postalCodes
    except:
        #Exception if no content is found
        print('Something Went Wrong in: {page}'.format(page=page))
        return 0

#DataFrame creation and import of CSV file
results = pd.DataFrame(columns = ['Kod', 'Miejscowość', 'Gmina', 'Powiat', 'Województwo'])
codes = pd.read_csv(r'kody.csv', sep=';')

#Cookie bypass
driver.get('https://docelu.pl/kody-pocztowe')
try:
    cookie_accept = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[9]/div[1]/div[2]/div/div[2]/button[2]'))
    )
    cookie_accept.click()
except:
    print("No cookie ????")

#Itaring over a little amount of codes to scrape pages.
postalCodesCleaning = codes[~codes.POWIAT.str.contains(' na prawach powiatu')]['KOD POCZTOWY'] #Clean dupilcate postal codes
for code in postalCodesCleaning.drop_duplicates():
    print(code)
    scraped = dataScraping(code) #Scraping data
    if scraped != 0:
        for element in scraped: #itarating over elements in scraped table
            if len(element) != 0: #Checking if table is empty
                #Check if first record is postal code
                if bool(re.search('([0123456789][0123456789])-([0123456789][0123456789][0123456789])', str(element[0].text))) == True:        
                    results.loc[len(results.index)] = [element[0].text,element[1].text,element[-3].text,element[-2].text,element[-1].text] #Saving to dataframe   
    results = results.drop_duplicates(subset=['Kod', 'Miejscowość', 'Gmina', 'Powiat', 'Województwo']) #Cleaning duplicates in rows
    print(results) #Funzies
#Profit
results.to_csv('male.csv')
driver.quit()