# -*- coding: UTF-8 -*-

import g

class BaseWebEntity():
    __title = ''
    __description = ''
    __notification = ''
    __error_messages = []
    __records = []
    __login_status = False

    def set_title(self, title):
        self.__title = title
        return self

    def get_title(self):
        return self.__title

    def set_description(self, description):
        self.__description = description
        return self

    def get_description(self):
        return self.__description
    
    def set_notification(self, notification):
        self.__notification = notification
        return self

    def get_notification(self):
        return self.__notification
    
    def set_error_messages(self, error_messages):
        self.__error_messages = error_messages
        return self

    def get_error_messages(self):
        return self.__error_messages
    
    def set_records(self, records):
        self.__records = records
        return self

    def get_records(self):
        return self.__records
    
    def to_array(self):
        return [
            self.get_title(),
            self.get_description(),
            self.get_explanation(),
            self.get_records(),
            self.get_error_messages()
        ]

    def set_login_status(self, user_id):
        self.__login_status = True if len(str(user_id)) > 0 else False

    def get_login_status(self):
        return self.__login_status