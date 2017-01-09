from unittest import TestCase
import bucketlist
import json


class TestBucketlistItemAPI(TestCase):

    def setUp(self):
        self.client = bucketlist.app.test_client()
        correct_credentials = json.dumps({"email":
                                          "mark.nganga@andela.com",
                                          "password": "p@ssw0rd"})
        response = self.client.post('/auth/login',
                                    data=correct_credentials,
                                    content_type='application/json')

        content = json.loads(response.get_data())
        self.access_token = content['access_token']

    def test_it_creates_bucketlist_item(self):
        new_bucketlist = json.dumps({"list_title": "Third List", "list_description": "This is the decription"})

        response = self.client.post('/bucketlists',
                                    data=new_bucketlist,
                                    content_type='application/json',
                                    headers={'Authorization': 'JWT %s' % self.access_token})

        content = json.loads(response.get_data(as_text=True))
        list_id = content['bucketlist']['list_id']

        new_item = json.dumps({"item_content": "Content of the first item"})

        response = self.client.post('/bucketlists/%s/items' % list_id,
                                    data=new_item,
                                    content_type='application/json',
                                    headers={'Authorization': 'JWT %s' % self.access_token})
        content = json.loads(response.get_data(as_text=True))

        self.assertEqual(201, response.status_code)
        self.assertEqual('Item created in bucketlist with ID %s' % list_id, content['message'])

    def test_it_updates_bucketlist_item(self):
        new_bucketlist = json.dumps({"list_title": "Third List", "list_description": "This is the decription"})

        response = self.client.post('/bucketlists',
                                    data=new_bucketlist,
                                    content_type='application/json',
                                    headers={'Authorization': 'JWT %s' % self.access_token})

        content = json.loads(response.get_data(as_text=True))
        list_id = content['bucketlist']['list_id']

        new_item = json.dumps({"item_content": "Content of the first item"})

        response = self.client.post('/bucketlists/%s/items' % list_id,
                                    data=new_item,
                                    content_type='application/json',
                                    headers={'Authorization': 'JWT %s' % self.access_token})
        content = json.loads(response.get_data(as_text=True))
        item_id = content['item']['item_id']

        new_item = json.dumps({"item_content": "Content of the first item updated"})

        response = self.client.put('/bucketlists/%s/items/%s' % (list_id, item_id),
                                    data=new_item,
                                    content_type='application/json',
                                    headers={'Authorization': 'JWT %s' % self.access_token})
        content = json.loads(response.get_data(as_text=True))


        self.assertEqual(200, response.status_code)
        self.assertEqual('Item with ID %s was updated' % item_id, content['message'])

    def test_it_deletes_bucketlist_item(self):
        pass

        # self.assertEqual('Item with ID %s was deleted' % self.item_id,
        #                  response[0]['message'])
