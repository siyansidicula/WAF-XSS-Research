from flask import Flask, request, render_template_string

app = Flask(__name__)

BLOCKED_PATTERNS = [
    "<",
    ">",
    "script",
    "javascript:",
    "onerror",
    "onload"
]

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>WAF Demo</title>
</head>
<body>
    <h2>WAF Character Filter Demo</h2>

    <form method="POST">
        <input type="text" name="user_input" placeholder="Enter text">
        <button type="submit">Submit</button>
    </form>

    {% if result %}
        <h3>{{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        user_input = request.form.get("user_input", "")

        blocked = False
        reason = ""

        for pattern in BLOCKED_PATTERNS:
            if pattern.lower() in user_input.lower():
                blocked = True
                reason = f"Matched filter: {pattern}"
                break

        if blocked:
            result = f"BLOCKED - {reason}"
        else:
            result = "ALLOWED"

    return render_template_string(HTML_PAGE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
