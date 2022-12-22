from concurrent.futures import ThreadPoolExecutor
import time
import random
import requests
import shutil
import cv2
import imutils
from PIL import Image

img_names = [
    'pexels-arthouse-studio-4534200.jpg',
    'pexels-fauxels-3183132.jpg',
    'pexels-fauxels-3183198.jpg',
    'pexels-lumn-167699.jpg',
    'pexels-maxime-francis-2246476.jpg',
    'pexels-piccinng-3075993.jpg',
    'pexels-roberto-nickson-2559941.jpg',
    'pexels-stefan-stefancik-919606.jpg',
    'pexels-tan-danh-1329711.jpg',
    'pexels-tim-mossholder-1000653.jpg'
]


def study(img_name):
    # img = requests.get('https://drive.google.com/drive/folders/1QE2zttYTayBjrTdOcpHySq3X5tyREsvG?usp=sharing/'+img_name, stream=True)
    # with open('./dump/'+img_name+'.jpg', 'wb') as out_file:
    #     shutil.copyfileobj(img.raw, out_file)
    # del img
    # print(img.status_code)
    # if img.status_code == 200:
    #     with open('./dump/'+img_name, 'wb') as f:
    #         shutil.copyfileobj(img.raw, f)
    # del img
    # print(f'{img_name} is studying ...')
    # time.sleep(1)
    # for img_name in img_names:
        img = Image.open("./images/"+img_name) 
        img = img.rotate(180) 
        width, height = img.size
        area = (0, 0, width/2, height/2)
        img = img.crop(area)
        width, height = img.size
        img = img.resize((width//2, height//2))
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img.save("./dump/"+img_name)
        time.sleep(1)


if __name__ == '__main__':
    t1 = time.perf_counter()
    for img_name in img_names:
        study(img_name)
    t2 = time.perf_counter()
    print(f'Finished in {t2-t1} seconds')
    
    t1 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=10) as executor:
        for img_name in img_names:
            future = executor.submit(study,img_name)
    t2 = time.perf_counter()
    print(f'Finished in {t2-t1} seconds')
