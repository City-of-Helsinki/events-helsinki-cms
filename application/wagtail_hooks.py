from wagtail.core import hooks


@hooks.register('after_create_page')
def do_after_create_page(request, page):
    parent_page = page.get_parent()
    page.move(parent_page, pos='first-child')
