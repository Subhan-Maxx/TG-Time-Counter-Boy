from pyrogram import Client, filters, enums
from os import environ
from calculate_time import get_data
import time

bot_token = environ.get('BOT_TOKEN')

counter = Client(    
    name='Time-Counter',
    api_id=24871620,
    api_hash='e4195bedc71234a179a3d9ac0cad6401',
    bot_token= "7106861798:AAEG1AhY5GLmT0N2NGM8w7AYysBH3b9sWsM"
) 

@counter.on_message(filters.command('start'))
async def counts(bot, update):
    await update.reply('Bot is Running!')

@counter.on_message(filters.chat(-1002223570290) & (filters.photo))
async def counts(bot, update):
    try:        
        y, m, d, h, mi = get_data()
        try:
             text = f"<b>Since 3 September 2023</b>\n\n<b>Total Years:</b> {y}\n<b>Total Months:</b> {m}\n<b>Total Days:</b> {d}\n<b>Total Hours:</b> {h}\n<b>Total Minutes:</b> {mi}"
             await bot.edit_message_text(
                   chat_id = -1001951908326,
                   text = text,
                   message_id = 7,
                   parse_mode = enums.ParseMode.HTML
             )
        except Exception as e:
            print(str(e))
            await update.reply(str(e))
    except Exception as e:
            print(str(e))
            await update.reply(str(e))            
print('Bot Started!')     
counter.run()
