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
    "SHORT SWORD": "KRÓTKI MIECZ",
    "MACE": "BUŁAWA",
    "SLING": "PROCA",
    "BOW": "ŁUK",
    "CROSBOW": "KUSZA",
    "FUR": "FUTRO",
    "YOU KILL": "ZABIŁEŚ",
    "YOU HIT": "ZRANIŁEŚ",
    "YOU MISS": "SPUDŁOWAŁEŚ W",
    "A MONSTER": "POTWORA",
    "YOU LIGHT A": "ZAPALIŁEŚ",
    "AND IT WILL GIVE YOU LIGHT FOR": "I BĘDZIE TOBIE DAWAĆ ŚWIATŁO PRZEZ",
    "TURNS": "TUR",
    "THIS TILE IS CLOSE": "TO POLE JEST ZAMKNIĘTE",
    "GOLD1": "ZŁOTO",
    "GOLD2": "ZŁOTE",
    "GOLD5": "ZŁOTYCH",
    }
def translate(ang, number = 0):
    lang = "PL"
    match lang:
        case "PL":
            return(l_pl(ang, number))
        case _:
            return(ang)
def l_pl(ang, number):
    global lang_PL
    return(lang_PL.get(ang+("" if number == 0 else "1" if number == 1 else "2" if number < 5 or number % 10 in [2, 3, 4] and number > 20 else "5"), ang))
