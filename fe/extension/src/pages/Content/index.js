import { ADD_PAGE_COMMAND } from '../../constants/message';

// Listen to DOMContentLoaded event
const collectData = async () => {
  const response = await chrome.runtime.sendMessage({
    type: ADD_PAGE_COMMAND,
    data: {
      url: window.location.href,
      title: document.title,
      html: document.documentElement.outerHTML,
      text: document.body.innerText,
      selection: window.getSelection().toString(),
      meta: {
        description: document.querySelector('meta[name="description"]')
          ?.content,
        keywords: document.querySelector('meta[name="keywords"]')?.content,

        // Open Graph
        ogTitle: document.querySelector('meta[property="og:title"]')?.content,
        ogDescription: document.querySelector('meta[property="og:description"]')
          ?.content,
        ogImage: document.querySelector('meta[property="og:image"]')?.content,
        ogUrl: document.querySelector('meta[property="og:url"]')?.content,
      },
      access_time: new Date().toISOString(),
    },
  });
};

collectData();
