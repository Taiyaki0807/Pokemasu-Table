from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Result(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    round_leader_key = models.CharField(max_length=100, unique=True)
    tickets_used = models.IntegerField(default=0)