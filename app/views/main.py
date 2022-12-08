from app.views import *
from app.services.language_service import *

def pages(request, page='index'):
    context = {'page': page}
    return render(request, f'main/{page}.html', context)


def change_lang(request, lang):
    ip = get_user_ip(request)
    update_lang_by_ip(ip, int(lang))
    return redirect_back(request)