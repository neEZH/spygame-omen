import bot
from dbModel import create_tables
create_tables()
print("tables created")
print("bot started")
bot.tbot.infinity_polling()
