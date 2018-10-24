from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from uiautomator import device as d
from time import sleep
import re


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
        self.distance = 1130
        self.uu = 0
        # 新建一个Session
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        self.wait = WebDriverWait(self.driver, 30)

    def comments(self):
        sleep(5)
        # app开启之后点击一次屏幕，确保页面的展示
        self.driver.tap([(500, 1200)], 500)

    def search(self):
        sleep(2)
        # search2=self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a9k')))
        # search2 = self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9k')
        # search2.click()
        self.driver.tap([(88, 158)], 100)
        print("-----------------------------------去搜索界面----------------------------------------")
        self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a1x'))).click()
        txt = self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a1x')))
        # # txt.clear()
        txt.send_keys("别克GL6")
        # txt.send_keys(u"qiche")
        print("-----------------------------------输入完成----------------------------------------")
        self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a1z'))).click()
        print("-----------------------------------搜索完成----------------------------------------")

        sleep(5)

        a = self.driver.find_element_by_xpath(
            '//*[@text="视频"]')
        a.click()

        print("-----------------------------------跳转到视频选项----------------------------------------")
        sleep(5)
        # 'com.ss.android.ugc.aweme:id/jn'  --videolist

    def scroll(self):
        self.driver.swipe(self.start_x, self.start_y, self.start_x, self.start_y - self.distance)

        # self.driver.getPageSource()

    def enterComments(self):
        sleep(2)
        print("-----------------------------------已经进入第一个视频----------------------------------------")
        sleep(5)
        # author = self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/bc')))

        # print(author.text+'这是作者')
        # title = self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a23')))
        # print(title.text + '这是标题')
        # dianzan = self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/al9')))
        # print(dianzan.text + '这是点赞数')
        # self.driver.tap([(288, 242), (576, 382)], 500)  #进入评论
        # self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/wp'))).click()
        # self.driver.tap([(1263, 1460), (1403, 1600)], 500)
        self.driver.tap([(1320, 1510)], 500)
        print("-----------------------------------评论窗口打开----------------------------------------")
        sleep(2)
        print("-----------------------------------好了----------------------------------------")
        sleep(2)
        try:
            pingluncount = self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/bc')))
            pingping = pingluncount.text
            matchObj = re.match(r'(.*)条评论', pingping, re.M | re.I)
            print('当前视频有%s条评论' % matchObj.group(1))
        except:
            return False
        return True

    def catchComments(self):

        pinglunshu = self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/bc')))
        print(pinglunshu.text + '这是评论数')

        result = self.driver.find_elements_by_xpath(
            '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout'
        )
        # print(result)
        # print(len(result))
        for i in range(len(result)):
            try:
                m=result[0]
                tt = m.find_elements_by_xpath('./*')
                
                if len(tt) < 5:  # (头像，作者外壳，作者壳，作者，评论内容)
                    break
                else:
                    commtauthors = self.driver.find_element_by_xpath()
                    commdetails = self.wait.until(
                        EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/v1')))
                    commdates = self.wait.until(
                        EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/ahw')))
                    commdianzans = self.wait.until(
                        EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/ak5')))
            except:
                pass

    def ppp(self):
        sleep(5)
        self.driver.tap([(350, 800)], 500)
        print("-----------------------------------点击进入第一个视频----------------------------------------")
        if self.enterComments():

            old_dict = {}
            i = 1
            while i <= 20:
                cache_dict = self.catchComments()
                # if not old:
                #     old_dict = self.catchComments()
                # else:
                #     if cache_dict == old_dict:
                #         break
                if old_dict:
                    print(old_dict)
                    print(cache_dict)
                    if cache_dict == old_dict:
                        break
                old_dict = self.catchComments()
                sleep(2)

                # self.scroll()
                self.driver.swipe(620, 2030, 620, 1110)
                i = i + 1
                print(i)
        sleep(5)
        # self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/is').click()
        self.driver.tap([(662, 228)], 500)
        print("-----------------------------------评论关闭----------------------------------------")
        sleep(5)
        # self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a1y').click()
        self.driver.tap([(80, 196)], 500)
        print("-----------------------------------返回视频选项卡----------------------------------------")
        sleep(2)
        #     ----------------------------------------------------------------
        self.driver.tap([(1110, 800)], 500)
        print("-----------------------------------点击进入第二个视频----------------------------------------")
        if self.enterComments():
            old_dict = {}
            i = 1
            while i <= 20:
                cache_dict = self.catchComments()
                # if not old:
                #     old_dict = self.catchComments()
                # else:
                #     if cache_dict == old_dict:
                #         break
                if old_dict:
                    print(old_dict)
                    print(cache_dict)
                    if cache_dict == old_dict:
                        break
                old_dict = self.catchComments()
                sleep(2)

                # self.scroll()
                self.driver.swipe(620, 2030, 620, 1110)
                i = i + 1
                print(i)
        sleep(5)
        # self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/is').click()
        self.driver.tap([(662, 228)], 500)
        print("-----------------------------------评论关闭----------------------------------------")
        sleep(3)
        # self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a1y').click()
        self.driver.tap([(80, 196)], 500)
        print("-----------------------------------返回视频选项卡----------------------------------------")
        sleep(2)

    def main(self):
        # self.comments()
        # self.search()
        j = 1
        while j <= 20:
            sleep(5)
            # self.driver.tap([(350, 800)], 500)
            # print("-----------------------------------点击进入第一个视频----------------------------------------")
            self.enterComments()
            self.catchComments()
            # self.ppp()
            # self.scroll()
            j = j + 1


if __name__ == '__main__':
    action = Action()
    action.main()
