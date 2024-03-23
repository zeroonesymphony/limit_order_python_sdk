import asyncio
from utils.limit_order import LimitOrder
from utils.mock_data import RPC_URL

async def get_remaining_amount(orderHash):
    limit_order = LimitOrder(RPC_URL)
    remaining_amount = await limit_order.get_remaining_amount(orderHash)
    print(remaining_amount)
    return remaining_amount

def main():
    asyncio.run(get_remaining_amount('order_hash'))

if __name__ == '__main__':
    main()