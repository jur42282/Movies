from dict import *
from users import hodnoceni_uzivatelu
import sys


user = input("Zadej sve jmeno: ").lower()


if user in hodnoceni_uzivatelu:
  print("V pořádku", oddelovac, sep="\n")
  print("VÍTEJ V NAŠÍ FILMOVÉ DATABÁZY".center(62), oddelovac, sep="\n")
  print(f"| {' | '.join(sluzby)} |".center(62), oddelovac, sep="\n")
else:
  sys.exit("Nemáte přístup do filmové databáze")

while True:
  service = input("Vyber službu: ").lower()

  if service == "dostupne filmy":
    print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())), oddelovac, sep="\n")
  elif service == "detaily filmu":
    film = input("Zadej jméno filmu: ")
    if film in filmy:
      print(f"{'DETAILY FILMU'.center(62)}", oddelovac, sep="\n")
      for k, v in filmy[film].items():
        if k == "HRAJI":
          print(f"{k}: {', '.join(v)}")
        else:
          print(f"{k}: {v}")
      print(oddelovac)
    else:
      print("Tento film není v naší databázi")
  elif service == "doporuc film":
    hodnoceni = {}
    for k, v in hodnoceni_uzivatelu.items():
      if k != user:
        for film in v:
          if film in hodnoceni:
            hodnoceni[film] += 1
          else:
            hodnoceni[film] = 1
    nejlepsi_film = max(hodnoceni, key=hodnoceni.get)
    print(f"Film, který bych ti doporučil je: {nejlepsi_film}")
  elif service == "exit":
    break
  else:
    print("Tato služba není dostupná")
