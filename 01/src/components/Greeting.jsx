import { useState } from "react";

function Greeting() {
  const [name, setName] = useState("");

  // 버튼별로 새 이름을 넘겨받아서 설정
  const handleClick = (newName) => {
    setName(newName);
    console.log("현재 이름:", newName);
  };

  return (
    <div>
      {/* <h2>안녕하세요 {name}</h2> */}
      <input type="text" placeholder="이름을 입력해주세요." value={name} onChange={(e) => setName(e.target.value)}/>

      {/* AND 연산자 */}
      {/* {name && <p>안녕하세요, {name}</p>}
      {!name && <p>이름을 입력해주세요.</p>} */}

      {/* 삼항연산자 */}
      {name ? <p>안녕하세요, {name}</p> : <p>이름을 입력해주세요.</p>}
      {/* <button onClick={() => handleClick("홍길동")}>홍길동</button>
      <button onClick={() => handleClick("김철수")}>김철수</button>
      <button onClick={() => handleClick("방문자")}>초기화</button> */}
    </div>
  );
}

export default Greeting;
