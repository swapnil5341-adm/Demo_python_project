from flask import Flask, render_template_string, request
# Import the custom function from your utils.py file
from utils import get_button_message

app = Flask(__name__)

# Track button clicks in memory (resets if the server restarts)
click_tracker = {"count": 0}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Production Test</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f9;
        }
        .container {
            text-align: center;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .blue-btn {
            background-color: #007BFF;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.2s;
        }
        .blue-btn:hover {
            background-color: #0056b3;
        }
        .message {
            margin-top: 20px;
            font-size: 16px;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>AlmaLinux Flask Deployment Test</h2>
        
        <!-- Form that sends a POST request back to this same URL -->
        <form method="POST">
            <button type="submit" class="blue-btn">Click Production Button</button>
        </form>

        {% if message %}
        <p class="message"><strong>Status:</strong> {{ message }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        click_tracker["count"] += 1
        # Call the utility function from utils.py
        message = get_button_message(click_tracker["count"])
        
    return render_template_string(HTML_TEMPLATE, message=message)

if __name__ == "__main__":
    # Local development fallback (Gunicorn overrides this in production)
    app.run(host="0.0.0.0", port=5000, debug=True)

