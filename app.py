import ezgmail
# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime
import time
from bs4 import BeautifulSoup


now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')
# Establish chrome driver and go to report site URL
# The url list should be a list of URLs that came from the second email they will have an 
# 'id" parameter that will be a randomly generated string of letters and numbers
urls = []

for index, url in enumerate(urls):
    driver = webdriver.Chrome()
    driver.get(url)

    if index == 0:
        # format: 1 - 12 (ex: 9)
        b_month = ''
        # format: 1 - 31 (ex: 6)
        b_day = ''
        # format: YYYY (ex: 1980)
        b_year = ''
        # this can be any valid email address
        email_to = ''
        # format: 123 N Rainbow Ave, Edmond, Oklahoma 73003, United States
        my_address = ''
        # acceptible values: 5, 10, 25, 50, 100, 400
        acceptible_distance = '25'

    # If you have more than one in your list of addresses from the second email, you can add their 
    # information into the following format
    # elif index == 1:
        # # format: 1 - 12 (ex: 9)
        # b_month = ''
        # # format: 1 - 31 (ex: 6)
        # b_day = ''
        # # format: YYYY (ex: 1980)
        # b_year = ''
        # # this can be any valid email address
        # email_to = ''
        # # format: 123 N Rainbow Ave, Edmond, Oklahoma 73003, United States
        # my_address = ''
        # # acceptible values: 5, 10, 25, 50, 100, 400
        # acceptible_distance = '25'

    # Update the month
    month = driver.find_element_by_id('vras_followupmonth')
    month.send_keys(b_month)

    # Update the day
    day = driver.find_element_by_id('vras_followupday')
    day.send_keys(b_day)

    # Update the Year
    year = driver.find_element_by_id('vras_followupyear')
    year.send_keys(b_year)

    driver.find_element_by_id('NextButton').click()

    time.sleep(10)

    # Update the map location
    address = driver.find_element_by_id('entity-list-map-location')
    address.send_keys(my_address)

    # Update the acceptible distance
    distance = driver.find_element_by_id('entity-list-map-distance')
    distance.send_keys(acceptible_distance)

    # "click" search
    driver.find_element_by_id('entity-list-map-search').click()
    time.sleep(10)

    # Get the location table
    the_list = driver.find_element_by_xpath('//*[@id="entity-list-map-locations"]/table')
    
    # 
    source = str(the_list.get_attribute('innerHTML'))
    soup = BeautifulSoup(source, 'lxml')

    locations = soup.find_all('tr')

    email_body = "<h2>Now only showing locations with the booking link.</h2><table>"
    appt_sites = ""

    for location in locations:
        if "Book Appointment" in location.get_text():
            appt_sites += str(location)

    if appt_sites == "":
        appt_sites = "<tr><td><h3>Sorry, no appointment sites currently available.</h3></td></tr>"

    email_body += appt_sites + "</table>"

    ezgmail.send(email_to, f'Vaccine Locations ({now})', f'{email_body}<a href="{url}"><h2>Go to Vaccine Page</h2></a>', mimeSubtype='html')

    driver.close()

driver.quit()