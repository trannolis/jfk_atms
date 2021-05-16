import unittest
from source import create_app


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app('source.settings', True)
        self.client = self.app.test_client()
        self.sess = self.client.session_transaction()

    def test_landing(self):
        """
        Tests the '/' endpoint for admins
        """
        page_html = str(self.client.get('/').data)
        title_elem = 'Welcome to ATMS'
        login_elem = 'Login'
        self.assertIn(title_elem, page_html)
        self.assertIn(login_elem, page_html)

    def test_login_page(self):
        """
        Tests the "Login" endpoint to for availability of page
        """
        page_html = str(self.client.get('/login').data)
        query_elem = 'Please select your role:'
        admin_elem = 'Admin'
        atc_elem = 'Air Traffic Controller'
        pilot_elem = 'Pilot'
        username_elem = 'username'
        password_elem = 'password'
        submit_elem = 'Login'
        back_elem = 'Go back'
        self.assertIn(query_elem, page_html)
        self.assertIn(admin_elem, page_html)
        self.assertIn(atc_elem, page_html)
        self.assertIn(pilot_elem, page_html)
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)

    def test_register_admin(self):
        """
        Tests registering Admins
        """
        page_html = str(self.client.get('/registerAdmin').data)
        title_elem = 'Register A New Admin'
        username_elem = 'Username'
        password_elem = 'Password'
        first_name_elem = 'First Name'
        last_name_elem = 'Last Name'
        email_elem = 'Email'
        phone_number_elem = 'Phone No.'
        submit_elem = 'Register'
        back_elem = 'Go back'
        self.assertIn(title_elem, page_html)
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)
        self.assertIn(first_name_elem, page_html)
        self.assertIn(last_name_elem, page_html)
        self.assertIn(email_elem, page_html)
        self.assertIn(phone_number_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)

    def test_login_admin(self):
        """
        Tests the ability of an admin to login
        """
        self.client.post('/loginAuth',
                         data=dict(username="admin",
                                   password="test",
                                   role="admin"),
                         follow_redirects=True)

#         page_html = str(self.client.get('/loginAuth').data)
#         print(page_html)

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
                         follow_redirects=False)
        page_html = str(self.client.get('/registerAtc').data)
        title_elem = 'Register A New Air Traffic Controller'
        username_elem = 'Username'
        password_elem = 'Password'
        first_name_elem = 'First Name'
        last_name_elem = 'Last Name'
        email_elem = 'Email'
        phone_number_elem = 'Phone No.'
        submit_elem = 'Register'
        back_elem = 'Go back'
        self.assertIn(title_elem, page_html)
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)
        self.assertIn(first_name_elem, page_html)
        self.assertIn(last_name_elem, page_html)
        self.assertIn(email_elem, page_html)
        self.assertIn(phone_number_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)

    def test_register_redirect_pilot(self):
        """
        Tests redirecting to register an pilot
        """
        self.client.post('/register',
                         data=dict(role="pilot"),
                         follow_redirects=False)
        page_html = str(self.client.get('/registerPilot').data)
        title_elem = 'Register A New Pilot'
        username_elem = 'Username'
        password_elem = 'Password'
        first_name_elem = 'First Name'
        last_name_elem = 'Last Name'
        email_elem = 'Email'
        phone_number_elem = 'Phone No.'
        submit_elem = 'Register'
        back_elem = 'Go back'
        self.assertIn(title_elem, page_html)
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)
        self.assertIn(first_name_elem, page_html)
        self.assertIn(last_name_elem, page_html)
        self.assertIn(email_elem, page_html)
        self.assertIn(phone_number_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)

    def test_register_atc(self):
        """
        Tests registering Air Traffic Controllers
        """
        page_html = str(self.client.get('/registerAtc').data)
        title_elem = 'Register A New Air Traffic Controller'
        username_elem = 'Username'
        password_elem = 'Password'
        first_name_elem = 'First Name'
        last_name_elem = 'Last Name'
        email_elem = 'Email'
        phone_number_elem = 'Phone No.'
        submit_elem = 'Register'
        back_elem = 'Go back'
        self.assertIn(title_elem, page_html)
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)
        self.assertIn(first_name_elem, page_html)
        self.assertIn(last_name_elem, page_html)
        self.assertIn(email_elem, page_html)
        self.assertIn(phone_number_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)

    def test_register_pilot(self):
        """
        Tests registering Pilots
        """
        page_html = str(self.client.get('/registerPilot').data)
        title_elem = 'Register A New Pilot'
        username_elem = 'Username'
        password_elem = 'Password'
        first_name_elem = 'First Name'
        last_name_elem = 'Last Name'
        email_elem = 'Email'
        phone_number_elem = 'Phone No.'
        submit_elem = 'Register'
        back_elem = 'Go back'
        self.assertIn(title_elem, page_html)
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)
        self.assertIn(first_name_elem, page_html)
        self.assertIn(last_name_elem, page_html)
        self.assertIn(email_elem, page_html)
        self.assertIn(phone_number_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)

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
                         follow_redirects=True)
