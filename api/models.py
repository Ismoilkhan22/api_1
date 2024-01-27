from django.db import models


class Telefon(models.Model):
    name = models.CharField(max_length=256)
    brand = models.CharField(max_length=128)
    xotira = models.IntegerField()
    xotira_type = models.CharField(max_length=2, choices=[
        ("MB", "MB"),
        ("GB", "GB"),
        ("TB", "TB")
    ])
    rangi = models.CharField(max_length=10, choices=[
        ("oq", "oq"),
        ("qora", "qora"),
        ("kuk", "kuk")
    ])
    narxi = models.CharField(max_length=128)
    narxi_tipi = models.CharField(max_length=3, choices=[
        ("USD", "USD"),
        ("USZ", "USZ"),
        ("EUR", "EUR"),
        ("RUB", "RUB")
    ])

    def __str__(self):
        return self.name

    def format(self):
        return {
            "id":self.id,
            "name": self.name,
            "brand": self.brand,
            "xotira": f"{self.xotira}{self.xotira_type}",
            "rangi": self.rangi,
            "narxi": f"{self.narxi}{self.narxi_tipi}",
        }
