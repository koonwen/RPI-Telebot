import telegram
import subprocess
import time

time.sleep(60)
bot = telegram.Bot(token="YOUR BOT TOKEN GOES HERE")
msg = subprocess.check_output("hostname -I", shell=True).decode('ascii')
status = bot.send_message(chat_id="@YOUR CHANNEL ID", text=msg, parse_mode=telegram.ParseMode.HTML)
print(status)