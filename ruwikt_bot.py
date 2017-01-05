'''
A wiktionary lookup bot for Telegram.
'''
import telepot
from telepot.exception import TelegramError
from wiktionaryparser import WiktionaryParser
import sys,time

parser = WiktionaryParser()

def handle(msg):
  content_type,chat_type,chat_id = telepot.glance(msg)
  print content_type,chat_type,chat_id
  if content_type == 'text':
    command = msg['text']

    if command.startswith('/define '):
      query = command.split()
      if len(query) < 3:
	bot.sendMessage(chat_id,'Proper syntax is /define <word> <lang>')
      else:
	try:
	  w = query[1]
	  lang = query[2:]
	  lang = ' '.join(lang)
	  wiki_link = 'www.wiktionary.org/wiki/'+w
	  d = parser.fetch(w,lang)[0]['definitions'][0]['text'].encode("utf-8")
	  bot.sendMessage(chat_id,d)
	except TelegramError:
	  bot.sendMessage(chat_id,'Either the entry is too long or it does not exist. You can try to find it here: '+wiki_link)
	except IndexError:
	  bot.sendMessage(chat_id,'Entry not found')
    else:
      bot.sendMessage(chat_id,'Proper syntax is /define <word> <lang>')

TOKEN = sys.argv[-1]
bot = telepot.Bot(TOKEN)
bot.message_loop(handle,run_forever='Listening...')

