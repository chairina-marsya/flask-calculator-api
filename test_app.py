import unittest
import json
from app import app

class CalculatorAPITest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_add(self):
        response = self.client.get("/add?a=10&b=10")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["result"], 20)
        
    def test_multiply(self):
        response = self.client.post("/calculate", json={"a":10,"b":5,"operation":"multiply"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["result"], 50)
        
if __name__ == '__main__':
    unittest.main()