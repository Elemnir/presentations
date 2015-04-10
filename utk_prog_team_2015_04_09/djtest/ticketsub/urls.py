from django.conf.urls import patterns, include, url

urlpatterns = patterns('ticketsub.views',
    url(r'^$', 'submit_ticket', name='ticketsub_submit'),
    url(r'^(\d+)/$', 'submit_ticket', name='ticketsub_submit_val'),
    url(r'^list/$', 'ticket_list', name='ticketsub_list'),
)
