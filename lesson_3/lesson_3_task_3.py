from address import Address
from mailing import Mailing

letter = Mailing(Address("182", "Pushkina St", "18", "Moscow", "RF", "92108"), 
                 Address("33",  "Elizabeth St", "1", "New York", "NY", "00000"), 
                 "$16.15", "1234567890")

print(f"Letter with the tracking number {letter.track} mailed from address: {letter.from_address} to: {letter.to_address}. Cost of mailing: {letter.cost}")