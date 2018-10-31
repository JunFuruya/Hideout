# -*- coding: utf-8 -*-

from beaker.middleware import SessionMiddleware

from bottle import app, error, get, post, request, run, static_file

from app.controller.admin_index_controller import AdminIndexController
from app.controller.admin_login_controller import AdminLoginController
from app.controller.error_controller import ErrorController
from app.controller.index_controller import IndexController
from app.controller.language_controller import LanguageController
from app.controller.link_category_controller import LinkCategoryController
from app.controller.link_controller import LinkController
from app.controller.word_controller import WordController

# TODO そのうち消す
from app.service.web_service import ConfigGetService
config = ConfigGetService().get_web_server_config()

###############################################################################
# 非ログインユーザ用画面
###############################################################################
@get('/')
def get_index():
    return IndexController(request).index()

###############################################################################
# 管理画面TOP
###############################################################################
@get('/admin')
def get_link_index():
    return AdminIndexController(request).index()

###############################################################################
# ログイン、ログアウト
###############################################################################
@get('/admin/login')
def get_admin_login():
    return AdminLoginController(request).index()

@post('/admin/login')
def post_admin_login_complete():
    return AdminLoginController(request).login()

@get('/admin/logout')
def get_admin_login_complete():
    return AdminLoginController(request).logout()

###############################################################################
# リンクカテゴリマスタ
###############################################################################
@get('/admin/link-categories')
def get_link_category_list():
    return LinkCategoryController(request).index()

@get('/admin/link-categories/create')
def get_link_category_create():
    return LinkCategoryController(request).create()

@get('/admin/link-categories/<link_category_id>')
def post_link_category_detail(link_category_id):
    return LinkCategoryController(request).detail(link_category_id)

@post('/admin/link-categories/<link_category_id>')
def post_link_category_edit(link_category_id):
    return LinkCategoryController(request).edit(link_category_id)

@post('/admin/link-categories/confirm')
def post_link_category_confirm():
    return LinkCategoryController(request).confirm()

@post('/admin/link-categories/insert')
def post_link_category_insert():
    return LinkCategoryController(request).insert()

@post('/admin/link-categories/<link_category_id>/update')
def post_link_category_update(link_category_id):
    return LinkCategoryController(request).update(link_category_id)

@post('/admin/link-categories/<link_category_id>/delete')
def post_link_category_delete(link_category_id):
    return LinkCategoryController(request).delete(link_category_id)

###############################################################################
# リンクマスタ
###############################################################################
@get('/admin/links')
def get_link_list():
    return LinkController(request).index()

@get('/admin/links/create')
def get_link_create():
    return LinkController(request).create()

@get('/admin/links/<link_id>')
def post_link_update(link_id):
    return LinkController(request).update(link_id)

@post('/admin/links/<link_id>')
def post_link_update(link_id):
    return LinkController(request).index(link_id)

@post('/admin/links/confirm')
def post_link_confirm():
    return LinkController(request).confirm()

@post('/admin/links/insert')
def post_link_complete():
    return LinkController(request).insert()

@post('/admin/links/update')
def post_link_complete():
    return LinkController(request).update()

@post('/admin/links/delete')
def post_link_complete():
    return LinkController(request).delete()

###############################################################################
# 言語マスタ
###############################################################################
@get('/admin/languages')
def get_language_list():
    return LanguageController(request).index()

@get('/admin/languages/create')
def get_language_create():
    return LanguageController(request).create()

@get('/admin/languages/<language_id>')
def post_language_detail(language_id):
    return LanguageController(request).detail(language_id)

@post('/admin/languages/<language_id>')
def post_language_edit(language_id):
    return LanguageController(request).edit(language_id)

@post('/admin/languages/confirm')
def post_language_confirm():
    return LanguageController(request).confirm()

@post('/admin/languages/insert')
def post_language_insert():
    return LanguageController(request).insert()

@post('/admin/languages/update')
def post_language_update():
    return LanguageController(request).update()

@post('/admin/languages/delete')
def post_language_delete():
    return LanguageController(request).delete()

###############################################################################
# 単語帳
###############################################################################
@get('/admin/languages/words')
def get_word_list():
    return WordController(request).index()

@get('/admin/languages/<language_id>/words')
def post_word_list(language_id):
    return WordController(request).index(language_id)

@get('/admin/languages/<language_id>/words/create')
def get_word_create(language_id):
    return WordController(request).create(language_id)

@get('/admin/languages/<language_id>/words/<word_id>')
def post_word_detail(language_id, word_id):
    return WordController(request).detail(language_id, word_id)

@post('/admin/languages/<language_id>/words/confirm')
def post_word_confirm(language_id):
    return WordController(request).confirm(language_id)

@post('/admin/languages/<language_id>/words/<word_id>/confirm')
def post_word_confirm(language_id, word_id):
    return WordController(request).confirm(language_id)

@post('/admin/languages/<language_id>/words/insert')
def post_word_insert(language_id):
    return WordController(request).insert(language_id)

@post('/admin/languages/<language_id>/words/<word_id>')
def post_word_edit(language_id, word_id):
    return WordController(request).edit(language_id, word_id)

@post('/admin/languages/<language_id>/words/<word_id>/update')
def post_word_update(language_id, word_id):
    return WordController(request).update(language_id, word_id)

@post('/admin/languages/<language_id>/words/<word_id>/delete')
def post_word_delete(language_id, word_id):
    return WordController(request).delete(language_id, word_id)

###############################################################################
# 静的ファイル
###############################################################################
@get('/public/<path:path>')
def get_static_file(path):
    return static_file(path, root='./public/')

###############################################################################
# エラー画面
###############################################################################
@error(404)
def error404(error):
    return ErrorController.error(404)

error(500)
def error500(error):
    return ErrorController.error(500)

if __name__ == "__main__":
    # TODO: create controller classes
    session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 300,
        'session.data_dir': './data',
        'session.auto': True
    }

    run(app=SessionMiddleware(app(), session_opts), host=config.get_web_host(), port=config.get_web_port(), debug=config.get_debug(), reloader=config.get_reloader())