import random
from datetime import datetime, timedelta

# Generate IST timestamp
ist_now = datetime.utcnow() + timedelta(hours=5, minutes=30)
timestamp = ist_now.strftime('%Y-%m-%d %H:%M:%S IST')

# Multilingual greetings with weights
greetings_with_weights = [
    # High frequency — visually complex, non-Latin scripts
    ("こんにちは、世界！ This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 30),  # Japanese
    ("안녕하세요, 세계! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 30),  # Korean
    ("你好，世界！This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 30),  # Chinese
    ("مرحبا بالعالم! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 30),  # Arabic
    ("ሰላም ዓለም! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 30),  # Amharic
    ("வணக்கம் உலகம்! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 30),  # Tamil
    ("हॅलो वर्ल्ड! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),  # Marathi
    ("হ্যালো বিশ্ব! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),  # Bengali
    ("ہیلو دنیا! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),  # Urdu
    ("ສະບາຍດີໂລກ! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),  # Lao
    ("မင်္ဂလာပါ ကမ္ဘာလောက! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),  # Burmese
    ("สวัสดีโลก! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),  # Thai
    ("שלום עולם! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 20),  # Hebrew
    ("བཀྲ་ཤིས་བདེ་ལེགས། འཛམ་གླིང་! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 15),  # Tibetan
    ("Բարեւ աշխարհ! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 15),  # Armenian
    ("გამარჯობა მსოფლიო! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 15),  # Georgian

    # Medium frequency — Indian + non-English Latin languages
    ("नमस्ते दुनिया! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # Hindi
    ("ਹੈਲੋ ਦੁਨਿਆ! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # Punjabi
    ("ନମସ୍କାର ବିଶ୍ୱ! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # Odia
    ("ഹലോ ലോകം! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # Malayalam
    ("Bonjour le monde! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # French
    ("¡Hola, mundo! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # Spanish
    ("Hallo Welt! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # German
    ("Olá, mundo! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # Portuguese
    ("Ciao mondo! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # Italian
    ("Witaj świecie! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # Polish
    ("Привет, мир! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # Russian
    ("Kamusta, mundo! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # Filipino
    ("Xin chào, thế giới! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 10),  # Vietnamese

    # Low frequency — English only
    ("Hello, world! This is [Jagadeesh](https://mummanajagadeesh.github.io/).", 1),  # English
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
