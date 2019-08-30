from django.http import HttpResponse
from django.shortcuts import render
import operator # learn this
def home(request):
    return render(request, 'home.html')

def hello(request):
    return HttpResponse('hellofriends')
def about(request):
    return HttpResponse('<h1>GO BACK</h>')

def count(request):

    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
            # learn the below line        we have to import operator
    sortedword = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist),'sortedword':sortedword})
