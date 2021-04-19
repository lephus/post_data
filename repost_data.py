import requests
import subprocess
subprocess.call(r"php D:\DOANPYTHON\UIPython\src\demo.php")
proc = subprocess.Popen(r"php D:\DOANPYTHON\UIPython\src\demo.php", shell=True, stdout=subprocess.PIPE)
script_response = proc.stdout.read()
print(script_response.decode('utf-8'))
url = 'https://dau123.000webhostapp.com/functionPhp/post_data.php'
myobj = {'code': '43A1-392333', 'img': script_response.decode('utf-8')}
x = requests.post(url, data = myobj)
print(x.text)