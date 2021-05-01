import unittest
import app


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()


if __name__ == "__main__":
    unittest.main()
