from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hithere':'this is me'})


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddic = {}

    for word in wordlist:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1
    sortedw = sorted(worddic.items(), key = operator.itemgetter(1), reverse=True)


    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sdic':sortedw})


def about(request):
    return render(request, 'about.html')

def submitted(request):
    return render(request, 'submitted.html')
