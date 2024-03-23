import asyncio
import timeit
from utils.limit_order import LimitOrder
from utils.personal_data import WALLET_ADDRESS
from return_types.orders import NonceResponse

async def get_nonce() -> NonceResponse:
    limit_order = LimitOrder()
    nonce = await limit_order.get_nonce(WALLET_ADDRESS)
    print(nonce)

async def run_code():
    start_time = timeit.default_timer()
    await get_nonce()
    end_time = timeit.default_timer()
    print(f"Execution time: {end_time - start_time} seconds")

def main():
    asyncio.run(run_code())

if __name__ == '__main__':
    main()