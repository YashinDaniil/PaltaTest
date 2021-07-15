from dadata import Dadata
from decouple import config


class Geokoder:
    token = config('DADATA_TOKEN')
    secret = config('DADATA_SECRET')

    dadata = Dadata(token, secret)


    def get_geo(self, address):
        result = self.dadata.clean("address", address)
        return {
            'geo_lat': result['geo_lat'],
            'geo_lon': result['geo_lon'],
        }
