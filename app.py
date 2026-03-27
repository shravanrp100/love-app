from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name", "Someone Special")

    return f"""
    <html>
    <head>
        <title>For You 💖</title>

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            body {{
                text-align: center;
                margin-top: 80px;
                font-family: Arial;
                background: linear-gradient(45deg, #ff9a9e, #fad0c4);
                overflow: hidden;
            }}

            h1 {{
                color: #fff;
                font-size: 40px;
                animation: glow 1s infinite alternate;
            }}

            @keyframes glow {{
                from {{ text-shadow: 0 0 10px #fff; }}
                to {{ text-shadow: 0 0 20px #ff4da6; }}
            }}

            button {{
                padding: 15px 25px;
                font-size: 18px;
                background-color: #ff4da6;
                color: white;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                margin-top: 20px;
            }}

            .hidden {{
                display: none;
                font-size: 22px;
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

            .footer {{
                position: fixed;
                bottom: 10px;
                width: 100%;
                color: white;
                font-size: 14px;
            }}
        </style>
    </head>

    <body>

        <h1>Hi {name} ❤️</h1>
        <p style="color:white;font-size:20px;">You are my best friend 💖</p>

        <button onclick="showMessage()">Click Me 💌</button>

        <div id="msg" class="hidden">
            💖 I am lucky to have you in my life 💖 <br><br>
            😊 Always stay happy 😊
        </div>

        <audio id="music" loop>
            <source src="https://www.bensound.com/bensound-music/bensound-love.mp3" type="audio/mpeg">
        </audio>

        <div class="footer">
            Made with ❤️ just for you
        </div>

        <script>
            function showMessage() {{
                document.getElementById("msg").style.display = "block";

                // Play music on click (mobile-friendly)
                document.getElementById("music").play();
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

# ✅ IMPORTANT FOR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
