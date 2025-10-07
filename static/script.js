const buttons = document.querySelectorAll("button");
const resultDiv = document.getElementById("result");
const userScoreSpan = document.getElementById("user-score");
const computerScoreSpan = document.getElementById("computer-score");

let userScore = 0;
let computerScore = 0;

buttons.forEach(btn => {
    btn.addEventListener("click", () => {
        const choice = btn.dataset.choice;

        fetch("/play", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_choice: choice })
        })
        .then(res => res.json())
        .then(data => {
            if (data.error) {
                resultDiv.textContent = data.error;
            } else {
                resultDiv.innerHTML = `
                    Você escolheu: ${data.user_choice} <br>
                    Computador escolheu: ${data.computer_choice} <br>
                    Resultado: <strong>${data.result}</strong>
                `;

                // Atualiza placar
                if (data.winner === "user") userScore++;
                if (data.winner === "computer") computerScore++;

                userScoreSpan.textContent = userScore;
                computerScoreSpan.textContent = computerScore;
            }
        });
    });
});
