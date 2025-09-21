from flask import Flask
from routes.chatbot import chatbot_bp
from routes.journal import journal_bp

app = Flask(__name__)

# Register Blueprints (modular routes)
app.register_blueprint(chatbot_bp, url_prefix="/chatbot")

@app.route("/")
def home():
    return {"message": "Hack2Skill Project Backend Running"}

if __name__ == "__main__":
    app.run(debug=True)
