const express = require('express')
const app = express()
const path = require("path")
const PORT = 3232

app.get("/", ()=>{
    app.use(express.static(path.join(__dirname, 'app')))
})

app.listen(PORT)