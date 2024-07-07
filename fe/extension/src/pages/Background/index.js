// chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
//   console.log(
//     sender.tab
//       ? 'from a content script:' + sender.tab.url
//       : 'from the extension'
//   );
//   if (request.greeting === 'hello') sendResponse({ farewell: 'goodbye' });
// });

import { ADD_PAGE_COMMAND } from '../../constants/message';

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === ADD_PAGE_COMMAND) {
    chrome.storage.sync.get('currentUser', function (res) {
      let { user_id } = res['currentUser'];
      // Save request.data to the database
      fetch('http://localhost:8000/api/guardiannet/web_access', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: user_id,
          web_url: request.data.url,
          title: request.data.title,
          access_time: new Date().toISOString(),
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log('Success:', data);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    });
  }

  //   if (request.type === 'translate') {
  //     getTranslateResult(sender.tab.id, request, sendResponse);
  //   } else if (request.type === 'audio') {
  //     getAudioFromText(request.text, request.from)
  //       .then((audio) => {
  //         sendResponse({ audio });
  //       })
  //       .catch((error) => {
  //         sendResponse({ error });
  //       });
  //   } else if (request.type === 'getCommands') {
  //     chrome.commands.getAll((commands) => {
  //       let missingShortcuts = [];

  //       for (let { name, shortcut } of commands) {
  //         if (shortcut === '') {
  //           missingShortcuts.push(name);
  //         }
  //       }

  //       if (missingShortcuts.length > 0) {
  //         sendResponse({ missingShortcuts });
  //       }
  //     });
  //   }

  return true;
});
