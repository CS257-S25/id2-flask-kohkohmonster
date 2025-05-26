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
    one = "Enter the URL /most_banned/<type>/<num>, "
    two = "to see the most banned books of a certain type.<br>"
    three = "A type is one of the following categories: author, title, district, or state.<br>"
    four = "A num is a number that represents how many of that type one wants to see.<br>"
    five = "For example, /most_banned/author/5 will show the 5 most banned authors."
    return_statement = one + two + three + four + five

    return return_statement

@app.route('/most_banned/<category>/<num>')
def most_banned_category(category, num):
    '''
    This function takes in a type and a number and returns the most banned books of that type.
    '''
    try:
        # This checks if the type is a string and the number is an integer greater than 0.
        if not num.isdigit():
            return "Please enter a valid number."
    except ValueError:
        return "Please enter a valid number."
    number = int(num)
    # This checks if the type is a string and the number is an integer greater than 0.
    if number < 1:
        return "Please enter a number greater than 0."
    # This grabs the author with the most banned books.
    if category == "author":
        most_banned_type = most_banned.most_banned_authors(number)
    # This grabs the title with the most banned books.
    elif category == "title":
        most_banned_type = most_banned.most_banned_titles(number)
    # This grabs the district with the most banned books.
    elif category == "district":
        most_banned_type = most_banned.most_banned_districts(number)
    # This grabs the state with the most banned books.
    elif category == "state":
        most_banned_type = most_banned.most_banned_states(number)
    # This is the default case if the type is not one of the above.
    else:
        most_banned_type = "Please enter a valid type: author, title, district, or state."
    return most_banned_type

@app.route('/search_genre/<genre>')
def search_genre(genre):
    '''
    This function takes in a genre and returns the books of that genre.
    '''

    # This checks if the genre is a string.
    if not isinstance(genre, str):
        return "Please enter a valid genre."
    # This checks if the genre is empty.
    elif genre == "":
        return "Please enter a valid genre."
    # This checks if the genre is a string and the number is an integer greater than 0.
    elif genre.isdigit():
        return "Please enter a valid genre."

    # This grabs the books of the genre.
    matching_books = search.search_genre(genre)
    return matching_books

@app.errorhandler(404)
def page_not_found(error):
    """The endpoint for the 404 error
    Args:
        _error (Exception): the error that was raised
    Returns:
        (str): 404: Sorry page not found with usage instructions
    """
    return "404: Sorry page not found.", 404

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
