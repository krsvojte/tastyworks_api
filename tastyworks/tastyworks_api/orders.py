import aiohttp

from tastyworks.tastyworks_api.tasty_session import TastyAPISession
from tastyworks.models import order as order_models


class OrdersManager(object):
    def __init__(self, session: TastyAPISession):
        if not session.session_valid():
            raise Exception('Cannot start an orders manager without a valid Tastyworks session')

        self.tasty_session = session

    async def _get_open_orders(self):
        url = '{}/accounts/{}/orders'.format(self.tasty_session.API_url, self.tasty_session.get_trading_account())
        async with aiohttp.request('GET', url, headers=self.tasty_session._get_request_headers()) as resp:
            if resp.status_code != 200:
                raise Exception('Could not get current open orders')
            data = await resp.json()



async def execute_order(self, dry_run=True):
    pass
