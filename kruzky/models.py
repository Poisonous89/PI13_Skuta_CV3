from django.db import models

class Veduci(models.Model):
    meno = models.CharField(max_length=150) # napr. "Mgr. Jana Nováková"
    email = models.EmailField()

    def __str__(self):
        return self.meno

class Kruzok(models.Model):
    nazov = models.CharField(max_length=100)
    den = models.CharField(max_length=20) # napr. "Pondelok"
    miestnost = models.CharField(max_length=20) # napr. "B2"
    veduci = models.ForeignKey(Veduci, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazov