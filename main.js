// Ваш main.js файл
const targetString = "methinks it is like a weasel";

function generateString(template) {
    const letters = "abcdefghijklmnopqrstuvwxyz ";
    let result = '';

    for (let i = 0; i < targetString.length; i++) {
        result += template[i] === targetString[i] ? targetString[i] : letters[Math.floor(Math.random() * letters.length)];
    }

    return result;
}

function evaluateString(generated) {
    let score = 0;
    for (let i = 0; i < generated.length; i++) {
        if (generated[i] === targetString[i]) {
            score++;
        }
    }
    return score / targetString.length;
}

function simulateMonkeyTyping(callback, onComplete) {
    let bestMatch = Array(targetString.length).fill(' ').join('');
    let bestScore = 0;
    let attempt = 0;

    function attemptGeneration() {
        if (bestScore < 1) {
            const generated = generateString(bestMatch);
            const score = evaluateString(generated);

            if (score > bestScore) {
                bestMatch = generated;
                bestScore = score;
                callback(`Attempt: ${attempt}, Best Match: '${bestMatch}', Score: ${(bestScore * 100).toFixed(2)}%`);
            }

            if (attempt % 1000 === 0) {
                callback(`Attempt: ${attempt}, Current Best Match: '${bestMatch}', Score: ${(bestScore * 100).toFixed(2)}%`);
            }

            attempt++;
            requestAnimationFrame(attemptGeneration);
        } else {
            callback(`Final Match: '${bestMatch}' after ${attempt} attempts`, true);
            onComplete();
        }
    }

    attemptGeneration();
}
