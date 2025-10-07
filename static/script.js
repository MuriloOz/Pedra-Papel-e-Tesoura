const buttons = document.querySelectorAll("button");
const resultDiv = document.getElementById("result");

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
            }
        });
    });
});
