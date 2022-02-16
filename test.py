import requests

redditurl = "https://www.reddit.com/"
redditData = {'grant_type': 'password', 'username': 'NearquadFarquad', 'password': 'Inheritance1'}
auth = requests.auth.HTTPBasicAuth('i9gheT9P680rW97oiuhXWA', 'dJ1iwMFSJEzuCGGyVR_KG0zF6Hp8TQ')
redditReq = requests.post(redditurl + 'api/v1/access_token', data = redditData, headers={'user-agent': 'script by Fayaz Ahmed'}, auth = auth)
redditD = redditReq.json()
token = redditD['access_token']

redditToken = 'bearer ' + token
apiurl = "https://oauth.reddit.com/r/all/search"
headers = {'Authorization': redditToken, 'User-Agent': 'Script by Fayaz Ahmed'}
payload = {'q': 'thilany', 'limit': 1, 'sort': 'relevance'}
response = requests.get(apiurl, headers = headers, params = payload)

print(response.json()['data']['children'][0])
