import fresh_tomatoes
import media

# Create Instances with Attributes to Determine Movie Characteristics
batman_forever = media.Movie(
    "Batman Forever",
    "2h 2m",
    "Percorrendo as ruas de Gothan, Batman está pronto para defender a lei, "
    "mas desta vez o perigo vem em dobro."
    "O vilão Duas Caras conta com a sorte para se vingar de Batman e Charada "
    "é um gênio criminoso cheio de truques e ideias diabólicas",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/Batman_Forever_poster.png",
    "The legendary dark knight, Batman.",
    "9 de junho de 1995 (EUA)",
    "https://www.youtube.com/watch?v=E5vZWrsaYWU"
    )

avatar = media.Movie(
    "Avatar",
    "2h 42m",
    "No exuberante mundo alienígena de Pandora vivem os Na'vi, seres que "
    "parecem ser primitivos, mas são altamente evoluídos."
    "Como o ambiente do planeta é tóxico, foram criados os avatares, "
    "corpos biológicos controlados pela mente humana que se movimentam"
    "livremente em Pandora.",
    "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "A marine on an alien Planet",
    "18 de dezembro de 2009 (Brasil)",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

hobbit_final = media.Movie(
    "The Battle of the Five Armies",
    "2h 44m",
    "O dragão Smaug lança sua fúria ardente contra a Cidade do Lago "
    "que fica próxima da montanha de Erebor. Bard consegue derrotá-lo, "
    "mas, rapidamente, sem a ameaça do dragão, inicia-se uma batalha "
    "pelo controle de Erebor e sua riqueza.",
    "https://upload.wikimedia.org/wikipedia/en/0/0e/"
    "The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg",
    "The fantastic battle of armies",
    "7 de dezembro de 2014 (Brasil)",
    "https://www.youtube.com/watch?v=hftfDwib1ds"
    )

thor_ragnarok = media.Movie(
    "Ragnarok",
    "2h 10m",
    "Thor está preso do outro lado do universo. Ele precisa correr contra "
    "o tempo para voltar a Asgard e parar Ragnarok, a destruição de "
    "seu mundo, que está nas mãos da poderosa e implacável vilã Hela.",
    "https://upload.wikimedia.org/wikipedia/id/b/be/"
    "Thor_Ragnarok_poster_2.jpg",
    "Thor is an American superhero based in the world of Marvel Comics",
    "October 10, 2017",
    "https://www.youtube.com/watch?v=UvNnqWLruXA"
    )

truman_show = media.Movie(
    "The Truman Show",
    "1h 43m",
    "Truman Burbank é um pacato vendedor de seguros que leva uma "
    "vida simples com sua esposa Meryl Burbank. Porém algumas coisas "
    "ao seu redor fazem com que ele passe a estranhar sua cidade, seus "
    "supostos amigos e até sua mulher.",
    "https://upload.wikimedia.org/wikipedia/pt/8/85/"
    "TheTrumanShow.jpg",
    "In this movie, Truman is a man whose life is a fake one",
    "30 de outubro de 1998 (Brasil)",
    "https://www.youtube.com/watch?v=c3gI9ms8Fdc"
    )

forrest_gump = media.Movie(
    "Forrest Gump",
    "2h 22m",
    "Mesmo com o raciocínio lento, Forrest Gump nunca se "
    "sentiu desfavorecido. Graças ao apoio da mãe, ele teve uma vida "
    "normal. Seja no campo de futebol como um astro do esporte, lutando "
    "no Vietnã ou como capitão de um barco de camarão, Forrest inspira a "
    "todos com seu otimismo infantil.",
    "https://upload.wikimedia.org/wikipedia/en/6/67/"
    "Forrest_Gump_poster.jpg",
    "Forrest Gump is a simple man with a low I.Q. but good intentions",
    "7 de dezembro de 1994 (Brasil)",
    "https://www.youtube.com/watch?v=p0p5CQUjTxI"
    )


# Objects that will bring content to the website
movies = [
    batman_forever, avatar, hobbit_final,
    thor_ragnarok, truman_show, forrest_gump
    ]

# Open an HTML to view the cover of the movies and their trailers
fresh_tomatoes.open_movies_page(movies)
