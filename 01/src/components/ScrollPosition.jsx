// ScrollPosition.jsx
import { useState, useEffect } from "react";

function ScrollPosition() {
  const [y, setY] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      setY(window.scrollY); // 현재 스크롤 위치(px)
    };

    window.addEventListener("scroll", handleScroll);
    handleScroll(); // 처음 렌더링 시 현재 위치도 반영

    // 컴포넌트가 사라질 때 리스너 제거
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <div
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        right: 0,
        padding: "8px 16px",
        background: "rgba(15, 23, 42, 0.9)",
        color: "#f9fafb",
        fontSize: "14px",
        zIndex: 9999,
      }}
    >
      현재 스크롤 위치: {Math.round(y)}px
    </div>
  );
}

export default ScrollPosition;
