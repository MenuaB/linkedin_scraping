import parameters
from parsel import Selector
from time import sleep
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from fake_useragent import UserAgent

writer = csv.writer(open(parameters.file_name, 'w'))
writer.writerow(['Name','Location','Profile','URL'])

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.get('https://www.linkedin.com')

username = driver.find_element_by_id('session_key')
username.send_keys(parameters.linkedin_username)
sleep(0.5)

password = driver.find_element_by_id('session_password')
password.send_keys(parameters.linkedin_password)
sleep(0.5)

log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
log_in_button.click()
sleep(0.5)

driver.get('https:www.google.com')
sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)
sleep(0.5)

search_query.send_keys(Keys.RETURN)
sleep(7)

linkedin_urls = []

for i in range(20):
   # linkedin_urls = driver.find_elements_by_css_selector('div.g')
   # linkedin_urls = 

   for url in driver.find_elements_by_css_selector('div.g'):
      linkedin_urls.append(url.find_element_by_tag_name("a").get_attribute("href"))
   # del linkedin_urls[2:6]
   sleep(0.5)

   driver.find_element_by_link_text("Հաջորդը").click()

   # For loop to iterate over each URL in the list
for linkedin_url in linkedin_urls:

   # get the profile URL 
   driver.get(linkedin_url)

   # add a 5 second pause loading each URL
   sleep(2)

   # assigning the source code for the webpage to variable sel
   sel = Selector(text=driver.page_source) 
   
   name, location, profile = '', '', ''

   name = sel.xpath('//h1/text()').extract_first()
   location = sel.xpath('//div[2]/div[2]/div[2]/span[1]/text()').extract_first()
   profile = sel.xpath('///div[2]/div/div/div/span[1]/text()').extract_first()
   

   if name:
      name = name.strip()
   else:
      name = ''
   if profile:
      profile = profile.strip()
   else:
      profile = ''
   if location:
      location = location.strip()
   else:
      location = ''
   # print('\n')
   # print('Name: ' + name)
   # print('Profile: ' + profile)
   # print('link: ' + linkedin_url)
   # print('********************')

   writer.writerow([name,
                    location,
                    profile,
                    linkedin_url])
# terminates the application
driver.quit()
