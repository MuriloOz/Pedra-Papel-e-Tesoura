Esse código ficou bem redondinho! Fiz um Pedra, Papel e Tesoura que roda no terminal e funciona de forma simples e direta.

Primeiro, criei a função get_user_choice() pra garantir que o jogador só escolhesse entre "pedra", "papel" ou "tesoura", evitando entradas inválidas. Depois, fiz o get_computer_choice(), que usa random.choice() pra o computador escolher aleatoriamente uma opção.

A decisão do vencedor rola dentro de determine_winner(), onde verifico todas as combinações possíveis pra definir quem ganha, perde ou empata. E, claro, play_game() é a função principal, onde tudo acontece: recebe a escolha do jogador, mostra a escolha do computador e exibe o resultado.

O código é simples, mas funcional! Dá pra melhorar colocando um loop pra jogar várias rodadas ou até um placar. Mas do jeito que tá, já dá pra se divertir rapidinho no terminal! 🚀
