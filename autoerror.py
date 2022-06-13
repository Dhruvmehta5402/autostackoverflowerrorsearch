from subprocess import Popen, PIPE
import requests
import webbrowser

FILE_TO_RUN = 'C:\\Users\\Dhruv\\stackoverauto\\test.py'

def execute_return(cmd):
    args = cmd.split()
    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    return out, err

def mak_req(error):
    resp = requests.get("https://api.stackexchange.com/" +
                        "/2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
    return resp.json()

def get_urls(json_dict):
    url_list = []
    count = 0

    for i in json_dict['items']:
        if i['is_answered']:
            url_list.append(i['link'])
            count += 1
            if count == 3 or count == len(i):
                break

    for i in url_list:
        webbrowser.open(i)


out, err = execute_return(f'python {FILE_TO_RUN}')

erro = err.decode("utf-8").strip().split('\r\n')[-1]
print(erro)

if erro:
    filter_error = erro.split(':')
    json = mak_req(erro)
    get_urls(json)

else:
    print('No error')