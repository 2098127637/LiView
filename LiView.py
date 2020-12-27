from configparser import ConfigParser
cf = ConfigParser()
f = open('INIT.INI')
cf.read_file(f)
entrance=cf.get('entrance', 'startPy')
python = cf.get('python', 'python')
print(entrance,python)
import win32api
win32api.ShellExecute(0, "open", python, entrance, '', 0)
