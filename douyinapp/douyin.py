from appium import webdriver
from time import sleep
import requests
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
# 设置滑动初始坐标和滑动距离
        self.start_x = 500
        self.start_y = 1500
        self.distance = 1300

    def comments(self):
        sleep(2)
# app开启之后点击一次屏幕，确保页面的展示
        self.driver.tap([(500, 1200)], 500)

    def scroll(self):
# 无限滑动
#         while True:
# 模拟滑动
        self.driver.swipe(self.start_x, self.start_y, self.start_x,self.start_y-self.distance)
# 设置延时等待
        sleep(10)

    def xiazai(self):
        print(222222)
        path = 'D:/video/'
        num = 5

        def response(flow):
            global num
            print(3333)
            # 经测试发现视频url前缀主要是3个
            # target_urls = ['http://v1-dy.ixigua.com/', 'http://v9-dy.ixigua.com/', 'http://v3-dy.ixigua.com/']
            target_urls = ['http://v1-dy.ixigua.com/', 'http://v1-dy-x.ixigua.com/', 'http://v1-dy-y.ixigua.com/',
                           'http://v1-dy-z.ixigua.com/',
                           'http://v3-dy.ixigua.com/', 'http://v3-dy-x.ixigua.com/', 'http://v3-dy-y.ixigua.com/',
                           'http://v3-dy-z.ixigua.com/',
                           'http://v6-dy.ixigua.com/', 'http://v6-dy-x.ixigua.com/', 'http://v6-dy-y.ixigua.com/',
                           'http://v6-dy-z.ixigua.com/',
                           'http://v9-dy.ixigua.com/', 'http://v9-dy-x.ixigua.com/', 'http://v9-dy-y.ixigua.com/',
                           'http://v9-dy-z.ixigua.com/']
            print(target_urls)
            print(3333)
            sleep(2)

            for url in target_urls:
            # 过滤掉不需要的url
                if flow.request.url.startswith(url):
                # 设置视频名
                    filename = path + str(num) + '.mp4'
                # 使用request获取视频url的内容
                # stream=True作用是推迟下载响应体直到访问Response.content属性
                    res = requests.get(flow.request.url, stream=True)
                # 将视频写入文件夹
                    with open(filename, 'ab') as f:
                        f.write(res.content)
                        f.flush()
                    print(filename + '下载完成')
                    num += 1

    def main(self):
        self.comments()
        while True:
            self.scroll()
            # self.xiazai()


if __name__ == '__main__':
    action = Action()
    action.main()