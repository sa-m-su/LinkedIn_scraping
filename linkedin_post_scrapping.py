from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests


browser = webdriver.Chrome("chromedriver.exe")
# Open web driver.chrome
browser.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
browser.maximize_window()
# Max the window
time.sleep(2)

username = browser.find_element_by_name("session_key")
username.send_keys("samsubca09@gmail.com")
# Enter username as mail id
password = browser.find_element_by_name("session_password")
password.send_keys("xxxxxx")
# Enter password

login_button = browser.find_element_by_class_name("login__form_action_container").click()
# Submit Login button

post_link = "https://www.linkedin.com/company/recruitnxt/posts/"
# In linkedin go to posts
browser.get(post_link)

start = time.time()

# Will be used in the while loop
initialScroll = 0
finalScroll = 1000

while True:
    browser.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    # The window starting from
    # The pixel value stored in the initialScroll
    # Variable to the pixel value stored at the finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000

    # Stop the script for 2 seconds
    # So that the data can load
    time.sleep(2)
    # You can change it as per your needs and internet speed

    end = time.time()

    # We will scroll for 20 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 20:
        break

src = browser.page_source

# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')
soup.prettify()

# Extracting the HTML of the complete introduction box
# that contains the company name, description and the location
intro = soup.find('div', {'class': 'block mt2'})

print(intro)

"""post1 = soup.find_all('div', {"class": 'ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex'}).select('img')
print(post1)"""

post2 = soup.find_all('img', {"class": 'ivm-view-attr__img--centered feed-shared-image__image feed-shared-image__image--constrained lazy-image ember-view'})

try:
  os.mkdir("Scraped photos")
except:
    print("Already exits")
i = 1

for posts in post2:
    print(posts['src'])
    if i <= 10:
        img_data = requests.get(posts['src']).content
        with open("Scraped photos/"+str(i)+'.jpg', 'wb+')as f:
            f.write(img_data)
        i += 1
    else:
        f.close()
