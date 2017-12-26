from flask import Flask, render_template, Response
import time

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/done')
def done():
	return 'done'

def getMap():
    print('bob')
    time.sleep(1)

def getIMDB():
    print('Imdb')
    time.sleep(1)

def getSteve():
    print('steve')
    time.sleep(1)

def getLory():
    print('lory')
    time.sleep(1)

@app.route('/loadcontent')
def progress():
    def main():
        tasks = 4
        progress = 0
        functions = [getMap, getIMDB, getSteve, getLory]

        while progress < tasks:
            functions[progress]()
            progress +=1
            yield "data:" + str(((100/tasks)*progress)/100) + "\n\n"
            #generateresponse()
            time.sleep(0.5)

    return Response(main(), mimetype= 'text/event-stream')

if __name__ == "__main__":
	app.run()