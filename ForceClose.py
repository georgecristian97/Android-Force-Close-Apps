from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import threading
import datetime
desired_cap={
    "platformName":"Android",
    "platformVersion" : "10",
    "deviceName" : "R58M88LXMBZ",
}
driver1 = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

driver1.implicitly_wait(30)
def kill_app(xt,textf):
    TouchAction(driver1).long_press(el=xt,duration=250).release().perform()
    time.sleep(1)
    driver1.find_element_by_accessibility_id('App info, Button').click()
    if driver1.find_element_by_id('com.android.settings:id/button3').is_enabled():
        textf = textf + '\n' + driver1.find_element_by_id('com.android.settings:id/entity_header_title').text + ' -- closed'
        driver1.find_element_by_id('com.android.settings:id/button3').click()
        driver1.find_element_by_id('com.android.settings:id/button1').click()
        time.sleep(2)

    else:
        textf = textf + '\n' + driver1.find_element_by_id('com.android.settings:id/entity_header_title').text + ' -- already closed'
    driver1.press_keycode('4')
    time.sleep(3)
    return textf
#exception list
x = ['Appium Settings','Bixby','BlueMail','Clock','Contacts','Internet Speed Meter Lite','Messages','Messenger','Orange','Phone','Setari Digi','Settings','WhatsApp']
#1 app pages
r= 1 #increase
textf = ''
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
textf = "ForceClose.py\nCurrent date and time : " + now.strftime("%Y-%m-%d %H:%M:%S")
for h in range(r):
    time.sleep(2)
    rx = driver1.find_elements_by_class_name('android.widget.TextView')

    for j in rx:
        time.sleep(1)
        if str(j.text) not in x:
            time.sleep(1)
            textf = kill_app(j,textf)
        #
    print(rx[0].tag_name)
    time.sleep(1)
    if h < r-1:
        k=0
        while str(rx[0].tag_name) == str(driver1.find_elements_by_class_name('android.widget.TextView')[0].tag_name):
            driver1.press_keycode('22')
            time.sleep(1)
            if len(rx) < k : #when we are at last page
                break

namef = now.strftime("%Y-%m-%d_%H.%M.%S")+".txt"
f = open(namef, "a")
f.write(textf)
f.close()