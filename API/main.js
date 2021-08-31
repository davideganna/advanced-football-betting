const puppeteer = require('puppeteer');
const cheerio = require('cheerio');
const pretty = require('pretty');

(async () => {
    const res = []
    const browser = await puppeteer.launch({
        headless: false,
        executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    });
    const page = await browser.newPage();
    await page.goto('https://sports.bwin.it/it/sports/eventi/nk-osijek-u19-nk-lokomotiva-zagreb-u19-2:2052742?tab=animation');
    const htmlContent = await page.content();
    const $ = cheerio.load(htmlContent);
    const liveResultNode = $('.option-group-container.single');
    const tableRows = liveResultNode.find('.option-indicator')
    tableRows.each((i, el) => {
        const names = ($(el).find('.name').text())
        const oddsValue = ($(el).find('.value').text())
    })
    await browser.close();

})();


