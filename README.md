# 24_2_KUCCTHON_4
## 외계인 심리 테스트: '내가 외계인으로 태어난다면?'
> "우주" 라는 해커톤 주제에 맞춘 개인 성향을 반영한 맞춤형 심리 테스트
<img src="https://github.com/user-attachments/assets/3af01b2e-9d48-4d4a-b0da-54a75b230bfd" width="200" height="200"/>

## 🪐 프로젝트 소개
**"우주"** 라는 해커톤 주제에 맞춰, 사용자에게 개인 맞춤형 외계인 캐릭터를 제공하는 심리 테스트를 개발하였다.<br/>
현대인의 자기 이해에 대한 관심을 반영하여 질문을 구성하였으며, 사용자가 답변을 통해 자신을 돌아볼 수 있도록 하였다.<br/>
본 테스트는 5단계의 평가 척도를 통해 다양한 질문에 답변하도록 하며, 개인의 성향을 기반으로 한 맞춤형 이미지를 제공한다.<br/>

**유형은 두 가지로 구분된다:**<br/>
1️⃣ *생성형 AI를 활용해 설문 결과에 따라 외형적 특성을 반영한 이미지*<br/>
2️⃣ *OpenCV를 사용해 설문 결과를 수치화하고 외부 기관의 개수를 표현한 이미지*

## 🚀 주요 기능

- 성향 분석 설문: 사용자는 5단계 평가 척도로 다양한 질문에 응답<br/>
- 맞춤형 이미지 생성: 생성형 AI와 OpenCV를 활용한 이미지

## 🛠 코드
OpenCV를 활용한 맞춤형 이미지 생성
1. 눈 이미지 생성
~~~
for i in range(num_eyes):
    x, y = features['eye']['coords'][0]
    w, h = features['eye']['size']
    subimg = img[x:x + h, y:y + w]
    eye_images.append(cv2.resize(subimg, (50, 20)))
~~~
2. 눈 위치 설정
~~~
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
~~~
3. 타겟 이미지에 특징 오버레이
~~~
for i in range(num_eyes):
    if i < len(eye_images):
        target_image = overlay_image(target_image, eye_images[i], positions[i])
if num_noses > 0 and len(nose_images) > 0:
    target_image = overlay_image(target_image, nose_images[0], positions[num_eyes])

if num_lips > 0 and len(lip_images) > 0:
    for i in range(num_lips):
        target_image = overlay_image(target_image, lip_images[i], positions[num_eyes + num_noses + i])
~~~
## 🖥 데모
<img src="https://github.com/user-attachments/assets/2e8e3656-79bb-4070-9dde-2201e95863b8" width="400" height="360"/>
<img src="https://github.com/user-attachments/assets/7db6880b-22a6-49f6-9a72-fb772c84b1f3" width="400" height="360"/>
<img src="https://github.com/user-attachments/assets/b926378b-c07f-4afc-91e3-679bf2953bb1" width="400" height="360"/>
<img src="https://github.com/user-attachments/assets/6552b6ed-7805-42c1-8d97-7669fe165fe1" width="400" height="360"/>



## 🗣 멤버
김혜미 / 이수형 / 채수 / 김지원
