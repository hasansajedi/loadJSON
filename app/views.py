import json
from urllib.request import urlopen

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app.models import EmailModel


@login_required
def analyze(request):
    """
    Create view to select Json file and analyze it.
    """
    return render(request, "app/index.html")


@csrf_exempt
@login_required
def parse(request):
    """
    If this is a POST request then process the Form data to read json file and save all of them in database,
    if item id is not exist in email table.
    :return:
    """
    if request.method == 'POST':
        try:
            url = request.POST.get('jsonURL')
            if url != '':
                messages = []
                response = urlopen(url)
                data = json.loads(response.read())
                if data is not None:
                    for item in data['items']:
                        email_obj = EmailModel.objects.get(id_got=item.get("id"))
                        if email_obj is None:
                            EmailModel.objects.create(id_got=item.get("id"),
                                                      title=item.get("title"),
                                                      description=item.get("description"),
                                                      imageUrl=item.get("imageUrl"),
                                                      creator=request.user)
                        else:
                            messages.append(
                                "Email with ID '{}' and Title '{}' exist in our table.".format(item.get("id"),
                                                                                               item.get(
                                                                                                   "title")))
                return render(request, "app/index.html", {'data': data['items'],
                                                          'messages': messages})
            else:
                return render(request, "app/index.html", {'errors': settings.NOT_VALID_URL})
        except Exception as e:
            return render(request, "app/index.html", {'errors': e})


@login_required
def report(request):
    """
    :return: List of Email submitted.
    """
    emails = EmailModel.objects.all().order_by('-id')  # Load all data in orders submitted.

    # Sent data to show in report page.
    return render(request, "app/report.html", {'emails': emails, })
