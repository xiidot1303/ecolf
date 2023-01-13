from app.views import *
from app.services.language_service import *

def pages(request, page='index'):
    products = Product.objects.all()
    context = {'page': page, 'products': products}
    return render(request, f'main/{page}.html', context)


def change_lang(request, lang):
    ip = get_user_ip(request)
    update_lang_by_ip(ip, int(lang))
    return redirect_back(request)


def get_file(request, path):
    file = open(f'files/{path}', 'rb')
    return FileResponse(file)