from flask import Flask, render_template, request, redirect
from tweets import getTweetsBTC, getTweetsBTCEmbedded, getTweetsDOGE, getTweetsDOGEEmbedded
import time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/bitcoin")
def BTC():
    coin = "Bitcoin"
    tweetsNum = getTweetsBTC()
    tweetsEm = getTweetsBTCEmbedded()
    seconds =  time.time()
    local_time = time.ctime(seconds)
    return render_template("index.html", tweets=tweetsNum, embed=tweetsEm, time=local_time, coin=coin)

@app.route("/doge")
def Doge():
    coin = "Dogecoin"
    tweetsNum = getTweetsDOGE()
    tweetsEm = getTweetsDOGEEmbedded()
    seconds =  time.time()
    local_time = time.ctime(seconds)
    return render_template("index.html", tweets=tweetsNum, embed=tweetsEm, time=local_time, coin=coin)

if __name__ == '__main__':
    app.run(debug=True)