from django.core.exceptions import PermissionDenied

def is_superuser(function=None):
    """
    Decorator for superuser only
    """
    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner

def error_dict_convert(error_dict):
    error = error_dict.copy()
    result = ''

    for key, value in error.items():
        for msg in value:
            # result = result + '&nbsp&nbsp&nbsp' + msg
            result = result + msg + '<br>'
            # result = result + '[' + msg + ']'
    result = '<label class="error_log">' + result + '</label>'
    return result