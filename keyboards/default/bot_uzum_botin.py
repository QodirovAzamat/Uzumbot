from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


main_markap = ReplyKeyboardMarkup(resize_keyboard=True)
main_markap.add(KeyboardButton(text="🛍Katalog"))
main_markap.row("Buyurtmalarim","Savol-javoblar")
main_markap.row("Uzumda sotish","topshirish punkitilari")