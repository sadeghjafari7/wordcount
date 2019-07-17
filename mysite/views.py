from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request , 'home.html', {'text1': 'this is homepage'})

def about(request):
    return render(request , 'about.html', {'about_text':'this is a sadegh`s site'})

def count(request):
    fulltext = request.GET['count text']
    text_list = fulltext.split()
    word_dic = {}
    for word in text_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return render(request , 'count.html',{'count':'countpage' , 'fulltext':fulltext , 'number_of_word':len(text_list) , 'word_dic':word_dic.items()})

def adding(request):
    return render(request , 'add.html')

def add_answer(request):
    text = request.GET['add text']
    textlist = text.split()
    answer = str(int(textlist[0]) + int(textlist[2]))
    return render(request , 'add_answer.html' , {'answer':answer})