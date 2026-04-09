# Binary Search: Concept and Strategy (picoCTF 2024)

## 1. Problem Overview
- **Challenge Name:** Binary Search
- **Category:** General Skills
- **Objective:** Find a secret number between 1 and 1000 within 10 guesses.
- **Core Concept:** Utilizing the Binary Search algorithm to efficiently narrow down search ranges in a CLI environment.

## 2. Theoretical Background: Why Binary Search?
Binary Search is a fundamental algorithm that finds the position of a target value within a sorted array. It compares the target value to the middle element of the array.

- **Efficiency:** By picking the middle number, you eliminate half of the remaining possibilities regardless of whether the guess is too high or too low.
- **The Math:** Since $2^{10} = 1024$, a maximum of 10 guesses is mathematically guaranteed to find any number between 1 and 1000.
- **Complexity:** $O(\log n)$ time complexity.


## 3. Step-by-Step Solution Strategy
To solve this challenge, I followed a systematic "Half-Split" approach:

1. **Initial Guess:** Always start at **500** (the midpoint of 1-1000).
2. **Analysis:** - If the response is **"Higher"**, the new range is 501–1000. Next guess: **750**.
   - If the response is **"Lower"**, the new range is 1–499. Next guess: **250**.
3. **Iteration:** Continue dividing the remaining range by two until the "Flag" is revealed.

## 4. Key Takeaways
- This algorithm is not just for games; it is a critical logic used in **Blind SQL Injection** or searching through large system logs in cybersecurity.
- The program resets the random number upon each connection, so the search must always restart from the midpoint (500) to maintain efficiency.

- ## 5. Practice Log (Actual Webshell Session)
Below is the actual sequence of guesses I used to capture the flag:

```bash
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500  -> Lower!
Enter your guess: 250  -> Higher!
Enter your guess: 375  -> Higher!
Enter your guess: 437  -> Lower!
Enter your guess: 406  -> Lower!
Enter your guess: 390  -> Lower!
Enter your guess: 382  -> Higher!
Enter your guess: 386  -> Higher!
Enter your guess: 388  -> Lower!
Enter your guess: 387  -> Congratulations! You guessed the correct number: 387

Here's your flag: picoCTF{g00d_gu355_6dcfb67c}
```
