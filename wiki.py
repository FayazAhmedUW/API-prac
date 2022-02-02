from webbrowser import get
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    search = input("Search Query: ") #This will be an input string
    results = []
    response = requests.get("https://en.wikipedia.org/w/api.php?action=opensearch&search=" + search + "&limit=10&namespace=0&format=json")
    for i in range(10):
        results.append([response.json()[1][i], response.json()[3][i]])

    for res in results:
        print(res[0] + ": " + res[1])

    return{search: results}
