
import os

#Cloud API details
API_KEY = "4HH4UMT6PS3AOK7L"#os.getenv('API_KEY',None)
API_SECRET_KEY = "WaXB9rxtPl9GUVNGN+kyNj4M6pD+w13k7uTFwgUEcswga0CflprPZ18indJdud4N" #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = "pkc-p11xm.us-east-1.aws.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)

#Authentication Related Variables 
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"


#Schema Related Variables
ENDPOINT_SCHEMA_URL  =  "https://psrc-kjwmg.ap-southeast-2.aws.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)
SCHEMA_REGISTRY_API_KEY = "W2J6SLY73EKVD7TC"#os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "MfCiygK2sk1yiWgUdcJM9S1oYZUtMqZIVIeU+poZOPQkknoBaB5Zqfup7oxMbflA"#os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    #print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

