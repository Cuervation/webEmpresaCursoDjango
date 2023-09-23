from .models import Link


def ctx_dict(request):
    #ctx = {'test':'hola'}
    ctx = {}
    links = Link.objects.all()    
    for link in links:
        ctx[link.key] = link.url        
    print(ctx)
    return ctx