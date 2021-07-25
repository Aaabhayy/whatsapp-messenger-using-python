from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys


def sendmsg():
	msg = input("enter message\n")
	count = int(input("enter count\n"))
	path = '//div[@data-tab = "6"]'
	box = driver.find_element_by_xpath(path)
	# box.send_keys(msg)
	# pathToSend = '//button[@data-icon = "send"]'
	for i in range(count):
		# sendButton = driver.find_element_by_xpath("//span[@data-icon='send']")
		box.send_keys(msg + Keys.ENTER)
		# box.clear()
		# time.sleep(0.5)

looper =1

	
while(True):
	browserChoice=int(input("Select Browser: \n1.Firefox \n2.Chrome\n3.Edge \n4.Safari\n"))
	if browserChoice == 1:
		try:
			driver = webdriver.Firefox()	
			# looper =0
			break
		except Exception as ex:
			print("browser unavailable, \nPlease check the browser and driver compatibiltiy.")

	else: 
		if browserChoice == 2:
			try:
				driver = webdriver.Chrome()
				break
			except Exception as ex:
				print("browser unavailable, \nPlease check the browser and driver compatibiltiy.")			
		else:
			if browserChoice == 3:
				try:	
					driver = webdriver.Edge()
					break
				except Exception as ex:
					print("browser unavailable, \nPlease check the browser and driver compatibiltiy.")			

			else:
				if browserChoice == 4:
					try:
						driver =  webdriver.Safari()
						break
					except Exception as ex:
						print("browser unavailable, \nPlease check the browser and driver compatibiltiy.")			


k=driver.get("https://web.whatsapp.com")

# /html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]
# /html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]
i=1
while (i == 1):
	i=2
	name = input("Enter Name\n")

	xpathToSearch = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"

	search = driver.find_element_by_xpath(xpath=xpathToSearch)
	search.clear()
	search.send_keys(name + Keys.ENTER)




	j= int(input("press 1 to send msg"))
	
	if(j==1):
		sendmsg()
	else:
		print("asshole!")
		sendmsg()

	i = int(input("enter 1 to repeat"))
driver.close()

