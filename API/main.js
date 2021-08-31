const getLiveData = require('./scraper/scraper');

const data = new getLiveData();

data.getLiveMatchOdds()
    .then((res) => console.log(res))





