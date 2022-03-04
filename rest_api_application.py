from binance.spot import Spot
import config

client = Spot(key=config.api_key, secret=config.secret_key)


print(client.account())


