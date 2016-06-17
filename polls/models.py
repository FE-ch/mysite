from django.db import models
import datetime

from django.utils import timezone

# Create your models here.
class Question(models.Model):

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <=now

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



class Choice(models.Model):

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"

    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


