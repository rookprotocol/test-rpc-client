from uniswap import Uniswap
import os
from dotenv import load_dotenv

dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
usdc = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

load_dotenv()
uniswap_client = Uniswap(
    address=os.getenv("ADDRESS"),
    private_key=os.getenv("PRIVATE_KEY"),
    version=3,
)


def uniswap_swap(
    buy_token_address: str, sell_token_address: str, sell_token_amount: int
):
    return uniswap_client.make_trade(
        sell_token_address,
        buy_token_address,
        sell_token_amount,
    )


if __name__ == "__main__":
    response = uniswap_swap(
        buy_token_address=usdc, sell_token_address=dai, sell_token_amount=1 * 10**18
    )
    print(str(response))
