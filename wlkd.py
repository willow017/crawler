import requests
import json
import time

token = ""
userid = ""
smid = ""

def userdata(token, userid, smid):
    url = 'https://wlkdapi.zhongchuanjukan.com/account/getTodayDetail'
    headers = {
        'Content-Type': 'application/json',
        'Host': 'wlkdapi.zhongchuanjukan.com',
        'User-Agent': 'wen lu kan dian/2.0.1 (iPad; iOS 15.3.1; Scale/2.00)',
        'sppid': 'e2c8a1489aa1deddd8968cb5db4fa8a5'
    }
    body = '{"channel":"AppStore","userid":'+'\"'+userid+'\"'+',"appversioncode":"201","brand":"apple","sysname":"wlkd","appversion":"2.0.1","optime":"1645945937","os":"ios","token":'+'\"'+token+'\"'+',"smid":'+'\"'+smid+'\"'+',"model":"iUnknown","osversion":"15.3.1","device_userid":""}'
    res = requests.post(url, headers=headers, data=body)
    sj = json.loads(res.text)
    print('当前账号总金币数量为:'+sj['balance']+', 共获得金币数量为:'+sj['todayReward'])

def qiandao(token, userid):
    url = 'https://wlkdapi.zhongchuanjukan.com/account/getTodayDetail'
    headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'Host': 'wlkdapi.zhongchuanjukan.com',
        'Origin': 'https://wlkdapi.zhongchuanjukan.com',
        'Referer': 'https://wlkdapi.zhongchuanjukan.com/task/view/?sysname=wlkd&token='+token+'&device_userid=&brand=apple&model=iUnknown&optime=1645768757&sppid=c30e8b71edd5c3d77f15a0b9923dd664',
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'X-Requested-With': 'XMLHttpRequest'
    }
    body = '{"token":'+'\"'+token+'\"'+',"userid":'+'\"'+userid+'\"'+',"sysname":"wlkd"}'
    res = requests.post(url, headers=headers, data=body)
    sj = json.loads(res.text)
    qdjb = sj['todayReward']
    print('签到获得'+str(qdjb)+'金币')


def spsj(token, userid, smid):
    url = 'https://wlkdapi.zhongchuanjukan.com/article/list'
    headers = {
        'Content-Type': 'application/json',
        'Host': 'wlkdapi.zhongchuanjukan.com',
        'User-Agent': 'wen lu kan dian/2.0.1 (iPad; iOS 15.3.1; Scale/2.00)',
        'sppid': 'e72265be8c426c85f59aa2b3a77b89bc'
    }
    body = '{"osversion":"15.3.1","classify":0,"channel":"AppStore","userid":'+'\"'+userid+'\"'+',"appversioncode":"201","brand":"apple","sysname":"wlkd","sceneType":"list","optime":"1645770699","appversion":"2.0.1","pullAction":"header","os":"ios","token":'+'\"'+token+'\"'+',"smid":'+'\"'+smid+'\"'+',"pageNo":3,"model":"iUnknown","typeid":36}'
    res = requests.post(url, headers=headers, data=body)
    sj = json.loads(res.text)
    for i in range(0, 10):
        spid = sj['artlist'][i]['artId']
        spname = sj['artlist'][i]['artTitle']
        return spid, spname
       # print('视频id:'+str(spid)+',   视频名字:'+spname)

def yd(token, userid, smid, spid, spname):
    url = 'https://wlkdapi.zhongchuanjukan.com/article/read'
    headers = {
        'Content-Type': 'application/json',
        'Host': 'wlkdapi.zhongchuanjukan.com',
        'User-Agent': 'wen lu kan dian/2.0.1 (iPad; iOS 15.3.1; Scale/2.00)',
        'sppid': 'af3f003d5272fed6347a47aa4e9a31cf'
    }
    body = '{"userid":'+'\"'+userid+'\"'+',"sceneType":"list","title":'+'\"'+spname+'\"'+',"optime":"1645769288","sysname":"wlkd","smid":'+'\"'+smid+'\"'+',"brand":"apple","channel":"AppStore","appversion":"2.0.1","artClassify":0,"os":"ios","sensorX":0,"sensorY":0,"device_userid":"","token":'+'\"'+token+'\"'+',"appversioncode":"201","model":"iUnknown","sensorZ":0,"osversion":"15.3.1","artId":'+'\"'+spid+'\"'+'}'
    res = requests.post(url, headers=headers, data=body.encode('utf-8'))
    sj = json.loads(res.text)
    print('本次阅读视频'+spname+'获得金币'+str(sj['profit'])+'金币')



def main(token, userid, smid):
    now = time.strftime("%H-%M-%S")
    if now == '12-10-12':
        qiandao(token, userid)
    if (now == '14-20-10') | (now == '16-30-15') | (now == '20-15-11') | (now == '09-30-15') | (now == '19-30-00'):
        for i in range(0, 5):
            sj = spsj(token, userid, smid)
            yd(token, userid, smid, sj[0], sj[1])
            time.sleep(60)
        userdata(token, userid, smid)



if __name__ == '__main__':
    while True:
        main(token, userid, smid)
