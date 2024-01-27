from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import Telefon


class TelefonVeiw(GenericAPIView):
    permission_classes = (AllowAny,)

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
        natija = []
        for i in telefonlar:
            natija.append(i.format())
        return Response(natija)

    def delete(self, request, pk):
        try:
            Telefon.objects.get(pk=pk).delete()
            return Response({"natija": "Deleted"})

        except:

            return Response({"natija": "aldama"})
