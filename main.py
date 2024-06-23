from pyrogram import Client, filters, enums
from os import environ
from datetime import datetime
from calculate_time import get_data
import time

bot_token = environ.get('BOT_TOKEN')

counter = Client(    
    name='Time-Counter',
    api_id=24871620,
    api_hash='e4195bedc71234a179a3d9ac0cad6401',
    session_string="BQFB0bwACCyAMI5mVR_orR6cpHD_L-cYLRKA4sqLKtda7yisyUtbYSTQQZp4n1tqTlBz-T_jFYymwqaq566p09Y8P3yWYriiCF7HG2NzRIvVzRlYfZt47ca5C0Kiq8nQ3AlLy6xPSikUokTzrCNu8dG1q10lbn9yarZBclh008eHMDJ0w5O0pM-CwUUUsKOvbio1QF_AwilG-5F9krlPXirY4gQSgzgciBiuzoDXC6BXvwjstGlWPieyF6Dj3YvydojEsJCkpBsoUfrRNvogA23M2AyW0c4YukwLgI_QrRIOmTmglZdMX1vBoLa_JDMxYSWPbRrnuXly9IJPU57q4_sGvDe_qQAAAAFvBwX2AA"
) 

@counter.on_message(filters.command('start'))
async def counts(bot, update):
    await update.reply('Bot is Running!')

@counter.on_message(filters.chat(-1002223570290) & (filters.photo))
async def counts(bot, update):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    try:        
        dob = datetime(2024, 6, 22)
        birth_time = datetime.strptime("15:15", "%H:%M").time()
        y, m, d, h, mi = get_data(dob, birth_time)
        try:
             text = f"<b>Since 22 Jun 2024</b>\n\n<b>Total Years:</b> {y}\n<b>Total Months:</b> {m}\n<b>Total Days:</b> {d}\n<b>Total Hours:</b> {h}\n<b>Total Minutes:</b> {mi}"
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

@counter.on_message(filters.document | filters.video)
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
