port = await navigator.serial.requestPort();
await port.open({ baudRate: 9600 });
writer = port.writable.getWriter();

async function sendChar(ch) {
  if (!writer) return;
  const data = new TextEncoder().encode(ch); // "1" -> [0x31]
  await writer.write(data);                  // 시리얼 포트로 전송
}
