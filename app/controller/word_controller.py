#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.word_service import WordService
from app.entity.word_entity import WordEntity

from app.helper.helper import HashHelper

'''
Word Controller Module
'''
class WordController(BaseController):

    def __init__(self):
        self.__service = WordService()
        self.__title = '単語帳'
        self.__description = '選択した言語の単語を登録・編集・削除します。'
        pass

    def index(self, request):
        # TODO セッションからとる
        user_id = 1
        # TODO もっと良い方法を考える
        language_id = request.query.get('language_id')
        language_id = language_id if language_id is not None else ''
        
        # TODO もっと良い方法を考える
        limit = request.query.get('limit')
        limit = limit if limit is not None else 10
            
        # TODO もっと良い方法を考える
        offset = request.query.get('offset')
        offset = offset if offset is not None else 0

        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('language_id')] = ''
        session[HashHelper.hexdigest('word_id')] = ''
        session[HashHelper.hexdigest('word_name')] = ''
        session.save()

        # TODO もっと良い方法を考える
        entity = self.__service.getList(user_id, language_id, limit, offset)
        # TODO もっと良い方法を考える
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        
        return self.view('./template/admin/words/list.html', entity=entity)
    
    def create(self, request):
        # TODO セッションからとる
        user_id = 1

        # TODO もっと良い方法を考える
        language_id = request.forms.get('language_id')
        language_id = language_id if language_id is not None else ''

        # TODO validation
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('language_id')] = language_id
        session.save()

        entity = self.__service.get_language(user_id, language_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/create.html', entity=entity)

    def detail(self, request, word_id):
        
        # TODO user_id 取得する
        user_id = 1
        # TODO validation
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('word_id')] = word_id
        session.save()
        
        entity = self.__service.get(user_id, word_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/detail.html', entity=entity)

    def edit(self, request, word_id):
        session = request.environ.get('beaker.session')
        word_id = session.get(HashHelper.hexdigest('word_id'), False)
        # TODO user_id 取得する
        user_id = 1
        
        entity = self.__service.get(user_id, word_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/edit.html', entity=entity)
    
    def confirm(self, request):
        session = request.environ.get('beaker.session')
        language_id = session.get(HashHelper.hexdigest('language_id'), False)
        word_id = session.get(HashHelper.hexdigest('word_id'), False)
        # TODO user_id 取得する
        user_id = 1
        
        word_spell = request.forms.get('word_spell')
        word_explanation = request.forms.get('word_explanation')
        word_pronanciation = request.forms.get('word_pronanciation')
        word_is_learned = 0
        word_note = request.forms.get('word_note')
        
        # TODO validation
        
        
        session[HashHelper.hexdigest('word_spell')] = word_spell
        session[HashHelper.hexdigest('word_explanation')] = word_explanation
        session[HashHelper.hexdigest('word_pronanciation')] = word_pronanciation
        session[HashHelper.hexdigest('word_is_learned')] = word_is_learned
        session[HashHelper.hexdigest('word_note')] = word_note
        session.save()
        
        # TODO もっと良い設計があるはず
        entity = self.__service.get_language(user_id, language_id)
        entity.set_title(self.__title)
        entity.set_word_id(word_id)
        entity.set_word_spell(word_spell)
        entity.set_word_explanation(word_explanation)
        entity.set_word_pronanciation(word_pronanciation)
        entity.set_word_is_learned(word_is_learned)
        entity.set_word_note(word_note)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/confirm.html', entity=entity)

    def insert(self, request):
        session = request.environ.get('beaker.session')
        language_id = session.get(HashHelper.hexdigest('language_id'), False)
        word_spell = session.get(HashHelper.hexdigest('word_spell'), False)
        word_explanation = session.get(HashHelper.hexdigest('word_explanation'), False)
        word_pronanciation = session.get(HashHelper.hexdigest('word_pronanciation'), False)
        word_is_learned = session.get(HashHelper.hexdigest('word_is_learned'), False)
        word_note = session.get(HashHelper.hexdigest('word_note'), False)
        
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        # TODO validation
        
        session = request.environ.get('beaker.session')
        
        session[HashHelper.hexdigest('language_id')] = ''
        session[HashHelper.hexdigest('word_id')] = ''
        session[HashHelper.hexdigest('word_name')] = ''
        session.save()

        entity = self.__service.create(user_id, language_id, word_spell, word_explanation, word_pronanciation, word_is_learned, word_note)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/complete.html', entity=entity)

    def update(self, request):
        session = request.environ.get('beaker.session')
        word_id = session.get(HashHelper.hexdigest('word_id'), False)
        word_name = session.get(HashHelper.hexdigest('word_name'), False)
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('word_id')] = ''
        session[HashHelper.hexdigest('word_name')] = ''
        session.save()

        entity = wordEntity()
        entity.set_word_id(self.__service.update(word_id, user_id, word_name))
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/complete.html', entity=entity)
    
    def delete(self, request):
        word_id = request.forms.get('word_id')
        #TODO ログイン時に取得するようにする 
        user_id = 1

        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('word_id')] = ''
        session[HashHelper.hexdigest('word_name')] = ''
        session.save()

        entity = wordEntity()
        entity.set_word_id(self.__service.delete(word_id, user_id))
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/complete.html', entity=entity)
    