import unittest
import sys
import password
from unittest.mock import patch
from io import StringIO
class TestPasswordGen(unittest.TestCase):

    def test_password_type_str(self):
        gen_pass = password.get_password(8)
        self.assertTrue(type(gen_pass), str)

    def test_password_len(self):
        gen_pass = password.get_password(5)
        print(gen_pass)
        self.assertEqual(len(gen_pass), 5)
    
    def test_create_pass(self):
        with patch('sys.stdout', StringIO()) as out:
            gen_pass = password.get_password(15)
            password.set_write_pass("John", gen_pass, "microsoft")
            output = out.getvalue().strip()
        self.assertEqual(output, "You have an account with the same info!")
        

sys.stdout = StringIO()
        
        


if __name__ == "__main__":
    unittest.main()


