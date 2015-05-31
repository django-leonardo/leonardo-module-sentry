
from leonardo.views.defaults import render_in_page


def error_handler(request):
    """
    500 error handler which includes ``request`` in the context.

    Templates: `500.html`
    Context: None
    """
    from django.template import Context, loader
    from django.http import HttpResponseServerError

    response = render_in_page(request, '500.html')

    if response:
        return response

    t = loader.get_template('500.html')
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))
