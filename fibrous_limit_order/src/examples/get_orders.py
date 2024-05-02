import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import aiohttp

from limit_order.limit_order import LimitOrder
from return_types.orders import GetOrdersResponse, OrdersFilter
from limit_order import utils

async def get_orders() -> GetOrdersResponse:
    limit_order = LimitOrder()
    filters: OrdersFilter = {
        'wallet_address': '',
        'makerAsset': '',
        'takerAsset': '',
        'makerAmount': '',
        'takerAmount': '',
        'orderPrice': '',
        'page': 1,
        'pageSize': 10,
    }

    open_orders: GetOrdersResponse = await limit_order.get_orders(filter=None)
    async with aiohttp.ClientSession() as session:
        async with session.get('https://graph.fibrous.finance/tokens') as response:
            tokens_data = await response.json()

    # Convert the first order to human readable format
    human_readable_order = utils.order_to_human_readable(open_orders.data[0], tokens_data)
    print('humanReadableOrder', human_readable_order)
    return open_orders

def main():
    asyncio.run(get_orders())

if __name__ == '__main__':
    main()