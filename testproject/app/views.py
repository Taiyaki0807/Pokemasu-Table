from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member, Result
from django.db.models import Sum

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
    members = Member.objects.all()
    for i in range(6, 31):
        round_data.append({'hp': exn_hp, 'name': f'Ex{i}'})
        
    if request.method == "POST": 
        for key, value in request.POST.items():
            if "_count" in key and value:
                member_key = key.replace("_count", "_member")
                member_name = request.POST.get(member_key)
                
                if member_name:
                    member_obj = Member.objects.filter(name=member_name).first()
                    if member_obj:
                        Result.objects.update_or_create(
                            round_leader_key=key,
                            defaults={'member': member_obj, 'tickets_used': int(value)}
                        )
        return redirect("third_page")

    saved_data = Result.objects.select_related('member').all()
    results_dict = {}
    for data in saved_data:
        results_dict[data.round_leader_key] = {
            'member_name': data.member.name if data.member else None,
            'tickets_used': str(data.tickets_used)
        }

    return render(request, "app/third.html", {
        "rounds": round_data, "leaders": leaders, "members": members, "results_dict": results_dict})

def ticket(request):
    if request.method == "POST":
        if "add_member" in request.POST:
            name = request.POST.get("name")
            if name and Member.objects.count() < 20:
                Member.objects.create(name=name)
        
        elif "delete_id" in request.POST:
            delete_id = request.POST.get("delete_id")
            Member.objects.filter(id=delete_id).delete()
            
        return redirect("ticket_page")
    
    members = Member.objects.all()
    for m in members:
        used = Result.objects.filter(member=m).aggregate(Sum('tickets_used'))['tickets_used__sum'] or 0
        m.used = used
        m.remaining = 30 - used
        if m.used > 30: # チケット使用数が30を超える場合の処理
            pass

    total_ticket = sum(m.remaining for m in members)
    total_used = sum(m.used for m in members)
    return render(request, "app/ticket.html", {"members": members, "total_ticket": total_ticket, "total_used": total_used})