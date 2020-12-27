from configparser import ConfigParser
cf = ConfigParser()
f = open('INIT.INI')
cf.read_file(f)
python = cf.get('python', 'python')
print(python)
import win32api
win32api.ShellExecute(0, "open", python,r'E:\LiView\userData\spider\XuanShuSpider\call\recommend.py', '', 1)