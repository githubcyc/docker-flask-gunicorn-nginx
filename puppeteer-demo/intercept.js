// https://zhaoqize.github.io/puppeteer-api-zh_CN/#/class-ElementHandle
const puppeteer = require('puppeteer');
const fs = require('fs');

(async() => {
  const browser = await puppeteer.launch({headless: false});
  const page = await browser.newPage();
  await page.setRequestInterception(true);
  page.on('request', request => {
    if (request.resourceType() === 'image')
      request.abort();
    else //(request.method() === 'POST')
      request.continue();
  });
  page.on('response', async response => {
    if ('xhr' !== response.request().resourceType()){
        return ;
    }
    
    if (response.url().endsWith("frontpage-data/"))
      console.log(response.url());
      console.log("response code: ", response.status());
      js = await response.text()
      fs.appendFile('api.json', js+'\n', _ => console.log('Json saved'));
    // do something here
  });
  await page.goto('https://coincall.io');
//   const html = await page.content();
//   console.log(html)
//   await page.screenshot({path: 'news.png', fullPage: true});

//   await browser.close();
})();