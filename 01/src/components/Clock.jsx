// Clock.jsx
import { useState, useEffect } from "react";

function Clock() {
  // 현재 시간 문자열 상태
  const [time, setTime] = useState(
    new Date().toLocaleTimeString("ko-KR", { hour12: false })
  );

  useEffect(() => {
    // 1초마다 현재 시간 갱신
    const timerId = setInterval(() => {
      setTime(new Date().toLocaleTimeString("ko-KR", { hour12: false }));
    }, 1000);

    // 컴포넌트가 사라질 때 타이머 정리
    return () => clearInterval(timerId);
  }, []); // []: 처음 마운트될 때만 setInterval 설정

  return (
    <div>
      <h2>디지털 시계</h2>
      <p>{time}</p>
    </div>
  );
}

export default Clock;
