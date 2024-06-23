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
    session_string="BQFB0bwAHkBGbCMScZNdpdnPVoVr0xeNEmdivl6Xc0Q-UnSoq_RZYs97oiE7HkrvWzGpVsaoozflUOcQYGQaLMfrEqvYgu3n525lY83iK11IbJCy2qTFB8KFveonuTHZqzhi7Q-hNwYycdil-Fw0nxIP_IorjGoAlDyN4bnVmR1LGE1tkPfcQ0ND5HcfXe775dq9B31UUX87CkOmTmuMi2t1oAoIVkkbYrqmbmUMHCuJUQDKvJlLcFSYRCDshVtJ1wWvBvKdysMcQdQR3RrIhAAD2QITtyr9q9ZDP2A1V6tm8oHsPFcpTwOh5x4Q3jFDu1liWX8qER8jWDdKq6cHaS_bcCoTEAAAAAFvBwX2AA"
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
