const timer = document.getElementById('timer');
const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');

let startTime = null;
let elapsedTime = 0;
let timerInterval = null;

function updateTimer() {
  const currentTime = Date.now();
  elapsedTime = currentTime - startTime;

  const seconds = Math.floor((elapsedTime / 1000) % 60);
  const minutes = Math.floor((elapsedTime / (1000 * 60)) % 60);
  const hours = Math.floor((elapsedTime / (1000 * 60 * 60)) % 24);

  timer.textContent = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

startBtn.addEventListener('click', () => {
  if (timerInterval) return; // 이미 실행 중인 경우 무시

  startTime = Date.now() - elapsedTime;
  timerInterval = setInterval(updateTimer, 1000);
  startBtn.textContent = 'Pause';
});

stopBtn.addEventListener('click', () => {
  clearInterval(timerInterval);
  timerInterval = null;
  startBtn.textContent = 'Resume';
});