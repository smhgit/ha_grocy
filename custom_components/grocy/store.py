'''Online grocery store'''

from .store_api_client import get_store_api_client


class Store:
    """Online store"""
    
    def __init__(self, store_name: str = 'default', username: str = None, password: str = None):
        self._client = get_store_api_client(store_name)
        self._username = username
        self._password = password

    @property
    def name(self):
        return self._client.name

    def get_product_by_barcode(self, barcode: str):
        return self._client.get_product_by_barcode(barcode)

    def add_to_cart(self):
        self._client.login(self._username, self._password)
        self._client.add_to_cart(self)
        self._client.logout()
        pass

    def delete_cart(self):
        pass

# def test():
#     store = Store(RamiLevyStoreApiClient())
#     p = store.get_product_by_barcode('100')
#     print('Pass: Found: ' + p.name) if p else print('Failure')
#     p = store.get_product_by_barcode('7290016096590')
#     print('Pass: Found: ' + p.name) if p else print('Failure')
#     p = store.get_product_by_barcode('7290102398065')
#     print('Pass: Found: ' + p.name) if p else print('Failure')
#     p = store.get_product_by_barcode('000')
#     print('Failure') if p else print('Pass: Product not exists')

#     store = Store(ShufersalStoreApiClient())
#     p = store.get_product_by_barcode('7290102395224')
#     print('Pass: Found: ' + p.name) if p else print('Failure')

# test()