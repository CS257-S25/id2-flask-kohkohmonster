'''
This code is a Flask application that serves as a web interface for
 the most_banned books as well as its statistics.
It allows users to select a type of data 
(author, title, district, or state) and the number of items to display.
'''

from flask import Flask
from ProductionCode import most_banned
from ProductionCode import search

app = Flask(__name__)

@app.route('/')
def homepage():
    '''
    This is the homepage where the user can select a link to another webpage.
    '''
    one = "Enter the URL /most_banned/<type>/<num>"
    two = "\nto see the most banned books of a certain type."
    three = "\nA type is one of the following categories: author, title, district, or state."
    four = "\nA num is a number that represents how many of that type one wants to see."
    five = "\nFor example, /most_banned/author/5 will show the 5 most banned authors."
    return_statement = one + two + three + four + five

    return return_statement

@app.route('/most_banned/<type>/<num>')
def most_banned_category(type, num):
    '''
    This function takes in a type and a number and returns the most banned books of that type.
    '''

    number = int(num)
    # This checks if the type is a string and the number is an integer greater than 0.
    if number < 1:
        return "Please enter a number greater than 0."
    # This grabs the author with the most banned books.
    if type == "author":
        most_banned_type = most_banned.most_banned_authors(number)
    # This grabs the title with the most banned books.
    elif type == "title":
        most_banned_type = most_banned.most_banned_titles(number)
    # This grabs the district with the most banned books.
    elif type == "district":
        most_banned_type = most_banned.most_banned_districts(number)
    # This grabs the state with the most banned books.
    elif type == "state":
        most_banned_type = most_banned.most_banned_states(number)
    # This is the default case if the type is not one of the above.
    else:
        return "Please enter a valid type: author, title, district, or state."
    return most_banned_type
if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)

@app.route('/search_genre/<genre>')
def search_genre(genre):
    '''
    This function takes in a genre and returns the books of that genre.
    '''

    # This checks if the genre is a string.
    if not isinstance(genre, str):
        return "Please enter a valid genre."
    
    # This checks if the genre is empty.
    if genre == "":
        return "Please enter a valid genre."
    
    # This checks if the genre is a string and the number is an integer greater than 0.
    if genre.isdigit():
        return "Please enter a valid genre."

    # This grabs the books of the genre.
    matching_books = search.search_genre(genre)
