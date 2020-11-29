from selenium import webdriver
from selenium.webdriver.common.keys import Keys# send some import to browser.
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule

class InstagramBot:
	def __init__(self,username,password):#constructor function
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox(executable_path = r"C:\Users\MR.SAUGAT\Desktop\Side projects\Insta Bot\geckodriver.exe")	# locate gecko driver

	def login(self):
		bot = self.bot
		bot.get('https://www.instagram.com/accounts/login/') ## go to insta site and wait 3 sec to load
		time.sleep(2)

		#accept button
		bot.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
		WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.aOOlW:nth-child(1)"))).click()
		time.sleep(2)

		#fill username and password
		email = bot.find_element_by_name('username').send_keys(self.username) # put username and pass and click Enter "return" and wait 3 sec
		password = bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
		time.sleep(6)

		#not now button
		bot.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
		WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sqdOP:nth-child(1)"))).click()
		time.sleep(2)
		
	def searchHashtag(self,hashtag):
		bot = self.bot

		bot.get('https://www.instagram.com/explore/tags/' + hashtag)
 

		# like amount doesnt work, only likes 1 
		#todo: fix likes, run it as batch with .bat file
		#post yourself?
		#if the post is liked then dont unlike it with if and else statement
		#try python deubugging mate?
		
	def likePhotos(self,amount):
		bot = self.bot
		bot.find_element_by_class_name('v1Nh3').click()

		i = 1
		while i <= amount:
			#if in a post fr66n is true then click the arrow 
			time.sleep(5)
			
			bot.find_element_by_class_name('fr66n').click()
			# bot = self.bot
			# if find_element_by_class_name('fr66n').click()==true{
			# 	bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
			# }
			time.sleep(5)
			bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
			time.sleep(5)
			i+=1
		
			#bot.get('https://instagram.com/'+ self.username)

insta = InstagramBot('stronggympeoples', 'Arnold6969')
insta.login()
insta.searchHashtag('gym')
insta.likePhotos(200)