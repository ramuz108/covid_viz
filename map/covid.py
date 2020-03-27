from flask import jsonify
from flask import Flask, render_template, request,redirect,url_for
from flask import flash
import json
import requests
app = Flask(__name__)
app.secret_key = "cyberdome"
@app.route('/')
def search():
    r = requests.get('https://volunteer.coronasafe.network/api/reports')
    res = r.content
    ress = json.loads(res)
    print(type(ress))
    #print(ress['kerala'].keys())
    print(ress['kerala'])
    #for i in range(0,25):
        #html += "<div id='child'>" 
        #html += "<h4> " 
        #html +=  res 
        #html += "</h4>" 
    return html
@app.route("/news")
def news():
    html = "<!DOCTYPE html><html lang='en'><head><title>Bootstrap Example</title><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css'><script src='https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js'></script><script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js'></script></head><body bgcolor='black'><div class='container' style='color:black'>"
    my_url = "http://newsapi.org/v2/top-headlines?q=coronavirus&country=in&apiKey=9daaf565f303400ba63c84d3f6124066"
    my_open_bbc_page = requests.get(my_url).json()
    my_article = my_open_bbc_page["articles"]
    my_results = []
    for ar in my_article:
        html += "<div class='card'><div class='card-body'>"
        html += "<img src='" + str(ar["urlToImage"]) + "' width=1060 height=500 />"
        html += "<p>" + ar["source"]["name"] + "</p>"  
        html += "<h1 class='card-title'>" + ar["title"] + "</h1>"
        html += "<a href=" + str(ar["url"]) + " class='card-link'> View full news </a>" 
        s =  "<a href='" + str(ar["url"]) + "'> View full news </a>" 
        print(s) 
        html += "</div>"
    html += "</div></body></html>"    
    
    return html
@app.route("/data")
def data():
    html = "<!DOCTYPE html><html lang='en'><head><title>Bootstrap Example</title><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css'><script src='https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js'></script><script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js'></script></head><body bgcolor='black'>"
    html += "<marquee style='color:red;bgcolor:black'><p>"
    for i in range(len(my_results)):
        html += "| " + my_results[i] + " |" 
    html += "</p></marquee>"
    r = requests.get('https://volunteer.coronasafe.network/api/reports')
    res = r.content
    ress = json.loads(res)
    html += "<table class='table table-dark table-hover'><thead><tr><th>OBSERVATION</th><th>HOME ISOLATION</th><th>TOTAL HOSPITALISED</th><th>HOSPITALISED TODAY</th><th>POSITIVE</th><th>CURED</th><th>DEATHS</th></tr></thead>"
    #print(ress['kerala'].keys())
    for key,val in ress['kerala'].items():
        html += "<tbody><tr>"
        html += "<td>" + key + "</td>"
        html += "<td>" + str(val["under_observation"]) + "</td>"
        html += "<td>" + str(val["under_home_isolation"]) + "</td>" 
        html += "<td>" + str(val["total_hospitalised"]) + "</td>"
        html += "<td>" + str(val["hospitalised_today"]) + "</td>"
        html += "<td>" + str(val["corona_positive"]) + "</td>"
        html += "<td>" + str(val["deaths"]) + "</td>"

    html += "</table></body></html>"
    return html    
if __name__ == '__main__':
    app.run(debug = True)
