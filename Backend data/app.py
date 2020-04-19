# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from data import getalldata
from flask_jsonpify import jsonpify
# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/getdata', methods=['GET'])
def home():
    data = getalldata()
    totalrows = data.shape[0]
    i = 0
    all_attend=[]
    for i in range(0, totalrows):
        all_attend.append('{ " type " : " Feature " , " geometry " : { "type": "Point","coordinates": ['+str(data.iloc[i, 6])+','+ str(data.iloc[i, 7])+']},"properties": {"zone": '+str(data.iloc[i, 5])+'} }' )

    return jsonify(all_attend)


# driver function
if __name__ == '__main__':

    app.run(host='0.0.0.0')
