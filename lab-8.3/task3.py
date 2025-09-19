import unittest
import re
# Function under test
def is_sentence_palindrome(sentence):
    # Normalize: remove punctuation, spaces, convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', sentence).lower()
    return cleaned == cleaned[::-1]
class TestIsSentencePalindrome(unittest.TestCase):
    def test_classic_palindrome(self):
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))
    def test_palindrome_with_punctuation(self):
        self.assertTrue(is_sentence_palindrome("No lemon, no melon"))
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_sentence_palindrome("Madam, I'm Adam"))
    def test_simple_word_palindrome(self):
        self.assertTrue(is_sentence_palindrome("Racecar"))
    def test_phrase_palindromes(self):
        self.assertTrue(is_sentence_palindrome("Never odd or even"))
        self.assertTrue(is_sentence_palindrome("Step on no pets"))
        self.assertTrue(is_sentence_palindrome("Able was I, ere I saw Elba"))
    def test_non_palindromes(self):
        self.assertFalse(is_sentence_palindrome("Hello World"))
        self.assertFalse(is_sentence_palindrome("OpenAI rocks"))
        self.assertFalse(is_sentence_palindrome("This is not a palindrome"))
    def test_edge_cases(self):
        self.assertTrue(is_sentence_palindrome(""))  # empty string
        self.assertTrue(is_sentence_palindrome("!!!"))  # only punctuation
        self.assertTrue(is_sentence_palindrome("A"))  # single character
if __name__ == "__main__":
    unittest.main()