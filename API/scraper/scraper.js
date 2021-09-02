const puppeteer = require("puppeteer");
const cheerio = require("cheerio");
const pretty = require("pretty");

class getLiveDataFromBwin {
    getCorrectExecutablePath = () => {
        const chromeExePath = {
            mac: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            linux: "/usr/bin/google-chrome-stable",
            windows: "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
        };

        const operatingSystem = process.platform;

        switch (operatingSystem) {
            case "win32":
                return chromeExePath.windows;
            case "darwin":
                return chromeExePath.mac;
            case "linux":
                return chromeExePath.linux;
            default:
                return undefined;
        }
    };

    getLiveMatchOdds = async() => {
        let namesList = [];
        let valuesList = [];
        let underOverList = [];
        let match = {
            win_draw_loose_odds: {},
            under_over_odds: {},
        };

        const browser = await puppeteer.launch({
            headless: false,
            executablePath: this.getCorrectExecutablePath(),
        });
        const page = await browser.newPage();
        await page.goto(
            "https://sports.bwin.it/it/sports/eventi/jjk-jyvaskyla-kemi-city-fc-2:2035528"
        );
        const htmlContent = await page.content();

        const $ = cheerio.load(htmlContent);
        const liveResultNode = $(".option-group-container.single");
        const tableRows = liveResultNode.find(".option-indicator");

        tableRows.each((i, el) => {
            const oddsValue = $(el).find(".value.option-value").text();
            const names = $(el).find(".name").text();
            namesList.push(names);
            if (oddsValue.length) {
                valuesList.push(oddsValue);
            } else {
                valuesList.push("This bet at the moment is offline");
            }
        });

        if (namesList[0] && namesList[1] && namesList[2]) {
            match.win_draw_loose_odds[namesList[0].replace(/\s/g, "_")] =
                valuesList[0];
            match.win_draw_loose_odds[namesList[1].replace(/\s/g, "_")] =
                valuesList[1];
            match.win_draw_loose_odds[namesList[2].replace(/\s/g, "_")] = 
                valuesList[2];

            const underOverNode = $(
                ".option-group-container.over-under-container.triple"
            ).first();
            const oddsNodes = underOverNode.find(".option-indicator");
            oddsNodes.each((i, el) => {
                const oddsWrapper = $(el).find("div");
                oddsWrapper.each((i, item) => {
                    const oddsChildValue = $(item).text();
                    if (oddsChildValue.length) {
                        underOverList.push(oddsChildValue);
                    } else {
                        underOverList.push("This bet is not avaiable");
                    }
                });
            });

            const chunkedList = this.sliceIntoChunks(underOverList, 2);
            chunkedList.forEach((item) => {
                const keyPattern = /,|\s+/g;
                const key = item[0].replace(keyPattern, "_");
                match.under_over_odds[key] = item[1];
            });

            await browser.close();
            return match;
        } else {
            this.getLiveMatchOdds();
        }
    };

    sliceIntoChunks = (arr, chunkSize) => {
        const res = [];
        if (arr) {
            for (let i = 0; i < arr.length; i += chunkSize) {
                const chunk = arr.slice(i, i + chunkSize);
                res.push(chunk);
            }
        }
        return res;
    };
}

module.exports = getLiveDataFromBwin;