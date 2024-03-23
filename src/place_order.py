import asyncio
from utils.limit_order import LimitOrder
from return_types.orders import Order, PlaceOrderResponse
from utils.mock_data import convert_date_to_unix_timestamp

async def place_order(_order) -> PlaceOrderResponse:
    limit_order = LimitOrder()
    response = await limit_order.place_order(_order)
    print(response)
    return response

order = Order(
    signer='0x00c2fd8e',
    maker_asset='0x00c2fd8e',
    taker_asset='0x00c2fd8e',
    maker_amount=1000000000000000000,
    taker_amount=1000000000000000000,
    order_price=2770000000000000000000, # price of the maker asset in terms of the taker asset (unit amount)
    expiration=convert_date_to_unix_timestamp(days=1), # expiration in 1 day
    use_solver=False, # if true, the order will be executed with the solver
    partial_fill=False, # if true, the order will be partially filled
    nonce=1, # ref. ./getNonce.ts
    order_hash='order_hash', # ref. ./signMessage.ts
    signature=['sig_r', 'sign_s'] # ref. ./signMessage.ts
)

def main():
    asyncio.run(place_order(order))

if __name__ == '__main__':
    main()