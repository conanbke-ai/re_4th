# React 소개

## React란?

**React**는 Facebook(현 Meta)에서 2013년 개발한 **JavaScript UI 라이브러리**입니다.

### 핵심 개념
- **사용자 인터페이스(UI)를 만들기 위한 도구**
- **JSX 문법**: HTML처럼 생겼지만 JavaScript의 강력함을 가진 문법
- **SPA(Single Page Application)**: 페이지 전체를 새로고침하지 않고 필요한 부분만 업데이트
- **현재 가장 인기 있는 프론트엔드 라이브러리** 중 하나

---

## 기존 JavaScript 방식의 문제점

바닐라 JavaScript(또는 jQuery)로 개발할 때의 문제점:

❌ **코드가 여기저기 흩어져 있어 관리하기 어려움**
- HTML, CSS, JavaScript가 각각 분리되어 있어 관련 코드를 찾기 힘듦

❌ **UI 상태를 직접 조작해야 함 (명령적 프로그래밍)**
- DOM 요소를 직접 선택하고 수정해야 함
- 예: `document.querySelector()`, `element.innerHTML = ...`

❌ **버그가 생기면 어디서 문제가 생겼는지 찾기 어려움**
- 여러 곳에서 같은 DOM을 조작하면 추적이 어려움

❌ **코드가 길어지면 유지보수가 복잡해짐**
- 스파게티 코드 발생

---

## React를 사용하면?

React를 사용했을 때의 장점:

✅ **상태가 변경되면 React가 자동으로 UI를 업데이트**
- 개발자는 상태만 관리하면 됨

✅ **관련 코드가 한 곳(컴포넌트)에 모여 있어 이해하기 쉬움**
- 컴포넌트 단위로 코드가 구조화됨

✅ **"UI가 어떻게 보여야 하는지"만 선언하면 됨 (선언적 프로그래밍)**
- "어떻게(How)"가 아닌 "무엇을(What)" 보여줄지에 집중

✅ **컴포넌트 재사용으로 개발 속도 향상**
- 한 번 만든 컴포넌트를 여러 곳에서 사용 가능

---

## 명령적 vs 선언적 프로그래밍 비교

### 명령적 프로그래밍 (바닐라 JS)
```javascript
// "어떻게(How)" 할지 단계별로 명령
const button = document.createElement('button');
button.textContent = '클릭';
button.addEventListener('click', () => {
  const count = parseInt(button.dataset.count || 0);
  button.dataset.count = count + 1;
  document.querySelector('#count').textContent = count + 1;
});
document.body.appendChild(button);
```

### 선언적 프로그래밍 (React)
```javascript
// "무엇을(What)" 보여줄지만 선언
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>카운트: {count}</p>
      <button onClick={() => setCount(count + 1)}>클릭</button>
    </div>
  );
}
```

---

## 다음 단계

React의 주요 특징들을 더 자세히 알아보려면 [02-react-features.md](./02-react-features.md)를 참고하세요.

# React의 주요 특징

React를 특별하게 만드는 6가지 핵심 특징에 대해 알아봅니다.

---

## 1️⃣ 컴포넌트 기반 개발 (Component-Based)

### 개념
**레고 블록처럼 작은 조각(컴포넌트)을 조합하여 복잡한 UI를 만듭니다.**

### 비유
- 레고 블록 하나하나 = 컴포넌트
- 완성된 작품 = 애플리케이션
- 각 블록은 독립적이고, 여러 블록들을 조합하면 큰 구조물을 만들 수 있음

### 장점
- ✅ **재사용 가능**: Button 컴포넌트를 만들면 어디서든 사용 가능
- ✅ **관리 용이**: 각 컴포넌트는 독립적으로 자기 역할만 수행
- ✅ **협업 효율**: 팀원 A는 Header, 팀원 B는 Footer 작업 가능
- ✅ **테스트 간편**: 각 컴포넌트를 독립적으로 테스트 가능

