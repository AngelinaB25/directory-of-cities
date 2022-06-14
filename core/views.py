from django.shortcuts import render
def main(request):
    path = request.path
    path = path.replace('/','')
    if path == "":
        path = 'main'
    cities = ['New York','Tel Aviv','Mexico city','Pariz','Los Angeles','Jerusalem']
    return render(request, f'{path}.html',{'cities':cities})
    
# Create your views here.
