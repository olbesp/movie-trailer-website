import fresh_tomatoes
import media

'''
These variables means my created objects or movies
which have three parameters:
1. Movie title
2. Link with movie poster
3. Link with movie trailer on YouTube.com
'''
fight_club = media.Movie(
    "Fight Club",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=J6UNxHywwXQ"
)

revolver = media.Movie(
    "Revolver",
    "https://upload.wikimedia.org/wikipedia/en/b/b6/Revolver2005.jpg",
    "https://www.youtube.com/watch?v=e3REQGksaVE"
)

the_revenant = media.Movie(
    "The Revenant",
    "https://goo.gl/jVaEjq",
    "https://www.youtube.com/watch?v=LoebZZ8K5N0"
    )

shutter_island = media.Movie(
    "Shutter Island",
    "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
    "https://www.youtube.com/watch?v=lhBTlYQcBC0"
)

prisoners = media.Movie(
    "Prisoners",
    "https://upload.wikimedia.org/wikipedia/en/6/63/Prisoners2013Poster.jpg",
    "https://www.youtube.com/watch?v=bpXfcTF6iVk"
)

hacksaw_ridge = media.Movie(
    "Hacksaw Ridge",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Hacksaw_Ridge_poster.png",
    "https://www.youtube.com/watch?v=s2-1hz1juBI"
)

inglourious_basterds = media.Movie(
    "Inglourious Basterds",
    "https://goo.gl/ZEype9",
    "https://www.youtube.com/watch?v=KnrRy6kSFF0"
)

a_beautiful_mind = media.Movie(
    "A Beautiful Mind",
    "https://goo.gl/wHpAaA",
    "https://www.youtube.com/watch?v=WFJgUm7iOKw"
)

gladiator = media.Movie(
    "Gladiator",
    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=W1rNFuKFTnc"
)

# A list contains all movies objects in it
movies = [
    fight_club, revolver, the_revenant, shutter_island, prisoners,
    hacksaw_ridge, inglourious_basterds, a_beautiful_mind, gladiator
]

fresh_tomatoes.open_movies_page(movies)
# takes as input a list of movies and opens the webpage with trailers