### 예시
```jsx
// Button 컴포넌트 정의
function Button({ text, onClick }) {
  return <button onClick={onClick}>{text}</button>;
}

// 여러 곳에서 재사용
function App() {
  return (
    <div>
      <Button text="저장" onClick={handleSave} />
      <Button text="취소" onClick={handleCancel} />
      <Button text="삭제" onClick={handleDelete} />
    </div>
  );
}
```

---

## 2️⃣ 가상 DOM (Virtual DOM)

### DOM이란?
**DOM(Document Object Model)**: 웹 페이지의 구조를 나타내는 객체

```html
<div>
  <h1>제목</h1>
  <p>내용</p>
</div>
```

### 기존 방식의 문제
- 브라우저에서 **실제 DOM을 변경하는 것은 매우 느린 작업**
- 작은 변경도 전체를 다시 렌더링 (비효율적)
- 여러 번 변경하면 = 칠하고, 또 칠하고... (비효율적)

**비유**: 건물 전체를 매번 새로 칠하는 것과 같음

### 가상 DOM 동작 원리

React는 **가상 DOM이라는 복사본을 메모리에** 만듭니다. (실제 DOM보다 훨씬 가볍고 빠름)

1. **상태 변경 발생**
   - 예: 사용자가 "좋아요" 버튼 클릭

2. **가상 DOM에서 먼저 변경**
   - 메모리에서만 작동하므로 매우 빠름

3. **이전 가상 DOM과 새 가상 DOM을 비교 (Diffing 알고리즘)**
   - "어? 좋아요 개수만 바뀌었네?"

4. **변경된 부분만 실제 DOM에 적용**
   - 최소한의 업데이트로 효율적

**비유**: 건물 전체를 새로 칠하는 대신, 바뀐 부분만 덧칠

### 예시
```jsx
function LikeButton() {
  const [likes, setLikes] = useState(0);

  return (
    <div>
      <p>좋아요: {likes}</p>  {/* 이 부분만 업데이트됨! */}
      <button onClick={() => setLikes(likes + 1)}>좋아요</button>
    </div>
  );
}
```

---

## 3️⃣ 선언적 프로그래밍 (Declarative)

### 명령적 vs 선언적

| 구분 | 설명 | 예시 |
|------|------|------|
| **명령적** | "어떻게(How)" 할지 단계별로 명령 | `element.style.color = "red"` |
| **선언적** | "무엇을(What)" 보여줄지만 선언 | `<p style={{color: "red"}}>텍스트</p>` |

### 비교 예시

**명령적 방식 (바닐라 JS)**
```javascript
const p = document.createElement('p');
p.style.color = 'red';
p.textContent = '새 텍스트';
document.body.appendChild(p);
```

**선언적 방식 (React)**
```jsx
<p style={{color: "red"}}>새 텍스트</p>
```

React에서는 "빨간색 텍스트를 보여줘"라고 선언하기만 하면, React가 알아서 DOM을 조작합니다.

---

## 4️⃣ 단방향 데이터 흐름 (One-Way Data Flow)

### 개념
**부모 컴포넌트 → 자식 컴포넌트**로만 데이터가 흐릅니다 (props를 통해)

### 장점
- 데이터의 흐름을 **예측 가능**하게 만듦
- 디버깅이 쉬움
- 어디서 데이터가 변경되는지 추적 용이

### 예시
```jsx
// 부모 컴포넌트
function Parent() {
  const [message, setMessage] = useState("안녕하세요");

  return <Child message={message} />;  // 부모 → 자식
}

// 자식 컴포넌트
function Child({ message }) {
  return <p>{message}</p>;  // 부모로부터 받은 데이터 사용
}
```

---

## 5️⃣ JSX 문법

**JavaScript를 확장한 문법**으로 UI를 직관적으로 작성할 수 있습니다.

자세한 내용은 [03-jsx.md](./03-jsx.md)를 참고하세요.

---

## 6️⃣ 활발한 생태계

### 풍부한 도구와 라이브러리

