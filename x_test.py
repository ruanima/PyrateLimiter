from pyrate_limiter import *
from time import sleep

rate = RequestRate(3, 5 * Duration.SECOND)
limiter = Limiter(rate)
item = 'vutran'

has_raised = False
try:
    for _ in range(4):
        limiter.try_acquire(item)
        sleep(1)
except BucketFullException as err:
    has_raised = True
    assert str(err)
    # Bucket for vutran with Rate 3/5 is already full
    assert isinstance(err.meta_info, dict)
    # {'error': 'Bucket for vutran with Rate 3/5 is already full', 'identity': 'tranvu', 'rate': '5/5', 'remaining_time': 2}
