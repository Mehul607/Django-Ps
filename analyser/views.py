from django.shortcuts import render
from .models import Word, Language, Sentence
from . import colour

def main(request):
    return render(request, 'Interface27/final.html')

def mainS(request):
    form_input=request.POST.get('sentence')
    if form_input!=[]:
        tempSentence=colour.colour_coder(form_input)
        wlist=[]
        s=Sentence(stext=form_input)
        for (a,b) in tempSentence:
            l=Language.objects.filter(language__startswith=b)
            w=Word(wtext=a,lang=l[0])
            wlist.append((a,l[0].colour.col,l[0].language))
            tempw=Word.objects.filter(wtext__startswith=a)
            for wt in tempw:
                if w.lang.language==wt.lang.language:
                    break
            else:
                w.save()
        s.save()
        return render(request, 'Interface27/final.html',{'word':wlist,})
    else:
        return render(request, 'Interface27/final.html')