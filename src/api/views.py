from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsSuperUser
from api.serializers import GamerSerializer, QuestionSerializer, QuizSerializer
from quiz.models import Question, Quiz


class GamerViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = GamerSerializer


class QuestionDetailView(RetrieveAPIView):
    serializer_class = QuestionSerializer

    def get_object(self):
        return Question.objects.get(quiz__pk=self.kwargs.get("pk"), order_number=self.kwargs.get("order"))


class QuizListView(ListAPIView):
    permission_classes = [IsSuperUser]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
