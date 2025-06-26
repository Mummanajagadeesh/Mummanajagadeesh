import random
from datetime import datetime, timedelta

ist_now = datetime.utcnow() + timedelta(hours=5, minutes=30)
timestamp = ist_now.strftime('%Y-%m-%d %H:%M:%S IST')

greetings = [
    "こんにちは、世界！これは [Jagadeesh](https://mummanajagadeesh.github.io/) です。",
    "Hello, world! This is [Jagadeesh](https://mummanajagadeesh.github.io/).",
    "Hola, mundo! This is [Jagadeesh](https://mummanajagadeesh.github.io/).",
    "Bonjour le monde ! This is [Jagadeesh](https://mummanajagadeesh.github.io/).",
    "Hallo Welt! This is [Jagadeesh](https://mummanajagadeesh.github.io/).",
    "Ciao mondo! This is [Jagadeesh](https://mummanajagadeesh.github.io/).",
    "Привет, мир! Это [Jagadeesh](https://mummanajagadeesh.github.io/).",
    "안녕하세요, 세계! 이것은 [Jagadeesh](https://mummanajagadeesh.github.io/) 입니다.",
    "你好，世界！这是 [Jagadeesh](https://mummanajagadeesh.github.io/)。",
    "नमस्ते दुनिया! यह [Jagadeesh](https://mummanajagadeesh.github.io/) है।"
]

new_greeting = random.choice(greetings)
greeting_line = f"# {new_greeting} <!-- updated: {timestamp} -->\n"

with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

lines[0] = greeting_line

with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(lines)
