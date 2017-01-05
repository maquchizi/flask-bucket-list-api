from unittest import TestCase
from server import BucketlistItem


class TestBucketlistItem(TestCase):

    def setUp(self):
        self.bucketlist_item = BucketlistItem()
        self.list_id = 1
        self.item_id = 2

    def test_it_creates_bucketlist_item(self):
        response = self.bucketlist_item.post(self.list_id)
        self.assertEqual(201, response[1])

        self.assertEqual('Item created in bucketlist with ID %s' %
                         self.list_id,
                         response[0]['message'])

    def test_it_updates_bucketlist_item(self):
        response = self.bucketlist_item.put(self.list_id, self.item_id)
        self.assertEqual(200, response[1])

        self.assertEqual('Item with ID %s was updated' % self.item_id,
                         response[0]['message'])

    def test_it_deletes_bucketlist_item(self):
        response = self.bucketlist_item.delete(self.list_id, self.item_id)
        self.assertEqual(200, response[1])

        self.assertEqual('Item with ID %s was deleted' % self.item_id,
                         response[0]['message'])
