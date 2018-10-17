import json
import subprocess

from bottle import Bottle, run, request, debug

app = Bottle()

auth_key = 'asdfg' # Keep this private, it is your private key
exec_args = ['echo', 'test'] # Example args to execute on the system shell

@app.route('/', method='POST')
def receive():
    if not request.json:
        return {'error': 'json required'}
    data = request.json
    print(data)
    if data != {'auth': auth_key}:
        return {'error': 'not authenticated'}
    
    else:
        try:
            subprocess.call(exec_args)
            return {'success': True}

        except Exception as e:
            print('\033[91mEncountered an exception: %s\033[0m' % e)
            return {'error': 'uncaught server error'}

run(app, host='0.0.0.0', port=8088)
