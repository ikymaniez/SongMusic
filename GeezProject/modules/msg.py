import os
from GeezProject.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello š [{}](tg://user?id={})!**\n\nš¤ I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\nā Send me /help for more info."
      HELP_MSG = [
        ".",
f"""
**Hey š Welcome back to {PROJECT_NAME}

āŖļø {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

āŖļø Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**Setting up**

1) Make bot admin
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**Commands**

**=>> Song Playing š§**

- /play: Play song using youtube music
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /dplay: Play song via deezer
- /splay: Play song via jio saavn

**=>> Playback āÆ**

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist
""",

f"""
**=>> More tools š§āš§**

- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
"""
      ]
