from builtins import print  # type: ignore
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializer import *
import csv
from django.http import HttpResponse




class TaskView(APIView):
   
    def get(self,request,id =None):
        
        if id==None:
           
            all_wrk=Task.objects.all()
            
            task_data=Task_serializer(all_wrk, many=True).data

            return Response(task_data)
        
        else:
            
            single_id=Task.objects.get(id =id)
    
            task_data=Task_serializer(single_id).data
            
            return Response(task_data)


        

    def post(self,request):
        
        task_wrk=Task_serializer(data=request.data)
        
        if task_wrk.is_valid():
        
            task_wrk.save()
        
            return Response("wrk is done")
        
        else:
        
            return Response(task_wrk.errors)
        
        
    
    
    def patch (self,request,id):
        
        all_update=Task.objects.get(id=id)
        
        update_data=Task_serializer(all_update,data=request.data,partial=True)
        
        if update_data.is_valid():
        
            update_data.save()

            return Response("data updated")
        
        
    def delete(self,request,id):
        
        data_delete=Task.objects.get(id=id)
                
        data_delete.delete()
            
        return Response("Data Deleted")
    
    
class TaskCSVDownload(APIView):
    def get(self, request):
       
       response = HttpResponse(content_type='text/csv')
       
       response['Content-Disposition'] = 'attachment; filename="tasks.csv"'

       writer = csv.writer(response)
      
       writer.writerow(['ID', 'Title', 'Description', 'Created At', 'Updated At'])

       tasks = Task.objects.values_list('id', 'title', 'description', 'created_at', 'updated_at')
       
       for task in tasks:
           
          writer.writerow(task)

        return response


            
            
            
                
                
        
        
        


