# -*- coding: utf-8 -*-

from app.infrastructure.base_db import DbBase

'''
word database module
'''
class DbWords(DbBase):
    def __init__(self):
        super().__init__()
        pass
    
    def select(self, limit, offset):
        sql = 'SELECT m_word_id, m_word_name FROM m_words limit %s offset %s'
        bindings = (limit, offset)
        return super().select(sql, bindings)

    def selectOne(self, user_id, word_id):
        sql = 'SELECT m_word_id, m_word_name FROM m_words WHERE m_user_id = %s AND m_word_id = %s;'
        bindings = (user_id, word_id)
        return super().selectOne(sql, bindings)

    def insert(self, user_id, word_name):
        sql = 'INSERT INTO m_words(m_user_id, m_word_name) VALUES(%s, %s);'
        bindings = (user_id, word_name)
        
        # TODO 全体的に例外処理を入れる
        try:
            id = super().insert(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()
        
        return id
    
    def update(self, word_id, user_id, word_name):
        sql = 'UPDATE m_words SET m_word_name = %s WHERE m_word_id = %s AND m_user_id = %s;'
        bindings = (word_name, word_id, user_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().update(sql, bindings)
            super().commit()
        except:
            super().rollback()
        return is_success
    
    def delete(self, word_id, user_id):
        sql = 'DELETE FROM m_words WHERE m_word_id = %s AND m_user_id = %s;'
        bindings = (word_id, user_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().delete(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()

        return is_success
