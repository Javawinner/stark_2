from stark.service.v1 import site
from app01 import models
from django.shortcuts import HttpResponse


class DepartHandler(object):
    def __init__(self, model_class):
        self.model_class = model_class

    def Changelist(self, request):
        '''
        列表页面
        :return:
        '''
        return HttpResponse('depart的列表页面')

    def add_view(self, request):
        '''
        添加页面
        :return:
        '''
        return HttpResponse('depart的添加页面')

    def change_view(self, request, pk):
        '''
        编辑页面
        :param request:
        :param pk:
        :return:
        '''
        return HttpResponse('depart的编辑页面')

    def delete_view(self, request, pk):
        '''
        删除页面
        :param request:
        :return:
        '''
        return HttpResponse('depart的删除页面')


class UserInfoHandler(object):
    def __init__(self, model_class):
        self.model_class = model_class

    def Changelist(self, request):
        '''
        列表页面
        :return:
        '''
        return HttpResponse('Userinfo的列表页面')

    def add_view(self, request):
        '''
        添加页面
        :return:
        '''
        return HttpResponse('Userinfo的添加页面')

    def change_view(self, request, pk):
        '''
        编辑页面
        :param request:
        :param pk:
        :return:
        '''
        return HttpResponse('Userinfo的编辑页面')

    def delete_view(self, request, pk):
        '''
        删除页面
        :param request:
        :return:
        '''
        return HttpResponse('Userinfo的删除页面')



site.register(models.Depart, DepartHandler)
site.register(models.Userinfo, UserInfoHandler)
print(site.__dict__)