React는 강력한 생태계를 가지고 있어, 다양한 도구와 라이브러리를 활용할 수 있습니다.

**주요 도구들**:
- **React Router**: 페이지 라우팅 (SPA 내에서 페이지 전환)
- **Redux / Zustand**: 전역 상태 관리
- **Next.js**: React 기반 풀스택 프레임워크 (SSR, SSG)
- **Material-UI / Ant Design**: UI 컴포넌트 라이브러리
- **React Query**: 서버 상태 관리
- **Styled-components**: CSS-in-JS 스타일링

### 커뮤니티 지원
- 방대한 문서와 튜토리얼
- 활발한 Stack Overflow 커뮤니티
- 수많은 오픈소스 프로젝트

---

## 정리

React의 6가지 주요 특징:

1. ✅ 컴포넌트 기반 개발 - 재사용 가능한 블록
2. ✅ 가상 DOM - 효율적인 업데이트
3. ✅ 선언적 프로그래밍 - 직관적인 코드
4. ✅ 단방향 데이터 흐름 - 예측 가능한 상태 관리
5. ✅ JSX 문법 - 편리한 UI 작성
6. ✅ 활발한 생태계 - 풍부한 도구와 커뮤니티

---

## 다음 단계

JSX 문법에 대해 더 자세히 알아보려면 [03-jsx.md](./03-jsx.md)를 참고하세요.

# JSX (JavaScript XML) 문법

JSX는 React에서 UI를 작성하는 문법입니다. HTML처럼 보이지만 실제로는 JavaScript입니다.

---

## JSX란?

### 정의
- **JavaScript를 확장한 문법**
- **HTML 같은 코드를 JavaScript로 변환**하는 문법적 설탕(Syntactic Sugar)
- **React.createElement()**를 편리하게 작성하기 위한 도구

### JSX는 번역기
JSX 코드는 최종적으로 JavaScript 코드로 변환됩니다.

```jsx
// JSX 코드
<h1>안녕하세요</h1>

// ↓ 변환됨 (Babel이 자동으로 처리)

// JavaScript 코드
React.createElement('h1', null, '안녕하세요')
```

---

## JSX의 장점

### 1️⃣ 가독성

**React.createElement 방식 (JSX 없이)**
```javascript
React.createElement('div', null,
  React.createElement('header', null,
    React.createElement('h1', null, '제목'),
    React.createElement('nav', null,
      React.createElement('a', { href: '#' }, '링크1'),
      React.createElement('a', { href: '#' }, '링크2')
    )
  )
);
```

**JSX 방식 - 한눈에 구조가 보임!**
```jsx
<div>
  <header>
    <h1>제목</h1>
    <nav>
      <a href="#">링크1</a>
      <a href="#">링크2</a>
    </nav>
  </header>
</div>
```

---

### 2️⃣ 편의성 - JavaScript 표현식 자유롭게 사용

**중괄호 `{}`** 안에 모든 JavaScript 표현식을 사용할 수 있습니다.

```jsx
const name = "철수";
const age = 25;
const hobbies = ["독서", "운동", "영화"];

<div>
  <h1>{name}님의 프로필</h1>              {/* 변수 */}
  <p>나이: {age}세</p>                    {/* 변수 */}
  <p>내년: {age + 1}세</p>                {/* 연산 */}
  <p>취미 개수: {hobbies.length}개</p>    {/* 메서드 */}
  <p>성인: {age >= 20 ? "O" : "X"}</p>   {/* 삼항연산자 */}
</div>
```

---

### 3️⃣ 안정성 - XSS 공격 자동 방지

**XSS(Cross-Site Scripting)**: 악의적인 스크립트를 주입하는 공격

```jsx
const userInput = '<script>alert("해킹!")</script>';

// JSX는 자동으로 이스케이프 처리
<p>{userInput}</p>
// 결과: "<script>alert("해킹!")</script>" (문자열로 안전하게 표시)
```

