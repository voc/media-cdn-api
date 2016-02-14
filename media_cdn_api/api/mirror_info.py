from django.db import connection

class MirrorInfo:
    def dict(self, mirror):
        data = {}
        data['identifier'] = mirror.identifier
        data['baseurl'] = mirror.baseurl
        data['baseurl_ftp'] = mirror.baseurl_ftp
        data['enabled'] = mirror.enabled
        data['status_baseurl'] = mirror.status_baseurl
        data['region'] = mirror.region
        data['country'] = mirror.country
        data['asn'] = str(mirror.asn)
        data['lat'] = str(mirror.lat)
        data['lng'] = str(mirror.lng)
        data['prefix'] = mirror.prefix
        data['last_scan'] = str(mirror.last_scan)
        data['operator_url'] = mirror.operator_url
        data['nfiles'] = self.nfiles(mirror.identifier)
        return data

    def nfiles(self, identifier):
        cursor = connection.cursor()
        cursor.execute('SELECT mirr_get_nfiles(%s)', [identifier])
        return cursor.fetchone()[0]

