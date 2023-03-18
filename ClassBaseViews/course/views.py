from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins 
from .models import Courses
from .serializers import CourseSerializer
class CourseList(APIView):
    def get(self,request,*args, **kwargs):
       try:
            course=Courses.objects.all()
            serializer=CourseSerializer(course,many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
       except Courses.DoesNotExist:
           return Response({'status':status.HTTP_404_NOT_FOUND})
    def post(self,request,*args, **kwargs):
            serializer=CourseSerializer(data=request.data)
            if serializer.is_valid():
                 return Response({'data':serializer.data,'status':status.HTTP_201_CREATED})
            return Response({'error':serializer.errors,'status':status.HTTP_401_UNAUTHORIZED})


class CourseDetails(APIView):
     def get(self,request,pk):
          try:
               course=Courses.objects.get(pk=pk)
               serializer=CourseSerializer(course)
               return Response({'data':serializer.data,'status':status.HTTP_200_OK})
          except Courses.DoesNotExist:
               return Response({'status':status.HTTP_204_NO_CONTENT})
     
     def put(self,request,pk):
          course=Courses.objects.get(pk=pk)
          serializer=CourseSerializer(course,data=request.data)
          if serializer.is_valid():
               return Response({'data':serializer.data,'status':status.HTTP_200_OK})
          return Response({'errors':serializer.errors,'status':status.HTTP_401_UNAUTHORIZED})

     def delete(self,reuest,pk):
          course=Courses.objects.get(pk=pk)
          course.delete()
          return Response({'status':status.HTTP_204_NO_CONTENT})
     
     def patch(self,request,pk):
          course=Courses.objects.get(pk=pk)
          serializer=CourseSerializer(course,data=request.data,partial=True)
          if serializer.is_valid():
               return Response({'data':serializer.data,'status':status.HTTP_200_OK})
          return Response({'errors':serializer.errors,'status':status.HTTP_401_UNAUTHORIZED})
