const express = require('express')

const catRouter = require('./routers/catRoutes')

const app = express();

app.use(express.json());
app.use('/api/v1/cats', catRouter);

app.get('/', (req, res) => {
    const url = req.url;
    res.status(200).send(`you are now visiting ${url}`)
})

module.exports = app