from aiogram import Bot, Dispatcher, executor, types
from decouple import config
import random, os

bot = Bot(config("API_TOKEN"))
dp = Dispatcher(bot)

Category = {
    "людей": "people",
    "людьми": "people",
    "космосу": "space",
    "космоса": "space",
    "природи": "nature",
    "природою": "nature"
}

def list_images(folder):
    img_list = []
    try:
        for file in os.listdir(folder):
            files, extension = file.rsplit('.', 1)
            if extension.lower() in {'jpg'}:
                img_list.append(os.path.join(folder, file))
    except FileNotFoundError:
        pass
    return img_list

@dp.message_handler(lambda message: any(user_message in message.text.lower() for user_message in Category))
async def send_image(message: types.Message):
    for user_message, folder in Category.items():
        if user_message in message.text.lower():
            img_list = list_images(folder)
            if img_list:
                image = random.choice(img_list)
                with open(image, 'rb') as img_file:
                    await bot.send_photo(message.chat.id, img_file)
            break

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



