from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    data = request.get_json()
    user_choice = data.get("user_choice")
    if user_choice not in ['pedra', 'papel', 'tesoura']:
        return jsonify({"error": "Escolha inválida!"}), 400

    computer_choice = random.choice(['pedra', 'papel', 'tesoura'])
    
    if user_choice == computer_choice:
        result = "Empate!"
        winner = "none"
    elif (user_choice == 'pedra' and computer_choice == 'tesoura') or \
         (user_choice == 'papel' and computer_choice == 'pedra') or \
         (user_choice == 'tesoura' and computer_choice == 'papel'):
        result = "Você ganhou!"
        winner = "user"
    else:
        result = "Você perdeu!"
        winner = "computer"
    
    return jsonify({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result,
        "winner": winner
    })

if __name__ == "__main__":
    app.run(debug=True)
