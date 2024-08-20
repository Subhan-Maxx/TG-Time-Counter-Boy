from pyrogram import Client, filters, enums
from os import environ
from datetime import datetime
from calculate_time import get_data
import time
import pytz

bot_token = environ.get('BOT_TOKEN')

counter = Client(    
    name='Time-Counter',
    api_id=24871620,
    api_hash='e4195bedc71234a179a3d9ac0cad6401',
    session_string= "BQFRNDIAjgsfeis-pnSKOMuF62lX253qJTwtvI_lTz2qQLHKxV7DPTTdgF1TlyM8XsGuoiC3Ltx0zBrKRhQt-_BZ8STaW1kZO4Hdfta8Tem07CScYz5SOarn1hBd-PWB_FEsSMUk6mkBNvdL0SkHYCDvYZY8sa04wF_3ZvSLTiLS224i62pE2_v7_oDInva_TUPo4zKFSA1Wr0uDcsJHVwazWc_ZpeU-FuHcaSgYzdhHsaVJMPqmUWPQ83syld5eyq3deHrhfwjJaZGxdSfUX6HEEHDSeiBuhyKyGCB7bZEdBv0SNDZO2VYz96yBknE39RZcSHz5_W12KOXIHsqDGP3JSmYCBwAAAAGeBZcgAA"    
) 

@counter.on_message(filters.command('start'))
async def counts(bot, update):
    await update.reply('Bot is Running!')

@counter.on_message(filters.chat(-1002223570290) & (filters.photo))
async def counts(bot, update):
    timezone = pytz.timezone("Asia/Kolkata")
    current_datetime = datetime.now(timezone)
    formatted_datetime = current_datetime.strftime("%d %b %Y, %H:%M")
    try:        
        dob = datetime(2024, 6, 26)
        birth_time = datetime.strptime("17:24", "%H:%M").time()
        y, m, d, h, mi = get_data(dob, birth_time)
        try:
             text = f"<b>Since 26 Jun 2024</b>\n\n<b>Total Years:</b> {y}\n<b>Total Months:</b> {m}\n<b>Total Days:</b> {d}\n<b>Total Hours:</b> {h}\n<b>Total Minutes:</b> {mi}"
             await bot.edit_message_text(
                   chat_id = -1001951908326,
                   text = text,
                   message_id = 7,
                   parse_mode = enums.ParseMode.HTML
             )            
             await update.reply(f"Last Time Updated! {formatted_datetime}")
        except Exception as e:
            print(str(e))
            await update.reply(str(e))
    except Exception as e:
            print(str(e))
            await update.reply(str(e))        

@counter.on_message(filters.channel & (filters.document | filters.video))
async def forward(bot, update):
    if int(update.chat.id) == -1001150560733:
        return
    try:
        await bot.copy_message(
            chat_id=-1001150560733,
            from_chat_id=update.chat.id,
            message_id=update.id,
            caption=f"**{update.caption}**",
            parse_mode=enums.ParseMode.MARKDOWN
        )
    except Exception as e:
        print(str(e)) 
        
print('Bot Started!')     
counter.run()
