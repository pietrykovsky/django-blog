from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from functools import wraps

from .models import Comment

def user_is_redactor(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_redactor or request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap

def user_is_comment_author(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        pk = kwargs['pk']
        obj = get_object_or_404(Comment, pk=pk)
        if request.user == obj.author or request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap