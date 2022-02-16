from webbrowser import get
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results

import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    source = input("Reddit, Wikipedia or Twitter(NO TWITTER)?: ")
    search = input("Search Query: ") #This will be an input string
    results = []
    limit = 1

    if source.lower() == 'wikipedia':
        wikiurl = "https://en.wikipedia.org/w/api.php?action=opensearch&search=" + search + "&limit=10&namespace=0&format=json"
        response = requests.get(wikiurl)

        for i in range(limit):
            results.append([response.json()[1][i], response.json()[3][i]])


    elif source.lower() == 'reddit':
        redditurl = "https://www.reddit.com/"
        redditData = {'grant_type': 'password', 'username': 'FayazTestsAPI', 'password': 'APITestingWithFayaz'}
        auth = requests.auth.HTTPBasicAuth('qTgintKTLlcLhma-KR9ZAA', 'SpMdvn3rH8b8zbqZgQPxjL-s-IQLeA')
        redditReq = requests.post(redditurl + 'api/v1/access_token',
                                    data = redditData, headers={'user-agent': 'script by Fayaz Ahmed'},
                                    auth = auth)
        redditD = redditReq.json()
        redditToken = 'bearer' + redditD['access_token']
        redditurl = 'https://oauth.reddit.com/r/all/search'
        redHeaders = {'Authorization': redditToken, 'User-Agent': 'Script by Fayaz Ahmed'}
        redParams = {'q': search, 'limit': limit, 'sort': 'top'}
        response = requests.get(redditurl, headers = redHeaders, params = redParams)

        for i in range(limit):
            full = response.json()['data']['children'][i]['data']
            results.append([full['title'], 'https://reddit.com' + full['permalink'], full['thumbnail']])


    '''
    elif source.lower() == 'twitter':
        twiturl = "https://api.twitter.com/1.1/search/tweets.json?q=" + search + "&count=" + str(limit) + "&result_type=popular"
        twitAPI = "UUJH8fe6OkF7RaglDurbjssq4"
        twitSecret = "YXXhwpNEpe8gBb57Ugmj4D6BjEB1pf5ch9PPbH05oB7XGJasTL"
        twitBearer = "AAAAAAAAAAAAAAAAAAAAACcbZQEAAAAAk4wW2OMMtPjKa0Gob3ruYsdKlAI%3DKHJQBUX6HinobsueJynN5bQGF0sLuYG0WbCKeZfQQpgaJe9nMa"
        twitReq = requests.get(twiturl, headers = headers)

        enterpriseSearchArgs = load_credentials(STUFF)
        rule = gen_rule_payload(search, results_per_call=limit)
        tweets = collect_results(rule, max_results=limit, result_stream_args=enterpriseSearchArgs)



        results.append['','']
        #print(twitReq.json())
    '''


    for res in results:
        print(res[0] + ": " + res[1])

    return{search: results}