#         page_html = str(self.client.get('/adminHome').data)
#         reg_atc_elem = 'Register a new Air Traffic Controller'
#         reg_pilot_elem = 'Register a new Pilot'
#         user_elem = 'Delete an existing user'
#         logout_elem = 'Logout'
#         self.assertIn(reg_atc_elem, page_html)
#         self.assertIn(reg_pilot_elem, page_html)
#         self.assertIn(user_elem, page_html)
#         self.assertIn(logout_elem, page_html)

    def test_pilot_home(self):
        """
        Tests endpoint for pilot home page
        """
        self.client.post('/pilotHome',
                         data=dict(username="pilot"),
                         follow_redirects=True)

    def test_atc_home(self):
        """
        Tests endpoint for atc home page
        """
        self.client.post('/atcHome',
                         data=dict(username="atc"),
                         follow_redirects=True)

    def test_show_user(self):
        """
        Tests showUser endpoint
        """
        page_html = str(self.client.get('/showUser').data)
        title_elem = 'Please select the role of the user you want to delete'
        admin_elem = 'Admin'
        atc_elem = 'ATC'
        pilot_elem = 'Pilot'
        submit_elem = 'Continue'
        back_elem = 'Go back'
        self.assertIn(title_elem, page_html)
        self.assertIn(admin_elem, page_html)
        self.assertIn(atc_elem, page_html)
        self.assertIn(pilot_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)

    def test_select_admins(self):
        """
        Tests endpoint for selecting admins
        """
        self.client.post('/selectUser',
                         data=dict(role="admin"),
                         follow_redirects=True)
        page_html = str(self.client.get('/showUser').data)
        query_elem = 'Please select the role of the user you want to delete'
        admin_elem = 'Admin'
        atc_elem = 'ATC'
        pilot_elem = 'Pilot'
        submit_elem = 'Continue'
        back_elem = 'Go back'
        self.assertIn(query_elem, page_html)
        self.assertIn(admin_elem, page_html)
        self.assertIn(atc_elem, page_html)
        self.assertIn(pilot_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)

    def test_select_pilot(self):
        """
        Tests endpoint for selecting pilots
        """
        self.client.post('/selectUser',
                         data=dict(role="pilot"),
                         follow_redirects=True)
        page_html = str(self.client.get('/showUser').data)
        query_elem = 'Please select the role of the user you want to delete'
        admin_elem = 'Admin'
        atc_elem = 'ATC'
        pilot_elem = 'Pilot'
        submit_elem = 'Continue'
        back_elem = 'Go back'
        self.assertIn(query_elem, page_html)
        self.assertIn(admin_elem, page_html)
        self.assertIn(atc_elem, page_html)
        self.assertIn(pilot_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)

    def test_select_atc(self):
        """
        Tests endpoint for selecting atcs
        """
        self.client.post('/selectUser',
                         data=dict(role="atc"),
                         follow_redirects=True)
        page_html = str(self.client.get('/showUser').data)
        query_elem = 'Please select the role of the user you want to delete'
        admin_elem = 'Admin'
        atc_elem = 'ATC'
        pilot_elem = 'Pilot'
        submit_elem = 'Continue'
        back_elem = 'Go back'
        self.assertIn(query_elem, page_html)
        self.assertIn(admin_elem, page_html)
        self.assertIn(atc_elem, page_html)
        self.assertIn(pilot_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)

    def test_remove_user(self):
        """
        Tests removing users
        """
        self.client.post('/removeUser',
                         data=dict(user="admin"),
                         follow_redirects=True)
        page_html = str(self.client.get('/removeUser').data)
        success_elem = 'You have successfully deleted'
        delete_elem = 'Delete another user'
        back_elem = 'Go Home'
        self.assertIn(success_elem, page_html)
        self.assertIn(delete_elem, page_html)
        self.assertIn(back_elem, page_html)

    def test_get_flights(self):
        """
        Tests retrieving flights
        """
        page_html = str(self.client.get('/getFlights').data)
        title_elem = 'All Scheduled Flights'
        select_elem = 'Select'
        id_elem = 'ID'
        atime_elem = 'Arrival Time'
        dtime_elem = 'Departure Time'
        dloc_elem = 'Departure Location'
        aloc_elem = 'Arrival Location'
        plane_elem = 'Airplane ID'
        gate_elem = 'Gate Number'
        runway_elem = 'Runway Number'
        updateg_elem = 'Update Gate'
        updater_elem = 'Update Runway'
        submit_elem = 'Continue'
        back_elem = 'Back'
        logout_elem = 'Logout'
        self.assertIn(title_elem, page_html)
        self.assertIn(select_elem, page_html)
        self.assertIn(id_elem, page_html)
        self.assertIn(atime_elem, page_html)
        self.assertIn(dtime_elem, page_html)
        self.assertIn(dloc_elem, page_html)
        self.assertIn(aloc_elem, page_html)
        self.assertIn(plane_elem, page_html)
        self.assertIn(gate_elem, page_html)
        self.assertIn(runway_elem, page_html)
        self.assertIn(updateg_elem, page_html)
        self.assertIn(updater_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)
        self.assertIn(logout_elem, page_html)

    def test_show_flights_vacant_gate(self):
        """
        Tests endpoint for showing flights with vacant gates
        """
        self.client.post('/showFlights',
                         data=dict(select="299",
                                   update="gate"),
                         follow_redirects=True)
        page_html = str(self.client.get('/vacantGates').data)
        title_elem = 'Available Gates'
        select_elem = 'Select'
        id_elem = 'ID'
        x_elem = 'X_coord'
        y_elem = 'Y_coord'
        vacant_elem = 'Is vacant'
        service_elem = 'In service'
        terminal_elem = 'Terminal'
        submit_elem = 'Continue'
        back_elem = 'Back'
        logout_elem = 'Logout'
        self.assertIn(title_elem, page_html)
        self.assertIn(select_elem, page_html)
        self.assertIn(id_elem, page_html)
        self.assertIn(x_elem, page_html)
        self.assertIn(y_elem, page_html)
        self.assertIn(vacant_elem, page_html)
        self.assertIn(service_elem, page_html)
        self.assertIn(terminal_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)
        self.assertIn(logout_elem, page_html)

    def test_show_flights_vacant_runway(self):
        """
        Tests endpoint for showing flights with vacant runways
        """
        self.client.post('/showFlights',
                         data=dict(select="299",
                                   update="runway"),
                         follow_redirects=True)
        page_html = str(self.client.get('/vacantRunways').data)
        title_elem = 'Available Runways'
        select_elem = 'Select'
        runway_elem = 'Runway Number'
        vacant_elem = 'Is vacant'
        submit_elem = 'Continue'
        back_elem = 'Back'
        logout_elem = 'Logout'
        self.assertIn(title_elem, page_html)
        self.assertIn(select_elem, page_html)
        self.assertIn(runway_elem, page_html)
        self.assertIn(vacant_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)
        self.assertIn(logout_elem, page_html)

    def test_occupied_gates(self):
        """
        Tests endpoint for occupied gates
        """
        page_html = str(self.client.get('/occupiedGates').data)
        title_elem = 'Occupied Gates'
        select_elem = 'Select'
        id_elem = 'ID'
        x_elem = 'X_coord'
        y_elem = 'Y_coord'
        vacant_elem = 'Is vacant'
        service_elem = 'In service'
        terminal_elem = 'Terminal'
        submit_elem = 'Continue'
        back_elem = 'Back'
        logout_elem = 'Logout'
        self.assertIn(title_elem, page_html)
        self.assertIn(select_elem, page_html)
        self.assertIn(id_elem, page_html)
        self.assertIn(x_elem, page_html)
        self.assertIn(y_elem, page_html)
        self.assertIn(vacant_elem, page_html)
        self.assertIn(service_elem, page_html)
        self.assertIn(terminal_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)
        self.assertIn(logout_elem, page_html)

    def test_occupied_runways(self):
        """
        Tests endpoint for occupied runways
        """
        self.client.post('/occupiedRunways',
                         data=dict(select="1"),
                         follow_redirects=True)
        page_html = str(self.client.get('/occupiedRunways').data)
        title_elem = 'Occupied Runways'
        select_elem = 'Select'
        runway_elem = 'Runway Number'
        vacant_elem = 'Is vacant'
        submit_elem = 'Continue'
        back_elem = 'Back'
        logout_elem = 'Logout'
        self.assertIn(title_elem, page_html)
        self.assertIn(select_elem, page_html)
        self.assertIn(runway_elem, page_html)
        self.assertIn(vacant_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)
        self.assertIn(logout_elem, page_html)

    def test_vacate_gate(self):
        """
        Tests vacating a gate
        """
        self.client.post('/vacateGate',
                         data=dict(select="6"),
                         follow_redirects=True)
        page_html = str(self.client.get('/getFlights').data)
        title_elem = 'All Scheduled Flights'
        select_elem = 'Select'
        id_elem = 'ID'
        atime_elem = 'Arrival Time'
        dtime_elem = 'Departure Time'
        dloc_elem = 'Departure Location'
        aloc_elem = 'Arrival Location'
        plane_elem = 'Airplane ID'
        gate_elem = 'Gate Number'
        runway_elem = 'Runway Number'
        updateg_elem = 'Update Gate'
        updater_elem = 'Update Runway'
        submit_elem = 'Continue'
        back_elem = 'Back'
        logout_elem = 'Logout'
        self.assertIn(title_elem, page_html)
        self.assertIn(select_elem, page_html)
        self.assertIn(id_elem, page_html)
        self.assertIn(atime_elem, page_html)
        self.assertIn(dtime_elem, page_html)
        self.assertIn(dloc_elem, page_html)
        self.assertIn(aloc_elem, page_html)
        self.assertIn(plane_elem, page_html)
        self.assertIn(gate_elem, page_html)
        self.assertIn(runway_elem, page_html)
        self.assertIn(updateg_elem, page_html)
        self.assertIn(updater_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)
        self.assertIn(logout_elem, page_html)

    def test_vacate_runway(self):
        """
        Tests vacating a runway
        """
        self.client.post('/vacateRunway',
                         data=dict(select="3"),
                         follow_redirects=True)
        page_html = str(self.client.get('/getFlights').data)
        title_elem = 'All Scheduled Flights'
        select_elem = 'Select'
        id_elem = 'ID'
        atime_elem = 'Arrival Time'
        dtime_elem = 'Departure Time'
        dloc_elem = 'Departure Location'
        aloc_elem = 'Arrival Location'
        plane_elem = 'Airplane ID'
        gate_elem = 'Gate Number'
        runway_elem = 'Runway Number'
        updateg_elem = 'Update Gate'
        updater_elem = 'Update Runway'
        submit_elem = 'Continue'
        back_elem = 'Back'
        logout_elem = 'Logout'
        self.assertIn(title_elem, page_html)
        self.assertIn(select_elem, page_html)
        self.assertIn(id_elem, page_html)
        self.assertIn(atime_elem, page_html)
        self.assertIn(dtime_elem, page_html)
        self.assertIn(dloc_elem, page_html)
        self.assertIn(aloc_elem, page_html)
        self.assertIn(plane_elem, page_html)
        self.assertIn(gate_elem, page_html)
        self.assertIn(runway_elem, page_html)
        self.assertIn(updateg_elem, page_html)
        self.assertIn(updater_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)
        self.assertIn(logout_elem, page_html)

    def test_vacant_gates(self):
        """
        Tests vacant gates
        """
        page_html = str(self.client.get('/vacantGates').data)
        title_elem = 'Available Gates'
        select_elem = 'Select'
        id_elem = 'ID'
        x_elem = 'X_coord'
        y_elem = 'Y_coord'
        vacant_elem = 'Is vacant'
        service_elem = 'In service'
        terminal_elem = 'Terminal'
        submit_elem = 'Continue'
        back_elem = 'Back'
        logout_elem = 'Logout'
        self.assertIn(title_elem, page_html)
        self.assertIn(select_elem, page_html)
        self.assertIn(id_elem, page_html)
        self.assertIn(x_elem, page_html)
        self.assertIn(y_elem, page_html)
        self.assertIn(vacant_elem, page_html)
        self.assertIn(service_elem, page_html)
        self.assertIn(terminal_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)
        self.assertIn(logout_elem, page_html)

    def test_vacant_runways(self):
        """
        Tests vacant runways
        """
        self.client.post('/vacantRunways',
                         data=dict(select="3"),
                         follow_redirects=True)
        page_html = str(self.client.get('/vacantRunways').data)
        title_elem = 'Available Runways'
        select_elem = 'Select'
        runway_elem = 'Runway Number'
        vacant_elem = 'Is vacant'
        submit_elem = 'Continue'
        back_elem = 'Back'
        logout_elem = 'Logout'
        self.assertIn(title_elem, page_html)
        self.assertIn(select_elem, page_html)
        self.assertIn(runway_elem, page_html)
        self.assertIn(vacant_elem, page_html)
        self.assertIn(submit_elem, page_html)
        self.assertIn(back_elem, page_html)
        self.assertIn(logout_elem, page_html)

