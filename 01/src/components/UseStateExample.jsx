import { useState } from "react";

function UseStateExample() {
  //   let count = 0;
  const [count, setCount] = useState(0);

  const increase = () => {
    // count = count + 1;
    setCount((pre) => pre + 1);
    console.log(count);
  };

  const decrease = () => {
    setCount((pre) => pre - 1);
    console.log(count);
  };

  const reset = () => {
    setCount(pre => 0);
    console.log(count);
  };

  const double = () => {
    setCount((pre) => pre * 2);
    console.log(count);
  };

  return (
    <div>
      <p>{count}</p>
      <button onClick={increase}>증가</button>

      <button onClick={decrease}>감소</button>

      <button onClick={reset}>초기화</button>

      <button onClick={double}>2배증가</button>
    </div>
  );
}

export default UseStateExample;