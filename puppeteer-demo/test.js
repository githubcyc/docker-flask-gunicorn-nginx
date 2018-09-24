
const puppeteer = require('puppeteer');
 
(async () => {
  const browser = await puppeteer.launch({headless: false}); //打开浏览器
  const page = await browser.newPage(); //打开一个空白页
  await page.goto('https://coincall.io'); //在地址栏输入网址并等待加载
//   await page.screenshot({path: 'example.png'}); 
  await page.click('#changeDropdown');
  await page.waitForNavigation({
    waitUntil: 'load'
  });//等待页面加载出来，等同于window.onload
//   await browser.close();//关掉浏览器
})();