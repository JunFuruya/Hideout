# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
from app.validator.user_validator import UserValidator
from app.service.user_service import UserService
from app.entity.user_entity import UserEntity

'''
User Controller Module
'''
class UserController(BaseController):

    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('ユーザマスタ', 'ユーザを登録・編集・削除します。', '')
        self.__user_id = self.get_login_user()
        self.__service = UserService()
        self.__validator = UserValidator()
        pass

    def index(self):
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)

        self.set_session('user_id', '')

        return self.view('./template/admin/users/list.html', self.__service.getList(limit, offset))
    
    def create(self):
        return self.view('./template/admin/users/create.html', UserEntity())

    def detail(self, user_id):
        user_id = self.get_param('user_id')
        # TODO validation
        
        self.set_session('user_id', user_id)
        return self.view('./template/admin/users/detail.html', self.__service.get(user_id))

    def edit(self, user_id):
        user_id = self.get_session('user_id')
        # TODO validation
        
        self.set_session('user_id', user_id)
        return self.view('./template/admin/users/edit.html', self.__service.get(user_id))
    
    def confirm(self):
        user_id = self.get_session('user_id')
        user_username = self.get_param('user_username')
        user_hashed_password = self.get_param('user_hashed_password')
        user_hashed_password_check = self.get_session('user_hashed_password_check')

        error_messages = self.__validator.get_error_messages(user_username, user_hashed_password)
        if(len(error_messages) == 0):
            self.set_session('user_id', user_id)
            self.set_session('user_username', user_username)
            self.set_session('user_hashed_password', user_hashed_password)
            template = './template/admin/users/confirm.html'
        else:
            # TODO 新規と編集でテンプレート出し分け
            template = './template/admin/users/create.html'

        # TODO Factory Class
        entity = UserEntity()
        entity.set_user_id(user_id)
        entity.set_user_username(user_username)
        entity.set_user_hashed_password(user_hashed_password)
        entity.set_error_messages(error_messages)
        return self.view(template, entity)

    def insert(self):
        user_username = self.get_session('user_username')
        user_hashed_password = self.get_session('user_hashed_password')
                
        # TODO validation
        
        self.set_session('user_id', '')
        self.set_session('user_username', '')
        self.set_session('user_hashed_password', '')
        return self.view('./template/admin/users/complete.html', self.__service.create(user_username, user_hashed_password))

    def update(self, user_id):
        user_id = self.get_session('user_id')
        user_username = self.get_session('user_username')
        user_hashed_password = self.get_session('user_hashed_password')
        
        # TODO validation
        
        self.set_session('user_id', '')
        self.set_session('user_username', '')
        self.set_session('user_hashed_password', '')

        entity = UserEntity()
        is_success = self.__service.update(user_id, user_username, user_hashed_password)
        return self.view('./template/admin/users/complete.html', entity.set_user_id(user_id))
    
    def delete(self, user_id):
        user_id = self.get_param('user_id')

        self.set_session('user_id', '')
        self.set_session('user_username', '')
        self.set_session('user_hashed_password', '')

        entity = UserEntity()
        is_success = self.__service.delete(user_id)
        return self.view('./template/admin/users/complete.html', entity.set_user_id(user_id))