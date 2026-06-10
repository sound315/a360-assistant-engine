const TARGET_PATTERN = /\/#\/bots\/repository\/private\/files\/task\/[^/]+\/edit/;

chrome.runtime.sendMessage({ type: "GET_TAB_INFO" }, (response) => {
  const url = response?.tab?.url || "";
  const dot = document.getElementById("dot");
  const text = document.getElementById("status-text");

  if (TARGET_PATTERN.test(url)) {
    text.textContent = "활성 — 챗봇이 임베딩되어 있습니다";
  } else {
    dot.classList.add("inactive");
    text.textContent = "비활성 — A360 편집기 페이지에서 사용하세요";
  }
});
