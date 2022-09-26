from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class FacebookBot:

    def __init__(self, usuario, clave):
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.push.enabled", False)
        self.usuario = usuario
        self.clave = clave
        self.bot = webdriver.Firefox(options=options)

    def login(self):
        bot = self.bot
        bot.get("https://es-la.facebook.com/")    
        time.sleep(2)

        mail = bot.find_element_by_name('email')
        contrasena = bot.find_element_by_name('pass')
        #bot.find_element_by_id("email-input")
        mail.clear()
        contrasena.clear()
        mail.send_keys(self.usuario)
        contrasena.send_keys(self.clave)
        contrasena.send_keys(Keys.RETURN)

    def buscar(self, q):
        bot = self.bot
        time.sleep(2)

        link = 'https://www.facebook.com/search/top/?q={}&epa=SEARCH_BOX'.format(q)
        bot.get(link)


bot = FacebookBot("mail@gmail.com", "contraseña")
bot.login()
bot.buscar("Eventos en Buenos Aires")

