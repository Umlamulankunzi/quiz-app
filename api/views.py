from rest_framework import generics, permissions
from quizzes.models import Quiz  # UserResult
from .serializers import QuizSerializer, UserResultSerializer
from django.http import JsonResponse

# Create your views here.
def index(request):
    data = {"message": "hello Quiz App"}
    return JsonResponse(data)


class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.filter(approved=True)
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class QuizDetailView(generics.RetrieveAPIView):
    queryset = Quiz.objects.filter(approved=True)
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SubmitQuizView(generics.CreateAPIView):
    serializer_class = UserResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
