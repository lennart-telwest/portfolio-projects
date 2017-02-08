import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://youtu.be/d1_JBMrrYw8")

single_man = media.Movie("A Single Man",
                        "An unhappy single day in the life of an unhappy single man",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/A_Single_Man.jpg",
                        "https://youtu.be/sC9Zm1UJ7zs")

big_short = media.Movie("The Big Short",
                        "An eccentric hedge fund manager discovers that the United States housing market is extremely unstable",
                        "https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg",
                        "https://youtu.be/vgqG3ITMv1Q")

inception = media.Movie("Inception",
                        "A professional thief who steals information by infiltrating the subconscious",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://youtu.be/8hP9D6kZseM")

social_network = media.Movie("The Social Network",
                        "Fictional story about the founding of facebook",
                        "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                        "https://youtu.be/2RB3edZyeYw")

francs = media.Movie("39,90",
                        "A marketeer in an existential crisis",
                        "https://images-na.ssl-images-amazon.com/images/I/71VZEkStTVL._SY445_.jpg",
                        "https://youtu.be/DiyWOU0doLc")

movies = [single_man, big_short, inception, social_network, francs, avatar]
# This function call uses list of movie instances as input to generate an HTML file
# and open it in the browser
fresh_tomatoes.open_movies_page(movies)
