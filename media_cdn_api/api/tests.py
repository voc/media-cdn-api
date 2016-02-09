from django.test import TestCase
from media_cdn_api.api.models import Server
from media_cdn_api.api.hexhash import Hexhash


class ServerTestCasE(TestCase):
    def test_can_get_server_list(self):
        servers = Server.objects.all()
        self.assertTrue(servers)

