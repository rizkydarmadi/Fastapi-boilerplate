from unittest import IsolatedAsyncioTestCase

class TestUserApp(IsolatedAsyncioTestCase):

    async def test_aja(self):
        
        a = 2 * 3

        self.assertEqual(a,6)