❌ 일반 HTML이었다면 스크립트가 실행되어 위험!
✅ JSX는 자동으로 안전하게 처리!

---

## JSX 문법 규칙

JSX를 사용할 때 반드시 지켜야 할 규칙들입니다.

---

### 📌 규칙 1: 하나의 루트 요소로 감싸기

React 컴포넌트는 **하나의 값만 반환**할 수 있습니다.

#### ❌ 잘못된 예
```jsx
function App() {
  return (
    <h1>제목</h1>
    <p>내용</p>  // 에러! 두 개의 요소를 반환할 수 없음
  );
}
```

#### ✅ 올바른 예 1: `<div>`로 감싸기
```jsx
function App() {
  return (
    <div>
      <h1>제목</h1>
      <p>내용</p>
    </div>
  );
}
```

#### ✅ 올바른 예 2: Fragment 사용 (불필요한 `<div>` 없이)
```jsx
function App() {
  return (
    <>
      <h1>제목</h1>
      <p>내용</p>
    </>
  );
}

// 또는

function App() {
  return (
    <React.Fragment>
      <h1>제목</h1>
      <p>내용</p>
    </React.Fragment>
  );
}
```

**Fragment를 사용하는 이유**:
- 불필요한 `<div>` 추가를 피함
- DOM 구조를 깔끔하게 유지

---

### 📌 규칙 2: JavaScript 표현식은 중괄호 `{}` 사용

#### ✅ 사용 가능한 것들
```jsx
function Example() {
  const name = "홍길동";
  const age = 20;
  const items = ["사과", "바나나"];

  return (
    <div>
      {/* 변수 */}
      <p>{name}</p>

      {/* 삼항 연산자 (조건부 렌더링) */}
      <p>{age >= 20 ? "성인" : "미성년자"}</p>

      {/* map (배열 렌더링) */}
      <ul>
        {items.map((item, idx) => <li key={idx}>{item}</li>)}
      </ul>

      {/* 즉시 실행 함수 */}
      <p>{(() => "반환값")()}</p>
    </div>
  );
}
```

#### ❌ 사용할 수 없는 것들
```jsx
{/* ❌ if 문 사용 불가 */}
{if (age >= 20) { return "성인" }}  // 에러!

{/* ✅ 대신 삼항 연산자 사용 */}
{age >= 20 ? "성인" : "미성년자"}

{/* ❌ for 문 사용 불가 */}
{for (let i = 0; i < 5; i++) { ... }}  // 에러!

{/* ✅ 대신 map 사용 */}
{items.map((item) => <div>{item}</div>)}

{/* ❌ 함수 선언 사용 불가 */}
{function hello() { return "hi" }}  // 에러!

{/* ✅ 대신 즉시 실행 함수 사용 */}
{(() => "hi")()}
```

---

### 📌 규칙 3: `className` 사용 (class 아님)

HTML의 `class` 속성은 JavaScript 예약어이므로 **`className`**을 사용합니다.

```jsx
// ❌ 잘못된 예
<div class="container">내용</div>

// ✅ 올바른 예
<div className="container">내용</div>
```

---

### 📌 규칙 4: 자체 닫는 태그는 반드시 슬래시(`/`) 포함

HTML에서는 `<img>`, `<input>` 등을 닫지 않아도 되지만, JSX에서는 **반드시 닫아야** 합니다.

```jsx
// ❌ 잘못된 예
<img src="...">
<input type="text">
<br>

// ✅ 올바른 예
<img src="..." />
<input type="text" />
<br />
```

---

### 📌 규칙 5: 카멜 케이스(camelCase) 사용

HTML 속성은 kebab-case(`onclick`, `tabindex`)이지만,
JSX에서는 **camelCase**(`onClick`, `tabIndex`)를 사용합니다.

```jsx
// ❌ 잘못된 예
<button onclick={handleClick}>클릭</button>
<div tabindex="0">...</div>

// ✅ 올바른 예
<button onClick={handleClick}>클릭</button>
<div tabIndex="0">...</div>
```

