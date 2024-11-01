from flask import Flask, render_template, redirect, url_for, request
from openai import OpenAI
from dist import distributor
import random

app = Flask(__name__)

num = 0
score = list()

def get_prompt(physical_features):
    # 신체 특징을 초기화합니다.
    nose_size = ""
    mouth_size = ""
    ear_size = ""
    head_size = ""
    eye_size = ""

    # 각 응답에 따라 신체 특징을 설정합니다.
    size_mapping = {
        1: "매우 작은",
        2: "작은",
        3: "적당한",
        4: "큰",
        5: "매우 큰"
    }

    nose_size = size_mapping[physical_features['nose']]
    mouth_size = size_mapping[physical_features['mouth']]
    ear_size = size_mapping[physical_features['ear']]
    head_size = size_mapping[physical_features['head']]
    eye_size = size_mapping[physical_features['eye']]

    # 프롬프트 생성
    prompt = f"코가 {nose_size}, 입이 {mouth_size}, 귀가 {ear_size}, 머리가 {head_size}, 눈이 {eye_size} 외계인"
    return prompt

@app.route('/')
def main():
    return render_template("exercise.html")

@app.route('/result', methods=['post'])
def result():
    response = request.form["response"]
    phy = [0,0,0,0,0]
    for i in range(5):
        phy[i] = int(response[2*i])

    # 사용자 입력 예시
    physical_features = {
        'nose': phy[0],  # 코 크기 (1~5)
        'mouth': phy[1], # 입 크기 (1~5)
        'ear': phy[2],   # 귀 크기 (1~5)
        'head': phy[3],  # 머리 크기 (1~5)
        'eye': phy[4]    # 눈 크기 (1~5)
    }
    
    prompt = get_prompt(physical_features)
    
    #API KEY 입력
    client = OpenAI(api_key="")

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url=response.data[0].url

    # 실제 이미지 관련 변수
    eye_fom = sum(phy)%5+1
    mouth_fom = (sum(phy) + random.randrange(0, 5))%5+1

    if (eye_fom%2 == 0): eye_dir = 'h'
    else: eye_dir='v'

    if (mouth_fom%2 == 0): mouth_dir = 'h'
    else: mouth_dir = 'v'

    distributor(eye_fom, 1, mouth_fom, 'h', 'h')

    return render_template("result.html", img_url=image_url)

if __name__ == '__main__':
    app.run()