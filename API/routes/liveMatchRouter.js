const express = require('express');
const Scraper = require('../scraper/scraper')
const matchController = require('../controllers/liveMatchController');

const router = express.Router();
const dataScraper = new Scraper
const routesList = dataScraper.getLiveEventsUrls()

routesList
.then((res) => {
    res.urls.forEach((url, index) => {
        const homeTeamName = res.matchInfo[`match_${index}`].homeTeam.toLowerCase().trim().replace(/\s/g, "_");
        const awayTeamName = res.matchInfo[`match_${index}`].awayTeam.toLowerCase().trim().replace(/\s/g, "_");
        const route = `/${homeTeamName}-${awayTeamName}`
        console.log(route)
    router
    .route(route)
    .get(matchController.getMatch)
    })
})

module.exports = router;