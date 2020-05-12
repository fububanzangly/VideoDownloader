import requests
import json
def download(download_url):
    url = 'http://192.168.1.136:6800/jsonrpc'
    json_rpc = json.dumps({
        'id': '',
        'jsonrpc': '2.0',
        'method': 'aria2.addUri',
        'params': ["token:Passw0rd",[download_url]]
        })
    response = requests.post(url=url, data=json_rpc)
    print(response.content)