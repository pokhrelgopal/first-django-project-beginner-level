# --> Made my me.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    dj_text = request.GET.get('text', 'default')
    remove_punc = request.GET.get('removePunc', 'off')
    capital_text = request.GET.get('capitalText', 'off')
    newline_remove = request.GET.get('newLineRemove', 'off')
    character_counter = request.GET.get('characterCounter', 'off')

    if remove_punc == "on":
        punctuations = '''!@#$%^&*()'''
        analyzed = ""
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose': 'Removed Punctuations',
            'analyzed_text': analyzed
        }
        dj_text = analyzed

    if capital_text == "on":
        analyzed = ""
        for item in dj_text:
            fixed_item = item.capitalize()
            analyzed = analyzed + fixed_item

        params = {
            'purpose': 'Capitalize',
            'analyzed_text': analyzed
        }
        dj_text = analyzed

    if newline_remove == "on":
        analyzed = ""
        for char in dj_text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {
            'purpose': 'New Line Removed',
            'analyzed_text': analyzed
        }
        dj_text = analyzed

    if character_counter == 'on':
        count_num = 0
        for char in dj_text:
            if char != '\n':
                count_num = count_num + 1
        params = {
            'purpose': 'Counting Characters',
            'analyzed_text': count_num
        }

    return render(request, 'index.html', params)
