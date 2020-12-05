from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import winsound

SLEEP = 6


class bot():
	def close(self):
		self.driver.close()
		
	def __init__(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.wait = WebDriverWait(self.driver, 10)
		
	def checkBestBuyXbox(self):
		self.driver.get('https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324')
		time.sleep(SLEEP)
		buyButton = (self.driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8]/div[1]/div/div/div/button"))
		text =buyButton.text
		print("-----Best Buy Xbox-----")
		print(text)
		return text != "Sold Out"
		
	def checkBestBuyPS5(self):
		self.driver.get('https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149')
		time.sleep(SLEEP)
		buyButton = (self.driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8]/div[1]/div/div/div/button"))
		text =buyButton.text
		print("-----Best Buy PS5-----")
		print(text)
		return text != "Sold Out"
				
	def checkTargetXbox(self):
		self.driver.get('https://www.target.com/p/xbox-series-x-console/-/A-80790841#lnk=sametab')
		time.sleep(SLEEP)
		text = self.driver.find_element_by_xpath('//*[@id="viewport"]/div[5]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[1]').text
		print("-----Target Xbox------")
		print(text)
		return text != "Out of stock in stores near you"
		
	def checkTargetPS5(self):
		self.driver.get('https://www.target.com/p/playstation-5-console/-/A-81114595#lnk=sametab')
		time.sleep(SLEEP)
		text = self.driver.find_element_by_xpath('//*[@id="viewport"]/div[5]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[1]').text
		print("-----Target PS5------")
		print(text)
		return text != "Out of stock in stores near you"
		
	def checkGameStopXbox(self):
		self.driver.get('https://www.gamestop.com/accessories/xbox-series-x/products/xbox-series-x/11108371.html?condition=New')
		time.sleep(SLEEP)
		text = self.driver.find_element_by_xpath('//*[@id="primary-details"]/div[4]/div[10]/div[2]/div[1]/label/div/div[5]/span[2]').text
		print( "------Game Stop Xbox-----")
		print(text)
		return text != "OUT OF STOCK"
		
	def checkGameStopPS5(self):
		self.driver.get('https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5-digital-edition/11108141.html?condition=New')
		time.sleep(SLEEP)
		text = self.driver.find_element_by_xpath('//*[@id="primary-details"]/div[4]/div[9]/div[2]/div[1]/label/div').text
		print( "------Game Stop PS5-----")
		print(text)
		return text != "Ship To Home\nOUT OF STOCK"
		
	def checkWallMartXbox(self):
		self.driver.get('https://www.walmart.com/ip/XB1-Xbox-Series-X/443574645')
		time.sleep(SLEEP)
		text = self.driver.find_element_by_xpath('//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span/span').text
		print( "------WallMart Xbox-----")
		print(text)
		return text != "Get in-stock alert"
		
	def checkWallMartPS5(self):
		self.driver.get('https://www.walmart.com/ip/PlayStation-5-Console/363472942')
		time.sleep(SLEEP)
		text = self.driver.find_element_by_xpath('//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span/span').text
		print( "------WallMart PS5-----")
		print(text)
		return text != "Get in-stock alert"
		
b = bot()
BBX = False 
TX = False
GSX = False
BBP = False 
TP = False
GSP = False
WMX = False
WMP = False
while not (BBX or TX or GSX or BBP or TP or GSP or WMX or WMP):
	# BBX = b.checkBestBuyXbox()
	# TX  = b.checkTargetXbox()
	# GSX = b.checkGameStopXbox()
	# BBP = b.checkBestBuyPS5()
	# TP  = b.checkTargetPS5()
	# GSP = b.checkGameStopPS5()
	WMX = b.checkWallMartXbox()
	WMP = b.checkWallMartPS5()
	

winsound.Beep(500,3500)
b.close()
