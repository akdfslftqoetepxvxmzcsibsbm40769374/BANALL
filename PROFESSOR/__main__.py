import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER = os.getenv("OWNER")

# pyrogram client
app = Client(
            "banall",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)

@app.on_message(
filters.command("start")
& filters.private            
)
async def start_command(client, message: Message):
  await message.reply_photo(
                            photo = f"https://telegra.ph/file/6a8872f745a225cb08dc5.jpg",
                            caption = f"⿕ ʜᴇʏ ɪ ᴀᴍ ᴀ ʙᴀɴ ᴀʟʟ ʙᴏᴛ ⿕\n➲ ᴀʟᴡᴀʏs 101% ᴡᴏʀᴋɪɴɢ & ᴜsᴇ\n⦿ ғʀɪsᴛ ᴀᴅᴅ ᴍᴇ ᴀ ᴀɴʏ ɢʀᴏᴜᴘ\n⦿ ɴᴏᴡ ɢɪᴠᴇ ʙᴀɴ ᴘᴏᴡᴇʀ ᴏᴜʀ ʙᴏᴛ\n⦿ ᴛʜᴇɴ ᴄᴏᴍᴇ ʙᴀᴄᴋ ɪɴ ɢʀᴏᴜᴘ\n⦿ /BANALL ( sᴇɴᴅ ɪɴ ɢʀᴏᴜᴘ )\n\n⦿ ʏᴏᴜʀ ᴡᴏʀᴋ ᴅᴏɴᴇ ᴜsᴇ ʙᴀɴ sᴛᴀʀᴛ",
  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⦿ ɪ'ᴍ ʀᴇᴀᴅʏ ғᴏʀ ғᴜᴄᴋɪɴɢ ⦿", url="https://t.me/Grp_banall_probot?startgroup=True&admin=ban_users")
                ],
                [
                    InlineKeyboardButton("⦿ sᴜᴘᴘᴏʀᴛ ⦿", url="https://t.me/PROFESSORxNETWORK"),
                    InlineKeyboardButton("⦿ ᴜᴘᴅᴀᴛᴇ ⦿", url="https://t.me/PROFESSOR_NETWORK")
                ],
                [
                    InlineKeyboardButton("⦿ ʀᴇᴘᴏ ⦿", url="https://t.me/PrivateBotRepo"),
                    InlineKeyboardButton("⦿ ᴘʀᴏғᴇssᴏʀ ⦿", url="https://t.me/SOURABH_100RABH")
            ],       
           ]
      )
)

@app.on_message(
filters.command("banall") 
& filters.group
)
async def banall_command(client, message: Message):
    print("getting memebers from {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id = message.chat.id, user_id = i.user.id)
            print("kicked {} from {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("failed to kicked {} from {}".format(i.user.id, e))           
    print("process completed")
    

# start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()
