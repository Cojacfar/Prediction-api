import unittest
import app
import requests

class TestFlaskApiUsingRequests(unittest.TestCase):
    def test_basic(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.json(), {'CLASS': 'basic'})
    
    def test_predict(self):
        response = requests.get('http://localhost:5000/Predict', params={'Tweet': 'Hello'})
        self.assertEqual(response.json(), {'GET', 'World'})
