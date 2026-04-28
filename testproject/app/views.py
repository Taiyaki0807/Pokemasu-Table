from django.shortcuts import render
from django.http import HttpResponse
 
def index(request):
    return render(request, "app/home.html")

def third(request):
    exn_hp = '22,170,000'
    leaders = [
        {'name': 'ビオラ', 'color': '#9CB558'},
        {'name': 'ザクロ', 'color': '#A08C78'},
        {'name': 'コルニ', 'color': '#D67B47'},
        {'name': 'フクジ', 'color': '#459E4E'},
        {'name': 'シトロン', 'color': '#DCB40A'},
        {'name': 'マーシュ', 'color': '#ED9BB8'},
        {'name': 'ゴジカ', 'color': '#E66F9C'},
        {'name': 'ウルップ', 'color': '#6EB4B9'},
    ]
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
    for i in range(6, 31):
        round_data.append({'hp': exn_hp, 'name': f'Ex{i}'})
    return render(request, "app/third.html", {"rounds": round_data, "leaders": leaders})

def ticket(request):
    context = {
        "total_tickets": 100,
        "used_tickets": 0,
    }
    return render(request, "app/ticket.html", context)