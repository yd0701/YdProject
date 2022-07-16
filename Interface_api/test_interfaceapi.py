import requests
'''
接口的关键字驱动封装 是目前业内最为主流的接口框架的设计模式
将常用的请求方法进行函数封装,以便后续的可复用和易于维护的性质.
'''
class TestApiDemo:
    #POST
    def do_post(self, url, params = None, headers = None, **kwargs):
        return requests.post(url=url, params=params, headers=headers, **kwargs)
    #GET
    def do_get(self, url, params = None, headers = None, **kwargs):
        return requests.get(url=url, params=params, headers=headers, **kwargs)
    #PUT
    def do_put(self, url, params = None, headers = None, **kwargs):
        return requests.put(url=url, params=params, headers=headers, **kwargs)
    #DELETE
    def do_delete(self, url, params = None, headers = None, **kwargs):
        return requests.delete(url=url, params=params, headers=headers, **kwargs)