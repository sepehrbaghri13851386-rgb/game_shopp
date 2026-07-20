from .models import coment


def all_comments(request):
    """
    Makes the latest comments available in every template (via base.html).
    """
    return {
        'all_comments': coment.objects.all().order_by('-id')[:12]
    }