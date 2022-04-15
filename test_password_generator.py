
import unittest
from Chipak_strong_password_generator import is_pwd_valid


class TestPassword(unittest.TestCase):

    def test_is_pwd_valid(self):
        # uppercase availability test
        result = is_pwd_valid("upperlower123-=*")
        self.assertFalse(result, "Uppercase not found")

        # lowercase availability test
        result = is_pwd_valid("UPPERLOWER123-=*")
        self.assertFalse(result, "Lowercase not found")

        # numbers availability test
        result = is_pwd_valid("UPPERlower_nums-=*")
        self.assertFalse(result, "Numbers not found")

        # symbols availability test
        result = is_pwd_valid("UPPERlower123symbols")
        self.assertFalse(result, "Symbols not found")

        # validity password test
        result = is_pwd_valid("UPPERlower123-=*/")
        self.assertTrue(result, "Validity test result is incorrect")


if __name__ == '__main__':
    unittest.main()
