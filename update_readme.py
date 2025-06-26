import random
from datetime import datetime, timedelta

# Generate IST timestamp
ist_now = datetime.utcnow() + timedelta(hours=5, minutes=30)
timestamp = ist_now.strftime('%Y-%m-%d %H:%M:%S IST')

# Multilingual greetings (language noted in comments)
greetings = [
    "こんにちは、世界！これは [Jagadeesh](https://mummanajagadeesh.github.io/) です。",  # Japanese
    "Hello, world! This is [Jagadeesh](https://mummanajagadeesh.github.io/).",  # English
    "¡Hola, mundo! Este es [Jagadeesh](https://mummanajagadeesh.github.io/).",  # Spanish
    "Bonjour le monde ! C'est [Jagadeesh](https://mummanajagadeesh.github.io/).",  # French
    "Hallo Welt! Das ist [Jagadeesh](https://mummanajagadeesh.github.io/).",  # German
    "Ciao mondo! Questo è [Jagadeesh](https://mummanajagadeesh.github.io/).",  # Italian
    "Привет, мир! Это [Jagadeesh](https://mummanajagadeesh.github.io/).",  # Russian
    "안녕하세요, 세계! 이것은 [Jagadeesh](https://mummanajagadeesh.github.io/) 입니다.",  # Korean
    "你好，世界！这是 [Jagadeesh](https://mummanajagadeesh.github.io/)。",  # Chinese (Simplified)
    "नमस्ते दुनिया! यह [Jagadeesh](https://mummanajagadeesh.github.io/) है।",  # Hindi
    "Olá, mundo! Este é o [Jagadeesh](https://mummanajagadeesh.github.io/).",  # Portuguese
    "Merhaba dünya! Bu [Jagadeesh](https://mummanajagadeesh.github.io/).",  # Turkish
    "مرحبا بالعالم! هذا هو [Jagadeesh](https://mummanajagadeesh.github.io/).",  # Arabic
    "Witaj świecie! To jest [Jagadeesh](https://mummanajagadeesh.github.io/).",  # Polish
    "Kamusta, mundo! Ito si [Jagadeesh](https://mummanajagadeesh.github.io/).",  # Filipino
    "Xin chào, thế giới! Đây là [Jagadeesh](https://mummanajagadeesh.github.io/).",  # Vietnamese
]

# Choose one greeting at random
new_greeting = random.choice(greetings)

# Create the updated greeting section
greeting_line = f"# 🌍 Multilingual Greeting\n\n{new_greeting}  \n<!-- updated: {timestamp} -->\n\n"

# Read the existing README
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Replace the first line with the new greeting section
lines[0] = greeting_line

# Write back to README
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(lines)
