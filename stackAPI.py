import re

import requests
from pandas.core.dtypes.dtypes import Ordered

urls = []
for i in range(1, 1000):
    urls.append(
        f"https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow&pagesize=10&page={i}"
    )

for url in urls:
    results = requests.get(url)
    print(results.json())

# this is a synchronous program since we rely on a a for loop to
# collect data from stackoverflow and the for loop dictates an Order
# the program can be asnch since the order is not important and the
# the time complexity of the program can be reduced from O(N) to...
