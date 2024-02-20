oddelovac = "=" * 62
sluzby = ("dostupne filmy", "detaily filmu", "doporuc film")

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}

film_5 = {
    "JMENO": "Oppenheimer",
    "HODNOCENI": "90/100",
    "ROK": 2023,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 180,
    "HRAJI": ("Cillian Murphy", "Emily Blunt", "Matt Damon",
    "Robert Downey Jr.", "Kenneth Branagh", "Aaron Taylor-Johnson",
    "James D'Arcy"
    )
}

film_6 = {
    "JMENO": "Interstellar",
    "HODNOCENI": "74/100",
    "ROK": 2014,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 169,
    "HRAJI": ("Matthew McConaughey", "Anne Hathaway", "Jessica Chastain",
    "Bill Irwin", "Ellen Burstyn", "John Lithgow", "Michael Caine", "Casey Affleck"
    )
}

filmy = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3,
    film_4["JMENO"]: film_4,
    film_5["JMENO"]: film_5,
    film_6["JMENO"]: film_6
}