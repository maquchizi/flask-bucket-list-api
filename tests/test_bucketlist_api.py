from unittest import TestCase
import bucketlist
import json
from bucketlist.app import BucketListAPI


class TestBucketlistAPI(TestCase):

    def setUp(self):
        self.bucketlist = BucketListAPI()
        self.client = bucketlist.app.test_client()
        correct_credentials = json.dumps({"email":
                                          "mark.nganga@andela.com",
                                          "password": "p@ssw0rd"})
        response = self.client.post('/auth/login',
                                    data=correct_credentials,
                                    content_type='application/json')

        content = json.loads(response.get_data())
        self.access_token = content['access_token']

    def test_it_creates_bucketlist(self):
        new_bucketlist = json.dumps({"list_title": "Third List", "list_description": "This is the decription"})

        response = self.client.post('/bucketlists',
                                    data=new_bucketlist,
                                    content_type='application/json',
                                    headers={'Authorization': 'JWT %s' % self.access_token})

        content = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 201)

    def test_it_updates_bucketlist(self):
        list_id = 1
        response = self.bucketlist.put(list_id)
        self.assertEqual(200, response[1])

        self.assertEqual('The bucketlist with ID %s was updated' % list_id,
                         response[0]['message'])

    def test_it_deletes_bucketlist(self):
        list_id = 1
        response = self.bucketlist.delete(list_id)
        self.assertEqual(200, response[1])

        self.assertEqual('The bucketlist with ID %s was deleted' % list_id,
                         response[0]['message'])

    def test_it_fails_to_create_bucketlist_if_fields_missing(self):
        pass

    def test_does_not_list_bucketlists_if_not_logged_in(self):
        pass

    def test_it_does_not_create_buckelist_if_not_logged_in(self):
        pass

    def test_it_does_not_edit_bucketlist_if_not_logged_in(self):
        pass

    def test_it_does_not_delete_bucketlist_if_not_logged_in(self):
        pass

    def test_it_does_not_edit_list_not_owned_by_user(self):
        pass

    def test_it_does_not_delete_list_not_owned_by_user(self):
        pass

    def test_it_does_not_list_bucketlists_not_owned_by_user(self):
        pass
