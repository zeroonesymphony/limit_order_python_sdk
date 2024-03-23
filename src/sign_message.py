import asyncio
import utils.limit_order as _limit_order
from return_types.orders import SignMessageResponse
from utils.mock_data import mock_order, RPC_URL

async def sign_message(_mock_order) -> SignMessageResponse:
    limit_order = _limit_order.LimitOrder(RPC_URL)

    sign_message_resp: SignMessageResponse = await limit_order.sign_message(_mock_order)

    for key, value in sign_message_resp.__dict__.items():
        print(f'{key}: {value}')
        
    return sign_message_resp

def main():
    asyncio.run(sign_message(mock_order))

if __name__ == "__main__":
    main()
