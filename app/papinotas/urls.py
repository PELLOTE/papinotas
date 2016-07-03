from django.conf.urls import url, include
from app.papinotas.views import * 

urlpatterns = [
    url(r'^grupos/$', get_stockondemand ),
    
]
