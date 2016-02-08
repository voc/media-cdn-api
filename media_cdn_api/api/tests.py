from django.test import TestCase
from media_cdn_api.api.models import Server
from media_cdn_api.api.models import Hexhash


class ServerTestCasE(TestCase):
    # Create your tests here.
    def test_can_get_server_list(self):
        servers = Server.objects.all()
        self.assertTrue(servers)

    def test_can_get_server_file_count(self):
        Server.objects.create(identifier="server01", enabled=True)
        server = Server.objects.get(0)
        server.nfiles()
        # TODO assert?

class TorrentTestCase(TestCase):
    def test_can_get_torrent_hashes(self):
        Hexhash.objects.all()

