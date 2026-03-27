from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name", "Raghu Sir")

    return f"""
    <html>
    <head>
        <title>Welcome</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            body {{
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #f4f6f9;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}

            .card {{
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 400px;
                width: 90%;
            }}

            .logo {{
                font-size: 28px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 10px;
            }}

            h1 {{
                color: #2c3e50;
                margin-bottom: 10px;
            }}

            p {{
                color: #555;
                font-size: 18px;
            }}

            .btn {{
                margin-top: 20px;
                padding: 12px 20px;
                border: none;
                background: #2c3e50;
                color: white;
                font-size: 16px;
                border-radius: 8px;
                cursor: pointer;
            }}

            .message {{
                display: none;
                margin-top: 20px;
                font-size: 16px;
                color: #333;
            }}

            .footer {{
                margin-top: 20px;
                font-size: 13px;
                color: #999;
            }}
        </style>
    </head>

    <body>

        <div class="card">
            <div class="logo">🏢 Company Name</div>

            <h1>Welcome, {name}</h1>
            <p>We are glad to have you in the office today.</p>

            <button class="btn" onclick="showMessage()">View Message</button>

            <div id="msg" class="message">
                Wishing you a productive and successful day ahead. <br><br>
                Let's achieve great things together.
            </div>

            <div class="footer">
                © 2026 Company. All rights reserved.
            </div>
        </div>

        <script>
            function showMessage() {{
                document.getElementById("msg").style.display = "block";
            }}
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)