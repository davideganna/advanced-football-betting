const express = require('express');

const liveMatchRouter = require('./routes/liveMatchRouter');

const app = express();
app.use(express.json());

app.use('/api/v1/match/live', liveMatchRouter);

module.exports = app;