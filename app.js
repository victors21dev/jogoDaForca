const express = require('express')
const app = express()
const path = require("path")
const cors = require('cors')
const PORT = 3232

app.use(cors())
// app.use(express.static(path.join(__dirname, "./app/")))
app.get("/",(req, res)=>{
    res.send(`<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" href="data:,">
        <title>Document</title>
    </head>
    <body>
        <h1>Aqui vai ser nosso jogo   😀</h1>
        <p>Tem que fazer...</p>
        <ol>
            <li>Escolher palavras relacionadas com Fundamentos de Redes de Computadores</li>
            <li>Terá 8 chances</li>
            <li>Verificar se há letras disponíveis para jogar</li>
            <li>Mostrar letras já jogadas</li>
            <li>Deverá ter dica e nível de dificuldade da palavra</li>
            <li>As palavras deverá ter de 1 a 3 níveis. Exemplo: Roteador - nível 1. Proxy - Nível 3.</li>
            <li>Contador de rodadas.(Esse contador começa a contar se tiver mais de 1 rodada)</li>
            <li>Bonequinho na forca (Ir aparecendo se errar a letra (8 partes))</li>
            <li>Seria intessante um esquema de pontuação?</li>
            <li>Ver pontuação de rodadas anteriores (Isso se a rodada atual for maior que 1)</li>
            <li>Como rodaria isso?...</li>
            <ul>
                <li>Interface gráfica, utilizar html, css, javascript e se preciso bootstrap (para botões)</li>
                <li>Por preferência de linguagem do curso, vamos fazer toda regra do jogo em python</li>
                <li>Python terá o papel de sortear a palavra, verificar se letra disponível e enviar informações para o javascript</li>
                <li>Javascript recebendo essas informações do python, envia dados na tela para o usuário</li>
                <li>Para rodar na internet de qualquer dispositivo, configurar github com vercel, utilizando nodejs (funcionando no momento)</li>
            </ul>
        </ol>
    
        <div>
            <h4>Obs: Relaxem, um vai ajudando o outro, vamos separar as tarefas com o ponto forte de cada pessoa.</h4>
        </div>
    </body>
    </html>`)
})

app.listen(PORT, ()=>{
    console.log("Servidor rodando na porta")
})