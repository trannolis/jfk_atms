import unittest
from source import create_app


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app('source.settings', True)
        self.client = self.app.test_client()

    def test_landing(self):
        """
        Tests the "Landing" endpoint for admins
        """
        page_html = str(self.client.get('/').data)
        login_elem = 'Login'
        reg_admin_elem = 'Register a new admin'
        self.assertIn(login_elem, page_html)
        self.assertIn(reg_admin_elem, page_html)

    def test_login(self):
        """
        Tests the "Login" endpoint
        """
        page_html = str(self.client.get('/login').data)
        username_elem = 'username'
        password_elem = 'password'
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)

    def test_register_admin(self):
        """
        Tests registering Admins
        """
        page_html = str(self.client.get('/registerAdmin').data)
        username_elem = 'Username'
        password_elem = 'Password'
        first_name_elem = 'First Name'
        last_name_elem = 'Last Name'
        email_elem = 'Email'
        phone_number_elem = 'Phone No.'
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)
        self.assertIn(first_name_elem, page_html)
        self.assertIn(last_name_elem, page_html)
        self.assertIn(email_elem, page_html)
        self.assertIn(phone_number_elem, page_html)

    def test_register_atc(self):
        """
        Tests registering Air Traffic Controllers
        """
        page_html = str(self.client.get('/registerAtc').data)
        username_elem = 'Username'
        password_elem = 'Password'
        first_name_elem = 'First Name'
        last_name_elem = 'Last Name'
        email_elem = 'Email'
        phone_number_elem = 'Phone No.'
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)
        self.assertIn(first_name_elem, page_html)
        self.assertIn(last_name_elem, page_html)
        self.assertIn(email_elem, page_html)
        self.assertIn(phone_number_elem, page_html)

    def test_register_pilot(self):
        """
        Tests registering Pilots
        """
        page_html = str(self.client.get('/registerPilot').data)
        username_elem = 'Username'
        password_elem = 'Password'
        first_name_elem = 'First Name'
        last_name_elem = 'Last Name'
        email_elem = 'Email'
        phone_number_elem = 'Phone No.'
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)
        self.assertIn(first_name_elem, page_html)
        self.assertIn(last_name_elem, page_html)
        self.assertIn(email_elem, page_html)
        self.assertIn(phone_number_elem, page_html)


if __name__ == "__main__":
    unittest.main()
