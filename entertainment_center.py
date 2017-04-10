import media
import fresh_tomatoes


godzilla = media.Movie("Godzilla","urban",
                       "http://www.planwallpaper.com/static/images/canberra_hero_image_JiMVvYU.jpg",
                       "https://www.youtube.com/watch?v=vIu85WQTPRc")



avatar = media.Movie("Avatar","A story about Bishop",
                     "https://www.w3schools.com/css/trolltunga.jpg",
                     "https://www.youtube.com/watch?v=helEv0kGHd4")



jezebels = media.Movie("The Jezebels", " A story about nigerian love",
                       "http://www.planwallpaper.com/static/images/tree-247122.jpg",
                       "https://www.youtube.com/watch?v=I8EOrcZ00rE")

black_apple = media.Movie("Black Apple", "A story about wicked men",
                          "http://www.planwallpaper.com/static/images/nasas-images-of-most-remarkable-events-you-cant-miss.jpg",
                          "https://www.youtube.com/watch?v=aTo9nhoPlAE")

black_apple = media.Movie("Black Apple", "A story about wicked men",
                          "http://www.planwallpaper.com/static/images/nasas-images-of-most-remarkable-events-you-cant-miss.jpg",
                          "https://www.youtube.com/watch?v=aTo9nhoPlAE")

black_apple = media.Movie("Black Apple", "A story about wicked men",
                          "http://www.planwallpaper.com/static/images/nasas-images-of-most-remarkable-events-you-cant-miss.jpg",
                          "https://www.youtube.com/watch?v=aTo9nhoPlAE"


movies = [godzilla, avatar,jezebels,black_apple]
fresh_tomatoes.open_movies_page(movies)

