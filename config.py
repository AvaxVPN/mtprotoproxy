import json
import os
import sys

from dotenv import load_dotenv

try:
    load_dotenv(sys.argv[1])
except IndexError:
    load_dotenv()

PORT = os.getenv('PORT', 443)

# name -> secret (32 hex chars)
with open(os.getenv('CONFIG_JSON', '/etc/avaxvpn/mtproto/config.json')) as file:
    config_data = json.load(file)

USERS = config_data['USERS']

USER_MAX_TCP_CONNS = config_data['USER_MAX_TCP_CONNS']

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = os.getenv('TLS_DOMAIN', 'www.google.com')

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = os.getenv('AD_TAG', '')

METRICS_PORT = 9909
