import aiohttp

from tastyworks.tastyworks_api.tasty_session import TastyAPISession
from tastyworks.models.order import Order, OrderStatus


class OrdersManager(object):
    def __init__(self, session: TastyAPISession):
        if not session.session_valid():
            raise Exception('Cannot start an orders manager without a valid Tastyworks session')

        self.tasty_session = session

    async def _get_orders(self, filters: dict):
        filters = filters or {
            'status': OrderStatus.RECEIVED
        }
        url = '{}/accounts/{}/orders'.format(
            self.tasty_session.API_url,
            self.tasty_session.get_trading_account()
        )
        url = '{}?{}'.format(
            url,
            '&'.join([f'{k}={v}' for k, v in filters.items()])
        )
        async with aiohttp.request('GET', url, headers=self.tasty_session._get_request_headers()) as resp:
            if resp.status_code != 200:
                raise Exception('Could not get current open orders')
            data = (await resp.json())['data']['items']

        return data
        # TODO: Test this function


    # TODO: rethink this design. make it more object-oriented. Also, test this
    async def execute_order(self, order: Order, dry_run=True):
        """
        Execute an order. If doing a dry run, the order isn't placed but simulated (server-side).

        Args:
            
        """
        url = '{}/accounts/{}/orders'.format(
            self.tasty_session.API_url,
            self.tasty_session.account_data[0]['account-number']
        )
        if dry_run:
            url = f'{url}/dry-run'

        async with aiohttp.request('POST', url, headers=self.tasty_session._get_request_headers()) as resp:
            if resp.status_code not in (200, 201):
                raise Exception('Could not execute a trade order successfully')
            data = await resp.json()['data']['order']
            
            if data['status'] != 'Received':
                return False, 
