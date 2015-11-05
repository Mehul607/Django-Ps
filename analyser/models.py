from django.db import models

class Colour(models.Model):
    col=models.CharField(max_length=10)
    hashcode=models.CharField(max_length=10,default='#FFF000')
    def __unicode__(self):
        return self.col

class Language(models.Model):
    language=models.CharField(max_length=15)
    colour=models.ForeignKey(Colour)
    def __unicode__(self):
        return self.language

class Word(models.Model):
    wtext=models.CharField(max_length=20)
    lang=models.ForeignKey(Language)
    def __unicode__(self):
        return self.wtext

class Sentence(models.Model):
    stext=models.CharField(max_length=100)
    def __unicode__(self):
        return self.stext
