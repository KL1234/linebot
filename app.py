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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="吃我的毛"))
    if event.message.text.find("黑豆") != -1:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="好可愛"))    
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
