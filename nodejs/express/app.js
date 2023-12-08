const express = require('express')
const app = express()
const router = require('./router')

app.get('./user/list', function (req, res) {
    res.send(req.params)
})

app.use(router)

app.listen('3000', () => {
    console.log('express is runnig on http://127.0.0.1:3000');
})