import urllib.parse
import json
import requests
from itemadapter import ItemAdapter
import os

class ElasticSearchPipeline:
    index_name = os.environ.get('ES_INDEX')
    type_name = os.environ.get('ES_TYPE')
    id_field = os.environ.get('ES_ID')

    def __init__(self, es_host, es_user, es_password):
        self.es_host = es_host
        self.es_user = es_user
        self.es_password = es_password
        self.auth = (es_user, es_password)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            es_host=os.environ.get('ES_HOST'),
            es_user=os.environ.get('ES_USER'),
            es_password=os.environ.get('ES_PASSWORD'),
        )

    def process_item(self, item, spider):
        body = ItemAdapter(item).asdict()
        id_value = urllib.parse.quote(body[self.id_field].encode('utf8'), safe='')
        del body[self.id_field]

        url = f'{self.es_host}/{self.index_name}/{self.type_name}/{id_value}'
        headers = { "Content-Type": "application/json" }
        r = requests.put(url, auth=self.auth, headers=headers, data=json.dumps(body))
        return item
