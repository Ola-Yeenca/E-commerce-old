# config.py

# stripe_integration/config.py

from decouple import config as decouple_config

STRIPE_PUBLIC_KEY = decouple_config('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = decouple_config('STRIPE_SECRET_KEY')



STRIPE_PUBLIC_KEY = 'pk_test_51HQAqcARwBP3zBgzrKV2H6MWcM8h5cbc2PicDm9fXhp57xl29OE4nJfpvseTYvi7ltzxQtCD1DiOAisjq9ZKVS9r00pPvXHVty'
STRIPE_SECRET_KEY = 'sk_test_51HQAqcARwBP3zBgziDMpzpNEJ0CZv2NfWhOLFtdvUFzKihP49GDOqn5HW7RwdCdnkUZqJ7aP8hr2YUmBxcrmUcJO00GsNBalLX'
