from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html',{'Teacher':'Nick', 'Course':'Django'})

def count(request):
    fulltext = request.POST['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1


    return render(request,'count.html', {'fulltext':fulltext, 'count': len(wordlist), 'worddictionary':worddictionary.items()})
