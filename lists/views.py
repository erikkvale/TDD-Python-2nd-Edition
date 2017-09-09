from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home_page(request):
    if request.method == 'POST':
        return render(
            request=request,
            template_name='home.html',
            context={
                'new_item_text': request.POST['item_text']
            }
        )
    return render(request, 'home.html')