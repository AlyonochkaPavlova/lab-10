from PIL import Image
img = Image.open('hh.jpg')
x1, y1, x2, y2 = 20, 40 , img.width, img.height
cropped_img = img.crop((x1, y1, x2, y2))
cropped_img.save('cropped_image.jpg')
print("Изображение обрезано и сохранено как 'cropped_image.jpg'.")