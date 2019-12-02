import requests
from bs4 import BeautifulSoup
import bs4


# 从目标url中提取文本信息的函数
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        # 设置连接成功提醒
        r.raise_for_status()
        # 改变编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 在所有文本中提取表格前三列的信息
def fillUnivList(ulist, html):
    # html.parser解释器可以将提取出的文本按标签进行分行，保证可读性
    soup = BeautifulSoup(html, "html.parser")
    # 从源代码可以观察到，表格信息都是嵌套在tbody中，而每一行的信息由是嵌套在每一个tr标签中，每一行的每一格信息嵌套在td中，这也是html语言的特点。
    # 因此要遍历tbody中的每一个tr标签，即遍历每一行。
    for tr in soup.find('tbody').children:
        # 为了防止文本字符中含有“tr"字段的信息被误认为html标签，因此需要进行标签确认
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            # 提取出每一行表格前3列的信息
            ulist.append([tds[0].string, tds[1].string, tds[2].string])


# 打印提取出的表格信息
def printUnivList(ulist, num):
    # 对输出结果进行format格式化输出，其中"{1:{3}^10}"中的{3}表示的是空余位置用format函数的第四个参数填充
    # 因为如果是按照默认的话，format中空余位置会用英文字符进行填充，这就造成了长短不一，输出不美观的影响
    # 而chr（12288）是中文空格对应的Unicode编码，这样就可以用中文空格填充空余位置了。
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校", "分数", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    # 20代表爬取前20个学校
    num = 20
    printUnivList(uinfo,num)


main()


