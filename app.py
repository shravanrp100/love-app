from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    name1 = request.args.get("name1", "Simran")
    name2 = request.args.get("name2", "Nikhil")

    return f"""
    <html>
    <head>
    <title>Engagement Wishes 💍</title>

    <style>
    body {{
        text-align: center;
        margin-top: 80px;
        font-family: Arial;
        background: linear-gradient(45deg, #ff758c, #ff7eb3);
        overflow: hidden;
    }}

    h1 {{
        color: white;
        font-size: 40px;
    }}

    p {{
        color: white;
        font-size: 22px;
    }}

    button {{
        padding: 15px 25px;
        font-size: 18px;
        background-color: #fff;
        color: #ff4da6;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        margin-top: 20px;
    }}

    .hidden {{
        display: none;
        font-size: 26px;
        color: white;
        margin-top: 20px;
    }}

    .heart {{
        position: absolute;
        color: red;
        animation: float 5s linear infinite;
    }}

    @keyframes float {{
        0% {{ transform: translateY(100vh); opacity: 1; }}
        100% {{ transform: translateY(-10vh); opacity: 0; }}
    }}
    </style>
    </head>

    <body>

    <h1>💍 Congratulations {name1} & {name2} 💖</h1>

    <p>Wishing you both a lifetime of love, happiness, and togetherness 💕</p>

    <button onclick="showMessage()">Click for Surprise 💌</button>

    <div id="msg" class="hidden">
        💖 May your love grow stronger every day 💖 <br><br>
        💫 Two hearts, one beautiful journey 💫 <br><br>
        💍 Happy Engagement 💍
    </div>

    <audio autoplay loop>
        <source src="https://www.bensound.com/bensound-music/bensound-romantic.mp3" type="audio/mpeg">
    </audio>

    <script>
    function showMessage() {{
        document.getElementById("msg").style.display = "block";
    }}

    function createHeart() {{
        let heart = document.createElement("div");
        heart.className = "heart";
        heart.innerHTML = "❤️";
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.fontSize = (Math.random() * 20 + 20) + "px";
        document.body.appendChild(heart);

        setTimeout(() => {{
            heart.remove();
        }}, 5000);
    }}

    setInterval(createHeart, 300);
    </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)