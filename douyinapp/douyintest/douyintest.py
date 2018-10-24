from appium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import  expected_conditions as EC
from time import sleep
class Action():
    def __init__(self):
    # 初始化配置，设置Desired Capabilities参数
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "Google_Nexus_6___5_1_0___API_22___1440x2560",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
            "noReset": "True",
            "unicodeKeyboard": "True",
            "resetKeyboard": "True"
        }
# 指定Appium Server
        self.server = 'http://localhost:4723/wd/hub'
# 新建一个Session
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        # self.wait = WebDriverWait(self.driver, 30)

    def comments(self):
        sleep(5)
        # app开启之后点击一次屏幕，确保页面的展示
        self.driver.tap([(500, 1200)], 500)
    def search(self):
        sleep(2)
        # 'com.ss.android.ugc.aweme:id/a9k'  --更新之后的id
        # search2=self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a8i')))
        search2=self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9k')
        search2.click()
        print("-----------------------------------去搜索界面----------------------------------------")
        sleep(3)
        # 'com.ss.android.ugc.aweme:id/a1x'
        # 'com.ss.android.ugc.aweme:id/a1a'  'com.ss.android.ugc.aweme:id/a1b' 'com.ss.android.ugc.aweme:id/pa'
        txt = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/a1x")
        # txt.clear()
        txt.send_keys("别克GL6")
        # txt.send_keys("666")
        print("-----------------------------------输入完成----------------------------------------")
        # 'com.ss.android.ugc.aweme:id/a1z'
        # 'com.ss.android.ugc.aweme:id/a1b'
        self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/a1z").click()
        sleep(3)
        print("-----------------------------------搜索完成----------------------------------------")
        # '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[2]'

        # self.driver.find_elements_by_id("com.ss.android.ugc.aweme:id/a5p").click()
        # print("-----------------------------------跳转到视频选项----------------------------------------")
        # 'com.ss.android.ugc.aweme:id/jn'  --videolist

    def fechAllResults(self):
        sleep(2)
        # el1 = driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout")
        # el1.click()
        # el1 = driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout[*]/android.widget.LinearLayout/*")
        # el1.click()
        Results = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/jn")

        titles = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout[*]/android.widget.LinearLayout/*")
        for title in titles:
            print(title.text)
            # print(title.id)
    def main(self):
        self.comments()
        self.search()
        # self.fechAllResults()


if __name__ == '__main__':
    action = Action()
    action.main()