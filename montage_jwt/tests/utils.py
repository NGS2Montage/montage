from montage_jwt.settings import api_settings
import os

def set_key_pair():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    p_key_file = dir_path + '/private.pem'
    pub_key_file = dir_path + '/public.pem'

    with open(p_key_file, 'r') as f:
        p_key = f.read().strip()

    with open(pub_key_file, 'r') as f:
        pub_key = f.read().strip()

    api_settings.PRIVATE_KEY = p_key
    api_settings.PUBLIC_KEY = pub_key
