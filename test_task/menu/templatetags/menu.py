from django import template
from django.shortcuts import get_object_or_404
from ..models import MenuItem
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = get_object_or_404(MenuItem, name=menu_name, parent=None)
    local_context = {'menu_item': menu}
    requested_url = context['request'].path
    print(requested_url)
    try:
        active_menu_item = MenuItem.objects.get(url=requested_url)
    except ObjectDoesNotExist:
        pass
    else:
        inactive_menu_item_ids = active_menu_item.get_parent_ids() + [active_menu_item.id]
        local_context['inactive_menu_item_ids'] = inactive_menu_item_ids
    return local_context


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu_item_children(context, menu_item_id):
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    local_context = {'menu_item': menu_item}
    if 'inactive_menu_item_ids' in context:
        local_context['inactive_menu_item_ids'] = context['inactive_menu_item_ids']
    return local_context
