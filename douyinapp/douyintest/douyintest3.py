from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from uiautomator import device as d
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
        self.start_x = 720
        self.start_y = 1532
        self.distance = 383   #1130
# 新建一个Session
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        self.wait = WebDriverWait(self.driver, 30)

    def comments(self):
        sleep(5)
        # app开启之后点击一次屏幕，确保页面的展示
        self.driver.tap([(500, 1200)], 500)

    def search(self):
        sleep(2)
        search2=self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a9k')))
        # search2 = self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9k')
        search2.click()
        print("-----------------------------------去搜索界面----------------------------------------")
        txt = self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a1x')))
        # # txt.clear()
        # txt.send_keys("别克GL6")
        txt.send_keys("存货回补")  #  发票缴税 存货回补 报关 车关税 购置税 发票税（无结果）
        # txt.send_keys(u"qiche")
        print("-----------------------------------输入完成----------------------------------------")
        self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a1z'))).click()
        print("-----------------------------------搜索完成----------------------------------------")
        # 'android.widget.TextView' 'com.ss.android.ugc.aweme'  checked  checkable
        # d(text=u'视频', className='android.widget.TextView').click()
        # self.wait.until(self.driver.tap([(35, 98), (154, 217)], 500))
        # self.wait.until(EC.presence_of_elements_located((By.CLASS_NAME, 'android.widget.TextView')))
        sleep(5)
        # self.driver.tap([(288, 242), (576, 382)], 500)
        # a = self.driver.find_element_by_xpath(
        #     '//android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[2]')
        a = self.driver.find_element_by_xpath(
            '//*[@text="视频"]')
        a.click()
        # print(a)

        # self.locator = ("className", "android.widget.TextView")
        # self.text = u'视频'
        # self.wait.until(EC.text_to_be_present_in_element(self.locator, self.text)).click()

        print("-----------------------------------跳转到视频选项----------------------------------------")
        # 'com.ss.android.ugc.aweme:id/jn'  --videolist

    def enterVideo(self):
        sleep(2)
        self.driver.tap([(288, 242), (576, 382)], 500)

    def scroll(self):
        # self.driver.swipe(self.start_x, self.start_y, self.start_x, self.start_y - self.distance)
        self.driver.swipe(self.start_x, self.start_y, self.start_x, 380, 800)
        # self.driver.perform(TouchAction().press(718, 1532).moveTo(718, 383).release())

        # self.driver.getPageSource()

    def catchComments(self):
        sleep(2)
        self.driver.tap([(288, 242), (576, 382)], 500)

    def fechAllResults(self):
        # '#在抖音，记录美好生活#别克GL6对开雨刷，刮的面积很大，副驾驶前面也有好视线。
        # http://v.douyin.com/d6rdRC/ 复制此链接，打开【抖音短视频】，直接观看视频！'
        sleep(2)

        # 'com.ss.android.ugc.aweme:id/a23' 'com.ss.android.ugc.aweme:id/asp' 'com.ss.android.ugc.aweme:id/w5' 'com.ss.android.ugc.aweme:id/a3i'
        # titles  authimages  authors  dianzans
        # titles = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout[*]/android.widget.LinearLayout/*")
        alllist = self.driver.find_elements_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[*]/*')
        for list in alllist:
            sleep(2)
            titles = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/a23')))
            # titles = self.driver.find_elements_by_id('com.ss.android.ugc.aweme:id/a23')
            authors = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/w5')))
            dianzans = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/a3i')))
            # self.driver.find_element_by_xpath(
            #         '//*[@text="没有更多了"]')

            for title in titles:
                sleep(2)
                print(title.text + '这是视频标题')
            for author in authors:
                sleep(2)
                print(author.text + '这是视频作者')
            for dianzan in dianzans:
                sleep(2)
                print(dianzan.text + '这是视频点赞数')

            self.scroll()




        '''
        titles = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/a23')))
        # titles = self.driver.find_elements_by_id('com.ss.android.ugc.aweme:id/a23')
        authors = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/w5')))
        dianzans = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/a3i')))
        # self.driver.find_element_by_xpath(
        #         '//*[@text="没有更多了"]')

        for title in titles:
            sleep(2)
            print(title.text + '这是视频标题')
        for author in authors:
            sleep(2)
            print(author.text + '这是视频作者')
        for dianzan in dianzans:
            sleep(2)
            print(dianzan.text + '这是视频点赞数')
        '''


    def main(self):
        self.comments()
        self.search()
        while True:
            self.fechAllResults()



if __name__ == '__main__':
    action = Action()
    action.main()