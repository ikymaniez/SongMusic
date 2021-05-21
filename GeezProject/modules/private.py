from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Haii.. 👋🏻 {message.from_user.first_name} Welcome To 𓊈Virtual Music𓊉\n
𝘈𝘒𝘜 𝘈𝘋𝘈𝘓𝘈𝘏 𝘉𝘖𝘛 𝘔𝘜𝘚𝘐𝘒 𝘛𝘌𝘓𝘌𝘎𝘙𝘈𝘔 𝘠𝘈𝘕𝘎 𝘋𝘐 𝘒𝘌𝘔𝘉𝘈𝘕𝘎𝘒𝘈𝘕 𝘖𝘓𝘌𝘏 : [King](https://t.me/boyfriendnice)

𝘈𝘗𝘈𝘉𝘐𝘓𝘈 𝘐𝘕𝘎𝘐𝘕 𝘔𝘌𝘕𝘎𝘎𝘜𝘕𝘈𝘒𝘈𝘕 𝘈𝘒𝘜 𝘐𝘕𝘝𝘐𝘛𝘌 𝘈𝘒𝘜 𝘋𝘈𝘕 𝘈𝘚𝘐𝘚𝘚𝘛𝘈𝘕𝘛 𝘕𝘠𝘈 𝘓𝘈𝘓𝘜 𝘑𝘈𝘋𝘐𝘒𝘈𝘕 𝘈𝘋𝘔𝘐𝘕 𝘒𝘌𝘋𝘜𝘈𝘕𝘠𝘈 𝘈𝘎𝘈𝘙 𝘉𝘐𝘚𝘈 𝘉𝘌𝘙𝘑𝘈𝘓𝘈𝘕 𝘋𝘌𝘕𝘎𝘈𝘕 𝘓𝘈𝘕𝘊𝘈𝘙, 𝘑𝘐𝘒𝘈 𝘈𝘋𝘈 𝘒𝘌𝘕𝘋𝘈𝘓𝘈 𝘉𝘐𝘚𝘈 𝘊𝘏𝘈𝘛 𝘖𝘞𝘕𝘌𝘙𝘕𝘠𝘈.
┏━━━━━━━━━━━━━━
┣ > 𝙼𝚎𝚖𝚞𝚝𝚊𝚛 𝚖𝚞𝚜𝚒𝚔 𝚍𝚒𝚐𝚛𝚞𝚙 𝚔𝚊𝚖𝚞.
┣ > 𝙱𝚒𝚜𝚊 𝚕𝚒𝚜𝚝 𝚕𝚊𝚐𝚞, 𝚌𝚞𝚖𝚊𝚗 𝚓𝚊𝚗𝚐𝚊𝚗 𝚜𝚎𝚔𝚊𝚕𝚒𝚐𝚞𝚜 𝚝𝚊𝚔𝚞𝚝 𝚎𝚛𝚛𝚘𝚛.
┣ > 𝙼𝚎𝚗𝚌𝚊𝚛𝚒 𝚍𝚊𝚗 𝚖𝚎𝚖𝚞𝚕𝚊𝚒 𝚕𝚊𝚐𝚞 𝚋𝚎𝚛𝚜𝚊𝚖𝚊 𝚝𝚎𝚖𝚊𝚗-𝚝𝚎𝚖𝚊𝚗𝚖𝚞.
┣ > 𝙼𝚎𝚗𝚌𝚊𝚛𝚒 𝚕𝚊𝚐𝚞 𝚔𝚊𝚖𝚞 𝚍𝚊𝚗 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝚕𝚊𝚐𝚞 𝚔𝚊𝚖𝚞 𝚖𝚎𝚕𝚊𝚕𝚞𝚒 𝚊𝚔𝚞.
┗━━━━━━━━━━━━━━
🤵𝓒𝓻𝓮𝓪𝓽𝓮𝓭 𝓫𝔂 : [King](https://t.me/boyfriendnice)
☘️𝓣𝓱𝓪𝓷𝓴𝓼 𝓯𝓸𝓻 : [Grup Support](https://t.me/remaja_virtual62)
━━━━━━━━━━━━━━
𝐁𝐎𝐓 𝐌𝐔𝐒𝐈𝐊 : @Virtualsongbot - 𝐀𝐒𝐈𝐒𝐒𝐓𝐀𝐍𝐓 𝐌𝐔𝐒𝐈𝐊 : @AsisstantMusicVirtual
 
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🤵Owner Music", url="https://t.me/afterdaytoxic")
                  ],[
                    InlineKeyboardButton(
                        "👥Official Group", url="https://t.me/captionanakmuda"
                    ),
                    InlineKeyboardButton(
                        "📢Official Channel", url="https://t.me/humangabutguys") 
                  ],[
                    InlineKeyboardButton(
                        "🍀Instagram", url="https://www.instagram.com/ikyyy_35"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aku sudah online, ayo kita joget ceria! 🎶**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤵Owner Music", url="https://t.me/afterdaytoxic"
                    )
                ],[
                    InlineKeyboardButton(
                        "✅ Yes!", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ No!", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**Klik tombol dibawah untuk melihat panduan menggunakan bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦇 Cara Memakai Bot Music!", url="https://t.me/humangabutguys/91577"
                    )
                ]
            ]
        ),
    )
