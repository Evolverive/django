from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html', {'hithere':'this is me'})

def count(request):
    full = request.GET['fulltext']
    print(full)
    wordlist=full.split()
    worddict={}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    sorted_list=sorted(worddict.items(), key=lambda dict:dict[1], reverse=True)
    return render(request, 'count.html', {'full':full, 'count':len(wordlist), 'worddict':sorted_list})
def przygoda(request):
    return render(request, 'przygoda.html', {'key':'klucz'})