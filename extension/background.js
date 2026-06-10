chrome.runtime.onInstalled.addListener(() => {
  console.log("[A360 Assistant] Extension installed.");
});

// 팝업에서 탭 정보 요청 처리
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "GET_TAB_INFO") {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      sendResponse({ tab: tabs[0] });
    });
    return true;
  }
});
