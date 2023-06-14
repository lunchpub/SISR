from PIL import Image, ImageFile
from tqdm import tqdm
import os

ImageFile.LOAD_TRUNCATED_IMAGES = True

raw_path = 'C:/Users/drew/Projects/SISR/VSAIv1/split_ss_444_lsv/train/images' # 원본 이미지 경로
token_list = os.listdir(raw_path) # 원본 이미지 경로 내 폴더들 list
data_path = 'C:/Users/drew/Projects/SISR/VSAIv1/train_X4'  # 저장할 이미지 경로

# resize 시작 --------------------
for token in token_list:
#원본 이미지 경로와 저장할 경로 이미지 지정
    image_path = raw_path + '/'
    save_path = data_path + '/'

  # 저장할 경로 없으면 생성
    if not os.path.exists(save_path):
        os.mkdir(save_path)

  #원본 이미지 경로의 모든 이미지 list 지정
data_list = os.listdir(image_path)
print(len(data_list))

  # 모든 이미지 resize 후 저장하기
for name in tqdm(data_list):
      # 이미지 열기
    im = Image.open(image_path + name)

      # 이미지 resize
    im = im.resize((256, 256))

      # 이미지 JPG로 저장
    im.save(save_path + name)
print('end ::: ' + token)