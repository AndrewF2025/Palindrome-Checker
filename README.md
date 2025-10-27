# Palindrome-Checker

A simple Python palindrome checker app.

---

## How Input Works

Your app accepts input in three ways:

1. **Command-Line Argument**  
   Provide the text directly:
   ```
   python Palindrome-Checker-App.py "Was it a car or a cat I saw?"
   ```

2. **Interactive Prompt**  
   If no argument is given, the app will prompt you:
   ```
   python Palindrome-Checker-App.py
   Enter text to check for palindrome: deified
   ```

3. **Standard Input (stdin)**  
   You can pipe text into the app:
   ```
   echo "racecar" | python Palindrome-Checker-App.py
   ```
   - Here, `stdin` is the data stream sent to the app from another command or file.

**Note:**
- The app uses the interactive prompt if no argument or piped input is provided.
- If you pipe data, the app reads from `stdin` (the standard input stream).

---

## Usage

### Check a string from the command line
```
python Palindrome-Checker-App.py "Drab as a fool, as aloof as a bard"
```

### Treat punctuation as significant (raw mode)
```
python Palindrome-Checker-App.py --raw "A dog! A panic in a pagoda!"
```

### Library usage
```python
from palindrome_checker import is_palindrome

is_palindrome("Cigar? Toss it in a can. It is so tragic.")  # True
```
