const questions = [
  "나는 단체에서 존재감을 드러내고 싶어한다.",
  "나는 감정표현에 서툴다.",
  "나는 남의 말을 잘 들어준다.",
  "나는 내가 머리가 나쁘진 않은 편이라고 생각한다.",
  "사람 얼굴과 이름을 잘 매칭시키는가?"
];

let currentQuestionIndex = 0;
const responses = []; // 각 질문의 답변 점수를 저장

function showNext(nextId) {
  document.getElementById("story1").classList.add("hidden");
  document.getElementById("story2").classList.add("hidden");
  document.getElementById("test").classList.add("hidden");
  document.getElementById("resultScreen").classList.add("hidden");

  document.getElementById(nextId).classList.remove("hidden");
}

function nextQuestion() {
  const radios = document.getElementsByName('q1');
  let answerSelected = false;

  for (let i = 0; i < radios.length; i++) {
    if (radios[i].checked) {
      answerSelected = true;
      responses.push(parseInt(radios[i].value));
      radios[i].checked = false;
      break;
    }
  }

  if (!answerSelected) {
    alert("답변을 선택해주세요.");
    return;
  }

  currentQuestionIndex++;
  if (currentQuestionIndex < questions.length) {
    document.getElementById('questionText').textContent = questions[currentQuestionIndex];
  } else {
    showResults();
  }
}

function showResults() {
  document.getElementById('test').classList.add('hidden');
  document.getElementById('resultScreen').classList.remove('hidden');
  generateAlien();
}

function generateAlien() {
  const alienContainer = document.getElementById("alienImage");
  alienContainer.innerHTML = '<img src="images/외계인정면샷.png" alt="외계인정면샷" id="baseAlien">'; // 기본 외계인 이미지

  // 코 생성
  for (let i = 0; i < responses[0]; i++) {
    const nose = document.createElement("div");
    nose.className = "feature nose";
    nose.style.left = `${48 + i * 5}%`; // 코 위치 조정
    alienContainer.appendChild(nose);
  }

  // 입 생성
  const mouth = document.createElement("div");
  mouth.className = "feature mouth";
  mouth.style.width = `${30 + (5 - responses[1]) * 10}px`; // 점수에 따라 입 크기 조정
  alienContainer.appendChild(mouth);

  // 귀 생성
  const leftEar = document.createElement("div");
  leftEar.className = "feature ear left-ear";
  leftEar.style.width = `${10 + responses[2] * 5}px`;
  alienContainer.appendChild(leftEar);

  const rightEar = document.createElement("div");
  rightEar.className = "feature ear right-ear";
  rightEar.style.width = `${10 + responses[2] * 5}px`;
  alienContainer.appendChild(rightEar);

  // 머리 생성
  for (let i = 0; i < responses[3]; i++) {
    const head = document.createElement("div");
    head.className = "feature head";
    head.style.top = `${10 + i * 5}%`;
    head.style.left = `${40 + i * 10}%`;
    alienContainer.appendChild(head);
  }

  // 눈 생성
  for (let i = 0; i < responses[4]; i++) {
    const eye = document.createElement("div");
    eye.className = "feature eye";
    eye.style.left = `${35 + i * 5}%`;
    alienContainer.appendChild(eye);
  }
}
