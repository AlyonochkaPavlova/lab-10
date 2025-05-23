from PIL import Image, ImageDraw, ImageFont
holiday_cards = {
    "Новый год": "hny.jpg",
    "День рождения": "hb.jpg",
    "День святого Валентина": "hvd.jpg",
}
holiday = input("Введите название праздника: ")
if holiday in holiday_cards:
    name = input("Введите имя того, кого хотите поздравить: ")
    img = Image.open(holiday_cards[holiday])
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 40)
    text = f"{name}, поздравляю!"
    draw.text((100,100), text, font = font, fill=(255, 0, 0))
    img.save('new_card.png')
    print("Новая открытка сохранена как 'new_card.png'.")
else:
    print("Открытка для этого праздника не найдена.")
