from PIL import Image
holiday_cards = {
    "Новый год": "hny.jpg",
    "День рождения": "hb.jpg",
    "День святого Валентина": "hvd.jpg",
}
holiday = input("Введите название праздника: ")
if holiday in holiday_cards:
    img = Image.open(holiday_cards[holiday])
    img.show()
else:
    print("Открытка для этого праздника не найдена.")