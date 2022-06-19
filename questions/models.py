import random
import uuid
from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class Question(BaseModel):
    course = models.ForeignKey(Course, related_name='course',on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    image = StdImageField('Image', upload_to="questions",variations={'tumb':(300, 300)}, blank = True)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question

    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question = self))
        data = []

        random.shuffle(answer_objs)

        for answer_obj in answer_objs:
            data.append({
                'answer': answer_obj.answer,
                'is_correct': answer_obj.is_correct,
            })

        return data


class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='question_answer',on_delete=models.CASCADE) 
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class ScoreBoard(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
