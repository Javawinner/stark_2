from stark.service.v1 import site
from app02 import models
from django.shortcuts import HttpResponse

class HostHandler(object):
    def __init__(self, model_class):
        self.model_class = model_class

    def Changelist(self, request):
        '''
        列表页面
        :return:
        '''
        return HttpResponse('Host的列表页面')

    def add_view(self, request):
        '''
        添加页面
        :return:
        '''
        return HttpResponse('Host的添加页面')

    def change_view(self, request, pk):
        '''
        编辑页面
        :param request:
        :param pk:
        :return:
        '''
        return HttpResponse('host的编辑页面')

    def delete_view(self, request, pk):
        '''
        删除页面
        :param request:
        :return:
        '''
        return HttpResponse('host的删除页面')


class RoleHandler(object):
    def __init__(self, model_class):
        self.model_class = model_class

    def Changelist(self, request):
        '''
        列表页面
        :return:
        '''
        return HttpResponse('Role的列表页面')

    def add_view(self, request):
        '''
        添加页面
        :return:
        '''
        return HttpResponse('Role的添加页面')

    def change_view(self, request, pk):
        '''
        编辑页面
        :param request:
        :param pk:
        :return:
        '''
        return HttpResponse('Role的编辑页面')

    def delete_view(self, request, pk):
        '''
        删除页面
        :param request:
        :return:
        '''
        return HttpResponse('Role的删除页面')


site.register(models.Host, HostHandler)
site.register(models.Role, RoleHandler)