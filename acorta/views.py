from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from acorta.models import ListUrls

@csrf_exempt
def inicio(request):

    list = ListUrls.objects.all()
    response = ''

    if request.method == "GET":

        response = ("<form action="" method='POST'> Introduce Url<br>" +
                    "<input type='text' name='url'><br>" +
                    "<input type='submit' value='Send'>" +
                    "</form></html>")

        if len(list) == 0:
            response = ("<form method='POST'>" + "Introduce Url" +
                        "<input type='text' name='url'><br>" +
                        "<input type='submit' value='Send'></form>") + "<br> Empty"
        else:
            for url in list:
                short_url = "http://localhost:1234/" + str(url.id)
                response += ("<br>url: " + url.long_url +
                             "url acortada: " "<a href" +
                             short_url + ">" + short_url + "</a>")

    elif request.method == "POST":
        long_url = request.POST['url']

        if long_url[0:7] != "http://" and long_url[0:8] != "https://":
            long_url = "http://" + long_url

            try:
                short_url = ListUrls.objects.get(long_url=long_url)

            except ListUrls.DoesNotExist:
                url = ListUrls(long_url=long_url)
                url.save()
                short_url = ListUrls.objects.get(long_url=long_url)

            short_url = "http://localhost:1234/" + str(short_url.id)
            response = ("Url de origen: " + long_url + "es" +
                        "<a href=" + short_url + ">" + short_url + "</a>")

    else:
        return HttpResponse("Method not allowed", status=405)

    return HttpResponse(response, status=200)


def redireccion(request, resource):
    try:
        long_url = ListUrls.objects.get(id=resource).long_url
        return HttpResponse(long_url)
    except ListUrls.DoesNotExist:
        response = "Recurso no disponible"
        return HttpResponse(response, status=404)

# sat12345
