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
