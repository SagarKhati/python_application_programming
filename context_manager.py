import sqlite3
import inspect
import os
import zipfile
import subprocess


with open('sample.txt', 'r') as fp:
    content = fp.read()
    
    
    


try:
    dbConnection = sqlite3.connect('TEST.db')
    cursor = dbConnection.cursor()
    '''
    Few db operations
    ...
    '''
except Exception:
    print('No Connection.')
finally:
    dbConnection.close()
    
    
    
    
class DbConnect(object):
    def __init__(self, dbname):
        self.dbname = dbname
    def __enter__(self):
        self.dbConnection = sqlite3.connect(self.dbname)
        return self.dbConnection
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbConnection.close()
with DbConnect('TEST.db') as db:
    cursor = db.cursor()
    '''
   Few db operations
   ...
    '''
    
    
    
    
    
def writeTo(filename, input_text):
    with open(filename, 'w') as fp:
        fp.write(input_text)

try:
    filename = str(input())
except:
    filename = None

try:
    input_text = str(input())
except:
    input_text = None

res = writeTo(filename, input_text)
if 'with' in inspect.getsource(writeTo):
    print("'with' used in 'writeTo' function definition.")
        
if os.path.exists(filename):
    print('File :',filename, 'is present on system.')
    with open(filename) as fp:
        content = fp.read()
    if content == input_text:
        print('File Contents are :', content)
        
        
        
        
# Define 'writeTo' function below, such that 
# it writes input_text string to filename.
def writeTo(filename, input_text):
    with open(filename, 'w') as fp:
        fp.write(input_text)
# Define the function 'archive' below, such that
# it archives 'filename' into the 'zipfile'
def archive(zfile, filename):
    with zipfile.ZipFile(zfile, 'w') as zp:
        zp.write(filename)

try:
    filename = str(input())
except:
    filename = None

try:
    input_text = str(input())
except:
    input_text = None
    
try:
    zip_file = str(input())
except:
    zip_file = None
        
res = writeTo(filename, input_text)
if 'with' in inspect.getsource(writeTo):
    print("'with' used in 'writeTo' function definition.")
        
if os.path.exists(filename):
    print('File :',filename, 'is present on system.')
 
res = archive(zip_file, filename)
    
if 'with' in inspect.getsource(archive):
    print("'with' used in 'archive' function definition.")
        
if os.path.exists(zip_file):
    print('ZipFile :',zip_file, 'is present on system.')    
    



def run_process(cmd_args):
    with subprocess.Popen(cmd_args, stdout=subprocess.PIPE) as p:
        out1 = p.communicate()[0]
    return out1


cmd_args_cnt = 0
cmd_args_cnt = int(input())
cmd_args_i = 0
cmd_args = []
while cmd_args_i < cmd_args_cnt:
    try:
        cmd_args_item = str(input())
    except:
        cmd_args_item = None
    cmd_args.append(cmd_args_item)
    cmd_args_i += 1


res = run_process(cmd_args);
#f.write(res.decode("utf-8") + "\n")
    
if 'with' in inspect.getsource(run_process):
    print("'with' used in 'run_process' function definition.\n")
    
if 'Popen' in inspect.getsource(run_process):
    print("'Popen' used in 'run_process' function definition.\n")
    print('Process Output : %s\n' % (res.decode("utf-8")))


    
