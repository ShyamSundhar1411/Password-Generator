from django.shortcuts import render
import random
def home(request):
    return render(request, 'generator/home.html',{'gen':'12345'})
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('up'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('no'):
        characters.extend(list('1234567890'))
    if request.GET.get('sp'):
        characters.extend(list('~!@#$%^&*()_+{}[]'))
    length = int(request.GET.get('length'))
    i = ''
    for x in range(length):
        i+=random.choice(characters)
    return render(request, 'generator/pass.html', {'pass': i })
def about(request):
    return render(request,'generator/about.html')
