# 랜덤 이미지
import cv2
import numpy as np
from PIL import Image

# 이미지 오버레이 함수
def overlay_image(target, feature, position):
    x, y = position
    h, w = feature.shape[:2]
    target[y:y + h, x:x + w] = feature
    return target

def distributor(eyes, nose, mouth, eye_dir, mouth_dir):
    base_image_path = 'image/woman2.JPG'
    target_image_path = 'image/moon_500.jpg'

    img = cv2.imread(base_image_path)

    features = {
        'eye': {'coords': [(300, 500)], 'size': (80, 45)},
        'lip': {'coords': [(407, 565)], 'size': (140, 70)},
        'nose': {'coords': [(285, 579)], 'size': (65, 125)},
    }

    # 사용자 입력: 개수 선택
    num_eyes = eyes
    num_noses = nose
    num_lips = mouth

    if not (1 <= num_eyes <= 5) or not (1 <= num_noses <= 1) or not (1 <= num_lips <= 5):
        raise ValueError("입력값이 범위를 벗어났습니다. 눈: 1-5, 코: 1, 입: 1-5")

    # 사용자 입력: 방향 선택
    eye_orientation = eye_dir.strip().lower()
    lip_orientation = mouth_dir.strip().lower()

    eye_images = []
    lip_images = []
    nose_images = []

    # 눈 이미지 생성
    for i in range(num_eyes):
        x, y = features['eye']['coords'][0]
        w, h = features['eye']['size']
        subimg = img[x:x + h, y:y + w]
        eye_images.append(cv2.resize(subimg, (50, 20)))

    # 입 이미지 생성
    for i in range(num_lips):
        x, y = features['lip']['coords'][0]
        w, h = features['lip']['size']
        subimg = img[x:x + h, y:y + w]
        lip_images.append(cv2.resize(subimg, (60, 30)))

    # 코 이미지 생성
    for i in range(num_noses):
        x, y = features['nose']['coords'][0]
        w, h = features['nose']['size']
        subimg = img[x:x + h, y:y + w]
        nose_images.append(cv2.resize(subimg, (40, 30)))

    target_image = cv2.imread(target_image_path)

    positions = []
    moon_height, moon_width = target_image.shape[:2]
    moon_x_center, moon_y_center = moon_width // 2, moon_height // 2

    # 눈 위치 설정
    if eye_orientation == 'h':
        for i in range(num_eyes):
            eye_x = moon_x_center - (50 * num_eyes // 2) + (i * 50)
            eye_y = moon_y_center - 40
            positions.append((eye_x, eye_y))
    elif eye_orientation == 'v':
        eye_start_y = moon_y_center - (30 * num_eyes // 2)
        for i in range(num_eyes):
            eye_x = moon_x_center - 25
            eye_y = eye_start_y + (i * 30)
            positions.append((eye_x, eye_y))
    else:
        raise ValueError("눈의 방향은 'h' 또는 'v'이어야 합니다.")

    # 코 위치 설정
    if num_noses > 0:
        nose_x = moon_x_center - 20
        nose_y = moon_y_center - 15
        positions.append((nose_x, nose_y))

    # 입 위치 설정
    if lip_orientation == 'h':
        for i in range(num_lips):
            lip_x = moon_x_center - (60 * num_lips // 2) + (i * 60)
            lip_y = moon_y_center + 20
            positions.append((lip_x, lip_y))
    elif lip_orientation == 'v':
        lip_start_y = moon_y_center + (30 * num_lips // 2)
        for i in range(num_lips):
            lip_x = moon_x_center - 30
            lip_y = lip_start_y - (i * 30)
            positions.append((lip_x, lip_y))
    else:
        raise ValueError("입의 방향은 'h' 또는 'v'이어야 합니다.")

    # 타겟 이미지에 특징 오버레이
    for i in range(num_eyes):
        if i < len(eye_images):
            target_image = overlay_image(target_image, eye_images[i], positions[i])

    if num_noses > 0 and len(nose_images) > 0:
        target_image = overlay_image(target_image, nose_images[0], positions[num_eyes])

    if num_lips > 0 and len(lip_images) > 0:
        for i in range(num_lips):
            target_image = overlay_image(target_image, lip_images[i], positions[num_eyes + num_noses + i])

    output_path = 'static/images/final1.jpg'
    cv2.imwrite(output_path, target_image)