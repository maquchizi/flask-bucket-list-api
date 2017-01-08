import bucketlist
import json
from unittest import TestCase


class TestAuthAPI(TestCase):

    def setUp(self):
        self.client = bucketlist.app.test_client()
        self.correct_credentials = json.dumps({"email":
                                              "mark.nganga@andela.com",
                                               "password": "p@ssw0rd"})
        self.incorrect_credentials = json.dumps({"email":
                                                "mark.nganga@andela.com",
                                                 "password": "wr0ngp@ssw0rd"})

    def test_it_allows_login(self):
        response = self.client.post('/auth/login',
                                    data=self.correct_credentials,
                                    content_type='application/json')

        content = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', content)

    def test_login_fails_with_incorrect_credentials(self):
        response = self.client.post('/auth/login',
                                    data=self.incorrect_credentials,
                                    content_type='application/json')

        self.assertEqual(response.status_code, 401)

    def test_login_method_only_allows_post_requests(self):
        response = self.client.get('/auth/login',
                                   data=self.correct_credentials,
                                   content_type='application/json')

        self.assertEqual(response.status_code, 405)

    def test_login_error_does_not_specify_incorrect_field(self):
        pass

    def test_login_error_does_not_specify_if_user_exists(self):
        pass

    def test_allows_registration(self):
        response = self.client.post('/auth/register',
                                    data=json.dumps({"forename": "Second",
                                                     "surname": "User",
                                                     "password": "pass",
                                                     "email":
                                                     "some.other@gmail.com"}),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_it_fails_registration_if_email_already_taken(self):
        response = self.client.post('/auth/register',
                                    data=json.dumps({"forename": "Second",
                                                     "surname": "User",
                                                     "password": "pass",
                                                     "email":
                                                     "some.other@gmail.com"}),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_registration_fails_if_all_fields_not_present(self):
        pass

    def test_registration_error_specifies_one_missing_field(self):
        pass

    def test_registration_error_specifies_all_missing_filelds(self):
        pass

    def test_returns_token_on_successful_registration(self):
        pass
