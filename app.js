const express = require('express')
const app = express()
const path = require("path")
const cors = require('cors')
const PORT = 3232

app.use(cors())
app.use(express.static(path.join(__dirname, "./app/")))

app.listen(PORT, ()=>{
    console.log("Servidor rodando na porta")
})