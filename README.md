# Advanced Football Betting

Advanced football betting is an experimental software which aims at predicting the results of football matches based on past data.

The software is divided into two main sections: `Predictions` and `API`.

## `Predictions`

This section contains the models and the backtesting script to evaluate past performances.
The models are based on data collected from the following leagues: England, Germany, Italy and Spain, ranging from 2016 to 2020 (5 Seasons each).
Predictions will be made based on the output of a Classification Random Forest model with an Elo model.

## `API`

This is the real time API used to fetch data from bwin. The API work in this way:

- First of all a web scraper written in node.js extract the data of the live match that the user want to follow
- The API establish a persistant connection with the client and every 30 seconds sends back a response in JSON format with the live odds of the match

### `Endpoints`

work in progress

### `Setup`

To start the API is necessary to download all the node dependencies related to the project. To do this is important to move in the folder called API by using the following command that must be entered in the command line.

- `cd /API`
  Once this is done it'time to download the dependecies by using this command:
- `npm ci`
  So now everyhing is done the API is ready to start.

### `Scripts`

To start runnig the API use this command:

- `npm run start`
  This command will run the API that will remain waiting for calls.

## `Technologies`

- Phyton
- Node.js
- Puppeteer
- Cheerio
