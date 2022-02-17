from webbrowser import get
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    results = []
    return render_template("index.html", data=results, site = ' ', search=' ', resNum=len(results))


@app.route('/post', methods=['POST'])
def post():
    userReq = request.form

    results = []
    site = userReq['searchSite']
    if userReq['numResults'].isnumeric():
        limit = int(userReq['numResults'])
    else:
        limit = 10
    search = userReq['searchQuery']
    if len(search) == 0:
        return render_template("index.html", data=results, site = ' ', search=' ', resNum=len(results))

    def wikiAPI(limit, search):
        wikiurl = "https://en.wikipedia.org/w/api.php?action=opensearch&search=" + search + "&limit=" + str(limit) + "&namespace=0&format=json"
        response = requests.get(wikiurl)

        for i in range(min(limit, len(response.json()[1]))):
            results.append([response.json()[1][i], response.json()[3][i]])

        return results

    def redditAPI(limit, search):
        redditurl = "https://www.reddit.com/"
        redditData = {'grant_type': 'password', 'username': 'USERNAME', 'password': 'PASSWORD'}
        auth = requests.auth.HTTPBasicAuth('APP-KEY', 'SECRET-KEY')
        redditReq = requests.post(redditurl + 'api/v1/access_token', data = redditData, headers={'user-agent': 'script by Fayaz Ahmed'}, auth = auth)
        redditD = redditReq.json()
        token = redditD['access_token']

        redditToken = 'bearer ' + token
        apiurl = "https://oauth.reddit.com/r/all/search"
        headers = {'Authorization': redditToken, 'User-Agent': 'Script by Fayaz Ahmed'}
        payload = {'q': search, 'limit': limit, 'sort': 'relevant'}
        response = requests.get(apiurl, headers = headers, params = payload)
        for i in range(min(limit, len(response.json()['data']['children']))):
            full = response.json()['data']['children'][i]['data']
            results.append([full['title'], 'https://reddit.com' + full['permalink']])

        return results

    if site == "Wikipedia":
        results = wikiAPI(limit, search)
    elif site == "Reddit":
        results = redditAPI(limit, search)

    return render_template("index.html", data = results, site = site +':', search = search, resNum=len(results))


if __name__ == "__main__":
    app.run()
