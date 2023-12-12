from config_data.config import load_config

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, BotCommand


from lexicon.lexicon import phraces

config = load_config(".env")
BOT_TOKEN = config.tg_bot.token
ADMIN_IDS = config.tg_bot.admin_ids[0]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def set_main_menu(bot: Bot):
    main_menu = [
        BotCommand(command="/mat_stat",
                   description="Ресурсы по математической статистике"),
        BotCommand(command="/lin_alg",
                   description="Ресурсы по линейной алгебре"),
        BotCommand(command="/ther_ver",
                   description="Ресурсы по теории вероятностей"),
        BotCommand(command="/mat_anal",
                   description="Ресурсы по математическому анализу"),
        BotCommand(command="/classic_ml",
                   description="Ресурсы по классическому машинному обучению"),
        BotCommand(command="/intro_to_nn",
                   description="Ресурсы по основам нейронных сетей"),
        BotCommand(command="/deep_learning",
                   description="Ресурсы по глубокому обучению")
    ]
    await bot.set_my_commands(main_menu)


@dp.message(Command(commands=["start"]))
async def index(message: Message):
    await message.answer(phraces["start"])


@dp.message(Command(commands=["mat_stat"]))
async def get_mat_stat_resources(message: Message):
    await message.answer(phraces["matStatCommand"])


@dp.message(Command(commands=["lin_alg"]))
async def get_lin_alg_resources(message: Message):
    await message.answer(phraces["linAlgCommand"])


@dp.message(Command(commands=["ther_ver"]))
async def get_ther_ver_resources(message: Message):
    await message.answer(phraces["therVerCommand"])


@dp.message(Command(commands=["mat_anal"]))
async def get_mat_anal_resources(message: Message):
    await message.answer(phraces["matAnalCommand"])


@dp.message(Command(commands=["classic_ml"]))
async def get_classic_ml_resources(message: Message):
    await message.answer(phraces["classicMlCommand"])


@dp.message(Command(commands=["intro_to_nn"]))
async def get_intro_to_nn_resources(message: Message):
    await message.answer(phraces["introToNnCommand"])


@dp.message(Command(commands=["deep_learning"]))
async def get_deep_learning_resources(message: Message):
    await message.answer(phraces["deepLearningCommand"])

if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)
