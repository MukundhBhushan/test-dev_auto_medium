from app import app
import unittest

class FlaskTestCases(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/',content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_postform(self):
        tester = app.test_client(self)
        response = tester.post(
      '/',
      data = dict(name="Mukundh",username="mukundh")
      )
        self.assertEqual(response.status_code,200)

    
    
if __name__ == "__main__":
    unittest.main()