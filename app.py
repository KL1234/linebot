from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()

prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)
options.add_argument("--headless")            #不開啟實體瀏覽器背景執行
options.add_argument("--incognito")           #開啟無痕模式
driver = webdriver.Chrome(options=options)

driver.get("https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6400900") 

Temp = driver.find_element_by_id('GT_C_T').text
bodyTemp = driver.find_element_by_id('GT_C_AT').text
RelativeHumidity = driver.find_element_by_id('GT_RH').text
Rain = driver.find_element_by_id('GT_Rain').text
Sunrise = driver.find_element_by_id('GT_Sunrise').text
Sunset = driver.find_element_by_id('GT_Sunset').text
driver.quit()
#建立LINE訊息要出現的內容
content="\n"+"前鎮區天氣概況"+"\n"+"\n"+"現在溫度 : "+Temp+"°C"+"\n"+"體感溫度 : "+bodyTemp+"°C"+"\n"+"相對溼度 : "+RelativeHumidity+"%"+"\n"+"降雨量 : "+Rain+"mm"+"\n"+"日出時間 : "+Sunrise+"\n"+"日落時間 : "+Sunset
#建立一個傳送訊息的函式
def lineNotifyMessage(token, msg):
    headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
#修改為你的權杖內容(將yourToken換成在申請到的LINE官方Token)
token = 'HgSH/M7XimOt6yMVTwc5m1yA2jKqmTaZOzavFMFl9pnRKJ14pmD4CH7eBisXb03/1Gv+0e3iW6jKEMj6FJpbfFfqz9XWIEUUVeQhlCPM7jgUG6+KEztr/0k9jG5gMncY1a6hoC8IG+b3egiAkbwMDAdB04t89/1O/w1cDnyilFU='
lineNotifyMessage(token, content)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('HgSH/M7XimOt6yMVTwc5m1yA2jKqmTaZOzavFMFl9pnRKJ14pmD4CH7eBisXb03/1Gv+0e3iW6jKEMj6FJpbfFfqz9XWIEUUVeQhlCPM7jgUG6+KEztr/0k9jG5gMncY1a6hoC8IG+b3egiAkbwMDAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7e7c4d1f3078c10248cb225c4c6687c7')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    if event.message.text.find("吃什麼") != -1:
        import random
        #四個一排
        list1 = ['吉野家','拉麵','添好運','椒麻雞',
        '燒肉','吃我的毛','牛排','胡椒廚房',
        '火鍋','夜市','滷肉飯','牛肉麵',
        '水餃']
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=list1[random.randint(0,12)]))
    if event.message.text.find("黑豆") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="好可愛"))
    if event.message.text.find("權祐") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Q毛"))    
    if event.message.text.find("魚") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="啵啵啵啵啵啵啵啵"))
    if event.message.text.find("肚子") != -1 or event.message.text.find("肚肚") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="肚子的肚子大大大"))
    if event.message.text.find("唱歌") != -1:
    import random
        list1 = ['哼哼哈ㄏ一ˋ 鹹魚七秒記憶\n哼哼哈ㄏ一ˋ 姬路城就是拉基\n哼哼哈ㄏ一ˋ AD名字就叫AD\n',
        '啦~~~~~~啦~~~~~~~~~啦~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',
        '當緣分讓我們相遇在光年之外~~~']
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=list1[random.randint(0,2)]))
    if event.message.text.find("時銘") != -1:
        import random
        list1 = ['傑尼傑尼','克里斯汀真香',
        '時銘:櫻花妹我來了!!!!!!']
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=list1[random.randint(0,2)]))
    if event.message.text.find("妹妹") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="妹妹乖喔"))
    if event.message.text.find("欸") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="欸~~~~~(破音")) 
    if event.message.text.find("難聽") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="欸.....很難聽")) 
    if event.message.text.find("好累") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="嫩"))
    if event.message.text.find("累死") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="嫩"))        
    if event.message.text.find("ㄎㄎ") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="笨米ㄎㄎ吃蛋糕"))         
    if event.message.text.find("傻眼") != -1:
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/r2v9qpw.jpg', preview_image_url='https://i.imgur.com/r2v9qpw.jpg'))        
    if event.message.text.find("虎") != -1:
        import random
        #四個一行
        list1 = ['https://i.imgur.com/rE06hft.jpg','https://i.imgur.com/yps2gB1.jpg','https://i.imgur.com/AXVJd7M.jpg','https://i.imgur.com/J6LRR2i.jpg',
        'https://i.imgur.com/vIPnwvi.jpg','https://i.imgur.com/25drqpo.jpg','https://i.imgur.com/LTb9P6x.jpg','https://i.imgur.com/r2v9qpw.jpg']
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=list1[random.randint(0,7)], preview_image_url=list1[random.randint(0,7)]))
    if event.message.text.find("灰") != -1:
        import random
        #四個一行
        list1 = ['https://i.imgur.com/X5yQVtV.jpg','https://i.imgur.com/3tgaaiI.jpg','https://i.imgur.com/ENhgcGd.jpg','https://i.imgur.com/Ope3LpQ.jpg',
        'https://i.imgur.com/C13WKX6.jpg','https://i.imgur.com/J4e41HY.jpg','https://i.imgur.com/85NyR92.jpg','https://i.imgur.com/LqOSjSn.jpg',
        'https://i.imgur.com/K4Wra0N.jpg','https://i.imgur.com/r2v9qpw.jpg']
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=list1[random.randint(0,9)], preview_image_url=list1[random.randint(0,9)]))
     
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
