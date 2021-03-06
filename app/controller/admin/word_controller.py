# -*- coding: UTF-8 -*-

import g

from app.controller.base_controller import BaseController
from app.validator.word_validator import WordValidator
from app.service.word_service import WordService
from app.entity.word_entity import WordEntity

'''
Word Controller Module
'''
class WordController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('単語帳', '選択した言語の単語を登録・編集・削除します。', '')
        self.__user_id = self.get_login_user()
        self.__service = WordService()
        self.__validator = WordValidator()
        pass

    def index(self, language_id=0):
        language_id = self.get_param('language_id') if self.get_param('language_id') != '' else self.get_session('language_id')
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)
        
        # TODO validation
        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('word_id', '')
        self.set_session('word_spell', '')
        self.set_session('word_explanation', '')
        self.set_session('word_pronunciation', '')
        self.set_session('word_is_learned', '')
        self.set_session('word_note', '')

        # TODO もっと良い方法を考える
        entity = self.__service.getList(self.__user_id, language_id, limit, offset)
        entity.set_language_id(language_id)
        return self.view('./template/admin/words/list.html', entity=entity)
    
    def create(self, language_id):
        # TODO validation
        
        self.set_session('language_id', language_id)

        entity = WordEntity()
        entity.set_language_id(language_id)
        entity.set_js_files('words.js')
        return self.view('./template/admin/words/create.html', entity=entity)

    def detail(self, language_id, word_id):
        # TODO validation
        
        # session に値をセットする
        self.set_session('language_id', language_id)
        self.set_session('word_id', word_id)
        
        return self.view('./template/admin/words/detail.html', entity=self.__service.get(self.__user_id, language_id, word_id))

    def edit(self, language_id, word_id):
        entity = self.__service.get(self.__user_id, language_id, word_id)
        entity.set_js_files('words.js')
        return self.view('./template/admin/words/edit.html', entity=entity)
    
    def confirm(self, language_id):
        language_id = self.get_session('language_id')
        word_id = self.get_session('word_id')
        
        word_spell = self.get_param('word_spell')
        word_explanation = self.get_param('word_explanation')
        word_pronunciation = self.get_param('word_pronunciation')
        word_is_learned = self.get_param('word_is_learned', 0)
        word_note = self.get_param('word_note')
        
        error_messages = self.__validator.get_error_messages(word_spell, word_explanation, word_pronunciation, word_is_learned, word_note)
        if(len(error_messages) == 0):
            self.set_session('word_spell', word_spell)
            self.set_session('word_explanation', word_explanation)
            self.set_session('word_pronunciation', word_pronunciation)
            self.set_session('word_is_learned', word_is_learned)
            self.set_session('word_note', word_note)
            template = './template/admin/words/confirm.html'
        else:
            template = './template/admin/words/create.html'
            
        # TODO Factory Class
        entity = WordEntity()
        entity.set_language_id(language_id)
        entity.set_word_id(word_id)
        entity.set_word_spell(word_spell)
        entity.set_word_explanation(word_explanation)
        entity.set_word_pronunciation(word_pronunciation)
        entity.set_word_is_learned(word_is_learned)
        entity.set_word_note(word_note)
        entity.set_error_message(error_messages)
        return self.view(template, entity=entity)

    def insert(self, language_id):
        language_id = self.get_session('language_id')
        word_spell = self.get_session('word_spell')
        word_explanation = self.get_session('word_explanation')
        word_pronunciation = self.get_session('word_pronunciation')
        word_is_learned = self.get_session('word_is_learned')
        word_note = self.get_session('word_note')
        
        # TODO validation
        
        # session をクリアする
        self.set_session('word_id', '')
        self.set_session('word_spell', '')
        self.set_session('word_explanation', '')
        self.set_session('word_pronunciation', '')
        self.set_session('word_is_learned', '')
        self.set_session('word_note', '')

        entity = self.__service.create(self.__user_id, language_id, word_spell, word_explanation, word_pronunciation, word_is_learned, word_note)
        entity.set_language_id(language_id)
        return self.view('./template/admin/words/complete.html', entity=entity)

    def update(self, language_id, word_id):
        language_id = self.get_session('language_id')
        word_id = self.get_session('word_id')
        word_spell = self.get_session('word_spell')
        word_explanation = self.get_session('word_explanation')
        word_pronunciation = self.get_session('word_pronunciation')
        word_is_learned = self.get_session('word_is_learned')
        word_note = self.get_session('word_note')
        
        # session をクリアする
        self.set_session('word_id', '')
        self.set_session('word_spell', '')
        self.set_session('word_explanation', '')
        self.set_session('word_pronunciation', '')
        self.set_session('word_is_learned', '')
        self.set_session('word_note', '')

        entity = WordEntity()
        entity.set_language_id(language_id)
        entity.set_word_id(self.__service.update(self.__user_id, language_id, word_id, word_spell, word_explanation, word_pronunciation, word_is_learned, word_note))
        return self.view('./template/admin/words/complete.html', entity=entity)
    
    def delete(self, language_id, word_id):
        word_id = self.get_param('word_id')

        self.set_session('language_id', language_id)
        # session をクリアする
        self.set_session('word_id', '')
        
        entity = WordEntity()
        entity.set_language_id(language_id)
        entity.set_word_id(self.__service.delete(self.__user_id, language_id, word_id))
        return self.view('./template/admin/words/complete.html', entity=entity)
    
    def import_csv(self):
        csv_file = self.get_params('csv_file', '');

        error_messages = self.__validator.get_csv_error_messages(csv_file)

        # エラーがなければ、取り込み実施
        if len(error_messages) == 0:
            csv_lines = open(file_path, 'r')
            for csv_line in csv_lines:
                language_id = csv_line[0]
                word_spell = csv_line[1]
                word_explanation = csv_line[2]
                word_pronunciation = csv_line[3]
                word_is_learned = 0 # 強制的に0
                word_note = csv_line[4]
                self.__service.create(self.__user_id, language_id, word_spell, word_explanation, word_pronunciation, word_is_learned, word_note)
            csv_lines.close()
        return self.view('./template/admin/words/detail.html', entity=entity.set_error_messages(error_messages))
    
    def ajax_google_dictionary_api(self, foreign_word):
        g.log.info(foreign_word)
        entity = self.__service.consult_dictionary(foreign_word)
        
        # TODO entity を json に変換して return する
        return ['a', 'b', 'c']
