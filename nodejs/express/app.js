const express = require('express')
const app = express();
const catRouter = require('./routers/catRoutes')

app.use(express.json());
app.use('/api/v1/cats', catRouter);
app.use(express.static('public'))

module.exports = app