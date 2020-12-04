from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import winsound



class bot():
	def __init__(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.wait = WebDriverWait(self.driver, 10)
		
	def checkBestBuy(self):
		self.driver.get('https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324')
		time.sleep(3)
		buyButton = (self.driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8]/div[1]/div/div/div/button"))
		text =buyButton.text
		print("-----Best Buy-----")						
		print(text)
		return text == "Sold Out"
		
	def close(self):
		self.driver.close()
		
	def checkTarget(self):
		self.driver.get('https://www.target.com/p/xbox-series-x-console/-/A-80790841#lnk=sametab')
		time.sleep(3)
		text = self.driver.find_element_by_xpath('//*[@id="viewport"]/div[5]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[1]').text
		print("-----Target------")
		print(text)
		return text == "Out of stock in stores near you"
		
	def checkGameStop(self):
		self.driver.get('https://www.gamestop.com/accessories/xbox-series-x/products/xbox-series-x/11108371.html?condition=New')
		time.sleep(3)
		text = self.driver.find_element_by_xpath('//*[@id="primary-details"]/div[4]/div[10]/div[2]/div[1]/label/div/div[5]/span[2]').text
		print( "------Game Stop-----")
		print(text)
		return text == "OUT OF STOCK"
		
b = bot()
BB =b.checkBestBuy()
T = b.checkTarget()
GS = b.checkGameStop()
if not BB or not T or not GS :
	winsound.Beep(1000,5000)
b.close()
