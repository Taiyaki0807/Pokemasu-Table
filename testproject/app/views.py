from django.shortcuts import render
from django.http import HttpResponse
 
def index(request):
    return render(request, "app/home.html")

def third(request):
    exn_hp = '22,170,000'
    leaders = ['ビオラ', 'ザクロ', 'コル二', 'フクジ', 'シトロン', 'マーシュ', 'ゴジカ', 'ウルップ']
    round_data = [
        {'hp': '500,000', 'name': '1'},
        {'hp': '3,460,000', 'name': '2'},
        {'hp': '5,540,000', 'name': '3'},
        {'hp': '7,980,000', 'name': 'Ex1'},
        {'hp': '10,860,000', 'name': 'Ex2'},
        {'hp': '14,190,000', 'name': 'Ex3'},
        {'hp': '17,960,000', 'name': 'Ex4'},
        {'hp': '22,170,000', 'name': 'Ex5'},
    ]
    for i in range(6, 21):
        round_data.append({'hp': exn_hp, 'name': f'Ex{i}'})
    return render(request, "app/third.html", {"rounds": round_data, "leaders": leaders})