import random
from datetime import datetime, timedelta

# Generate IST timestamp
ist_now = datetime.utcnow() + timedelta(hours=5, minutes=30)
timestamp = ist_now.strftime('%Y-%m-%d %H:%M:%S IST')

# Multilingual greetings with weights
greetings_with_weights = [
    # High frequency
    ("こんにちは、世界！これは [Jagadeesh](https://mummanajagadeesh.github.io/) です。", 20),  # Japanese
    ("Hallo Welt! Das ist [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),  # German
    ("¡Hola, mundo! Este es [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),  # Spanish
    ("Bonjour le monde ! C'est [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),  # French
    ("Ciao mondo! Questo è [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),  # Italian

    # Medium frequency
    ("Привет, мир! Это [Jagadeesh](https://mummanajagadeesh.github.io/).", 5),  # Russian
    ("안녕하세요, 세계! 이것은 [Jagadeesh](https://mummanajagadeesh.github.io/) 입니다.", 5),  # Korean
    ("你好，世界！这是 [Jagadeesh](https://mummanajagadeesh.github.io/)。", 5),  # Chinese
    ("Olá, mundo! Este é o [Jagadeesh](https://mummanajagadeesh.github.io/).", 5),  # Portuguese
    ("Merhaba dünya! Bu [Jagadeesh](https://mummanajagadeesh.github.io/).", 5),  # Turkish
    ("مرحبا بالعالم! هذا هو [Jagadeesh](https://mummanajagadeesh.github.io/).", 5),  # Arabic
    ("Witaj świecie! To jest [Jagadeesh](https://mummanajagadeesh.github.io/).", 5),  # Polish
    ("Kamusta, mundo! Ito si [Jagadeesh](https://mummanajagadeesh.github.io/).", 5),  # Filipino
    ("Xin chào, thế giới! Đây là [Jagadeesh](https://mummanajagadeesh.github.io/).", 5),  # Vietnamese

    # Low frequency
    ("Hello, world! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 1),  # English
    ("नमस्ते दुनिया! यह [Jagadeesh](https://mummanajagadeesh.github.io/) है।", 1),  # Hindi
]

# Separate greetings and weights
greetings, weights = zip(*greetings_with_weights)

# Choose one greeting based on frequency weights
new_greeting = random.choices(greetings, weights=weights, k=1)[0]

# Format as markdown header
greeting_line = f"# {new_greeting} <!-- updated: {timestamp} -->\n"

# Read current README
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Replace the first line with the weighted greeting
lines[0] = greeting_line

# Write updated lines back
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(lines)
