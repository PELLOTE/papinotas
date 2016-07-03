from django.shortcuts import render
from django.http import HttpResponse
from app.papinotas.models import *

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.papinotas.serializers import GroupsSerializer
try:
    import django.utils.simplejson
except:
    import json as simplejson

def get_stockondemand(request):
    data_list = []    
    data_list.append({
            'sku': 'perro',
            'stock_total': 100,
            'available_stock': False})
    return HttpResponse(simplejson.dumps(data_list))


class GrupsList(APIView):
  
    def get(self,request ):
        #serializer = GroupsSerializer(data1, many=True)
        #import pdb; pdb.set_trace()
        if len(request.GET.values()) != 0:
            token_get = request.GET['authentication_token']
        else:
            token_get = '1'
        authentication_token = '123'
        if token_get == authentication_token:
            groups = Groups.objects.all()
            data_st = []
            data_grup  = []
            data_list = []
            for g in groups:

                newOrder = dict()
                newOrder['id'] = g.id
                newOrder['name'] = g.name
                newOrder['group_type'] = g.group_type
                newOrder['students'] = Students.objects.filter(groups = g).values('id')
                newOrder['group_section'] = g.group_section
                newOrder['student_counter'] = g.student_counter
                newOrder['has_changes'] = g.has_changes
                data_grup.append(newOrder)
                #data_list.append('groups': newOrder)

            data_g = []    
            newOrder = dict()
            newOrder['groups'] =  data_grup
            data_g.append(newOrder)
            data_list.append({
                'status': 'success',
                'data': data_g,
                'message':'null'})
            return Response(data_list)
        else:
            data_list = []
            if token_get == '1':
                data_list.append({
                    'status': 'error',
                    'data': None,
                    'message':'le falta authentication_token'})
            else:
                data_list.append({
                    'status': 'error',
                    'data': None,
                    'message':'lo siento padre'})
            return Response(data_list)

class Studentslist(APIView):

     def get(self, request):
        #serializer = GroupsSerializer(data1, many=True)
        students = Students.objects.all()
        data_grup  = []
        data_list = []
        for st in students:
            newOrder = dict()
            newOrder['id'] = st.id
            newOrder['name'] = st.name
            newOrder['self'] = st.self
            newOrder['ap1'] = st.ap1
            newOrder['ap2'] = st.ap2
            data_grup.append(newOrder)
            #data_list.append('groups': newOrder)

        data_g = []    
        newOrder = dict()
        newOrder['students'] =  data_grup
        data_g.append(newOrder)
        data_list.append({
            'status': 'success',
            'data': data_g,
            'message':'null'})
        return Response(data_list)
