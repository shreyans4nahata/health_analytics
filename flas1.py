from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/')
def get_data():
	k={}
	i=0
	with open('data1.txt') as fin:
		for line in fin:
			j=[]
			j = list(map(str,line.split(',')))
			k[j[0]] = [float(j[z]) for z in range(1,11)]
	return jsonify(k)

if __name__ == '__main__':
    app.run(host= '0.0.0.0')