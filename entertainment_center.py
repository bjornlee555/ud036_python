import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story', 
						'A story about a boy and his toys that come to life',
						'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
						'https://www.youtube.com/watch?v=KYz2wyBy3kc')

print (toy_story.storyline)

avatar = media.Movie('Avatar',
					'A marine on an alien planet',
					'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
					'https://www.youtube.com/watch?v=a0CDJZu4M5I')

print avatar.storyline

terminator = media.Movie('Terminator',
						'Evil robot turns good',
						'https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg',
						'https://www.youtube.com/watch?v=c4Jo8QoOTQ4')


#avatar.show_trailer()
#terminator.show_trailer()

zoolander = media.Movie('Zoolander',
						'Male model comedy',
						'//upload.wikimedia.org/wikipedia/en/7/7c/Movie_poster_zoolander.jpg',
						'https://www.youtube.com/watch?v=YtQq0T3ExLs')

avengers = media.Movie('Avengers',
						'Superheroes unite!',
						'https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg',
						'https://www.youtube.com/watch?v=E-84FIZ8-Ow')

up = media.Movie('Up',
				'Unlikely adventure story of old man and boy',
				'https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg',
				'https://www.youtube.com/watch?v=pkqzFUhGPJg')

movies = [toy_story, avatar, terminator, zoolander, avengers, up]
fresh_tomatoes.open_movies_page(movies)