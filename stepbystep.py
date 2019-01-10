#항상 가장 먼저 Updater 객체를 만들고 토큰(API Key)을 입력하여 완성한다.
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging


updater=Updater(token="604582951:AAGCfEB-GsjenkFBE6eR04sK_Pzmd2kWjCc")

#updater의 dispatcher로 빠르게 접근하는 방법에는 지역변수 선언이 있다.
dispatcher=updater.dispatcher

logging.basicConfig(format="%(asctime)s - %(name)s - %(level)s - %(message)s", 
level=logging.INFO)

#시작시 메세지를 보내는 함수
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

#유저가 보낸 텍스트를 따라한다.
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

#유저가 보낸 메세지를 대문자로 반환하는 함수
def caps(bot, update, args):
    text_caps=' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

#inline 기능을 사용할 수 있는 함수
def inline_caps(bot, update):
    query=update.inline_query.query
    if not query:
        return
    results=list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)

#등록되어있지 않은 커맨드 입력 시 안내문구 출력
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")




#봇의 작동을 객체에 담는다.
start_handler=CommandHandler("start", start)
echo_handler=MessageHandler(Filters.text, echo)
caps_handler=CommandHandler('caps', caps, pass_args=True)
inline_caps_handler=InlineQueryHandler(inline_caps)
unknown_handler = MessageHandler(Filters.command, unknown)


#디스패처를 통해 봇을 업그레이드한다.
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(unknown_handler)


#봇을 시작한다.
updater.start_polling()

#봇을 서비스한다.
updater.idle()