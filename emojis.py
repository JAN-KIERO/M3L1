import random

def gen_emoji():
    emoji = [
    "\U0001F600",  # 😀 grinning face
    "\U0001F603",  # 😃 smiling face with open mouth
    "\U0001F604",  # 😄 smiling face with open mouth and smiling eyes
    "\U0001F601",  # 😁 beaming face with smiling eyes
    "\U0001F606",  # 😆 laughing
    "\U0001F605",  # 😅 smiling with sweat
    "\U0001F923",  # 🤣 rolling on the floor laughing
    "\U0001F602",  # 😂 tears of joy
    "\U0001F642",  # 🙂 slightly smiling face
    "\U0001F609",  # 😉 winking face
    "\U0001F60A",  # 😊 smiling face with smiling eyes
    "\U0001F60D",  # 😍 heart eyes
    "\U0001F618",  # 😘 blowing kiss
    "\U0001F617",  # 😗 kissing face
    "\U0001F619",  # 😙 kissing face with smiling eyes
    "\U0001F61A",  # 😚 kissing face with closed eyes
    "\U0001F970",  # 🥰 smiling with hearts
    "\U0001F60E",  # 😎 sunglasses
    "\U0001F913",  # 🤓 nerd face
    "\U0001F917",  # 🤗 hugging face
    "\U0001F92D",  # 🤭 hand over mouth
    "\U0001F92B",  # 🤫 shushing face
    "\U0001F637",  # 😷 face with mask
    "\U0001F912",  # 🤒 face with thermometer
    "\U0001F47B",  # 👻 ghost
    "\U0001F480",  # 💀 skull
    "\U0001F4A9",  # 💩 poop
    "\U0001F525",  # 🔥 fire
    "\U0001F339",  # 🌹 rose
    "\U0001F33A",  # 🌺 hibiscus
    "\U0001F331",  # 🌱 seedling
    "\U0001F340",  # 🍀 four leaf clover
    "\U0001F436",  # 🐶 dog
    "\U0001F431",  # 🐱 cat
    "\U0001F42D",  # 🐭 mouse
    "\U0001F438",  # 🐸 frog
    "\U0001F981",  # 🦁 lion
    "\U0001F42F",  # 🐯 tiger
    "\U0001F984",  # 🦄 unicorn
    "\U0001F3C6",  # 🏆 trophy
    "\U0001F389",  # 🎉 party popper
    "\U0001F381",  # 🎁 gift
    "\U0001F37A",  # 🍺 beer
    "\U0001F354",  # 🍔 burger
    "\U0001F355",  # 🍕 pizza
    "\U0001F34E",  # 🍎 red apple
    "\U0001F352",  # 🍒 cherries
    "\U0001F347",  # 🍇 grapes
    "\U0001F31F",  # 🌟 glowing star
    "\U00002764",  # ❤ heart
    "\U0001F49B",  # 💛 yellow heart
    "\U0001F49A",  # 💚 green heart
    "\U0001F499",  # 💙 blue heart
    "\U0001F49C",  # 💜 purple heart
]

    return random.choice(emoji)
