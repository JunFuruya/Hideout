# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
#from app.validator.mail_validator import MailValidator
from app.repository.mail_repository import MailRepository
from app.entity.mail_entity import MailEntity

from app.helper.log_helper import LogHelper

# TODO 動かす

'''
Mail Controller Module
'''
class MailController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('SCメール送信画面', 'SC社のご担当者様とのメールを管理します。', '')
        self.__user_id = self.get_login_user()
        self.__repository = MailRepository()
        #self.__validator = MailValidator()
        
        pass

    def index(self):
        #link_id = self.get_session('link_id')
        #limit = self.get_param('limit', 10)
        #offset = self.get_param('offset', 0)

        #self.set_session('link_id', '')
        #self.set_session('link_category_id', '')
        #self.set_session('link_site_name', '')
        #self.set_session('link_url', '')
        #self.set_session('link_display_order', '')

        # TODO ラベルは config からとる
        label = 'Label_3322926682986175335'
        entity = self.__repository.get_list(label)

        return self.view('./template/admin/mails/list.html', MailEntity())
        #return self.view('./template/admin/mails/list.html', entity=self.__service.getList(self.__user_id, limit, offset))

    #def create(self):
        # TODO validation
        #entity = LinkEntity()
        #entity.set_link_category_entity_list(self.__service.get_link_categories(self.__user_id, 100 ,0).get_link_category_entity_list())
        #return self.view('./template/admin/links/create.html', entity=entity)

    #def detail(self, link_id):
        #link_id = self.get_param('link_id')
        # TODO validation

        #self.set_session('link_id', link_id)

        #return self.view('./template/admin/links/detail.html', entity=self.__service.get(self.__user_id, link_id))

    #def edit(self, link_id):
        #link_id = self.get_session('link_id')
        #return self.view('./template/admin/links/edit.html', entity=self.__service.get(self.__user_id, link_id))

    #def confirm(self):
        #link_id = self.get_session('link_id')

        #link_category_id = self.get_param('link_category_id')
        #link_site_name = self.get_param('link_site_name')
        #link_url = self.get_param('link_url')
        #link_display_order = self.get_param('link_display_order')

        #error_messages = self.__validator.get_error_messages(link_site_name, link_url, link_display_order)
        #if(len(error_messages) == 0):
            #self.set_session('link_id', link_id)
            #self.set_session('link_category_id', link_category_id)
            #self.set_session('link_site_name', link_site_name)
            #self.set_session('link_url', link_url)
            #self.set_session('link_display_order', link_display_order)
            #template = './template/admin/links/confirm.html'
        #else:
            #template = './template/admin/links/create.html'

        # TODO Factory class
        #entity = LinkEntity()
        #entity.set_link_id(link_id)
        #entity.set_link_category_id(link_category_id)
        #entity.set_link_site_name(link_site_name)
        #entity.set_link_url(link_url)
        #entity.set_link_display_order(link_display_order)
        #entity.set_error_messages(error_messages)
        #return self.view(template, entity=entity)

    #def insert(self):
        #link_category_id = self.get_session('link_category_id')
        #link_site_name = self.get_session('link_site_name')
        #link_url = self.get_session('link_url')
        #link_display_order = self.get_session('link_display_order')

        # TODO validation

        #self.set_session('link_category_id', '')
        #self.set_session('link_site_name', '')
        #self.set_session('link_url', '')
        #self.set_session('link_display_order', '')
        
        #try:
            #entity = self.__service.create(self.__user_id, link_category_id, link_site_name, link_url, link_display_order)
        #except:
            #entity = LinkEntity()
            #entity.set_link_category_entity_list(self.__service.get_link_categories(self.__user_id, 100 ,0).get_link_category_entity_list())
            #log = LogHelper()
            #log.error('DB Error')
        
        #return self.view('./template/admin/links/complete.html', entity=entity)

    #def update(self):
        #link_id = self.get_session('link_id')
        #link_category_id = self.get_session('link_category_id')
        #link_site_name = self.get_session('link_site_name')
        #link_url = self.get_session('link_url')
        #link_display_order = self.get_session('link_display_order')

        #self.set_session('link_id', '')
        #self.set_session('link_category_id', '')
        #self.set_session('link_site_name', '')
        #self.set_session('link_url', '')
        #self.set_session('link_display_order', '')

        #entity = LinkEntity()
        #entity.set_link_id(self.__service.update(self.__user_id, link_id, link_category_id, link_site_name, link_url, link_display_order))
        #return self.view('./template/admin/links/complete.html', entity=entity)

    #def delete(self):
        #link_id = self.get_param('link_id')

        #self.set_session('link_id', '')

        #entity = LinkEntity()
        #entity.set_link_id(self.__service.delete(self.__user_id, link_id))
        #return self.view('./template/admin/links/complete.html', entity=entity)