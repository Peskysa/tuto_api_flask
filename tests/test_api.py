import unittest
from index import create_app
class APITest(unittest.TestCase):
    def setUp(self): self.client=create_app().test_client()
    def test_original(self): self.assertIn(b'Pescaa',self.client.get('/').data)
    def test_health(self): self.assertEqual(self.client.get('/health').json['status'],'ok')
    def test_sum(self): self.assertEqual(self.client.post('/api/sumar',json={'a':2,'b':3}).json,{'resultado':5})
    def test_invalid(self):
        for data in [{},{'a':True,'b':2},{'a':'1','b':3},{'a':1,'b':2,'c':3},[],{'a':float('inf'),'b':1}]:
            with self.subTest(data=data):self.assertEqual(self.client.post('/api/sumar',json=data).status_code,400)
    def test_media(self): self.assertEqual(self.client.post('/api/sumar',data='x').status_code,415)
    def test_limit(self): self.assertEqual(self.client.post('/api/sumar',data='x'*5000,content_type='application/json').status_code,413)
    def test_missing(self): self.assertEqual(self.client.get('/missing').status_code,404)
if __name__=='__main__':unittest.main()
