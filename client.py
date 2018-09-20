import ssl
from kmip.pie.client import ProxyKmipClient
from kmip.pie import client
from kmip import enums

client = ProxyKmipClient(
    hostname='127.0.0.1',
    port=5696,
    cert='certs/client_certificate_jane_doe.pem',
    key='certs/client_key_jane_doe.pem',
    ca='certs/root_certificate.pem',
    ssl_version='PROTOCOL_SSLv23',
    username='example_username',
    password='example_password',
    config='client'
)

client.open()

key_id = client.create(
    enums.CryptographicAlgorithm.AES,
    256,
    operation_policy_name='default',
    name='Test_256_AES_Symmetric_Key',
    cryptographic_usage_mask=[
        enums.CryptographicUsageMask.ENCRYPT,
        enums.CryptographicUsageMask.DECRYPT
    ]
)
print('key[%s] created' % key_id)

key = client.get(key_id)
print('key: %s' % key)