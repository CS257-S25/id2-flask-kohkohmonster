from id2-flask-kohkohmonster.app import *
import unittest

class TestApp(unittest.TestCase):
    def test_homepage(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        return_statement = "Enter the URL /most_banned/<type>/<num> to see the most banned books of a certain type."
        +"\nA type is one of the following categories: author, title, district, or state."
        +"\nA num is a number that represents how many of that type one wants to see."
        +"\nFor example, /most_banned/author/5 will show the 5 most banned authors."
        self.assertIn(return_statement.encode(), response.data)

    def test_most_banned_authors(self):
        '''
        Arguments: none
        Returns: a list of the most banned authors
        This function takes in an author name and a number and returns the most banned books of that author.
        '''
        self.app = app.test_client()
        response = self.app.get('/most_banned/author/5', follow_redirects=True)
        self.assertIn(b'5 most banned authors', response.data)

    def test_most_banned_titles(self):
        '''
        Arguments: none
        Returns: a list of the most banned titles
        This function takes in a title name and a number and returns the most banned books of that title.
        '''

        self.app = app.test_client()
        response = self.app.get('/most_banned/title/5', follow_redirects=True)
        self.assertIn(b'5 most banned titles', response.data)

    def test_most_banned_districts(self):
        '''
        Arguments: none
        Returns: a list of the most banned districts
        This function takes in a district name and a number and returns the district with the most banned books.
        '''

        self.app = app.test_client()
        response = self.app.get('/most_banned/district/5', follow_redirects=True)
        self.assertIn(b'5 most banned districts', response.data)

    def test_most_banned_states(self):
        '''
        Arguments: none
        Returns: a list of the most banned states
        This function takes in a state name and a number and returns the state with the most banned books.
        '''

        self.app = app.test_client()
        response = self.app.get('/most_banned/state/5', follow_redirects=True)
        self.assertIn(b'5 most banned states', response.data)

    def test_invalid_type(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''

        self.app = app.test_client()
        response = self.app.get('/most_banned/invalid/5', follow_redirects=True)
        self.assertIn(b'Please enter a valid type: author, title, district, or state.', response.data)

    def test_invalid_number(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''

        self.app = app.test_client()
        response = self.app.get('/most_banned/author/0', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)

    def test_invalid_number_negative(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''

        self.app = app.test_client()
        response = self.app.get('/most_banned/author/-1', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)

    def test_invalid_number_non_integer(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''

        self.app = app.test_client()
        response = self.app.get('/most_banned/author/abc', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)

    def test_invalid_number_float(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''

        self.app = app.test_client()
        response = self.app.get('/most_banned/author/5.5', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)

    def test_invalid_number_string(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''

        self.app = app.test_client()
        response = self.app.get('/most_banned/author/abc', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)

    def test_invalid_number_special_characters(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''

        self.app = app.test_client()
        response = self.app.get('/most_banned/author/!@#$', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)

    def test_invalid_number_empty(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''

        self.app = app.test_client()
        response = self.app.get('/most_banned/author/', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)

    def test_invalid_number_none(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''

        self.app = app.test_client()
        response = self.app.get('/most_banned/author/None', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data) 
    
    def test_invalid_number_nan(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''
        self.app = app.test_client()
        response = self.app.get('/most_banned/author/nan', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)
    
    def test_invalid_number_inf(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''
        self.app = app.test_client()
        response = self.app.get('/most_banned/author/infinity', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)
    
    def test_invalid_number_inf_negative(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''
        self.app = app.test_client()
        response = self.app.get('/most_banned/author/-infinity', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)
    
    def test_invalid_number_inf_positive(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''
        self.app = app.test_client()
        response = self.app.get('/most_banned/author/+infinity', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)
    def test_invalid_number_inf_negative_positive(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''
        self.app = app.test_client()
        response = self.app.get('/most_banned/author/-+infinity', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)
    def test_invalid_number_inf_positive_negative(self):
        '''
        Arguments: none
        Returns: a list of the most banned books
        This function takes in a type and a number and returns the most banned books of that type. This is meant to be an edge case.
        '''
        self.app = app.test_client()
        response = self.app.get('/most_banned/author/+-infinity', follow_redirects=True)
        self.assertIn(b'Please enter a number greater than 0.', response.data)

        #How do I get flask to run? I keep receiving error 404. If my group is unable to help, ask Anya during office hours tomorrow (13:30-14:30).
        #Also, for homework one, how do I call the production code to test?
