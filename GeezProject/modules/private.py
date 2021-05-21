import logging
from GeezProject.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from GeezProject.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
       f"""<b>Haii.. 👋🏻 {message.from_user.first_name} Welcome To 𓊈Virtual Music𓊉\n
Aku Adalah Bot Music Telegram Yang Akan Menemani mu Di Voice Call Group.
Jika Ingin Menggunakan Invite Aku Dan Asisstantnya Ke Dalam Group Lalu Angkat Bot Menjadi Admin. Jika Ada Kendala Bisa Chat Pemilik Nya.
┏━━━━━━━━━━━━━━
┣ > 𝙼𝚎𝚖𝚞𝚝𝚊𝚛 𝚖𝚞𝚜𝚒𝚔 𝚍𝚒𝚐𝚛𝚞𝚙 𝚔𝚊𝚖𝚞.
┣ > 𝙱𝚒𝚜𝚊 𝚕𝚒𝚜𝚝 𝚕𝚊𝚐𝚞, 𝚌𝚞𝚖𝚊𝚗 𝚓𝚊𝚗𝚐𝚊𝚗 𝚜𝚎𝚔𝚊𝚕𝚒𝚐𝚞𝚜 𝚝𝚊𝚔𝚞𝚝 𝚎𝚛𝚛𝚘𝚛.
┣ > 𝙼𝚎𝚗𝚌𝚊𝚛𝚒 𝚍𝚊𝚗 𝚖𝚎𝚖𝚞𝚕𝚊𝚒 𝚕𝚊𝚐𝚞 𝚋𝚎𝚛𝚜𝚊𝚖𝚊 𝚝𝚎𝚖𝚊𝚗-𝚝𝚎𝚖𝚊𝚗𝚖𝚞.
┣ > 𝙼𝚎𝚗𝚌𝚊𝚛𝚒 𝚕𝚊𝚐𝚞 𝚔𝚊𝚖𝚞 𝚍𝚊𝚗 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝚕𝚊𝚐𝚞 𝚔𝚊𝚖𝚞 𝚖𝚎𝚕𝚊𝚕𝚞𝚒 𝚊𝚔𝚞.
┗━━━━━━━━━━━━━━
🤵𝓒𝓻𝓮𝓪𝓽𝓮𝓭 𝓫𝔂 : [King](https://t.me/boyfriendnice)
☘️𝓣𝓱𝓪𝓷𝓴𝓼 𝓯𝓸𝓻 : [Grup Support](https://t.me/Familythunder)
━━━━━━━━━━━━━━
𝐁𝐎𝐓 𝐌𝐔𝐒𝐈𝐊 : @Virtualsong_bot - 𝐀𝐒𝐈𝐒𝐒𝐓𝐀𝐍𝐓 𝐌𝐔𝐒𝐈𝐊 : @AsisstantMusicVirtual
         
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🤵 Owner Music", url="https://t.me/boyfriendnice")
                  ],[
                    InlineKeyboardButton(
                        "👥 Official Group", url="https://t.me/Familythunder"
                    ),
                    InlineKeyboardButton(
                        "📢 Official Channel", url="https://t.me/MusikManagement") 
                  ],[
                    InlineKeyboardButton(
                        "🍀 Instagram", url="https://www.instagram.com/ikyyy_35"
                    )
                ]
            ]
        ),
     reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**🔴 {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👥 Support Group", url="https://t.me/Familythunder"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️Next', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("🤵 Owner Music", url="https://t.me/boyfriendnice")
            [InlineKeyboardButton(text = '👥 Support Group', url="https://t.me/Familythunder"
             InlineKeyboardButton(text = '📢 Support Channel', url="https://t.me/MusikManagement"
            [InlineKeyboardButton(text = '🍀 Instagram', url="https://www.instagram.com/ikyyy_35"
            [InlineKeyboardButton(text = '◀️Undo', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️Undo', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️Next', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""<b>Haii.. 👋🏻 {message.from_user.first_name} Welcome To 𓊈Virtual Music𓊉\n
Aku Adalah Bot Music Telegram Yang Akan Menemani mu Di Voice Call Group.
Jika Ingin Menggunakan Invite Aku Dan Asisstantnya Ke Dalam Group Lalu Angkat Bot Menjadi Admin. Jika Ada Kendala Bisa Chat Pemilik Nya.
┏━━━━━━━━━━━━━━
┣ > 𝙼𝚎𝚖𝚞𝚝𝚊𝚛 𝚖𝚞𝚜𝚒𝚔 𝚍𝚒𝚐𝚛𝚞𝚙 𝚔𝚊𝚖𝚞.
┣ > 𝙱𝚒𝚜𝚊 𝚕𝚒𝚜𝚝 𝚕𝚊𝚐𝚞, 𝚌𝚞𝚖𝚊𝚗 𝚓𝚊𝚗𝚐𝚊𝚗 𝚜𝚎𝚔𝚊𝚕𝚒𝚐𝚞𝚜 𝚝𝚊𝚔𝚞𝚝 𝚎𝚛𝚛𝚘𝚛.
┣ > 𝙼𝚎𝚗𝚌𝚊𝚛𝚒 𝚍𝚊𝚗 𝚖𝚎𝚖𝚞𝚕𝚊𝚒 𝚕𝚊𝚐𝚞 𝚋𝚎𝚛𝚜𝚊𝚖𝚊 𝚝𝚎𝚖𝚊𝚗-𝚝𝚎𝚖𝚊𝚗𝚖𝚞.
┣ > 𝙼𝚎𝚗𝚌𝚊𝚛𝚒 𝚕𝚊𝚐𝚞 𝚔𝚊𝚖𝚞 𝚍𝚊𝚗 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝚕𝚊𝚐𝚞 𝚔𝚊𝚖𝚞 𝚖𝚎𝚕𝚊𝚕𝚞𝚒 𝚊𝚔𝚞.
┗━━━━━━━━━━━━━━
🤵𝓒𝓻𝓮𝓪𝓽𝓮𝓭 𝓫𝔂 : [King](https://t.me/boyfriendnice)
☘️𝓣𝓱𝓪𝓷𝓴𝓼 𝓯𝓸𝓻 : [Grup Support](https://t.me/Familythunder)
━━━━━━━━━━━━━━
𝐁𝐎𝐓 𝐌𝐔𝐒𝐈𝐊 : @Virtualsong_bot - 𝐀𝐒𝐈𝐒𝐒𝐓𝐀𝐍𝐓 𝐌𝐔𝐒𝐈𝐊 : @AsisstantMusicVirtual
         
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ Click here for help", url=f"https://t.me/{BOT_USERNAME}?start"
                    )
                ]
            ]
        ),
    )

