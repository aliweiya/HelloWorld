import requests
from lxml import etree
import ua
import openpyxl
from time import sleep


class ChiCtr(object):

    def __init__(self):
        self.base_url = 'http://www.chictr.org.cn/searchproj.aspx?page=%s'
        self.start_url = self.base_url % 1
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/ xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'www.chictr.org.cn',
        }
        self.headers['User-Agent'] = ua.get_ua()
        self.sleep_time = 10
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.start_request()
        self.num = 1

    def start_request(self):
        self.start_response = requests.get(self.start_url, headers=self.headers)

    @staticmethod
    def request(url, headers):
        response = requests.get(url, headers=headers)
        return response

    def start_parse(self):
        html = etree.HTML(self.start_response.text)
        div = html.xpath('//div[@id="pgProj"]')[0]
        span = div.xpath('./span')[0]
        label = span.xpath('./label/text()')[0]
        max_page = label.split()[1][1:-1]
        for i in range(2, int(max_page) + 1):
            yield self.base_url % i

    def parse(self, response):
        base_url = 'http://www.chictr.org.cn/'
        html = etree.HTML(response.text)
        table = html.xpath('//table[@class="table_list"]')[0]
        tr_list = table.xpath('./tbody/tr')[1:]
        for tr in tr_list:
            td = tr.xpath('./td')
            number = td[1].xpath('./text()')[0].strip()
            p = td[2].xpath('./p')
            a = p[0].xpath('./a')[0]
            link = base_url + a.xpath('./@href')[0]
            title = a.xpath('./text()')[0]
            institution = p[1].xpath('./text()')[0].strip()
            study_type = td[3].xpath('./text()')[0].strip('"').strip()
            date_of_registration = td[4].xpath('./text()')[0].strip('"').strip()

            self.sheet.cell(row=self.num, column=1, value=link)
            self.num += 1
            print(title, 'is ok!')

        print(response.url, 'is ok!')
        self.workbook.save('link.xlsx')

    def run(self):
        self.parse(self.start_response)
        url_list = self.start_parse()
        sleep(self.sleep_time)
        for url in url_list:
            self.headers['User-Agent'] = ua.get_ua()
            response = self.request(url, self.headers)
            self.parse(response)
            sleep(self.sleep_time)


if __name__ == '__main__':
    chictr = ChiCtr()
    chictr.run()
    # chictr.start_parse()
    print('完成')
