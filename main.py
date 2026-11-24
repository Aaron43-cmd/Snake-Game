
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Snake Mini</title>

<style>
body {
    background: #222;
    color: white;
    text-align: center;
    font-family: monospace;
}

canvas {
    background: #9bbc0f;
    display: block;
    margin: 15px auto;
    border: 3px solid #111;
}

button {
    padding: 8px 20px;
    cursor: pointer;
}
</style>
</head>

<body>

<h2>SNAKE MINI</h2>
<p>Score: <span id="score">0</span></p>

<canvas id="game" width="300" height="300"></canvas>

<p id="status">Tekan tombol panah untuk mulai</p>
<button onclick="start()">RESTART</button>

<script>
const c = document.getElementById("game");
const ctx = c.getContext("2d");
const size = 15;
const max = 20;

let snake, food, dx, dy, score, running, timer;

function start() {
    clearInterval(timer);

    snake = [{x: 10, y: 10}];
    food = {x: 15, y: 10};
    dx = 0;
    dy = 0;
    score = 0;
    running = true;

    document.getElementById("score").textContent = 0;
    document.getElementById("status").textContent = "PLAYING";

    draw();
    timer = setInterval(update, 150);
}

function draw() {
    ctx.fillStyle = "#9bbc0f";
    ctx.fillRect(0, 0, 300, 300);

    ctx.fillStyle = "#253406";
    ctx.fillRect(food.x * size, food.y * size, size, size);

    for (let p of snake) {
        ctx.fillRect(p.x * size, p.y * size, size, size);
    }
}

function update() {
    if (dx === 0 && dy === 0) return;

    let head = {
        x: snake[0].x + dx,
        y: snake[0].y + dy
    };

    let eating = head.x === food.x && head.y === food.y;

    if (
        head.x < 0 || head.y < 0 ||
        head.x >= max || head.y >= max
    ) {
        end();
        return;
    }

    let body = eating ? snake : snake.slice(0, -1);

    if (body.some(p => p.x === head.x && p.y === head.y)) {
        end();
        return;
    }

    snake.unshift(head);

    if (eating) {
        score += 10;
        document.getElementById("score").textContent = score;

        do {
            food = {
                x: Math.floor(Math.random() * max),
                y: Math.floor(Math.random() * max)
            };
        } while (snake.some(p =>
            p.x === food.x && p.y === food.y
        ));
    } else {
        snake.pop();
    }

    draw();
}

function end() {
    running = false;
    clearInterval(timer);
    document.getElementById("status").textContent = "GAME OVER";
}

document.addEventListener("keydown", e => {
    if (!running) return;

    if (e.key === "ArrowUp" && dy !== 1) {
        dx = 0; dy = -1;
    }
    if (e.key === "ArrowDown" && dy !== -1) {
        dx = 0; dy = 1;
    }
    if (e.key === "ArrowLeft" && dx !== 1) {
        dx = -1; dy = 0;
    }
    if (e.key === "ArrowRight" && dx !== -1) {
        dx = 1; dy = 0;
    }
});

start();
</script>

</body>
</html>
