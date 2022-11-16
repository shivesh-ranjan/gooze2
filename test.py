import main
import unittest

class TestMain(unittest.TestCase):

    def sertUp(self):
        self.app = main.app.test_client()
        self.app.testing = True
    
    
   # def test_status_code(self):
    #    response = self.app.get('/')
     #   self.assertEqual(response.status_code,200)
    
    def test_greeting(self):
        greeting = 'idk idk idk'
        self.assertEqual(main.greet(),greeting)


if __name__ == '__main__':
    unittest.main()


