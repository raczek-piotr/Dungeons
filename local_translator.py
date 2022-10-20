def translate(ang, number = 0):
    lang = "PL"
    lang_PL = {
        "HERE IS A WALL": "TU JEST ŚCIANA",
        "HERE IS": "TUTAJ JEST",
        "YOU TAKE": "WZIĄŁEŚ",
        "TORCH": "POCHODNIA",
        "TORCH1": "POCHODNIĘ",
        "MIXTURE": "MIXTURKA",
        "MIXTURE1": "MIXTURKĘ",
        "ARROWS1": "STRZAŁĘ",
        "ARROWS2": "STRZAŁY",
        "ARROWS5": "STRZAŁ",
        "KNIFE": "NÓŻ",
        "DAGGER": "SZTYLET",
        "SWORD": "MIECZ",
        "MACE": "BUŁAWA",
        "SLING": "PROCA",
        "BOW": "ŁUK",
        "CROSBOW": "KUSZA",
        "FUR": "FUTRO",
        "GOLD1": "ZŁOTO",
        "GOLD2": "ZŁOTE",
        "GOLD5": "ZŁOTYCH",
        }
    langs = {
        "PL": lang_PL.get(ang+("" if number == 0 else "1" if number == 1 else "2" if number < 5 or number % 10 in [2, 3, 4] and number > 20 else "5"), ang), 
        }
    return langs.get(lang, ang)
