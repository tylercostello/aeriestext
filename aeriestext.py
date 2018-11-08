from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime


a = open('period1.txt','r')
b = open('period2.txt','r')
c = open('period3.txt','r')
d = open('period4.txt','r')
per1=a.read()
per2=b.read()
per3=c.read()
per4=d.read()

now = datetime.datetime.now()
prevminute=-1
hour=now.hour
def sendtext(msg):
        driver = webdriver.Firefox()
        driver.get("https://accounts.google.com/ServiceLogin/identifier?service=grandcentral&passive=1209600&continue=https%3A%2F%2Fvoice.google.com%2Fsignup&followup=https%3A%2F%2Fvoice.google.com%2Fsignup&flowName=GlifWebSignIn&flowEntry=AddSession")
        text_area = driver.find_element_by_id('identifierId')
        text_area.send_keys("YOURGMAIL")

        text_area.send_keys(Keys.ENTER)
        time.sleep(5)
        text_area = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        #text_area = driver.find_element_by_name('Passwd')
        text_area.send_keys("YOURGMAILPASSWORD")

        text_area.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.get("https://voice.google.com/u/0/messages?itemId=t.%2B1"+"YOURNUMBER")

        time.sleep(10)
        try:
                        text_area = driver.find_element_by_id('input_3')
        except:
                        time.sleep(10)
                        text_area = driver.find_element_by_id('input_3')
        time.sleep(5)
        text_area.send_keys(msg)
        text_area.send_keys(Keys.ENTER)
        time.sleep(30)
        driver.close()
        print("Text sent")
while hour>=6 and hour<=23 and datetime.datetime.today().weekday()<5:
        now = datetime.datetime.now()
        currentminute=now.minute
        #if 1:
        if currentminute==15 or currentminute==45:
                        if currentminute!=prevminute:
                                prevminute=currentminute
                                #driver = webdriver.Firefox(Firefox_options=Firefox_options)
                                driver=webdriver.Firefox()  
                                driver.get('https://parent.sduhsd.net/ParentPortal/GradebookSummary.aspx')
                                text_area = driver.find_element_by_id('portalAccountUsername')
                                text_area.send_keys("YOURAERIESUSERNAME")
                                text_area.send_keys(Keys.ENTER)
                                time.sleep(1)
                                text_area = driver.find_element_by_id('portalAccountPassword')
                                text_area.send_keys("YOURAERIESPASSWORD")
                                text_area.send_keys(Keys.ENTER)
                                time.sleep(10)
                                print(now)
                                #print(per2)
                                #print(per4)
                                #print(driver.find_element_by_xpath('//*[@id="ctl00_MainContent_subGBS_DataDetails_ctl01_trGBKItem"]/td[7]/span').text)
                                newper1=driver.find_element_by_xpath('//*[@id="ctl00_MainContent_subGBS_DataDetails_ctl01_trGBKItem"]/td[7]/span').text
                                print(newper1)
                                newper2=driver.find_element_by_xpath('//*[@id="ctl00_MainContent_subGBS_DataDetails_ctl02_trGBKItem"]/td[7]/span').text
                                print(newper2)
                                newper3=driver.find_element_by_xpath('//*[@id="ctl00_MainContent_subGBS_DataDetails_ctl03_trGBKItem"]/td[7]/span').text
                                print(newper3)
                                #print(driver.find_element_by_xpath('//*[@id="ctl00_MainContent_subGBS_DataDetails_ctl02_trGBKItem"]/td[7]/span').text)
                                newper4=driver.find_element_by_xpath('//*[@id="ctl00_MainContent_subGBS_DataDetails_ctl04_trGBKItem"]/td[7]/span').text
                                print(newper4)
                                newper1=str(newper1)
                                newper2=str(newper2)
                                newper3=str(newper3)
                                newper4=str(newper4)
                                time.sleep(5)
                                driver.close()
                                if newper1!=per1:
                                        mymessage=" Period 1 "+str(newper1)
                                        sendtext(mymessage)
                                        a = open('period1.txt','w')
                                        a.write(newper1)
                                        a.close()
                                        per1=newper1
                                if newper2!=per2:
                                        mymessage=" Period 2 "+str(newper2)
                                        sendtext(mymessage)
                                        b = open('period2.txt','w')
                                        b.write(newper2)
                                        b.close()
                                        per2=newper2
                                if newper3!=per3:
                                        mymessage=" Period 3 "+str(newper3)
                                        sendtext(mymessage)
                                        c = open('period3.txt','w')
                                        c.write(newper3)
                                        c.close()
                                        per3=newper3
                                if newper4!=per4:
                                        mymessage="Period 4 "+str(newper4)
                                        sendtext(mymessage)
                                        d = open('period4.txt','w')
                                        d.write(newper4)
                                        d.close()
                                        per4=newper4
        time.sleep(10)

