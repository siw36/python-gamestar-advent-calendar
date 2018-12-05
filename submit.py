import mechanize                #sudo pip install python-mechanize
import datetime
import ConfigParser
import os

# Read the ini file
config = ConfigParser.ConfigParser()
config.sections()
config.read('config.ini')

# Current day
day = datetime.datetime.now().day
# Url with current day
url = "https://www.gamestar.de/kalender/xmas2018,3/tag" + str(day) + ".html"

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/63.0.3")]
br.open(url)
br.select_form(nr=0)
form = br.form
form["title"] = [config.get('FormData', 'title')]
form["firstname"] = config.get('FormData', 'firstname')
form["lastname"] = config.get('FormData', 'lastname')
form["street"] = config.get('FormData', 'street')
form["streetnumber"] = config.get('FormData', 'streetnumber')
form["adressext"] = config.get('FormData', 'adressext')
form["zipcode"] = config.get('FormData', 'zipcode')
form["city"] = config.get('FormData', 'city')
form["country"] = [config.get('FormData', 'country')]
form["email"] = config.get('FormData', 'email')
form["age"] = config.get('FormData', 'age')
br.find_control("usage").items[0].selected=True

response = br.submit()

print("done")
