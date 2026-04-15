import movie_rating_system

from unittest import TestCase

class MyTestCase(TestCase):
    def test_add_movies(self):

        movies = movie_rating_system
        actual = movies.add_movies("Supper man")
        actual = movies.add_movies("Wonder Woman")
        actual = movies.add_movies("Mika")
        actual = movies.add_movies("manny")

        self.assertEqual(actual,"Movie Added Successfully")


    def test_movie_rating(self):
        movies_ratings = movie_rating_system
        rate = movies_ratings.rate_movies(5)
        rate = movies_ratings.rate_movies(4)

        self.assertEqual(rate,"Rates will be reviewed")

    def test_average_rating(self):
        movies_ratings = movie_rating_system
        average = movies_ratings.average_ratings()
        self.assertTrue(average)

    def test_average_ratings_for_a_movie(self):
        movies_ratings = movie_rating_system
        average = movies_ratings.average_ratings_for_a_movie("super man")
        self.assertTrue(average)

# if __name__ == '__main__':
#     unittest.main()
