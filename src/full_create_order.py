import asyncio
from utils.limit_order import LimitOrder
from return_types.orders import SignMessageResponse
from utils.mock_data import mock_order, RPC_URL, ACCOUNT_PRIVATE_KEY, ACCOUNT_PUBLIC_KEY
from utils.accounts import account

async def full_place_order():
    limit_order = LimitOrder(RPC_URL)

    sign_message_resp: SignMessageResponse = await limit_order.sign_message(mock_order)
    my_account = account(RPC_URL, ACCOUNT_PUBLIC_KEY, ACCOUNT_PRIVATE_KEY, '1')

    signed_message: any = my_account.sign_message(sign_message_resp.typedData)

    approve_call_data = await limit_order.approve_order_amount(mock_order.maker_asset, mock_order.maker_amount)

    #tx_hash = await my_account.execute_v1(approve_call_data, auto_estimate = True)
 
    mock_order.order_hash = hex(sign_message_resp.orderHash)
    mock_order.signature = [str(signed_message[0]), str(signed_message[1])]

    place_order_resp = await limit_order.place_order(mock_order)

    print(f'sign_message_resp: {sign_message_resp}')
    print(f'signed_message: {signed_message}')
    print(f'approve_call_data: {approve_call_data}')
    print(f'mock_order: {mock_order}')
    print(f'place_order_resp: {place_order_resp}')
    print(f'status: {place_order_resp['status']} code {place_order_resp['code']}')

def main():
    asyncio.run(full_place_order())

if __name__ == '__main__':
    main()