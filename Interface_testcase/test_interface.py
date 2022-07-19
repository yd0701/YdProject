import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))   #获取当前路径
rootPath = os.path.split(curPath)[0]    #通过路径切割的方式,获取项目根目录
sys.path.append(rootPath)  #把项目根目录,添加到环境变量中
from Interface_api.test_interfaceapi import TestApiDemo


class Test_seafile:
    def test_login(self):
        global token
        global ad
        # 1.1
        # 请求数据的追捕
        url_login = 'http://42.192.62.88/api2/auth-token/'
        data_login = {
            'username': '1217550253@qq.com',
            'password': '123456'
        }
        ad = TestApiDemo()
        # 模拟请求下发
        res = ad.do_post(url=url_login, json=data_login)
        token = res.json()['token']
        # 断言校验本次测试是否成功
        assert res.status_code == 200, '断言失败'
        assert 'token' in res.text, '断言失败'
        # 解析响应结果 判断本次接口的请求是否响应成功
        print('1.1' + str(res))
        print(res.headers)
        print(token)
        print(res.text)

    def test_accountinfo(self):
        # 1.2
        url_account_info = ('http://42.192.62.88/api2/account/info/')
        headers_account_info = {
            'Authorization': 'Token ' + str(token)
        }
        res_account_info = ad.do_get(url=url_account_info, headers=headers_account_info)
        print('')
        print('1.2' + str(res_account_info))
        print(res_account_info.headers)
        print(res_account_info.text)
        assert res_account_info.status_code == 200, '断言失败'

    def test_repos(self):
        global repo_id
        # 1.3
        url_repos = ('http://42.192.62.88/api2/repos/')
        headers_repos = {
            'Authorization': 'Token ' + str(token)
        }
        data_repos = {
            'name': 'JMeter'
        }
        res_repos = ad.do_post(url=url_repos, headers=headers_repos, json=data_repos)
        repo_id = res_repos.json()['repo_id']
        print('')
        print('1.3' + str(repo_id))
        print(res_repos)
        print(res_repos.headers)
        print(res_repos.text)
        assert res_repos.status_code == 200, '断言失败'

    def test_repos2(self):
        # 1.4
        url_repos2 = ('http://42.192.62.88/api2/repos/')
        headers_repos2 = {
            'Authorization': 'Token ' + str(token)
        }
        res_repos2 = ad.do_get(url=url_repos2, headers=headers_repos2)
        print('')
        print('1.4' + str(res_repos2))
        print(res_repos2.headers)
        # print(res_repos.text)
        assert res_repos2.status_code == 200, '断言失败'

    def test_creatfile(self):
        # 1.6
        url_creat_file = ('http://42.192.62.88/api2/repos/' + str(repo_id) + '/file/?p=/qqq&reloaddir=true')
        headers_creat_file = {
            'Authorization': 'Token ' + str(token)
        }
        data_creat_file = {
            'operation': 'create'
        }
        res_creat_file = ad.do_post(url=url_creat_file, headers=headers_creat_file, data=data_creat_file)
        print('')
        print('1.6' + str(res_creat_file))
        print(res_creat_file.headers)
        print(res_creat_file.text)
        assert res_creat_file.status_code == 200, '断言失败'

    def test_delfile(self):
        # 1.7
        url_del_file = ('http://42.192.62.88/api2/repos/' + str(repo_id) + '/file/?p=/qqq&reloaddir=true')
        headers_del_file = {
            'Authorization': 'Token ' + str(token)
        }
        res_del_file = ad.do_delete(url=url_del_file, headers=headers_del_file)
        print('')
        print('1.7' + str(res_del_file))
        print(res_del_file.headers)
        print(res_del_file.text)
        assert res_del_file.status_code == 200, '断言失败'

    def test_delid(self):
        # 1.5
        url_del_id = ('http://42.192.62.88/api2/repos/' + str(repo_id) + '/')
        headers_del_id = {
            'Authorization': 'Token ' + str(token)
        }
        res_del_id = ad.do_delete(url=url_del_id, headers=headers_del_id)
        print('')
        print('1.5' + str(res_del_id))
        print(res_del_id.headers)
        print(res_del_id.text)
        assert res_del_id.status_code == 200, '断言失败'