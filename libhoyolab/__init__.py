import json
import os
import pathlib
import requests


requests.packages.urllib3.disable_warnings()

session = requests.session()

lib_version = '0.0.1'
home_dir = str(pathlib.Path.home())
app_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
run_dir = os.path.join(home_dir, '.libhoyolab')
config_dir = os.path.join(run_dir, 'configs')
account_file = os.path.join(config_dir, 'account.json')
current_user_file = os.path.join(config_dir, 'current_user')

public_key = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDvekdPMHN3AYhm/vktJT+YJr7\ncI5DcsNKqdsx5DZX0gDuWFuIjzdwButrIYPNmRJ1G8ybDIF7oDW2eEpm5sMbL9zs\n9ExXCdvqrn51qELbqj0XxtMTIpaCHFSI50PfPpTFV9Xt/hmyVwokoOXFlAEgCn+Q\nCgGs52bFoYMtyi+xEQIDAQAB\n-----END PUBLIC KEY-----'
Salt_K2 = 'F6tsiCZEIcL9Mor64OXVJEKRRQ6BpOZa'
Salt_LK2 = 'xc1lzZFOBGU0lz8ZkPgcrWZArZzEVMbA'
Salt_4X = 'xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs'
Salt_6X = 't0qEgfub6cvueAPgR5m9aQWWVciEer7v'
Salt_PROD = 'JwYDpKvLj6MrMqqYU6jTKF17KNO2PXoS'
mysVersion = '2.55.1'
mysClient_type = '2'

account_default = {'account': {}}

newsType = {'announce': '1', 'activity': '2', 'information': '3'}
actions = {"article": "文章", "recommend": "推荐", "announce": "公告", "activity": "活动", "information": "资讯",
           "history": "历史", "search": "搜索", "setting": "设置", "user": "用户", "error": "错误", "login": "登录"}

if not os.path.exists(run_dir):
    os.mkdir(run_dir)

if not os.path.exists(config_dir):
    os.mkdir(config_dir)

_current_user = '-1'
with open(current_user_file, 'w') as f:
    f.write(_current_user)


def getExistUser():
    try:
        with open(account_file) as f:
            account_set = json.load(f)
    except:
        account_set = account_default
        with open(account_file, 'w') as f:
            json.dump(account_set, f, indent=2, ensure_ascii=False)
    return list(account_set['account'].keys())


def get_current_user():
    global _current_user
    with open(current_user_file, 'r') as f:
        _current_user = f.read()
    if _current_user == '-1':
        _current_user = getExistUser()[0]
        with open(current_user_file, 'w') as f:
            f.write(_current_user)
    return _current_user


def set_current_user(uid):
    global _current_user
    if uid in getExistUser():
        _current_user = uid
        with open(current_user_file, 'w') as f:
            f.write(uid)
    return _current_user

