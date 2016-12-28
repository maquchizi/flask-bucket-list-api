from unittest import TestCase
import server


class TestBucketlist(TestCase):

    def test_it_creates_bucketlist(self):
        bucketlist = server.BucketList()
        response = server.BucketList.post(bucketlist)
        self.assertEqual(200, response[1])

    def test_it_edits_bucketlist(self):
        pass

    def test_it_deletes_bucketlist(self):
        pass

    def test_it_fails_to_create_bucketlist_if_fields_missing(self):
        pass

    def test_does_not_list_bucketlists_if_not_logged_in(self):
        pass

    def test_it_does_not_create_buckelist_if_not_logged_in(self):
        pass

    def test_it_does_edit_bucketlist_if_not_logged_in(self):
        pass

    def test_it_does_not_delete_bucketlist_if_not_logged_in(self):
        pass

    def test_it_does_not_edit_list_not_owned_by_user(self):
        pass

    def test_it_does_not_delete_list_not_owned_by_user(self):
        pass

    def test_it_does_not_list_bucketlists_not_owned_by_user(self):
        pass
