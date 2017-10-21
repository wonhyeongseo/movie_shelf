'''Where movies are stored and sent to movie_shelf.py for the creation of the webpage.'''
import media
import movie_shelf

the_imitation_game = media.Movie(
    title="The Imitation Game",
    description="Sometimes it is the people no one thinks anything of, who do the things no one can imagine.",
    run_time=114,
    genre="Drama / Thriller",
    youtube_url="https://www.youtube.com/watch?v=S5CjKEFb-sM",
    img_url="https://images-na.ssl-images-amazon.com/images/M/MV5BOTgwMzFiMWYtZDhlNS00ODNkLWJiODAtZDV" +
            "hNzgyNzJhYjQ4L2ltYWdlXkEyXkFqcGdeQXVyNzEzOTYxNTQ@._V1_UX182_CR0,0,182,268_AL_.jpg"
)

doctor_strange = media.Movie(
    title="Doctor Strange",
    description="After a fatal accident, a surgeon goes on a magical journey in a strange world. Our world.",
    run_time=115,
    genre="Fantasy / SF",
    youtube_url="https://www.youtube.com/watch?v=HSzx-zryEgM",
    img_url="https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg"
)

fantastic_beasts_awtft = media.Movie(
    title="Fantastic Beasts and Where to Find Them",
    description="The adventures of writer Newt Scamander in New York's secret community of witches and wizards seventy years before Harry Potter reads his book in school.",
    run_time=133,
    genre="Fantasy / Adventure",
    youtube_url="https://www.youtube.com/watch?v=Vso5o11LuGU",
    img_url="https://upload.wikimedia.org/wikipedia/en/5/5e/Fantastic_Beasts_and_Where_to_Find_Them_poster.png"
)

movie_shelf.open_movies_page([
    the_imitation_game,
    doctor_strange,
])