from flask import Flask
import random
from generator import gen

app = Flask(__name__)

facts_list = [
    "Sztuczna inteligencja może teraz generować realistyczne obrazy i teksty na podstawie krótkich opisów.",
    "Komputery kwantowe wykorzystują zjawiska kwantowe, takie jak superpozycja i splątanie, aby wykonywać obliczenia szybciej niż klasyczne komputery.",
    "Technologia 5G umożliwia przesyłanie danych z prędkością do 10 Gb/s, co jest nawet 100 razy szybsze niż 4G.",
    "Blockchain to technologia rozproszonego rejestru, która umożliwia bezpieczne i przejrzyste transakcje bez potrzeby centralnego pośrednika.",
    "Internet rzeczy (IoT) łączy codzienne urządzenia z internetem, pozwalając na zdalne sterowanie i zbieranie danych w czasie rzeczywistym.",
    "Drukowanie 3D pozwala na tworzenie trójwymiarowych obiektów z różnych materiałów, od plastiku po metal i żywe tkanki.",
    "Sztuczne sieci neuronowe są wzorowane na strukturze ludzkiego mózgu i stanowią podstawę nowoczesnego uczenia maszynowego.",
    "Technologie rozszerzonej rzeczywistości (AR) i wirtualnej rzeczywistości (VR) rewolucjonizują edukację, rozrywkę i medycynę.",
    "Autonomiczne pojazdy wykorzystują zaawansowane sensory i algorytmy AI do samodzielnej jazdy bez udziału człowieka.",
    "Kryptowaluty, takie jak Bitcoin, działają na zasadzie kryptografii i są zdecentralizowaną formą cyfrowych pieniędzy."
]

coin_list = ["🦅Orzeł🦅", "🪙Reszka🪙"]

@app.route("/")
def hello_world():
    return """
    <h1>Hello World!</h1>
    <a href="/ciekawostka">Kliknij tu aby zobaczyć ciekawostkę</a>
    <br>
    <a href="/moneta">Kliknij tu aby rzucić monetą </a>
    <br>
    <a href="/haslo">Kliknij tu aby wygenerować haslo </a>

"""

@app.route("/ciekawostka")
def ciekawostka():
    return f"""<p>{random.choice(facts_list)}</p>
        <a href="/">Kliknij tu aby zobaczyć wrócić na stronę główną</a>
    """
    
@app.route("/moneta")
def moneta():
    return f"""<p>{random.choice(coin_list)}</p>
        <a href="/">Kliknij tu aby zobaczyć wrócić na stronę główną</a>
    
    """

@app.route("/haslo")
def haslo():
    password_generated = gen()
    return f"""<p>{password_generated}</p>
<a href="/">Kliknij tu aby zobaczyć wrócić na stronę główną</a>
        
    """
        
    

app.run(debug=True)