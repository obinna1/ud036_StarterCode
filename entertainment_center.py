import media
import fresh_tomatoes


godzilla = media.Movie("Godzilla","urban",
                       "https://pmchollywoodlife.files.wordpress.com/2014/05/godzilla-poster-lead.jpg?w=600",
                       "https://www.youtube.com/watch?v=vIu85WQTPRc&t=2s")


avatar = media.Movie("Avatar","A story about Bishop",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


jezebels = media.Movie("The Jezebels", "A story about nigerian love",
                       "https://i.ytimg.com/vi/I8EOrcZ00rE/maxresdefault.jpg",
                       "https://www.youtube.com/watch?v=I8EOrcZ00rE")


black_apple = media.Movie("Black Apple", "A story about wicked men",
                          "http://img2.naijapals.com/pictures/600/ba54c1b972c3a0fc51a9748232283d21.jpg",
                          "https://www.youtube.com/watch?v=aTo9nhoPlAE")

instagram_girls = media.Movie("Instragram Girls", "A story about escort girls", 
                              "https://i.ytimg.com/vi/eHWC08Re_C8/maxresdefault.jpg",
                              "https://www.youtube.com/watch?v=oA3PeXQtXuk")

single_ladies = media.Movie("Single ladies", "A story about extravagant ladies",
                            "https://i.ytimg.com/vi/xjr-1DH3xA4/maxresdefault.jpg",
                            "https://www.youtube.com/watch?v=24Dc67ZQBug")

undercover_lover = media.Movie("Undercover Lover", "A story about love",
                               "https://i.ytimg.com/vi/XzJJBeAVZVE/maxresdefault.jpg",
                               "https://www.youtube.com/watch?v=3Vj94AB5gtE")


movies = [godzilla, avatar,jezebels,black_apple,instagram_girls,single_ladies,undercover_lover]
fresh_tomatoes.open_movies_page(movies)
