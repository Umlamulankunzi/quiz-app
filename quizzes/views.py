from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, UserResult
from .forms import QuizForm, QuestionForm


def home(request):
    quizzes = Quiz.objects.filter(approved=True)
    return render(request, 'quizzes/home.html', {'quizzes': quizzes})



@login_required
def user_dashboard(request):
    user_results = UserResult.objects.filter(user=request.user)
    return render(request, 'quizzes/user_dashboard.html', {'user_results': user_results})


@login_required
def quiz_master_dashboard(request):
    if not request.user.is_quiz_master:
        return HttpResponse("Unauthorized", status=401)

    quizzes = Quiz.objects.filter(created_by=request.user)
    return render(request, 'quizzes/quiz_master_dashboard.html', {'quizzes': quizzes})


# View for displaying all quizzes
def quiz_list(request):
    quizzes = Quiz.objects.filter(approved=True)
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})

# View for displaying a single quiz
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id, approved=True)
    questions = quiz.questions.all()
    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz, 'questions': questions})

# View for creating a quiz (for quiz masters)
@login_required
def create_quiz(request):
    if not request.user.is_quiz_master:
        return HttpResponse("Unauthorized", status=401)

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.created_by = request.user
            quiz.save()
            return redirect('quiz_list')
    else:
        form = QuizForm()

    return render(request, 'quizzes/create_quiz.html', {'form': form})

# View for updating a quiz (for quiz masters)
@login_required
def update_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id, created_by=request.user)

    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect('quiz_list')
    else:
        form = QuizForm(instance=quiz)

    return render(request, 'quizzes/update_quiz.html', {'form': form})

# View for deleting a quiz (for quiz masters)
@login_required
def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id, created_by=request.user)

    if request.method == 'POST':
        quiz.delete()
        return redirect('quiz_list')

    return render(request, 'quizzes/delete_quiz.html', {'quiz': quiz})

# View for submitting quiz answers and showing results
@login_required
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id, approved=True)
    questions = quiz.questions.all()

    if request.method == 'POST':
        score = 0
        for question in questions:
            answer = request.POST.get(str(question.id))
            if answer == question.correct_answer:
                score += 1
        result = UserResult(user=request.user, quiz=quiz, score=score)
        result.save()
        return render(request, 'quizzes/quiz_result.html', {'result': result})

    return render(request, 'quizzes/submit_quiz.html', {'quiz': quiz, 'questions': questions})



# Create your views here.
