// Countdown.jsx
import { useState, useEffect } from "react";

function Countdown() {
  const [seconds, setSeconds] = useState(10);   // 남은 시간
  const [isRunning, setIsRunning] = useState(false); // 타이머 동작 여부

  useEffect(() => {
    // 동작 중이 아니면 타이머 설정 안 함
    if (!isRunning) return;

    const id = setInterval(() => {
      setSeconds((prev) => {
        if (prev <= 1) {
          // 0이 되면 멈추고 "시간 종료!"
          clearInterval(id);
          setIsRunning(false);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    // 컴포넌트 언마운트 or isRunning 변경 시 타이머 정리
    return () => clearInterval(id);
  }, [isRunning]);

  const handleStart = () => {
    if (seconds === 0) return;       // 이미 0이면 시작 안 함
    setIsRunning(true);
  };

  const handlePause = () => {
    setIsRunning(false);
  };

  const handleReset = () => {
    setIsRunning(false);
    setSeconds(10);                  // 다시 10초로 초기화
  };

  return (
    <div>
      <h2>카운트다운 타이머</h2>

      <div style={{ fontSize: "32px", marginBottom: "8px" }}>
        {seconds}s
      </div>

      {seconds === 0 && <p>시간 종료!</p>}

      <button onClick={handleStart} disabled={isRunning || seconds === 0}>
        시작
      </button>
      <button onClick={handlePause} disabled={!isRunning}>
        정지
      </button>
      <button onClick={handleReset}>리셋</button>
    </div>
  );
}

export default Countdown;
