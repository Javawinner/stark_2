from django.conf.urls import url


class StarkSite(object):
    def __init__(self):
        self._registry = []
        self.app_name = 'stark'
        self.namespace = 'stark'

    def register(self, model_Class, handler_class):
        '''
        :param model_Class: 是models中数据库表对应的类
        :param handler_class: 处理请求的视图函数所在的类
        :return:
        '''

        self._registry.append({'model_class': model_Class, 'handler_class': handler_class(handler_class)})

    @property
    def get_urls(self):
        patterns = []
        '''
        测试
           patterns.append(url(r'^x1/', lambda request: HttpResponse('x1')))
           patterns.append(url(r'^x2/', lambda request: HttpResponse('x2')))
        '''
        for item in self._registry:
            # 把每个数据库表对应的类拿到
            model_class = item['model_class']
            handler_class = item['handler_class']
            # 把处理表的增删改查的对象拿到
            '''
            <class 'app01.models.Depart'>
            <class 'app01.models.Userinfo'>
            <class 'app02.models.Host'>
            '''
            # 为每个model_class 生成4个url
            # 需要拿到每个对应数据库的表的类名称对应的应用名，类名小写，来拼成路由的名字
            '''
             / app01 / depart / list /
            / app01 / depart / add /
            / app01 / depart / edit / (\d+) /
            / app01 / depart /del / (\d+) /
            '''
            # 拿到数据库的表的类名称对应的应用名
            app_label = model_class._meta.app_label  # 比如说 app01

            # 拿到数据库的表的类名称对应的类名
            model_name = model_class._meta.model_name  # 比如说 depart
            patterns.append(url(r'^%s/%s/list' % (app_label, model_name), handler_class.Changelist))
            patterns.append(url(r'^%s/%s/add' % (app_label, model_name), handler_class.add_view))
            patterns.append(url(r'^%s/%s/edit/(\d+)' % (app_label, model_name), handler_class.change_view))
            patterns.append(url(r'^%s/%s/del/(\d+)' % (app_label, model_name), handler_class.delete_view))

        return patterns

    @property
    def urls(self):
        return self.get_urls, self.app_name, self.namespace


site = StarkSite()
'''
stark文件是在路由分发前执行

第一步， 调用register方法就传一个参数(models里面的类名，就是数据库中的表)
stark文件中做的操作： 
site.register(models.Depart)
site.register(models.Userinfo)
site.register(models.Host)
self._registry=[{'model_class': models.Depart},{'model_class': models.Userinfo},{'model_class': models.Host}]

启动django后，
site.__dict__= app02 {'_registry': [{'model_class': <class 'app01.models.Depart'>}, 
{'model_class': <class 'app01.models.Userinfo'>}, {'model_class': <class 'app02.models.Host'>}], 
'app_name': 'stark', 'namespace': 'stark'}

第二步  再传一个参数给register,也是一个类，对应的是增删改查的方法,但是最后传给_registry键值，值是这个类实例化的对象，实例化再将前面的类名作为参数传递给这个对象
启动django后，
site.__dict__= {'_registry': [
{'model_class': <class 'app01.models.Depart'>, 'handler_class': <app01.stark.DepartHandler object at 0x1044d9c88>}, 
{'model_class': <class 'app01.models.Userinfo'>, 'handler_class': <app01.stark.UserInfoHandler object at 0x1044d9d30>}, 
{'model_class': <class 'app02.models.Host'>, 'handler_class': <app02.stark.HostHandler object at 0x1044e8160>}
], 'app_name': 'stark', 'namespace': 'stark'}

'''
