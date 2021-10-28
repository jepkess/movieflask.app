import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
    """
    Test class that test the reviews of the review class.
    """
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_review = Review(1234,'Test title','/khsjha27hbs','test review')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))
if __name__=='__main__':
    unittest.main()       