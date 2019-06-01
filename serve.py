import string
import googleapiclient.discovery

import config
import random

DEVELOPER_KEY = config.CONFIG['secret_key']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def search_list_by_keyword(client, **kwargs):

  response = client.search().list(
    **kwargs
  ).execute()

  return response.get('items')


def getvideo():

    client = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, developerKey=DEVELOPER_KEY)

    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(1))
    output = search_list_by_keyword(client,
                                  part='snippet',
                                  maxResults=25,
                                  q=random_string,
                                  channelId='UCFKE7WVJfvaHW5q283SxchA',
                                  type='video',
                                  videoEmbeddable ='true')

    return output