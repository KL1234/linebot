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
    if event.message.text.find("灰") != -1:
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://i.imgur.com/RzKU1hM.jpg', preview_image_url='https://i.imgur.com/RzKU1hM.jpg'))            
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
