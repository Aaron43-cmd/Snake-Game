
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Snake Game</title>

<style>
* {
    box-sizing: border-box;
}

body {
    background: #111;
    color: white;
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 0;
    padding: 20px;
}

h1 {
    color: limegreen;
}

canvas {
    background: black;
    border: 3px solid limegreen;
    max-width: 100%;
    height: auto;
}

.info {
    font-size: 20px;
    margin: 12px;
}

button {
    padding: 12px 22px;
    background: limegreen;
    color: black;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    margin: 5px;
}

button:hover {
    background: green;
    color: white;
}
</style>
</head>

<body>

<h1>🐍 SNAKE GAME</h1>

<div class="info">
    Score: <span id="score">0</span>
</div>

<canvas id="game" width="600" height="600"></canvas>

<br>
<button onclick="restartGame()">RESTART</button>

<p>Gunakan tombol panah ⬆ ⬇ ⬅ ➡</p>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const ukuran = 20;
const jumlah = 30;

let ular, makanan, arah, skor, gameOver, loop;

function restartGame() {
    ular = [
        {x: 10, y: 10}
    ];

    makanan = {
        x: 20,
        y: 15
    };

    arah = {x: 0, y: 0};
    skor = 0;
    gameOver = false;

    document.getElementById("score").textContent = skor;

    clearInterval(loop);
    gambar();
    loop = setInterval(update, 120);
}

function gambar() {
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, 600, 600);

    // Makanan
    ctx.fillStyle = "red";
    ctx.fillRect(
        makanan.x * ukuran,
        makanan.y * ukuran,
        ukuran,
        ukuran
    );

    // Ular
    ular.forEach((bagian, index) => {
        ctx.fillStyle = index === 0 ? "lime" : "lightgreen";

        ctx.fillRect(
            bagian.x * ukuran,
            bagian.y * ukuran,
            ukuran - 2,
            ukuran - 2
        );
    });
}

function update() {
    if (gameOver) return;

    if (arah.x === 0 && arah.y === 0) {
        gambar();
        return;
    }

    const kepala = {
        x: ular[0].x + arah.x,
        y: ular[0].y + arah.y
    };

    // Tabrak dinding
    if (
        kepala.x < 0 ||
        kepala.x >= jumlah ||
        kepala.y < 0 ||
        kepala.y >= jumlah
    ) {
        selesai();
        return;
    }

    // Cek makanan
    const makan =
        kepala.x === makanan.x &&
        kepala.y === makanan.y;

    // Tabrak tubuh sendiri
    const tubuhDicek = makan ? ular : ular.slice(0, -1);

    if (tubuhDicek.some(b =>
        b.x === kepala.x && b.y === kepala.y
    )) {
        selesai();
        return;
    }

    ular.unshift(kepala);

    if (makan) {
        skor += 10;
        document.getElementById("score").textContent = skor;

        makanan = {
            x: Math.floor(Math.random() * jumlah),
            y: Math.floor(Math.random() * jumlah)
        };

        while (ular.some(b =>
            b.x === makanan.x && b.y === makanan.y
        )) {
            makanan = {
                x: Math.floor(Math.random() * jumlah),
                y: Math.floor(Math.random() * jumlah)
            };
        }
    } else {
        ular.pop();
    }

    gambar();
}

function selesai() {
    gameOver = true;
    clearInterval(loop);

    ctx.fillStyle = "white";
    ctx.font = "bold 40px Arial";
    ctx.textAlign = "center";
    ctx.fillText("GAME OVER", 300, 280);

    ctx.font = "20px Arial";
    ctx.fillText("Score: " + skor, 300, 320);
}

document.addEventListener("keydown", function(e) {
    switch (e.key) {
        case "ArrowUp":
            if (arah.y !== 1) arah = {x: 0, y: -1};
            e.preventDefault();
            break;

        case "ArrowDown":
            if (arah.y !== -1) arah = {x: 0, y: 1};
            e.preventDefault();
            break;

        case "ArrowLeft":
            if (arah.x !== 1) arah = {x: -1, y: 0};
            e.preventDefault();
            break;

        case "ArrowRight":
            if (arah.x !== -1) arah = {x: 1, y: 0};
            e.preventDefault();
            break;
    }
});

restartGame();
</script>

</body>
</html>
