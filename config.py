from dotenv import load_dotenv
import os
load_dotenv()
# путь к базе данных
DB_PATH = "database.db"
# этот токен нужно получить при создании бота у @BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN")


# поддерживаемые команды
DEFAULT_COMMANDS = (
    ("newtask", "Создать задачу"),
    ("tasks", "Последние 10 задач"),
    ("today", "Задачи на сегодня"),
)

# формат назначенной даты у задачи
DATE_FORMAT = "%d.%m.%Y"
