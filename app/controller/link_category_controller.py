# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.link_category_service import LinkCategoryService
from app.entity.link_category_entity import LinkCategoryEntity

from app.helper.helper import HashHelper

'''
Link Category Controller Module
'''
class LinkCategoryController(BaseController):

    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('リンクカテゴリマスタ', 'リンクを分類するためのカテゴリを登録・編集・削除します。', '')
        self.__user_id = self.get_login_user()
        self.__service = LinkCategoryService()

    def index(self):
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)

        self.set_session('link_category_id', '')

        return self.view('./template/admin/link_categories/list.html', self.__service.getList(self.__user_id, limit, offset))
    
    def create(self):
        return self.view('./template/admin/link_categories/create.html', LinkCategoryEntity())

    def detail(self, link_category_id):
        link_categoty_id = self.get_param('link_categoty_id')
        # TODO validation
        
        self.set_session('link_category_id', link_categoty_id)
        return self.view('./template/admin/link_categories/detail.html', self.__service.get(self.__user_id, link_category_id))

    def edit(self, link_category_id):
        # TODO validation
        
        self.set_session('link_category_id', link_category_id)
        return self.view('./template/admin/link_categories/edit.html', self.__service.get(self.__user_id, link_category_id))
    
    def confirm(self):
        link_category_id = self.get_session('link_category_id')
        link_category_name = self.get_param('link_category_name')
        link_category_display_order = self.get_param('link_category_display_order')

        # TODO validation
        
        self.set_session('link_category_id', link_category_id)
        self.set_session('link_category_name', link_category_name)
        self.set_session('link_category_display_order', link_category_display_order)
        
        # TODO もっと良い設計があるはず
        entity = LinkCategoryEntity()
        entity.set_link_category_id(link_category_id)
        entity.set_link_category_name(link_category_name)
        entity.set_link_category_display_order(link_category_display_order)
        return self.view('./template/admin/link_categories/confirm.html', entity)

    def insert(self):
        link_category_name = self.get_session('link_category_name')
        link_category_display_order = self.get_session('link_category_display_order')
                
        # TODO validation
        
        self.set_session('link_category_id', '')
        self.set_session('link_category_name', '')
        self.set_session('link_category_display_order', '')
        return self.view('./template/admin/link_categories/complete.html', self.__service.create(self.__user_id, link_category_name, link_category_display_order))

    def update(self, link_category_id):
        link_category_id = self.get_session('link_category_id')
        link_category_name = self.get_session('link_category_name')
        link_category_display_order = self.get_session('link_category_display_order')
        
        self.set_session('link_category_id', '')
        self.set_session('link_category_name', '')
        self.set_session('link_category_display_order', '')

        entity = LinkCategoryEntity()
        entity.set_link_category_id(self.__service.update(link_category_id, self.__user_id, link_category_name, link_category_display_order))
        return self.view('./template/admin/link_categories/complete.html', entity)
    
    def delete(self, link_category_id):
        link_category_id = self.get_param('link_category_id')

        self.set_session('link_category_id', '')
        self.set_session('link_category_name', '')
        self.set_session('link_category_display_order', '')

        entity = LinkCategoryEntity()
        entity.set_link_category_id(self.__service.delete(link_category_id, self.__user_id))
        return self.view('./template/admin/link_categories/complete.html', entity)