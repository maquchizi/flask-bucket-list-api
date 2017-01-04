import bucketlist
import json
from unittest import TestCase


class TestAuth(TestCase):

    def setUp(self):
        self.client = bucketlist.app.test_client()

    def test_it_allows_login(self):
        response = self.client.post('/auth/login', data=json.dumps({"email": "mark.nganga@andela.com", "password": "p@ssw0rd"}), content_type='application/json')

        content = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', content)

    def test_login_fails_with_incorrect_credentials(self):
        pass

    def test_it_returns_token_on_login(self):
        pass

    def test_login_method_only_allows_post_requests(self):
        pass

    def test_login_error_does_not_specify_incorrect_field(self):
        pass

    def test_login_error_does_not_specify_if_user_exists(self):
        pass

    def test_allows_registration(self):
        pass

    def test_it_fails_registration_if_email_already_taken(self):
        pass

    def test_registration_fails_if_all_fields_not_present(self):
        pass

    def test_registration_error_specifies_one_missing_field(self):
        pass

    def test_registration_error_specifies_all_missing_filelds(self):
        pass

    def test_returns_token_on_successful_registration(self):
        pass
