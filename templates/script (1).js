const questions = [
  "���� ��ü���� ���簨�� �巯���� �;��Ѵ�.",
  "���� ����ǥ���� ������.",
  "���� ���� ���� �� ����ش�.",
  "���� ���� �Ӹ��� ������ ���� ���̶�� �����Ѵ�.",
  "��� �󱼰� �̸��� �� ��Ī��Ű�°�?"
];

let currentQuestionIndex = 0;
const responses = []; // �� ������ �亯 ������ ����

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
    alert("�亯�� �������ּ���.");
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
  alienContainer.innerHTML = '<img src="images/�ܰ������鼦.png" alt="�ܰ������鼦" id="baseAlien">'; // �⺻ �ܰ��� �̹���

  // �� ����
  for (let i = 0; i < responses[0]; i++) {
    const nose = document.createElement("div");
    nose.className = "feature nose";
    nose.style.left = `${48 + i * 5}%`; // �� ��ġ ����
    alienContainer.appendChild(nose);
  }

  // �� ����
  const mouth = document.createElement("div");
  mouth.className = "feature mouth";
  mouth.style.width = `${30 + (5 - responses[1]) * 10}px`; // ������ ���� �� ũ�� ����
  alienContainer.appendChild(mouth);

  // �� ����
  const leftEar = document.createElement("div");
  leftEar.className = "feature ear left-ear";
  leftEar.style.width = `${10 + responses[2] * 5}px`;
  alienContainer.appendChild(leftEar);

  const rightEar = document.createElement("div");
  rightEar.className = "feature ear right-ear";
  rightEar.style.width = `${10 + responses[2] * 5}px`;
  alienContainer.appendChild(rightEar);

  // �Ӹ� ����
  for (let i = 0; i < responses[3]; i++) {
    const head = document.createElement("div");
    head.className = "feature head";
    head.style.top = `${10 + i * 5}%`;
    head.style.left = `${40 + i * 10}%`;
    alienContainer.appendChild(head);
  }

  // �� ����
  for (let i = 0; i < responses[4]; i++) {
    const eye = document.createElement("div");
    eye.className = "feature eye";
    eye.style.left = `${35 + i * 5}%`;
    alienContainer.appendChild(eye);
  }
}
