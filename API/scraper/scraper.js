const puppeteer = require("puppeteer");
const cheerio = require("cheerio");
const pretty = require("pretty");

class getLiveDataFromBwin {

    getCorrectExecutablePath = () => {
        const chromeExePath = {
            mac: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            linux: "/usr/bin/google-chrome-stable",
            windows: "",
        }

        const operatingSystem = process.platform

        switch (operatingSystem) {
            case "win32":
                return chromeExePath.windows
            case "darwin":
                return chromeExePath.mac
            case "linux":
                return chromeExePath.linux
            default:
                return undefined
        }
    }

    getLiveMatchOdds = async () => {
        let namesList = [];
        let valuesList = [];
        let underOverTrasholdValues = [];
        let underOverTrasholdList = [];
        let match = {
            win_draw_loose_odds: {},
            under_over_odds: {}
        };

        const browser = await puppeteer.launch({
            headless: false,
            executablePath: this.getCorrectExecutablePath()
        });
        const page = await browser.newPage()
        await page.goto('https://sports.bwin.it/it/sports/eventi/bsg-chemie-leipzig-fsv-luckenwalde-2:2006311');
        const htmlContent = await page.content();

        const $ = cheerio.load(htmlContent);
        const liveResultNode = $('.option-group-container.single');
        const tableRows = liveResultNode.find('.option-indicator')
        tableRows.each((i, el) => {
            const oddsValue = ($(el).find('.value.option-value').text())
            const names = ($(el).find('.name').text())
            namesList.push(names)
            valuesList.push(oddsValue)
        })

        match.win_draw_loose_odds[await namesList[0].replace(/\s/g, "_")] = valuesList[0]
        match.win_draw_loose_odds[await namesList[1].replace(/\s/g, "_")] = valuesList[1]
        match.win_draw_loose_odds[await namesList[2].replace(/\s/g, "_")] = valuesList[2]

        const underOverNode = $('.option-group-container.over-under-container.triple');
        underOverNode.find('.option-indicator');

        const underOverTrasholdOdds = ($(underOverNode).find('.value'))
        underOverTrasholdOdds.each((i, el) => {
            underOverTrasholdValues.push($(el).text())
        })

        const underOverTrashold = ($(underOverNode).find('.name'))
        underOverTrashold.each((i, el) => {
            underOverTrasholdList.push($(el).text().replace(/,|\s+/g, "_"))
        })

        underOverTrasholdList.forEach((key, index) => {
            match.under_over_odds[key] = underOverTrasholdValues[index]
        })

        await browser.close();
        return match
    };
}

module.exports = getLiveDataFromBwin
