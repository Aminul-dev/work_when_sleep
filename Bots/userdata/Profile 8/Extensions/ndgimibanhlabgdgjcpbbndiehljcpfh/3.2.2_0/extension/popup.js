var openedRecorder=!1,recorderOpen=document.querySelector(".recorderButton"),isOpera=!!window.opr&&!!opr.addons||!!window.opera||0<=navigator.userAgent.indexOf(" OPR/"),isFirefox="undefined"!==typeof InstallTrigger,isSafari=/constructor/i.test(window.HTMLElement)||function(a){return"[object SafariRemoteNotification]"===a.toString()}(!window.safari||"undefined"!==typeof safari&&safari.pushNotification),isEdge=-1<window.navigator.userAgent.indexOf("Edg/")?!0:!1,isChrome=!!window.chrome&&(!!window.chrome.webstore||
!!window.chrome.runtime),reviewLink=document.querySelector(".review-link"),browserType=chrome;isFirefox&&(reviewLink.setAttribute("href","https://addons.mozilla.org/en-US/firefox/addon/selectorshub/"),browserType=browser,document.querySelector("body").style.width="343px",document.querySelector(".demoPic").style.marginLeft="96px");isOpera&&reviewLink.setAttribute("href","https://addons.opera.com/en-gb/extensions/details/selectorshub/");isEdge&&reviewLink.setAttribute("href","https://microsoftedge.microsoft.com/addons/detail/selectorshub/iklfpdeiaeeookjohbiblmkffnhdippe");
var OS=window.navigator.userAgent.includes("Mac")?"mac":"windows";OS.includes("mac")||(document.querySelector("body").style.fontFamily="Helvetica",document.querySelector(".sponsors").style.fontSize="11px",document.querySelector("body").style.fontSize="12px",document.querySelector(".contextMenuFilter").style.fontSize="11px");var port=browserType.runtime.connect({name:"Sample Communication"});
browserType.runtime.onMessage.addListener(function(a,b,c){"AttachStudio"===a.message&&(openedRecorder=!0);"DeattachStudio"===a.message&&(openedRecorder=!1)});recorderOpen.addEventListener("click",function(){openedRecorder=!0;port.postMessage({name:"openStudio"})});var toggleElement=document.querySelector(".toggle-btn"),contextMenuFilter=document.querySelector(".contextMenuFilter");toggleElement.addEventListener("click",function(){toggleAction();browserType.runtime.sendMessage({contextMenu:toggleElement.className})});
function toggleAction(){toggleElement.classList.contains("active")?(browserType.storage.local.set({toggleElement:"inactive"},function(){}),toggleElement.classList.remove("active"),toggleElement.classList.add("inactive"),contextMenuFilter.style.display="none"):(browserType.storage.local.set({toggleElement:"active"},function(){}),toggleElement.classList.remove("inactive"),toggleElement.classList.add("active"),contextMenuFilter.style.display="block");var a=document.querySelector(".toggle.toolTip");toggleElement.classList.contains("inactive")?
a.textContent="Turn on contextMenu.":a.textContent="Turn off contextMenu."}var relXpathOption=document.querySelector(".chooseSelector.relXpath"),cssSelectorOption=document.querySelector(".chooseSelector.cssSelector"),jspathOption=document.querySelector(".chooseSelector.jspath"),absXpathOption=document.querySelector(".chooseSelector.absXpath");
setTimeout(function(){browserType.storage.local.get(["toggleElement"],function(a){"inactive"==a.toggleElement&&(toggleElement.classList.remove("active"),toggleElement.classList.add("inactive"),contextMenuFilter.style.display="none");a=document.querySelector(".toggle.toolTip");toggleElement.classList.contains("inactive")?a.textContent="Turn on contextMenu.":a.textContent="Turn off contextMenu."});browserType.storage.local.get(["relXpathChecked"],function(a){a.relXpathChecked=void 0==a.relXpathChecked?
"relXpathOn":a.relXpathChecked;relXpathOption.checked="relXpathOn"==a.relXpathChecked?!0:!1});browserType.storage.local.get(["cssSelectorChecked"],function(a){a.cssSelectorChecked=void 0==a.cssSelectorChecked?"cssSelectorOff":a.cssSelectorChecked;cssSelectorOption.checked="cssSelectorOn"==a.cssSelectorChecked?!0:!1});browserType.storage.local.get(["jspathChecked"],function(a){a.jspathChecked=void 0==a.jspathChecked?"jspathOff":a.jspathChecked;jspathOption.checked="jspathOn"==a.jspathChecked?!0:!1});
browserType.storage.local.get(["absXpathChecked"],function(a){a.absXpathChecked=void 0==a.absXpathChecked?"absXpathOff":a.absXpathChecked;absXpathOption.checked="absXpathOn"==a.absXpathChecked?!0:!1})},500);relXpathOption.addEventListener("click",function(){var a=relXpathOption.checked?"relXpathOn":"relXpathOff";browserType.storage.local.set({relXpathChecked:a},function(){});browserType.runtime.sendMessage({relXpathChecked:a})});
cssSelectorOption.addEventListener("click",function(){var a=cssSelectorOption.checked?"cssSelectorOn":"cssSelectorOff";browserType.storage.local.set({cssSelectorChecked:a},function(){});browserType.runtime.sendMessage({cssSelectorChecked:a})});jspathOption.addEventListener("click",function(){var a=jspathOption.checked?"jspathOn":"jspathOff";browserType.storage.local.set({jspathChecked:a},function(){});browserType.runtime.sendMessage({jspathChecked:a})});
absXpathOption.addEventListener("click",function(){var a=absXpathOption.checked?"absXpathOn":"absXpathOff";browserType.storage.local.set({absXpathChecked:a},function(){});browserType.runtime.sendMessage({absXpathChecked:a})});function popup(){var a=document.querySelector(".toggle-btn").className;chrome.tabs.query({currentWindow:!0,active:!0},function(b){chrome.tabs.sendMessage(b[0].id,{name:a})})}
function popupRelXpath(){var a=relXpathOption.checked?"relXpathOn":"relXpathOff";chrome.tabs.query({currentWindow:!0,active:!0},function(b){chrome.tabs.sendMessage(b[0].id,{name:a})})}function popupCssSelector(){var a="cssSelectorOn";a=cssSelectorOption.checked||jspathOption.checked?"cssSelectorOn":"cssSelectorOff";chrome.tabs.query({currentWindow:!0,active:!0},function(b){chrome.tabs.sendMessage(b[0].id,{name:a})})}
document.addEventListener("DOMContentLoaded",function(){toggleElement.addEventListener("click",popup);relXpathOption.addEventListener("click",popupRelXpath);cssSelectorOption.addEventListener("click",popupCssSelector);jspathOption.addEventListener("click",popupCssSelector)});