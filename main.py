# Remove all non-numeric characters from a String in Python 

import re

my_str = 'bo_1bby_2_ha_3_dz.com'

result = re.sub(r'[^0-9]', '', my_str)

print(result)  # 👉️ '123'