import urllib

def read_text():

	quotes = open('/Users/bjornlee/Downloads/movie_quotes.txt')
	contents = quotes.read()
	print(contents)
	quotes.close()
	check_profanity(contents)

def check_profanity(some_text):

	connection = urllib.urlopen('http://www.wdyl.com/profanity?q=' + some_text)
	output = connection.read()
	print(output)
	connection.close()

read_text()

