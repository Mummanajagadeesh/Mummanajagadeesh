import random
from datetime import datetime, timedelta

# Generate IST timestamp
ist_now = datetime.utcnow() + timedelta(hours=5, minutes=30)
timestamp = ist_now.strftime('%Y-%m-%d %H:%M:%S IST')

# Greetings with base weights
greetings_with_weights = [
    ("こんにちは、世界！ I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 30),
    ("안녕하세요, 세계! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 30),
    ("你好，世界！I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 30),
    ("ሰላም ዓለም! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 30),
    ("வணக்கம் உலகம்! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 30),

    ("हॅलो वर्ल्ड! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),
    ("হ্যালো বিশ্ব! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),
    ("ສະບາຍດີໂລກ! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),
    ("မင်္ဂလာပါ ကမ္ဘာလောက! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),
    ("สวัสดีโลก! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),

    ("བཀྲ་ཤིས་བདེ་ལེགས། འཛམ་གླིང་! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 15),
    ("Բարեւ աշխարհ! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 15),
    ("გამარჯობა მსოფლიო! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 15),

    ("नमस्ते दुनिया! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),
    ("ਹੈਲੋ ਦੁਨਿਆ! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),
    ("ନମସ୍କାର ବିଶ୍ୱ! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),
    ("ഹലോ ലോകം! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),

    ("Bonjour le monde! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),
    ("¡Hola, mundo! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),
    ("Hallo Welt! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),
    ("Olá, mundo! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),
    ("Ciao mondo! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),
    ("Witaj świecie! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),
    ("Привет, мир! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),
    ("Kamusta, mundo! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),
    ("Xin chào, thế giới! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),

    ("Hello, world! I'm [Jagadeesh](https://mummanajagadeesh.github.io/).", 1),
]


def non_latin_ratio(text):
    chars = [c for c in text if c.isalpha()]
    if not chars:
        return 0
    non_latin = sum(1 for c in chars if ord(c) > 127)
    return non_latin / len(chars)

boosted = []
for greeting, base_weight in greetings_with_weights:
    ratio = non_latin_ratio(greeting)

    # Boost factor: 1.0 → 3.0
    boost = 1 + (ratio * 2)

    boosted_weight = int(base_weight * boost)
    boosted.append((greeting, boosted_weight))

# Separate greetings and weights
greetings, weights = zip(*boosted)

# Weighted random selection
new_greeting = random.choices(greetings, weights=weights, k=1)[0]

# Markdown header with timestamp
greeting_line = f"# {new_greeting} <!-- updated: {timestamp} -->\n"

# Update README.md
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

lines[0] = greeting_line

with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(lines)
