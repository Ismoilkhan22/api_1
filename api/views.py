from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import Telefon
from api.serializer import TelefonSerializer


class TelefonVeiw(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TelefonSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            # telefon = Telefon.objects.filter(pk=pk).first() # birinhi usul edi bu
            # if telefon:
            #     return Response(telefon.format())
            # else:
            #     return Response({"Error": "bunaqa id yo'q"})

            #  2- chi usul
            try:
                return Response(Telefon.objects.get(pk=pk).format())
            except:
                return Response({"Error": "Bunaqa id yo'q "})

        telefonlar = Telefon.objects.all().order_by("-pk")
        return Response([x.format() for x in telefonlar])

    def delete(self, request, pk):
        try:
            Telefon.objects.get(pk=pk).delete()
            return Response({"natija": "Deleted"})

        except:

            return Response({"natija": "aldama"})

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        telefon = serializer.save()

        return Response(telefon.format())

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        root = Telefon.objects.filter(pk=pk).first()
        if not root:
            return Response({"error": "Bunaqa narsa yo'q"})
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True,)
        telefon = serializer.save()

        return Response(telefon.format())