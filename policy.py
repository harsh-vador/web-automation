from selenium import webdriver
# from selenium.selenium import selenium
from selenium import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver.exe")

driver.get('https://orientalinsurance.org.in/web/guest/renew?isSelected=renew&isRefresh=true')
searchbox = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[1]/div/div/div/div/div/div/div/div/span/span/form/span[5]/span[2]/span[1]/input')
# searchbox = driver.find_element_by_xpath(
#     '/html/body/div[2]/div/div[1]/div/div/div/div/div/div/div/div/span/span/form/span/span[3]/span[1]/input')
searchbox.send_keys('131401/48/2020/8481')
searchbutton = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[1]/div/div/div/div/div/div/div/div/span/span/form/span[5]/span[2]/span[2]/span/input')
searchbutton.click()

renewButton = driver.find_element_by_xpath(
    '//*[@id="_RenewPolicy_WAR_OICLportlet_:accordpanel:policyDet:btnCalculatePremium"]')
renewButton.click()

closeButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div/div/div/div/div/div[2]/div[1]/a[1]/span')
closeButton.click();

calcPremium = driver.find_element_by_xpath('//*[@id="_RenewPolicy_WAR_OICLportlet_:accordpanel:policyDet:btnCalculatePremium"]');
calcPremium.click()

closeButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div/div/div/div/div/div[2]/div[1]/a[1]/span')
closeButton.click();

calculatePremium = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div/div/div/div/div/span/span/span[2]/span/div/div[1]/form/span/span/input')
calculatePremium.click();