#     def test_change_gate(self):
#         """
#         Tests changing gates
#         """
#         self.client.post('/changeGate',
#                          data=dict(select="6"),
#                          follow_redirects=True)
#         page_html = str(self.client.get('/getFlights').data)
#         title_elem = 'All Scheduled Flights'
#         select_elem = 'Select'
#         id_elem = 'ID'
#         atime_elem = 'Arrival Time'
#         dtime_elem = 'Departure Time'
#         dloc_elem = 'Departure Location'
#         aloc_elem = 'Arrival Location'
#         plane_elem = 'Airplane ID'
#         gate_elem = 'Gate Number'
#         runway_elem = 'Runway Number'
#         updateg_elem = 'Update Gate'
#         updater_elem = 'Update Runway'
#         freeg_elem = 'Free Up Gate'
#         freer_elem = 'Free Up Runway'
#         submit_elem = 'Continue'
#         back_elem = 'Back'
#         logout_elem = 'Logout'
#         self.assertIn(title_elem, page_html)
#         self.assertIn(select_elem, page_html)
#         self.assertIn(id_elem, page_html)
#         self.assertIn(atime_elem, page_html)
#         self.assertIn(dtime_elem, page_html)
#         self.assertIn(dloc_elem, page_html)
#         self.assertIn(aloc_elem, page_html)
#         self.assertIn(plane_elem, page_html)
#         self.assertIn(gate_elem, page_html)
#         self.assertIn(runway_elem, page_html)
#         self.assertIn(updateg_elem, page_html)
#         self.assertIn(updater_elem, page_html)
#         self.assertIn(freeg_elem, page_html)
#         self.assertIn(freer_elem, page_html)
#         self.assertIn(submit_elem, page_html)
#         self.assertIn(back_elem, page_html)
#         self.assertIn(logout_elem, page_html)

#     def test_logout(self):
#         """
#         Tests logout
#         """
#         page_html = str(self.client.get('/logout').data)
#         login_elem = 'Login'
#         self.assertIn(login_elem, page_html)

    def test_chatroom(self):
        """
        Tests a chatroom
        """
        page_html = str(self.client.get('/chatroom').data)
        title_elem = 'Chatroom'
        status_elem = 'No message yet..'
        user_elem = 'User Name'
        message_elem = 'Messages'
        self.assertIn(title_elem, page_html)
        self.assertIn(status_elem, page_html)
        self.assertIn(user_elem, page_html)
        self.assertIn(message_elem, page_html)


if __name__ == "__main__":
    unittest.main()
