import requests
from bs4 import BeautifulSoup


# 保存到csv
def saveCSV(ls):
    fw = open('university_rank_2021.csv','w')
    fw.write('排名,学校名称,省市,类型,总分,办学层次\n')
    for row in ls:
        print(row)
        fw.write(','.join(row)+'\n')
    fw.close()


def main():
    # 获取网页
    r = requests.get("https://www.shanghairanking.cn/rankings/bcur/2021")
    r.encoding = "utf-8"
    # 将网页内容转为soup对象
    soup = BeautifulSoup(r.text)
    # 找第一个表格体
    tbody = soup.find('tbody')
    # 找里面找所有tr
    trResSet = tbody.find_all('tr')
    # 处理每一行数据，得到需要的信息
    ls = []  # 二维数组存信息
    for tr in trResSet:
        # 得到当前行的每个td
        tdResSet = tr.find_all('td')
        rank = tdResSet[0].text.strip()     # 得到排名
        name = tdResSet[1].find('a', {'class': 'name-cn'}).text.strip()     # 得到名字
        province = tdResSet[2].text.strip()     # 得到省市
        type = tdResSet[3].text.strip()     # 得到类型
        score = tdResSet[4].text.strip()    # 得到总分
        level = tdResSet[5].text.strip()    # 得到办学层次
        ls.append([rank, name, province, type, score, level])   # 添加到结果列表
    saveCSV(ls) # 将结果列表保存到csv文件


main()
