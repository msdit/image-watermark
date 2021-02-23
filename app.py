
from PIL import Image, ImageDraw, ImageFont, ImageFile, ExifTags
import glob
import random


SRC_PATH = './src/*'
DIST_PATH = './dist/'
FONT_PATH = './font.ttf'
INPUT_PATH = './input.txt'
OUTPUT_SUFFIX = 'bmbzr'
IMAGE_FORMATS = ['JPG', 'JPEG', 'PNG']
FONTSIZE_RATIO = 35


ImageFile.LOAD_TRUNCATED_IMAGES = True


f = open(INPUT_PATH, "r")
txt_val = f.readline().rstrip()
print(txt_val)
start_hour = txt_val.split(' ')[-1]
last_hour = start_hour
start_minutes = f"{random.randint(0,10):02d}"
last_minutes = start_minutes


def watermark_text(photo, index):
    global last_minutes
    global last_hour

    black = (0, 0, 0)
    red = (255, 0, 0)
    white = (255, 255, 255)

    minutes = f"{(int(last_minutes) + random.randint(1,3)):02d}"
    last_minutes = f"{(int(minutes) % 60):02d}"
    if int(minutes) >= 60:
        last_hour = f"{(int(last_hour) + 1):02d}"
    seconds = str(random.randint(10,55))
    time = f"{last_hour}:{last_minutes}:{seconds}"
    water_txt = f"{txt_val.split(' ')[0]} {time}"

    width, height = photo.size
    font = ImageFont.truetype(FONT_PATH, min(int(min(width, height) / FONTSIZE_RATIO), 20))
    text_width, text_height = font.getsize(water_txt)
    text_pos_x = int(width * 3 / 100) # int((width - text_width) / 2)
    text_pos_y = height - text_height - int(height * 3 / 100)
    padding_x = int(width / 75)
    padding_y = int(height / 100)

    rec_pos_x = text_pos_x - padding_x
    rec_pos_y = text_pos_y - padding_y
    rec_width = rec_pos_x + text_width + (2 * padding_x)
    rec_height = rec_pos_y + text_height + (3 * padding_y)

    drawing = ImageDraw.Draw(photo)
    # drawing.rectangle((rec_pos_x, rec_pos_y, rec_width, rec_height), fill=black)
    drawing.text((text_pos_x, text_pos_y), water_txt, fill=red, font=font)

    new_name = f"{OUTPUT_SUFFIX}-{water_txt.replace(' ', '-').replace('/', '-').replace(':', '-')}-{str(index)}"
    file_format = photo.format.lower()
    photo.save(f"{DIST_PATH}{new_name}.{file_format}")
    print(new_name)
    # photo.show()

if __name__ == '__main__':
    i = 0
    for filename in glob.glob(SRC_PATH):
        im=Image.open(filename)
        if im.format.upper() in IMAGE_FORMATS:
            i += 1
            watermark_text(im, i)
