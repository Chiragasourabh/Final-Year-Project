from flask import Flask, request, jsonify, render_template
import joblib
import random
import test
import database
from PhishTankAPI import PhishTank
PhishTankObj = PhishTank()
app = Flask(__name__)
app.config["DEBUG"] = True

apiKey = "vXSDrKoBvByAPkIzQIfQuiYDLx2OvH7wIypN67Mn"
# dbPass= "tXsDi9pEJ8M6tmk"  #74936
# dbCursor = database.dbInit(app)
# dbCursor.execute("CREATE TABLE Persons ( PersonID int,LastName varchar(255));")
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
     {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'}
]
dashboard = {'apiCall': 0 ,
            'pish': 0,
            'notPish': 0,
            'failed': 0
            }

model = joblib.load('random_forest.pkl')
print("Pickle Unpacked")
@app.route("/")
def index():
    print("Root Opened in Browser")
    return render_template('Home.html')

@app.route("/Dashboard")
def dashboard1():
    print("Root Opened in Browser")
    return render_template('Dashboard/index.html')


@app.route("/api/v0/pishcheck",methods=['POST','GET'])
def api0():
    print("\n")
    print("################### API V0 Called ##################")
    flag = False
    if request.method == 'POST':
        key = request.form['key']
        url = request.form['url']
        flag=True
    elif request.method == 'GET':
        if 'key' in request.args and 'url' in request.args:
            key = str(request.args['key'])
            url = str(request.args['url'])
            flag=True
        else:
            dashboard['failed']+=1
            print(dashboard)
            return "Please Follow the format ------> ?key=key&url=url"
    if(flag):
        if key =="vXSDrKoBvByAPkIzQIfQuiYDLx2OvH7wIypN67Mn":
            print("Key Validation Successful")
            dashboard['apiCall']+=1
            ret = {'url':url,'pish':str(bool(random.getrandbits(1)))}
            # print(dashboard)
            print(ret)
            return jsonify(ret)
        else:
            print("Key Validation Failed")
    dashboard['failed']+=1
    print(dashboard)
    print(ret)
    return "Key Error"

@app.route("/api/v1/pishcheck",methods=['GET'])
def api1():
    print("API V1 Called")
    if 'id' in request.args:
        id = int(request.args['id'])
        results = []

        for book in books:
            if book['id'] == id:
                results.append(book)
        return jsonify(results)
    return jsonify(books)

@app.route("/api/v2/pishcheck",methods=['POST','GET'])
def api2():
    print("\n")
    print("################### API V2 Called ###################")
    flag = False
    if request.method == 'POST':
        key = request.form['key']
        url = request.form['url']
        flag=True
    elif request.method == 'GET':
        if 'key' in request.args and 'url' in request.args:
            key = str(request.args['key'])
            url = str(request.args['url'])
            flag=True
        else:
            dashboard['failed']+=1
            print(dashboard)
            return "Please Follow the format ------> ?key=key&url=url"
    if(flag):
        if key == apiKey:
            print("Key Validation Successful")
            PhishTankResult = PhishTankObj.check(url)
            if PhishTankResult.in_database:
                if PhishTankResult.valid:
                    print("\n")
                    print("{url} is a phish!".format(url=PhishTankResult.url))
                    print("\n")
                    ret = {'url':url, 'pish':"True"}
                else:
                    print("\n")
                    print("{url} is not a phish!".format(url=PhishTankResult.url))
                    print("\n")
                    ret = {'url':url,'pish':"False"}
            else:
                # print("{url} is not in the PhishTank database".format(url=PhishTankResult.url))
                x = test.check(url,model)
                ret = {'url':url, 'pish':str(x)}

            return jsonify(ret)
        else:
            print("Key Validation Failed")
            return "Key Validation failed"
    else:
        return "Please Follow the format ------> ?key=key&url=url"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("PageNotFound.html")
    