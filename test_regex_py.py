import unittest
import regex_py

class TestRegex(unittest.TestCase):

    def test_web_address(self):
        test_list = {"gmail.com": True,
                     "www@google": False,
                     "www.Coursera.org": True,
                     "web-address.com/homepage": False,
                     "My_Favorite-Blog.US": True}

        for test in test_list:
            self.assertEqual(regex_py.check_web_address(test), test_list.get(test))

    def test_check_time(self):
        test_list = {"12:45pm": True,
                     "9:59 AM": True,
                     "6:60am": False,
                     "five o'clock": False}

        for test in test_list:
            self.assertEqual(regex_py.check_time(test), test_list.get(test))

    def test_contains_acronym(self):

        test_list = {"Instant messaging (IM) is a set of communication technologies used for text-based communication": True,
                     "American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication": True,
                     "Please do NOT enter without permission!": False,
                     "PostScript is a fourth-generation programming language (4GL)": True,
                     "Have fun using a self-contained underwater breathing apparatus (Scuba)!": True}

        for test in test_list:
            self.assertEqual(regex_py.contains_acronym(test), test_list.get(test))

    def test_check_zip_code(self):

        test_list = {"The zip codes for New York are 10001 thru 11104.": True,
                     "90210 is a TV show": False,
                     "Their address is: 123 Main Street, Anytown, AZ 85258-0001.": True,
                     "The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.": False}

        for test in test_list:
            self.assertEqual(regex_py.check_zip_code(test), test_list.get(test))

    def test_transform_record(self):

        test_list = {"Sabrina Green,802-867-5309,System Administrator": "Sabrina Green,+1-802-867-5309,System Administrator",
                     "Eli Jones,684-3481127, IT specialist": "Eli Jones,+1-684-3481127, IT specialist",
                     "Melody Daniels,846-687-7436, Programmer": "Melody Daniels,+1-846-687-7436, Programmer",
                     "Charlie Rivera,698-746-3357, Web Developer": "Charlie Rivera,+1-698-746-3357, Web Developer"}

        for test in test_list:
            self.assertEqual(regex_py.transform_record(test), test_list.get(test))


    def test_multi_vowel_words(self):

        test_list = {"Life is beautiful": ['beautiful'],
                     "Obviously, the queen is courageous and gracious.": ['Obviously', 'queen', 'courageous', 'gracious'],
                     "The rambunctious children had to sit quietly and await their delicious dinner.": ['rambunctious', 'quietly', 'delicious'],
                     "The order of a data queue is First In First Out (FIFO)": ['queue'],
                     "Hello world!": []}

        for test in test_list:
            self.assertEqual(regex_py.multi_vowel_words(test), test_list.get(test))

    def test_transform_comments(self):

        test_list = {"### Start of program": "// Start of program",
                     "  number = 0   ## Initialize the variable": "  number = 0   // Initialize the variable",
                     "  number += 1   # Increment the variable": "  number += 1   // Increment the variable",
                     "  return(number)": "  return(number)"}

        for test in test_list:
            self.assertEqual(regex_py.transform_comments(test), test_list.get(test))

    def test_convert_phone_number(self):
        test_list = {"My number is 212-345-9999.": "My number is (212) 345-9999.",
                     "Please call 888-555-1234": "Please call (888) 555-1234",
                     "123-123-12345": "(123) 123-12345",
                     "Phone number of Buckingham Palace is +44 303 123 7300": "Phone number of Buckingham Palace is +44 303 123 7300"}
        for test in test_list:
            self.assertEqual(regex_py.convert_phone_number(test), test_list.get(test))


if __name__ == "__main__":
    unittest.main()
