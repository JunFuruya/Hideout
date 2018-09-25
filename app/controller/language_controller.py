#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.web_service import LanguageService
from app.entity.language_entity import LanguageEntity

'''
Language Controller Module
'''
class LanguageController(BaseController):

    def __init__(self):
        self.__service = LanguageService()
        self.__title = '言語マスタ'
        self.__description = '単語帳を作成する言語を登録・編集・削除します。'
        pass

    def index(self, request):
        # TODO もっと良い方法を考える
        limit = request.query.get('limit')
        limit = limit if limit is not None else 10
            
        # TODO もっと良い方法を考える
        offset = request.query.get('offset')
        offset = offset if offset is not None else 0
        
        # TODO もっと良い方法を考える
        entity = self.__service.getList(limit, offset)
        # TODO もっと良い方法を考える
        if(entity is not None):
            entity.set_title(self.__title)
            entity.set_description(self.__description)
            entity.set_notification('This is the index page.')
        
        return entity
    
    def detail(self, request):
        language_id = request.query.get('language_id')
        entity = self.__service.get(language_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        pass
    
    def create(self, request):
        entity = LanguageEntity()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return entity

    def confirm(self, request):
        language_name = request.forms.get('language_name')
        # TODO validation
        print(language_name)
        # TODO もっと良い設計があるはず
        entity = LanguageEntity()
        entity.set_title(self.__title)
        entity.set_language_name(language_name)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return entity

    def insert(self, request):
        session = request.environ.get('beaker.session')
        language_name = session.get(HashHelper.hexdigest('language_name'), False)
        # TODO validation
        entity = self.__service.insert(language_name)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return entity

    def update(self, request):
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return entity
    
    def delete(self, request):
        entity = self.__service.get()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return entity

    def complete(self, request):
        entity = LanguageEntity()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return entity
    