import os   
import argparse
from functions import ghApi

appdir = os.getcwd()
firstdir = '/home/astin/Documents/Tools'
secondir = '/home/astin/Documents/projects'

prohe = (f'''
chose the project directory Default is "1"
1) {firstdir}
2) {secondir}
''')

parser = argparse.ArgumentParser()
parser.add_argument('filename',help='name of the project' ,type=str)
parser.add_argument('-p', '--path',help=prohe,default='')


args = parser.parse_args()

filename = args.filename
path = args.path

# filename = 'test'
# path = ''



if path == '2':
    os.chdir(secondir)
    filep = secondir + '/' + filename
    # os.system('pwd')
else:
    os.chdir(firstdir)
    filep = firstdir + '/' + filename
    # os.system('pwd')


ghApi.gh_repo(filename,filep,appdir)

os.chdir(filep)


os.system('code .')