import requests
from selenium import webdriver
from getpass import getpass
from bs4 import BeautifulSoup

# user_id = str(input('Enter the user id: '))
# Twitter_Site = "https://twitter.com/"+user_id+"/followers"
# source_code = requests.get(Twitter_Site)
# plain_text = source_code.text
# soup = BeautifulSoup(plain_text, "html.parser")
# print(soup.findAll('a'))

user = input('Enter your username: ')
password = getpass('Enter your Password: ')

driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

user_box = driver.find_element_by_class_name('session[username_or_email]')
user_box.send_keys(user)

pass_box = driver.find_element_by_class_name('session[password]')
pass_box.send_keys(password)

login_button = driver.find_element_by_css_selector('button.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-vlx1xi.r-zg41ew.r-1jayybb.r-17bavie.r-icoktb.r-15bsvpr.r-o7ynqc.r-6416eg.r-lrvibr')
login_button.submit()

def Twitter_Followers(max_followers):    
    user_id = str(input('Enter the user id: '))
    Follower = 0
    while Follower <= max_followers:
        Twitter_Site = "https://twitter.com/"+str(user_id)+"/followers"
        source_code = requests.get(Twitter_Site)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        print(soup.title.text)
        for url in soup.findAll('span',{'class': 'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0'}):
#             href = "https://twitter.com"+url.get('href')
            username = Follower.append(url.text.strip())
            Follower += 1
            title = url.string
            print(username)
            print(title)
        
  
Twitter_Followers(10)
