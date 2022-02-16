from webbrowser import get
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")
"""
@app.route('/post', methods=['POST'])
def post():
    #userReq = request.form[0]
    '''
    source = input("Reddit or Wikipedia?: ")
    search = input("Search Query: ") #This will be an input string
    results = []
    limit = 10

    if 'w' in source.lower():
        wikiurl = "https://en.wikipedia.org/w/api.php?action=opensearch&search=" + search + "&limit=10&namespace=0&format=json"
        response = requests.get(wikiurl)

        for i in range(limit):
            results.append([response.json()[1][i], response.json()[3][i]])


    elif 'r' in source.lower():
        redditurl = "https://www.reddit.com/"
        redditData = {'grant_type': 'password', 'username': 'FayazTestsAPI', 'password': 'APITestingWithFayaz'}
        auth = requests.auth.HTTPBasicAuth('qTgintKTLlcLhma-KR9ZAA', 'SpMdvn3rH8b8zbqZgQPxjL-s-IQLeA')
        redditReq = requests.post(redditurl + 'api/v1/access_token', data = redditData, headers={'user-agent': 'script by Fayaz Ahmed'}, auth = auth)
        redditD = redditReq.json()
        token = redditD['access_token']

        redditToken = 'bearer ' + token
        apiurl = "https://oauth.reddit.com/r/all/search"
        headers = {'Authorization': redditToken, 'User-Agent': 'Script by Fayaz Ahmed'}
        payload = {'q': search, 'limit': limit, 'sort': 'top'}
        response = requests.get(apiurl, headers = headers, params = payload)

        for i in range(limit):
            full = response.json()['data']['children'][i]['data']
            results.append([full['title'], 'https://reddit.com' + full['permalink'], full['thumbnail']])
    '''

    return "received: {}".format(userReq)
'''
if __name__ == "__main__":
    app.run()
"""


#for res in results:
#    print(res[0] + ": " + res[1])
