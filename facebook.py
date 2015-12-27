# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 09:31:58 2015

@author: steve
"""

import facebook  
from collections import Counter
import itertools 

access_token = 'CAACEdEose0cBACOQrU8Biztt2Kv1IgTQxiBG1XDN6TX5BwwHg1bnziWhGw9iGPinAsmZAr2AeEb6bEjcTi4mTCU9ZAk5eUcmhzKr7Fbm4XuTQw89U4tB440TORAgZBwIlywUoZCIIZAN0JFWeQ5jPP7yRLnZC10aSO4DyKpeoCXa1HOMZCsCyafsFTAOektWAXj6tgB3ZB2IR6hLZC7xbKyo7'
g = facebook.GraphAPI(access_token)

friends = g.get_connections(id="me", connection_name="friends")
#g.put_object(parent_object='me', connection_name='feed',
#                 message='This is a test, posting through the Facebook API and Python. Go Hawks.')
profile = g.get_object("me")