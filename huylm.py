import requests, os, sys, re
from time import sleep

cl = '\033[1;34m['+'☇'+'\033[1;34m]\033[1;34m ➠ \033[1;32m'  
w="\033[1;37m"
key=requests.get('https://pastebin.com/raw/QpwVdXXd').text
if key == 'open':
  print(w+'Tool đang hoạt động')
else:
  exit(w+'''Tool đã dừng hoạt động
Vui lòng liên hệ:
Facebook: Facebook.com/trungbb8
Zalo: 0367784857''')
sleep(1)
os.system('clear')


t=open('cookie_fb.txt',mode='a+')
t=open('cookie_fb.txt',mode='r')
ckc=t.read()
t.close()
print('Cookie Facebook Hiện Tại: ',ckc)
print('='*40)
chose=input('Bạn Có Muốn Đổi Cookie Facebook Không? Y/n: ')
if chose == 'Y' or chose == 'y':
  t=open('cookie_fb.txt',mode='w')
  ckm=input('Nhập Cookie Facebook Mới: ')
  t.write(ckm)
  t.close()
  cookie_fb=ckm
else:
  cookie_fb=ckc
os.system('clear')
  

head_fb={
  'Host':'mbasic.facebook.com',
  'sec-ch-ua':'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
  'sec-ch-ua-mobile':'?1',
  'upgrade-insecure-requests':'1',
  'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36',
  'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'cookie':''+cookie_fb
}
link='riends/center/requests/outgoing/?mfl_act=1&_rdr'
while True: 
  
  while True:
  
    truy=requests.get('https://mbasic.facebook.com/f'+link,headers=head_fb)
    j = truy.text
    links=j.split('href="/f')[2].split('"')[0].replace('amp;','')
    k = '/a/' in j   
    if k == False:
      
    #print(links)
      link=links
      break
    elif k == True:
      idfbh=truy.text.split('/a/friendrequest/cancel/?subject_id=')[1].split('&')[0]
      huy=truy.text.split('/a/friendrequest/cancel/')[1].split('"')[0].replace('amp;','')
#print(idfbh)
#print(truy.text)
      job=requests.get('https://mbasic.facebook.com/a/friendrequest/cancel/'+huy,headers=head_fb)
  #print(job.text)
      tt=job.text.split('><head><title>')[1].split('<')[0]
  #print(tt)
  
      if tt == 'Lỗi':
        print(cl+'Gỡ Lời Mời Kết Bạn Thành Công - ID: ',idfbh)
  
      else:
        print(cl+'Lỗi')
      sleep(0.1)
      break

