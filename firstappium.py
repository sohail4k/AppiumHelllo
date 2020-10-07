import os
from time import sleep

import unittest

from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
    )

class TestHello(unittest.TestCase):

    def setUp(self):
        
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '../../Downloads/sample-code-master/sample-code/apps/eribank.apk' 
           )
        
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    def tearDown(self):
         self.driver.quit()
         


    def test_logon_valid(self):
        self.driver.find_element_by_id('usernameTextField').send_keys('company')
        
        self.driver.find_element_by_id('passwordTextField').send_keys('company')
        self.driver.find_element_by_id('loginButton').click()
        self.driver.implicitly_wait(15)
        webview = self.driver.contexts[-1]
        #self.driver.switch_to.context(webview)
        e1=self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]')
        self.assertEqual("Your balance is: 100.00$",e1.text)
        print('passed')
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()