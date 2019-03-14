import requests
from bs4 import BeautifulSoup
import os


url = 'https://www.dcard.tw/f/sex'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
html = requests.get(url, headers=header)


soup = BeautifulSoup(html.text, 'html.parser')
titles = soup.select('h3')

href = soup.select('div.PostList_entry_1rq5Lf a.PostEntry_root_V6g0rd')

iii=0
jjj=0

for i in href:
    a = i.get("href")[6:18]
    url1 = 'https://www.dcard.tw/f/sex'+a
    html1 = requests.get(url1,headers=header)
    fib_text = BeautifulSoup(html1.text,'html.parser')
    image = fib_text.select("div.Post_content_NKEl9d div div div img.GalleryImage_image_3lGzO5")
    image3 = fib_text.select("div.CommentEntry_content_1ATrw1 div div div img.GalleryImage_image_3lGzO5")
    for aaa in image:
        pic = requests.get(aaa["src"],headers=header)
        img2 = pic.content
        path = "/Users/user/PycharmProjects/untitled1/venv/save/"+str(i.get("href")[20:30])
        path2 = path + "/留言"
        if not os.path.isdir(path):
            os.mkdir(path)
        pic_out = open(path+'/'+i.get("href")[20:30]+'img'+str(iii)+'.png','wb')  #成功將圖片下載到指定路徑
        iii = iii + 1
        pic_out.write(img2)
        pic_out.close()
        print(aaa.get("src"))

    for bbb in image3:
        pic = requests.get(bbb["src"], headers=header)
        img2 = pic.content
        path = "/Users/user/PycharmProjects/untitled1/venv/save/" + str(i.get("href")[20:30])
        path2 = path + "/留言"
        if not os.path.isdir(path2):
            os.mkdir(path2)
        pic_out2 = open(path2 + '/' + i.get("href")[20:30] + 'img' + str(jjj) + '.png', 'wb')
        jjj = jjj + 1
        pic_out2.write(img2)
        pic_out2.close()

    #print(url1)
    #print(html1.status_code)
    #print(i.get("href")[0:18]+"  "+i.get("href")[20:30])



#測試抓圖片
'''
pic=requests.get('https://imgur.dcard.tw/eujySyR.jpg',headers=header)
print(pic.status_code)
img2 = pic.content
pic_out = open('img1.png','wb')
pic_out.write(img2)
pic_out.close()

'''

'''
abc = 'https://www.dcard.tw/f/sex/p/230829789'

cde = requests.get(abc, headers=header)

fgh = BeautifulSoup(cde.text,'html.parser')

print(cde.status_code)
egg = fgh.select("div.Post_content_NKEl9d div div div img.GalleryImage_image_3lGzO5")

for aaa in egg:
    print(aaa.get("src"))

'''


'''
for i in titles:
    print(i.text)
＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

"""
如果指定目錄不存在就建立目錄
要不然的話就直接開檔案
"""
import os
path = "C:\\alarm"
if not os.path.isdir(path):
    os.mkdir(path)
file = open(path + "\\" + "我要開檔案.txt", "w")    
＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
'''
