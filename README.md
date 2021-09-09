# Advanced Football Betting

Advanced football betting is an experimental software which aims at predicting the results of football matches based on past data.

The software is divided into two main sections: `Predictions` and `API`.

## `Predictions`

This section contains the models and the backtesting script to evaluate past performances.
The models are based on data collected from the following leagues: England, Germany, Italy and Spain, ranging from 2016 to 2020 (5 Seasons each).
Predictions will be made based on the output of a Classification Random Forest model with an Elo model.

## `API`

This is the real time API used to fetch data from Bwin. The API consists of:

- A web scraper written in node.js which extracts the data of the live match that the user wants to follow.
- A persistant connection with the client which every 30 seconds sends a response in JSON format with the live odds of the desired match.

### `Endpoints`

work in progress

### `Setup`

Downloading the project's node dependencies is required to build the API. In order to do so, navigate in the folder called `API` by using the following command:

- `cd /API`

Download the dependecies:

- `npm ci`

The API is now ready to start.

On Linux machines, it is important to check the path of the executable file of Chrome. This is a necessary step to correctly launch the web-scraper.
To check the path, open a terminal and enter the following command:
- `which google-chrome-stable`

Then, copy the path and paste it at line 9 of the main.js file at the voice `executablePath`. 

### `Scripts`

To start running the API use this command:

- `npm run start`
  This command will run the API that will wait for calls.

## `Technologies`

- Python
- Node.js
- Puppeteer
- Cheerio
