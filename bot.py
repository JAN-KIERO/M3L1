import discord
import os
import random
import requests
from discord.ext import commands
from generator import gen
from young import you
from emojis import gen_emoji
from flip_coin import flip


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
    
@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user:
        return
    
    await before.channel.send("Treść wiedomości przed edycją: " + before.content)
    
@bot.command()
async def password(ctx, count_gen = 8):
    await ctx.send(gen(count_gen))
    

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def spam(ctx, yourword = "", count_word = 5):
    await ctx.send(yourword * count_word)


@bot.command()
async def word(ctx, wordls = ""):
    await ctx.send(you(wordls))

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emoji())
    
@bot.command()
async def flip_coin(ctx):
    await ctx.send(flip())
    
@bot.command()
async def bye(ctx):
    await ctx.send("\U0001F44B")

@bot.command()
async def mem(ctx):
    imgs = os.listdir("images")
    img_name = random.choice(imgs)
    with open(f'images/{img_name}', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

@bot.command()
async def photocar(ctx):
    imgsc = os.listdir("cars")
    imgc_name = random.choice(imgsc)
    with open(f'cars/{imgc_name}', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
    
@bot.command()
async def photoele(ctx):
    imgse = os.listdir("ele")
    imge_name = random.choice(imgse)
    with open(f'ele/{imge_name}', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)



def get_random_image_url():    
    url = 'https://picsum.photos/3840/2160'
    res = requests.get(url)
    return res.url

@bot.command('photo')
async def photo(ctx):
    image_url = get_random_image_url()
    await ctx.send(image_url)


def get_random_imagegrayscale_url():    
    url = 'https://picsum.photos/3840/2160/?grayscale'
    res = requests.get(url)
    return res.url

@bot.command('photobaw')
async def photobaw(ctx):
    imagegrayscale_url = get_random_imagegrayscale_url()
    await ctx.send(imagegrayscale_url)
    
    
def get_random_imageblur_url():    
    url = 'https://picsum.photos/3840/2160/?blur'
    res = requests.get(url)
    return res.url

@bot.command('photoblur')
async def photoblur(ctx):
    imageblur_url = get_random_imageblur_url()
    await ctx.send(imageblur_url)


animals = [("https://random-d.uk/api/random", "url"), ("https://randomfox.ca/floof/", "image"), ("https://dog.ceo/api/breeds/image/random", "message"), ("https://api.thecatapi.com/v1/images/search", "url_list"), ("https://some-random-api.com/img/panda", "link"), ("https://some-random-api.com/img/koala", "link")]

def get_animals_image_url():    
    url, kind = random.choice(animals)
    res = requests.get(url)
    data = res.json()

    
    if kind == 'url':
        result = data['url']
    elif kind == 'image':
        result = data['image']
    elif kind == 'message':
        result = data['message']
    elif kind == 'url_list':
        result = data[0]['url']
    elif kind == 'text':
        result = data['text']
    elif kind == 'link':
        result = data['link']
    
    return result

@bot.command('animal')
async def animal(ctx):
    imageanimal_url = get_animals_image_url()
    await ctx.send(imageanimal_url)
    
    
@bot.command()
async def helpbot(ctx):
    await ctx.send("❓💬 **JAK OBSŁUGIWAĆ CHATBOTA** 💬❓")
    await ctx.send("- 📌 **Edytowanie wiadomości:** jeśli edytujesz wiadomość, CHATBOT wyśle treść wiadomości **przed** edycją 📝📬")
    await ctx.send("- 🔑 **Generowanie hasła:** wpisz `$password <liczba znaków>` (jeśli liczba nie zostanie podana, domyślnie 8 znaków) 🔐🛡️")
    await ctx.send("- 👋 **Powitanie:** wpisz `$hello`, a bot się z Tobą przywita 🤖🙌")
    await ctx.send("- 👋 **Pożegnanie:** wpisz `$bye`, a bot się z Tobą pożegna 💬👋")
    await ctx.send("- ⚡ **Spam:** wpisz `$spam <słowo> <liczba powtórzeń>` (jeśli liczba nie zostanie podana, domyślnie 5 powtórzeń) 🌀🔁")
    await ctx.send("- 📖 **Definicje słów:** wpisz `$word <CRINGE/LOL/ROFL/SHEESH/CREEPY>`, a CHATBOT poda definicję 🧐📚")
    await ctx.send("- 😂 **Mem:** wpisz `$mem`, a bot wyśle losowego mema 🎉🤣")
    await ctx.send("- 🌄 **Losowe zdjęcie:** wpisz `$photo`, a bot wyśle losowe zdjęcie 📷🏞️")
    await ctx.send("- ⚫ **Czarno-białe zdjęcie:** wpisz `$photobaw`, a bot wyśle losowe czarno-białe zdjęcie 🖤🤍")
    await ctx.send("- 🌫️ **Rozmyte zdjęcie:** wpisz `$photoblur`, a bot wyśle losowe rozmyte zdjęcie 🌫️🎨")
    await ctx.send("- 🚗 **Zdjęcie samochodu:** wpisz `$photocar`, a bot wyśle losowe zdjęcie auta 🚘✨")
    await ctx.send("- 💻 **Zdjęcie elektroniki:** wpisz `$photoele`, a bot wyśle losowe zdjęcie elektroniki ⚙️🔋")
    await ctx.send("- 🐾 **Zdjęcie zwierzaka:** wpisz `$animal`, a bot wyśle losowe zdjęcie zwierzaka 🐶🐱❤️")
    await ctx.send("- 🪙 **Rzut monetą:** wpisz `$flip_coin`, a bot rzuci monetą i wyśle wynik 🪙✨")
    await ctx.send("- 😀 **Emotikon:** wpisz `$emoji`, a bot wyśle losowe emoji 😄🎭")




    
bot.run("")