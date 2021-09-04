const express = require('express');
const matchController = require('../controllers/liveMatchController');

const router = express.Router();

router
  .route('/')
  .get(matchController.getMatch)

module.exports = router;