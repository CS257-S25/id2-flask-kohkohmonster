'''
    This class tests the app.py file.
    It tests the functions in the app.py file.
    It tests the homepage function and the most_banned_category function.
    It tests the most_banned_authors function, the most_banned_titles function,
    the most_banned_districts function, and the most_banned_states function.
    It tests the search_genre function.
'''
import unittest
from app import app

class TestApp(unittest.TestCase):
    '''
   This class tests all the aspects of the app for banned books.
    '''
    def test_homepage(self):
        '''
        This is a test for the homepage of the app.
        '''

        client_one = app.test_client()
        response = client_one.get('/', follow_redirects=True)
        one = "Enter the URL /most_banned/<type>/<num>"
        two = "to see the most banned books of a certain type."
        three = "A type is one of the following categories: author, title, district, or state."
        four = "A num is a number that represents how many of that type one wants to see."
        five = "For example, /most_banned/author/5 will show the 5 most banned authors."
        return_statement = one + two + three + four + five
        self.assertIn(return_statement.encode(), response.data)

    def test_most_banned_authors(self):
        '''
        Arguments: none
        Returns: a list of the most banned authors
        This function takes in an author name and a number and returns
        the most banned books of that author.
        '''
        client_one = app.test_client()
        response = client_one.get('/most_banned/author/5', follow_redirects=True)
        one = "Ellen Hopkins: 791"
        two = "Sarah J. Maas: 657"
        three = "Jodi Picoult: 213"
        four = "John Green: 203"
        five = "Toni Morrison: 197"
        author = one+two+three+four+five
        self.assertIn(author.encode('utf-8'), response.data)

    def test_most_banned_titles(self):
        '''
        Arguments: none
        Returns: a list of the most banned titles
        This function takes in a title name and a number and returns
        the most banned books of that title.
        '''
        client_one = app.test_client()
        response = client_one.get('/most_banned/title/5', follow_redirects=True)
        one = "Looking for Alaska: 135"
        two = "Nineteen Minutes: 126"
        three = "The Perks of Being a Wallflower: 118"
        four = "Sold: 116"
        five = "Thirteen Reasons Why: 112"
        client = one+two+three+four+five
        self.assertIn(client.encode('utf-8'), response.data)

    def test_most_banned_districts(self):
        '''
        Arguments: none
        Returns: a list of the most banned districts
        This function takes in a district name and a number and returns
        the district with the most banned books.
        '''
        client_one = app.test_client()
        response = client_one.get('/most_banned/district/5', follow_redirects=True)
        one = "Escambia County Public Schools: 1787"
        two = "Clay County School District: 864"
        three = "Orange County Public Schools: 734"
        four = "North East Independent School District: 606"
        five = "Central York School District: 443"
        district = one+two+three+four+five
        self.assertIn(district.encode('utf-8'), response.data)

    def test_most_banned_states(self):
        '''
        Arguments: none
        Returns: a list of the most banned states
        This function takes in a state name and a number and returns
        the state with the most banned books.
        '''
        client_one = app.test_client()
        response = client_one.get('/most_banned/state/5', follow_redirects=True)
        one = "Florida: 6533"
        two = "Iowa: 3685"
        three = "Texas: 1964"
        four = "Pennsylvania: 664"
        five = "Wisconsin: 480"
        states = one + two + three + four + five
        self.assertIn(states.encode('utf-8'), response.data)

    def test_invalid_type(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns
        the most banned books of that type.
        This is meant to be an edge case.
        '''
        client_one = app.test_client()
        response = client_one.get('/most_banned/invalid/5', follow_redirects=True)
        self.assertIn(b'Please enter a valid type: author, title, district, or state.',
                      response.data)

    def test_invalid_number(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and
        returns the most banned books of that type. 
        This is meant to be an edge case.
        '''
        client_one = app.test_client()
        response = client_one.get('/most_banned/author/0', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)

    def test_invalid_number_negative(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns
        the most banned books of that type. 
        This is meant to be an edge case.
        '''
        client_one = app.test_client()
        response = client_one.get('/most_banned/author/-1', follow_redirects=True)
        self.assertIn(b'Please enter a valid number.', response.data)

    def test_invalid_number_non_integer(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns
        the most banned books of that type.
        This is meant to be an edge case.
        '''
        client_one = app.test_client()
        response = client_one.get('/most_banned/author/abc', follow_redirects=True)
        self.assertIn(b'Please enter a valid number.', response.data)

    def test_invalid_number_float(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns
        the most banned books of that type.
        This is meant to be an edge case.
        '''
        client_one = app.test_client()
        response = client_one.get('/most_banned/author/5.5', follow_redirects=True)
        self.assertIn(b'Please enter a valid number.', response.data)

    def test_invalid_number_string(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns
        the most banned books of that type.
        This is meant to be an edge case.
        '''
        client_one = app.test_client()
        response = client_one.get('/most_banned/author/abc', follow_redirects=True)
        self.assertIn(b'Please enter a valid number.', response.data)

    def test_invalid_number_special_characters(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and
        returns the most banned books of that type.
        This is meant to be an edge case.
        '''
        client_one = app.test_client()
        response = client_one.get('/most_banned/author/!@#$', follow_redirects=True)
        self.assertIn(b'Please enter a valid number.', response.data)

    def test_invalid_genre(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a genre and returns the books of that genre.
        This is meant to be an edge case.
        '''
        client_one = app.test_client()
        response = client_one.get('/search_genre/123', follow_redirects=True)
        self.assertIn(b'Please enter a valid genre.', response.data)

    def most_banned_category(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns
        the most banned books of that type.
        This is meant to be an edge case.
        '''
        client_one = app.test_client()
        response = client_one.get('/most_banned/author/5', follow_redirects=True)
        self.assertIn(b'Please enter a valid type: author, title, district, or state.', response.data)

    def test_search_genre_empty(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a genre and returns the books of that genre.
        This is meant to be an edge case.
        '''
        client_one = app.test_client()
        response = client_one.get('/search_genre/', follow_redirects=True)
        self.assertIn(b'Please enter a valid genre.', response.data)

    def page_not_found(self):
            '''
            Arguments: none
            Returns: a list of the most banned books
            This function takes in a type and a number and returns
            the most banned books of that type.
            This is meant to be an edge case.
            '''
            client_one = app.test_client()
            response = client_one.get('/invalid', follow_redirects=True)
            self.assertIn(b'Page not found', response.data)

    def error_handler(self):
            '''
            Arguments: none
            Returns: a list of the most banned books
            This function takes in a type and a number and returns
            the most banned books of that type.
            This is meant to be an edge case.
            '''
            client_one = app.test_client()
            response = client_one.get('/invalid', follow_redirects=True)
            self.assertIn(b'Page not found', response.data)
