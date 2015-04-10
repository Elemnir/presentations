from django.db import models
from django    import forms

class Ticket(models.Model):
    subject = models.CharField(
        max_length=200
    )
    sender  = models.EmailField()
    msgbody = models.TextField()
    subdate = models.DateTimeField(
        auto_now_add=True
    )

    def __unicode__(self):
        return self.sender + ' - ' + self.subject

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'subject',
            'sender',
            'msgbody'
        ]
