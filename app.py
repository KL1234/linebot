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
        a=random.randint(1,6)
        if a==1:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="吉野家"))
        if a==2:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="拉麵"))
        if a==3:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="添好運"))
        if a==4:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="椒麻雞"))
        if a==5:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="燒肉"))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="吃我的毛"))
    if event.message.text.find("黑豆") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="好可愛"))
    if event.message.text.find("權祐") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Q毛"))    
    if event.message.text.find("魚") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="啵啵啵啵啵啵啵啵"))
    if event.message.text.find("唱歌") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="哼哼哈ㄏ一ˋ 鹹魚七秒記憶\n哼哼哈ㄏ一ˋ 姬路城就是拉基\n哼哼哈ㄏ一ˋ AD名字就叫AD\n"))
    if event.message.text.find("時銘") != -1:
        import random
        a=random.randint(1,3)
        if a==1:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="傑尼傑尼"))
        if a==2:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="克里斯汀真香"))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="時銘:櫻花妹我來了!!!!!!"))
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
        a=random.randint(1,8)
        if a==1:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/rE06hft.jpg', preview_image_url='https://i.imgur.com/rE06hft.jpg'))        
        if a==2:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/yps2gB1.jpg', preview_image_url='https://i.imgur.com/yps2gB1.jpg'))        
        if a==3:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/AXVJd7M.jpg', preview_image_url='https://i.imgur.com/AXVJd7M.jpg'))        
        if a==4:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/J6LRR2i.jpg', preview_image_url='https://i.imgur.com/J6LRR2i.jpg'))        
        if a==5:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/vIPnwvi.jpg', preview_image_url='https://i.imgur.com/vIPnwvi.jpg'))        
        if a==6:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/25drqpo.jpg', preview_image_url='https://i.imgur.com/25drqpo.jpg'))        
        if a==7:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/LTb9P6x.jpg', preview_image_url='https://i.imgur.com/LTb9P6x.jpg'))        
        else:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/r2v9qpw.jpg', preview_image_url='https://i.imgur.com/r2v9qpw.jpg'))        
    if event.message.text.find("灰") != -1:
        import random
        a=random.randint(1,10)
        if a==1:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/X5yQVtV.jpg', preview_image_url='https://i.imgur.com/X5yQVtV.jpg'))        
        if a==2:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/3tgaaiI.jpg', preview_image_url='https://i.imgur.com/3tgaaiI.jpg'))        
        if a==3:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/ENhgcGd.jpg', preview_image_url='https://i.imgur.com/ENhgcGd.jpg'))        
        if a==4:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/Ope3LpQ.jpg', preview_image_url='https://i.imgur.com/Ope3LpQ.jpg'))        
        if a==5:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/C13WKX6.jpg', preview_image_url='https://i.imgur.com/C13WKX6.jpg'))        
        if a==6:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/J4e41HY.jpg', preview_image_url='https://i.imgur.com/J4e41HY.jpg'))        
        if a==7:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/85NyR92.jpg', preview_image_url='https://i.imgur.com/85NyR92.jpg'))        
        if a==8:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/LqOSjSn.jpg', preview_image_url='https://i.imgur.com/LqOSjSn.jpg'))        
        if a==9:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/K4Wra0N.jpg', preview_image_url='https://i.imgur.com/K4Wra0N.jpg'))            
        else:
            line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/r2v9qpw.jpg', preview_image_url='https://i.imgur.com/r2v9qpw.jpg'))                    
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
