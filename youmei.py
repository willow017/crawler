import requests
from bs4 import BeautifulSoup
import os
import time
from random import choice, randint
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

if not os.path.exists('套图'):
    os.mkdir('套图')

user_agent = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"

]

headers = {
    'user-agent': choice(user_agent),
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
def get_taotu():
    url = "https://www.umei.cc/bizhitupian/meinvbizhi/yangyanmeinv.htm"
    proxies = {
        "http": "http://221.239.44.70:8085",
       # 'https': 'https://117.69.47.190:14965',
    }
    resp = requests.get(url=url, proxies=proxies, timeout=5)
    resp.encoding = "utf-8"
    html = BeautifulSoup(resp.text, "html.parser")
    hrefs = html.find_all("a", attrs={"class": "TypeBigPics"})
    return hrefs

def get_tu():
    proxies = {
        "http": "http://221.239.44.70:8085",
        #'https': 'https://117.69.47.190:14965',
    }
    n = 1
    domain = "https://www.umei.cc/"
    hrefs = get_taotu()
    for href in hrefs:
        href_img = href.get("href")
        urls = domain + href_img
        img_resp = requests.get(url=urls, proxies=proxies, timeout=(3, 7))
        img_resp.encoding = "utf-8"
        html = BeautifulSoup(img_resp.text, "html.parser")
        urls = html.find("div", attrs={"class": "NewPages"})
        url = urls.find_all("a")
        for fimg in url:
            lianjie = fimg.get("href")
            img = domain + lianjie
            img_response = requests.get(url=img, proxies=proxies, timeout=(3, 7))
            img_response.encoding = "utf-8"
            html = BeautifulSoup(img_response.text, "html.parser")
            div = html.find("div", attrs={"class", "ImageBody"})
            img_src = div.find("img").get("src")
            img_resps = requests.get(img_src, headers=headers, proxies=proxies, timeout=300)
            if img_resps.status_code == 200:
                with open(r"./套图/{}.jpg".format(n), mode="wb") as f:
                    f.write(img_resps.content)
                print(f"{n}下载完成")
                n += 1
            else:
                print("下载失败")

if __name__ == '__main__':
    get_taotu()
    url = get_tu()
    print("game over")

