from django.shortcuts import render
from rest_framework import status, viewsets
from .models import Actor, Country, Film, Staff, Address, Customer, Store
from .serializer import ActorSerializer, CountLastNameSerializer, Query2Serializer, Query13Serializer, Query16Serializer
from .serializer import  Query6Serializer, Query10Serializer, Query11Serializer, Query12Serializer, Query14Serializer
from .serializer import  Query18Serializer, Query19Serializer, Query17Serializer
from rest_framework.response import Response


class ActorListView(viewsets.ModelViewSet):
    queryset = Actor.objects.raw(
        '''
       SELECT * 
       FROM V1
        '''
    )
    serializer_class = ActorSerializer

    def list(self, request):
        queryset = self.get_queryset()
        # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = ActorSerializer(list(queryset), many=True)
        return Response(serializer.data)


class CountLastNameListView(viewsets.ModelViewSet):
    queryset = Actor.objects.raw(
        '''
        SELECT*
        FROM V8
        '''
    )
    serializer_class = CountLastNameSerializer

    def list(self, request):
        queryset = self.get_queryset()
        # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = CountLastNameSerializer(list(queryset), many=True)
        return Response(serializer.data)

class Query2View(viewsets.ModelViewSet):
    queryset = Actor.objects.raw(
        '''
        SELECT*
        FROM V2
        '''
    )
    serializer_class = Query2Serializer

    def list(self, request):
        queryset = self.get_queryset()
        # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = Query2Serializer(list(queryset), many=True)
        return Response(serializer.data)

class Query3View(viewsets.ModelViewSet):
    queryset = Actor.objects.raw(
        '''
        SELECT*
        FROM V3
        '''
    )
    serializer_class = ActorSerializer

    def list(self, request):
        queryset = self.get_queryset()
        # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = ActorSerializer(list(queryset), many=True)
        return Response(serializer.data)

class Query4View(viewsets.ModelViewSet):
    queryset = Actor.objects.raw(
        '''
        SELECT*
        FROM V4
        '''
    )
    serializer_class = ActorSerializer

    def list(self, request):
        queryset = self.get_queryset()
        # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = ActorSerializer(list(queryset), many=True)
        return Response(serializer.data)

class Query5View(viewsets.ModelViewSet):
    queryset = Actor.objects.raw(
        '''
        SELECT*
        FROM V5
        '''
    )
    serializer_class = ActorSerializer

    def list(self, request):
        queryset = self.get_queryset()
        # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = ActorSerializer(list(queryset), many=True)
        return Response(serializer.data)

class Query6View(viewsets.ModelViewSet):
    queryset = Country.objects.raw(
        '''
        SELECT*
        FROM V6
        '''
    )
    serializer_class = Query6Serializer

    def list(self, request):
        queryset = self.get_queryset()
        # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = Query6Serializer(list(queryset), many=True)
        return Response(serializer.data)

class Query9View(viewsets.ModelViewSet):
    queryset = Actor.objects.raw(
            '''
            SELECT*
            FROM V9
            '''
    )
    serializer_class = CountLastNameSerializer

    def list(self, request):
        queryset = self.get_queryset()
         # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = CountLastNameSerializer(list(queryset), many=True)
        return Response(serializer.data)

class Query10View(viewsets.ReadOnlyModelViewSet):
    queryset = Film.objects.raw(
            '''
            SELECT*
            FROM V10
            '''
    )
    serializer_class = Query10Serializer

    def list(self, request):
        queryset = self.get_queryset()
         # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = Query10Serializer(list(queryset), many=True)
        return Response(serializer.data)

class Query11View(viewsets.ReadOnlyModelViewSet):
    queryset = Staff.objects.raw(
            '''
            SELECT*
            FROM V11
            '''
    )
    serializer_class = Query11Serializer

    def list(self, request):
        queryset = self.get_queryset()
         # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = Query11Serializer(list(queryset), many=True)
        return Response(serializer.data)

class Query12View(viewsets.ReadOnlyModelViewSet):
    queryset = Staff.objects.raw(
            '''
            SELECT*
            FROM V12
            '''
    )
    serializer_class = Query12Serializer

    def list(self, request):
        queryset = self.get_queryset()
         # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = Query12Serializer(list(queryset), many=True)
        return Response(serializer.data)

class Query13View(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.raw(
            '''
            SELECT*
            FROM V13
            '''
    )
    serializer_class = Query13Serializer

    def list(self, request):
        queryset = self.get_queryset()
         # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = Query13Serializer(list(queryset), many=True)
        return Response(serializer.data)

class Query14View(viewsets.ReadOnlyModelViewSet):
    queryset = Film.objects.raw(
            '''
            SELECT*
            FROM V14
            '''
    )
    serializer_class = Query14Serializer

    def list(self, request):
        queryset = self.get_queryset()
         # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = Query14Serializer(list(queryset), many=True)
        return Response(serializer.data)

class Query15View(viewsets.ReadOnlyModelViewSet):
    queryset = Actor.objects.raw(
            '''
            SELECT*
            FROM V15
            '''
    )
    serializer_class = ActorSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ActorSerializer(list(queryset), many=True)
        return Response(serializer.data)

class Query16View(viewsets.ReadOnlyModelViewSet):
    queryset = Store.objects.raw(
            '''
            SELECT*
            FROM V16
            '''
    )
    serializer_class =Query16Serializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = Query16Serializer(list(queryset), many=True)
        return Response(serializer.data)

class Query17View(viewsets.ReadOnlyModelViewSet):
    queryset = Store.objects.raw(
            '''
            SELECT*
            FROM V17
            '''
    )
    serializer_class =Query17Serializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = Query17Serializer(list(queryset), many=True)
        return Response(serializer.data)

class Query18View(viewsets.ReadOnlyModelViewSet):
    queryset = Film.objects.raw(
            '''
            SELECT*
            FROM V18
            '''
    )
    serializer_class =Query18Serializer

    def list(self, request):
        queryset = self.get_queryset()
         # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = Query18Serializer(list(queryset), many=True)
        return Response(serializer.data)

class Query19View(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.raw(
            '''
            SELECT*
            FROM V19
            '''
    )
    serializer_class =Query19Serializer

    def list(self, request):
        queryset = self.get_queryset()
         # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = Query19Serializer(list(queryset), many=True)
        return Response(serializer.data)