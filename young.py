def you(wordls):

    meme_dict = {
                "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
                "LOL": "Częsta reakcja na coś zabawnego", "ROFL": "odpowiedź na żart", "SHEESH": "lekka dezaprobata", "CREEPY": "straszny, złowieszczy", "AGGRO": "stać się agresywnym/zły"
                }
    if wordls in meme_dict:
        return meme_dict[wordls]
    else:
        return ("Nie ma takiego słowa!")