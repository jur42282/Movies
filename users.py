hodnoceni_uzivatelu = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"},
    "lukas": {"The Dark Knight", "Oppenheimer", "Interstellar"},
}



#register user
username = str(input("Zadej sve jmeno: ").lower())

if username in hodnoceni_uzivatelu:
    print("Už jsi registrován")
else:
    films = str(input("Zadej filmy, které jsi viděl: ").split(","))
    hodnoceni_uzivatelu[username] = films
