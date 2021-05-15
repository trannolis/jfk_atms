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
        self.assertIn(login_elem, page_html)

    def test_login_page(self):
        """
        Tests the "Login" endpoint to for availability of page
        """
        page_html = str(self.client.get('/login').data)
        username_elem = 'username'
        password_elem = 'password'
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)

    def test_login_admin(self):
        """
        Tests the ability of an admin to login
        """
        self.client.post('/loginAuth',
                         data=dict(username="admin",
                                   password="test",
                                   role="admin"),
                         follow_redirects=True)

    def test_login_pilot(self):
        """
        Tests the ability of an pilot to login
        """
        self.client.post('/loginAuth',
                         data=dict(username="pilot",
                                   password="test",
                                   role="pilot"),
                         follow_redirects=True)

    def test_login_atc(self):
        """
        Tests the ability of an atc to login
        """
        self.client.post('/loginAuth',
                         data=dict(username="atc",
                                   password="test",
                                   role="atc"),
                         follow_redirects=True)

    def test_register_redirect_atc(self):
        """
        Tests redirecting to register an atc
        """
        self.client.post('/register',
                         data=dict(role="atc"),
                         follow_redirects=True)

    def test_register_redirect_pilot(self):
        """
        Tests redirecting to register an pilot
        """
        self.client.post('/register',
                         data=dict(role="pilot"),
                         follow_redirects=True)

    def test_register_auth_admin(self):
        """
        Tests successful admin registering authentication
        """
        self.client.post('/registerAdminAuth',
                         data=dict(username="testUsername",
                                   password="testPassword",
                                   first_name="testName",
                                   last_name="testSurname",
                                   email="test@nyu.edu",
                                   phone_no="testNum"),
                         follow_redirects=True)
#         page_html = str(self.client.get('/registerAdminAuth').data)
#         reg_atc_elem = 'Register a new Air Traffic Controller'
#         reg_pilot_elem = 'Register a new Pilot'
#         user_elem = 'Delete an existing user'
#         logout_elem = 'Logout'
#         self.assertIn(reg_atc_elem, page_html)
#         self.assertIn(reg_pilot_elem, page_html)
#         self.assertIn(user_elem, page_html)
#         self.assertIn(logout_elem, page_html)

    def test_register_auth_pilot(self):
        """
        Tests successful pilot registering authentication
        """
        self.client.post('/registerPilotAuth',
                         data=dict(username="testUsername",
                                   password="testPassword",
                                   first_name="testName",
                                   last_name="testSurname",
                                   email="test@nyu.edu",
                                   phone_no="testNum"),
                         follow_redirects=True)

    def test_register_auth_atc(self):
        """
        Tests successful atc registering authentication
        """
        self.client.post('/registerAtcAuth',
                         data=dict(username="testUsername",
                                   password="testPassword",
                                   first_name="testName",
                                   last_name="testSurname",
                                   email="test@nyu.edu",
                                   phone_no="testNum"),
                         follow_redirects=True)

    def test_admin_home(self):
        """
        Tests endpoint for admin home page
        """
        self.client.post('/adminHome',
                         data=dict(username="admin"),
                         follow_redirects=False)
#         page_html = str(self.client.get('adminHome').data)
#         reg_atc_elem = 'Register a new Air Traffic Controller'
#         reg_pilot_elem = 'Register a new Pilot'
#         user_elem = 'Delete an existing user'
#         logout_elem = 'Logout'
#         self.assertIn(reg_atc_elem, page_html)
#         self.assertIn(reg_pilot_elem, page_html)
#         self.assertIn(user_elem, page_html)
#         self.assertIn(logout_elem, page_html)

    def test_show_user(self):
        """
        Tests showUser endpoint
        """
        page_html = str(self.client.get('/showUser').data)
        back_elem = 'Go back'
        self.assertIn(back_elem, page_html)

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
