import csv
import io

#from google.cloud import pubsub
from google.oauth2 import service_account
from googleapiclient import discovery
from googleapiclient.errors import HttpError



class CreateIotDevice(object):

  def __init__(self):
      pass


  def get_client(self, service_account_json):
    """Returns an authorized API client by discovering the IoT API and creating
    a service object using the service account credentials JSON."""
    api_scopes = ['https://www.googleapis.com/auth/cloud-platform']
    api_version = 'v1'
    discovery_api = 'https://cloudiot.googleapis.com/$discovery/rest'
    service_name = 'cloudiotcore'

    #credentials = service_account.Credentials.from_service_account_file(
    #        service_account_json)
    #scoped_credentials = credentials.with_scopes(api_scopes)

    discovery_url = '{}?version={}'.format(
            discovery_api, api_version)

    return discovery.build(
            service_name,
            api_version,
            discoveryServiceUrl=discovery_url,
            #credentials=scoped_credentials
            )


  def create_device(self, device_string):
    (device_id, public_key) = device_string.split('|')
    public_key = "-----BEGIN PUBLIC KEY-----\n" + public_key + "\n-----END PUBLIC KEY-----\n"

    service_account_json="serviceaccountkey.json"
    project_id="altostrat-demo"
    cloud_region="europe-west1"
    registry_id="altostrat-iot-power-registry"

    registry_name = 'projects/{}/locations/{}/registries/{}'.format(
            project_id, cloud_region, registry_id)

    client = self.get_client(service_account_json)

    #with io.open(public_key_file) as f:
    #    public_key = f.read()

    device_template = {
        'id': device_id,
        'credentials': [{
            'publicKey': {
                'format': 'ES256_PEM',
                'key': public_key
            }
        }]
    }

    devices = client.projects().locations().registries().devices()
    devices.create(parent=registry_name, body=device_template).execute()
    return "ca a marche"

# POST https://cloudiot.googleapis.com/v1/{parent=projects/*/locations/*/registries/*}/devices
# parent	string
# The name of the device registry where this device should be created. For example, projects/example-project/locations/us-central1/registries/my-registry.
# need cloudiot.devices.create


#    return None


# google-api-python-client




    #headers = {
    #        'authorization': 'Bearer {}'.format(jwt_token),
    #        'content-type': 'application/json',
    #        'cache-control': 'no-cache'
    #}

    #basepath = '{}/projects/{}/locations/{}/registries/{}/devices/{}/'
    #template = basepath + 'config?local_version={}'
    #config_url = template.format(
    #    base_url, project_id, cloud_region, registry_id, device_id, version)

    #resp = requests.get(config_url, headers=headers)

    #if (resp.status_code != 200):
    #    print('Error getting config: {}, retrying'.format(resp.status_code))
    #    raise AssertionError('Not OK response: {}'.format(resp.status_code))


