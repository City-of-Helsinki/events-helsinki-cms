from django.templatetags.static import static
from wagtail.core import hooks


@hooks.register('after_create_page')
def do_after_create_page(request, page):
    parent_page = page.get_parent()
    page.move(parent_page, pos='first-child')


@hooks.register('insert_editor_js')
def editor_js():
    custom_page_editor_snippets = static('application/custom_page_editor_snippets.js')
    return f'<script src="{custom_page_editor_snippets}"></script>'


@hooks.register('insert_global_admin_js')
def global_admin_js():
    custom_global_snippets = static('application/custom_global_snippets.js')
    return f'<script src="{custom_global_snippets}"></script>'
