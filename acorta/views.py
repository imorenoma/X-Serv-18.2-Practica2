from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def inicio(request):

    if request.method == "GET":

        response = ("<form method='POST>" + "Insert your URL" +
                    "input type='text' name='url'><br>" +
                    "input type='submit' value='Send'></form>")

        if len(list) == 0:
            response = ("<form method='POST>" + "Insert your URL" +
                    "input type='text' name='url'><br>" +
                    "input type='submit' value='Send'></form>" + "<br> Empty")

        else:
            for url in list:
                short_url = "https://localhost:1234/" + str(url.id)
                response += ("<br>url: " + url.long_url +
                             "url acortada: " + "<a href=" + short_url + ">" +
                             short_url + "</a>")

    elif request.method == "POST":
        long_url = request.POST['url']

        if long_url[0:7] != "http://" and long_url[0:8] != "https://":
            long_url = "http://" + long_url

            try:
                short_url = list_urls.objects.get(long_url=long_url)

            except list_urls.DoesNotExist:
                url = list_urls(long_url=long_url)
                url.save()
                short_url = list_urls.objects.get(long_url=long_url)


            short_url = "hhtp://localhost:1234/" + str(short_url.id)
            respose = ("Url de origen: " + long_url + "es" +
                       "<a href=" + short_url + ">" + short_url + "</a>")

    else:
        return HttpResponse("Method not allowed", status=404)


    return HttpResponse(response, status=200)


def redireccion(request, resource):
    try:
        long_url = list_urls.objects.get(id=resource).long_url
        return HttpRespose(long_url)
    except list.urls.DoesNotExist:
        response = "Recurso no disponible"
        return HttpRespose(response, status=404)



