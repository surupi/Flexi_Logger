# FlexiLogger 🪵✨

**FlexiLogger** is a highly versatile, feature-rich Java logging library designed for dynamic log transformations, formatting, security masking, and multi-output execution.

🔗 **Live Application:** [Streamlit Cloud Deployment](https://flexi-logger.streamlit.app/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌟 Key Features

### 🛡️ Security & Privacy
- **PII Data Masking**: Automatically redacts emails (`user***@***.com`), phone numbers (`***-***-****`), and credit card numbers (`****-****-****-****`).
- **SHA-256 Hashing**: Logs 64-character cryptographic SHA-256 digests of sensitive data.

### 🎨 Visual & Styling
- **ANSI Color & Effects**: Supports foreground colors, background colors, and text styles.
- **Emoji Support**: Native emoji logging (`Emoji.CORRECT`, `Emoji.ERROR`).
- **HTML/CSS Formatting**: Generates styled HTML `<span>` output powered by `j2html`.

### ⚙️ Multi-Format & Ciphers
- **Encodings**: Base64, Hexadecimal, 8-bit Binary representations.
- **Ciphers & Fun Translations**: Leetspeak, ROT13, Caesar Cipher, Pig Latin, NATO Phonetic Alphabet, and Morse Code.
- **Text Utilities**: Palindrome highlighting, word frequency counting, length scrambling, and synonym replacement.

### 🚀 Performance & Architecture
- **Async Logging**: Non-blocking log processing using `CompletableFuture`.
- **Composite Logger**: Broadcast single log calls to multiple log targets simultaneously.
- **Environment Aware**: Automatically adapts output for `development` vs `production`.
- **Level-Based Filtering**: standard `TRACE`, `DEBUG`, `INFO`, `WARN`, and `ERROR` thresholds.

---

## 🚀 Quick Start

### Build & Run Demonstration Suite

```bash
# Run Java Demonstration Suite
./gradlew runLoggerTest

# Run Interactive Streamlit Web App
python3 -m streamlit run app.py
```

### Usage Example

```java
import org.example.Logger;
import org.example.ColorCodes;

public class Example {
    public static void main(String[] args) {
        Logger logger = Logger.getDefaultLogger();

        // PII Masking
        logger.logWithMaskedPii("User email is john@example.com");

        // NATO Phonetic
        logger.logInNatoPhonetic("FlexiLogger");

        // Colored Logging
        Logger redLogger = Logger.getRedDefaultLogger();
        redLogger.log("Critical Alert!");
    }
}
```
