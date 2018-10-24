from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
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
        #search2=self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a9k')))
        # search2 = self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9k')
        #search2.click()
        self.driver.tap([(88, 158)], 100)
        print("-----------------------------------去搜索界面----------------------------------------")
        self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a3j'))).click()
        txt = self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a3j')))
        # # txt.clear()
        txt.send_keys("别克GL6")
        # txt.send_keys(u"qiche")
        print("-----------------------------------输入完成----------------------------------------")
        self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a3l'))).click()
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
            pingluncount = self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/bi')))
            pingping=pingluncount.text
            matchObj = re.match(r'(.*)条评论', pingping, re.M | re.I)
            print('当前视频有%s条评论' % matchObj.group(1))
        except:
            return False
        return True


    def catchComments(self):

        pinglunshu = self.wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/bi')))
        print(pinglunshu.text + '这是评论数')

        commtauthors = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/bi')))[1:]
        commdetails = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/v1')))
        commdates = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/ahw')))
        commdianzans = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/ak5')))


        # for commtauthor in commtauthors:
        #     sleep(2)
        #     print(commtauthor.text + '这是评论作者')
        # for commdetail in commdetails:
        #     sleep(2)
        #     print(commdetail.text + '这是评论详情')
        # for commdate in commdates:
        #     sleep(2)
        #     print(commdate.text + '这是评论时间')
        # for commdianzan in commdianzans:
        #     sleep(2)
        #     print(commdianzan.text + '这是该评论的点赞数')
        cache_dict = {'commtauthors': [],
        'commdetails': [],
        'commdates': [],
        'commdianzans': []}

        for i in range(len(commtauthors)):
            try:
                 commtauthor = commtauthors[i]
            except:
                pass
            else:
                cache_dict['commtauthors'].append(commtauthor.text)
                print(commtauthor.text + '这是评论详情')
            try:
                 commdetail = commdetails[i]
            except:
                pass
            else:
                cache_dict['commdetails'].append(commdetail.text)
                print(commdetail.text + '这是评论详情')
            try:
                 commdate = commdates[i]
            except:
                pass
            else:
                cache_dict['commdates'].append(commdate.text)
                print(commdate.text + '这是评论时间')
            try:
                 commdianzan = commdianzans[i]
            except:
                pass
            else:
                cache_dict['commdianzans'].append(commdianzan.text)
                print(commdianzan.text + '这是评论的点赞数')


        return cache_dict


    def fechAllResults(self):
        # '#在抖音，记录美好生活#别克GL6对开雨刷，刮的面积很大，副驾驶前面也有好视线。
        # http://v.douyin.com/d6rdRC/ 复制此链接，打开【抖音短视频】，直接观看视频！'
        sleep(2)

        # 'com.ss.android.ugc.aweme:id/a23' 'com.ss.android.ugc.aweme:id/asp' 'com.ss.android.ugc.aweme:id/w5' 'com.ss.android.ugc.aweme:id/a3i'
        # titles  authimages  authors  dianzans
        # titles = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout[*]/android.widget.LinearLayout/*")

        titles = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/a3p')))
        # titles = self.driver.find_elements_by_id('com.ss.android.ugc.aweme:id/a23')
        authors = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/xp')))
        dianzans = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.ss.android.ugc.aweme:id/a55')))
        # self.driver.find_element_by_xpath(
        #         '//*[@text="没有更多了"]')

        for title in titles:
            sleep(2)
            print(title.text)
        for author in authors:
            sleep(2)
            print(author.text)
        for dianzan in dianzans:
            sleep(2)
            print(dianzan.text)

    def ppp(self):
        sleep(5)
        self.driver.tap([(350, 800)], 500)
        print("-----------------------------------点击进入第一个视频----------------------------------------")
        if self.enterComments():
            
            old_dict = {}
            i = 1
            while i<=20:
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
        self.comments()
        self.search()
        j = 1
        while j <= 20:
            self.ppp()
            self.scroll()
            j = j + 1




if __name__ == '__main__':
    action = Action()
    action.main()