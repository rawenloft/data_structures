package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

const targetString = "methinks it is like a weasel"

func generateString(template string, r *rand.Rand) string {
	letters := "abcdefghijklmnopqrstuvwxyz "
	var result strings.Builder
	result.Grow(len(targetString))

	for i := range targetString {
		if template[i] == targetString[i] {
			result.WriteByte(targetString[i])
		} else {
			result.WriteByte(letters[r.Intn(len(letters))])
		}
	}
	return result.String()
}

func evaluateString(generated string) float64 {
	score := 0
	for i, char := range generated {
		if char == rune(targetString[i]) {
			score++
		}
	}
	return float64(score) / float64(len(targetString))
}

func simulateMonkeyTyping() {
	src := rand.NewSource(time.Now().UnixNano())
	r := rand.New(src)

	bestMatch := make([]byte, len(targetString))
	bestScore := 0.0
	attempt := 0

	for bestScore < 1 {
		generated := generateString(string(bestMatch), r)
		score := evaluateString(generated)

		if score > bestScore {
			bestScore = score
			copy(bestMatch, generated)
			fmt.Printf("Attempt: %d, Best Match: '%s', Score: %.2f%%\n", attempt, string(bestMatch), bestScore*100)
		}

		if attempt%1000 == 0 && attempt != 0 {
			fmt.Printf("Attempt: %d, Current Best Match: '%s', Score: %.2f%%\n", attempt, string(bestMatch), bestScore*100)
		}

		attempt++
	}

	fmt.Printf("Final Match: '%s' after %d attempts\n", string(bestMatch), attempt)
}

func main() {
	simulateMonkeyTyping()
}
