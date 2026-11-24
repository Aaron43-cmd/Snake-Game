
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Snake Nokia Classic</title>

<style>
    body {
        background: #222;
        color: #c7d6a5;
        font-family: monospace;
        text-align: center;
        padding: 20px;
    }

    h1 {
        font-size: 26px;
    }

    #screen {
        display: inline-block;
        background: #9bbc0f;
        padding: 10px;
        border: 5px solid #333;
        border-radius: 8px;
    }

    canvas {
        display: block;
        background: #9bbc0f;
        image-rendering: pixelated;
    }

    button {
        background: #596b25;
        color: #d8e7b0;
        border: 2px solid #9bbc0f;
        padding: 10px 20px;
        margin-top: 12px;
        font-family: monospace;
        cursor: pointer;
    }

    #info {
        margin: 12px;
        color: #c7d6a5;
    }
</style>
</head>

<body>

<h1>SNAKE NOKIA</h1>

<div id="screen">
    <div style="color:#253406; font-weight:bold; padding:5px">
        SCORE: <span id="score">0</span>
    </div>

    <canvas id="game" width="400" height="400"></canvas>
</div>

<div id="info">PRESS ARROW KEY TO START</div>

<br>
<button onclick="resetGame()">RESTART</button>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const cell = 20;
const grid = 20;

let snake;
let food;
let dx;
let dy;
let score;
let started;
let ended;
let timer;

function resetGame() {
    clearInterval(timer);

    snake = [
        {x: 8, y: 10},
        {x: 7, y: 10},
        {x: 6, y: 10}
    ];

    dx = 0;
    dy = 0;
    score = 0;
    started = false;
    ended = false;

    document.getElementById("score").textContent = score;
    document.getElementById("info").textContent =
        "PRESS ARROW KEY TO START";

    spawnFood();
    draw();

    timer = setInterval(update, 120);
}

function spawnFood() {
    do {
        food = {
            x: Math.floor(Math.random() * grid),
            y: Math.floor(Math.random() * grid)
        };
    } while (snake.some(part =>
        part.x === food.x && part.y === food.y
    ));
}

function draw() {
    ctx.fillStyle = "#9bbc0f";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Makanan
    ctx.fillStyle = "#253406";
    ctx.fillRect(
        food.x * cell,
        food.y * cell,
        cell,
        cell
    );

    // Ular
    snake.forEach(part => {
        ctx.fillStyle = "#253406";
        ctx.fillRect(
            part.x * cell,
            part.y * cell,
            cell,
            cell
        );
    });
}

function update() {
    if (!started || ended) return;

    const head = {
        x: snake[0].x + dx,
        y: snake[0].y + dy
    };

    const eating =
        head.x === food.x &&
        head.y === food.y;

    // Tabrak dinding
    if (
        head.x < 0 ||
        head.y < 0 ||
        head.x >= grid ||
        head.y >= grid
    ) {
        gameOver();
        return;
    }

    // Cek tubuh
    const checkBody = eating
        ? snake
        : snake.slice(0, -1);

    if (checkBody.some(part =>
        part.x === head.x && part.y === head.y
    )) {
        gameOver();
        return;
    }

    snake.unshift(head);

    if (eating) {
        score += 10;
        document.getElementById("score").textContent = score;
        spawnFood();
    } else {
        snake.pop();
    }

    draw();
}

function gameOver() {
    ended = true;
    clearInterval(timer);

    document.getElementById("info").textContent =
        "GAME OVER - PRESS RESTART";

    draw();

    ctx.fillStyle = "#253406";
    ctx.textAlign = "center";
    ctx.font = "bold 24px monospace";
    ctx.fillText("GAME OVER", 200, 200);
}

document.addEventListener("keydown", function(e) {
    const key = e.key;

    if (["ArrowUp", "ArrowDown",
          "ArrowLeft", "ArrowRight"].includes(key)) {
        e.preventDefault();
    }

    if (ended) return;

    if (!started) {
        started = true;
        document.getElementById("info").textContent =
            "PLAYING";
    }

    if (key === "ArrowUp" && dy !== 1) {
        dx = 0;
        dy = -1;
    }
    else if (key === "ArrowDown" && dy !== -1) {
        dx = 0;
        dy = 1;
    }
    else if (key === "ArrowLeft" && dx !== 1) {
        dx = -1;
        dy = 0;
    }
    else if (key === "ArrowRight" && dx !== -1) {
        dx = 1;
        dy = 0;
    }
});

resetGame();
</script>

</body>
</html>
