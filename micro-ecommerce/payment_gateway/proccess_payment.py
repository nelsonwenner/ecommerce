from hashids import Hashids
import time

def proccess_payment_simulation(payment_method, card_hash):
    time.sleep(60)
    hashids = Hashids(alphabet='abcdefghijklmnopqrstuvwxyz1234567890', min_length=22)
    return hashids.encode(1)