**주요 속성들**:
- `onclick` → `onClick`
- `onchange` → `onChange`
- `tabindex` → `tabIndex`
- `class` → `className`
- `for` → `htmlFor`

---

### 📌 규칙 6: 인라인 스타일은 객체로 작성

CSS 스타일을 인라인으로 작성할 때는 **객체 형태**로 작성합니다.

```jsx
// ❌ 잘못된 예
<div style="color: red; font-size: 16px;">텍스트</div>

// ✅ 올바른 예
<div style={{ color: "red", fontSize: "16px" }}>텍스트</div>
```

**주의사항**:
- CSS 속성명은 camelCase 사용 (`font-size` → `fontSize`)
- 값은 문자열로 작성
- 중괄호 2개 사용: 바깥쪽은 JSX 표현식, 안쪽은 객체

---

## 조건부 렌더링

조건에 따라 다른 UI를 렌더링하는 방법입니다.

### 1. 삼항 연산자
```jsx
function Greeting({ isLoggedIn }) {
  return (
    <div>
      {isLoggedIn ? <p>환영합니다!</p> : <p>로그인하세요.</p>}
    </div>
  );
}
```

### 2. `&&` 연산자
```jsx
function Notification({ hasMessage }) {
  return (
    <div>
      {hasMessage && <p>새 메시지가 있습니다.</p>}
    </div>
  );
}
```

### 3. 변수 사용
```jsx
function Status({ status }) {
  let message;
  if (status === 'success') {
    message = <p>성공!</p>;
  } else {
    message = <p>실패...</p>;
  }

  return <div>{message}</div>;
}
```

---

## 리스트 렌더링

배열을 순회하며 여러 요소를 렌더링할 때는 **`map`** 메서드를 사용합니다.

### 기본 예시
```jsx
function FruitList() {
  const fruits = ["사과", "바나나", "오렌지"];

  return (
    <ul>
      {fruits.map((fruit, index) => (
        <li key={index}>{fruit}</li>
      ))}
    </ul>
  );
}
```

### `key` 속성의 중요성

**`key`는 React가 어떤 항목이 변경/추가/삭제되었는지 식별하는 데 사용됩니다.**

#### ❌ 잘못된 예 (key 없음)
```jsx
{fruits.map((fruit) => <li>{fruit}</li>)}  // 경고 발생
```

#### ⚠️ 권장하지 않는 예 (index를 key로 사용)
```jsx
{fruits.map((fruit, index) => <li key={index}>{fruit}</li>)}
// 항목 순서가 바뀌면 비효율적
```

#### ✅ 올바른 예 (고유한 id를 key로 사용)
```jsx
const fruits = [
  { id: 1, name: "사과" },
  { id: 2, name: "바나나" },
  { id: 3, name: "오렌지" }
];

{fruits.map((fruit) => <li key={fruit.id}>{fruit.name}</li>)}
```

---

## 정리

### JSX의 핵심
- HTML처럼 생겼지만 JavaScript
- 중괄호 `{}`로 JavaScript 표현식 사용
- React.createElement()의 편리한 대체 문법

### 필수 규칙
1. ✅ 하나의 루트 요소로 감싸기
2. ✅ JavaScript 표현식은 `{}` 사용
3. ✅ `className` 사용 (class 아님)
4. ✅ 자체 닫는 태그는 `/` 포함
5. ✅ camelCase 속성명 사용
6. ✅ 인라인 스타일은 객체로 작성

### 자주 사용하는 패턴
- 조건부 렌더링: 삼항 연산자, `&&` 연산자
- 리스트 렌더링: `map` 메서드 + `key` 속성

---

## 추가 학습 자료

- [React 공식 문서 - JSX 소개](https://react.dev/learn/writing-markup-with-jsx)
- [React 공식 문서 - 조건부 렌더링](https://react.dev/learn/conditional-rendering)
- [React 공식 문서 - 리스트 렌더링](https://react.dev/learn/rendering-lists)