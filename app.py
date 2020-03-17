from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *



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
        '水餃','不要吃','吃黑豆的毛','泰式']
        #line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='欣園椒麻雞', address='Taipei', latitude=25.044229, longitude=121.516455))
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=list1[random.randint(0,15)]))    
    if event.message.text.find("笨蛋") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="傑尼"))  
    if event.message.text.find("黑豆") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="好可愛"))  
    if event.message.text.find("糖糖") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="糖什麼糖????\n本虎無論智商顏質都屌打糖糖\n本虎要靠魅力征服人類!!!!!"))
    if event.message.text.find("妹妹") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="妹妹乖喔"))
    if event.message.text.find("謝時銘") != -1:
        import random
        a=random.randint(1,2)
        if a==1:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="克莉絲丁真香"))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="傑尼傑尼"))
    if event.message.text.find("當機") != -1:
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/RuK4kjY.jpg', preview_image_url='https://i.imgur.com/RuK4kjY.jpg'))
    if event.message.text.find("精靈") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="你才精靈 你全家精靈"))
    if event.message.text.find("RZ") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="RZ:研華我來惹!!!!"))
    if event.message.text.find("幾點") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="歡樂21點 "))    
    if event.message.text.find("KL") != -1 or event.message.text.find("kl") != -1 or event.message.text.find("明融") != -1 or event.message.text.find("融融") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="KL大帥哥"))
    if event.message.text.find("妹妹") != -1 or event.message.text.find("聖:D") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="妹妹乖喔"))    
    if event.message.text.find("黑豆") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="好可愛"))
    if event.message.text.find("螃蟹") != -1 or event.message.text.find("誼靜") != -1:
        import random
        list1 = [              
        '螃蟹最喜歡灰灰了',
        '螃蟹最喜歡虎虎了',
        '螃蟹最喜歡斑斑了',
        ]
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=list1[random.randint(0,2)]))          
    if event.message.text.find("權祐") != -1 or event.message.text.find("木子") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Q毛"))   
    if event.message.text.find("奕翔") != -1 or event.message.text.find("AD") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="奕翔是誰? AD名字就叫AD"))        
    if event.message.text.find("魚") != -1 or event.message.text.find("禹賢") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="啵啵啵啵啵啵啵啵"))
    if event.message.text.find("肚子") != -1 or event.message.text.find("肚肚") != -1 or event.message.text.find("書緯") != -1 or event.message.text.find("書瑋") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="肚子的肚子大大大"))
    if event.message.text.find("唱歌") != -1:
        import random
        list1 = ['哼哼哈ㄏ一ˋ 鹹魚七秒記憶\n哼哼哈ㄏ一ˋ 姬路城就是拉基\n哼哼哈ㄏ一ˋ AD名字就叫AD\n',
        '啦~~~~~~啦~~~~~~~~~啦~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',
        '當緣分讓我們相遇在光年之外~~~']
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=list1[random.randint(0,2)]))
    if event.message.text.find("時銘") != -1 or event.message.text.find("傑尼") != -1:
        import random
        list1 = ['傑尼傑尼','克里斯汀真香',
        '時銘:櫻花妹我來了!!!!!!']
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=list1[random.randint(0,2)]))
    if event.message.text.find("欸") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="欸~~~~~(破音")) 
    if event.message.text.find("難聽") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="欸.....很難聽")) 
    if event.message.text.find("累死") != -1 or event.message.text.find("好累") != -1 or event.message.text.find("超累") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="嫩!"))
    if event.message.text.find("ㄎㄎ") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="笨米ㄎㄎ吃蛋糕"))         
    if event.message.text.find("傻眼") != -1:
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/r2v9qpw.jpg', preview_image_url='https://i.imgur.com/r2v9qpw.jpg'))        
    if event.message.text.find("虎") != -1:
        import random
        #四個一行
        list1 = ['https://i.imgur.com/rE06hft.jpg','https://i.imgur.com/yps2gB1.jpg','https://i.imgur.com/AXVJd7M.jpg','https://i.imgur.com/J6LRR2i.jpg',
        'https://i.imgur.com/vIPnwvi.jpg','https://i.imgur.com/25drqpo.jpg','https://i.imgur.com/LTb9P6x.jpg','https://i.imgur.com/RuK4kjY.jpg']
        a=random.randint(0,7)
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=list1[a], preview_image_url=list1[a]))
    if event.message.text.find("灰") != -1:
        import random
        #四個一行
        list1 = ['https://i.imgur.com/X5yQVtV.jpg','https://i.imgur.com/3tgaaiI.jpg','https://i.imgur.com/ENhgcGd.jpg','https://i.imgur.com/Ope3LpQ.jpg',
        'https://i.imgur.com/C13WKX6.jpg','https://i.imgur.com/J4e41HY.jpg','https://i.imgur.com/85NyR92.jpg','https://i.imgur.com/LqOSjSn.jpg',
        'https://i.imgur.com/K4Wra0N.jpg']
        a=random.randint(0,8)
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=list1[a], preview_image_url=list1[a]))
    if event.message.text.find("斑斑") != -1 or event.message.text.find("班班") != -1:
        import random
        #四個一行
        list1 = ['https://i.imgur.com/VTpUUgx.jpg','https://i.imgur.com/Xlu4NLB.jpg','https://i.imgur.com/00350d8.jpg','https://i.imgur.com/Jgp0eUY.jpg',
        'https://i.imgur.com/xERMF7i.jpg','https://i.imgur.com/icmUB5a.jpg','https://i.imgur.com/8fM5IG3.jpg','https://i.imgur.com/6k12hci.jpg',
        'https://i.imgur.com/aeSMY3W.jpg','https://i.imgur.com/0CiLTa2.jpg','https://i.imgur.com/58nraOg.jpg','https://i.imgur.com/RIIxMCD.jpg',
        'https://i.imgur.com/bVMYeqk.jpg']
        a=random.randint(0,12)
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=list1[a], preview_image_url=list1[a]))
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
