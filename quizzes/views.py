from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Category, Question, Quiz, UserResult
from .forms import CategoryForm, QuestionForm, QuizSelectionForm

# Category list will be category detail, with cards showing category details
# showing number of questions in category so far.

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'quizzes/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    questions = Question.objects.filter(category=category, is_approved=True)
    return render(request, 'quizzes/category_detail.html', {'category': category, 'questions': questions})

@login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            return redirect('category_detail', category_id=question.category.id)
    else:
        form = QuestionForm()
    return render(request, 'quizzes/add_question.html', {'form': form})


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz})



@login_required
def generate_quiz(request):
    num_questions = request.GET.get('num_questions')
    category_id = request.GET.get('category_id')
    difficulty = request.GET.get('difficulty')
    time_limit = int(request.GET.get('time_limit')) * int(num_questions)

    category = get_object_or_404(Category, id=category_id)

    difficulty_filter = Q()
    if difficulty in ["easy", "medium", "hard"]:
        difficulty_filter = Q(difficulty=difficulty)

    questions = list(
        # Using Django query utils for complex query
        Question.objects.filter(
            Q(category=category) &
            difficulty_filter &
            Q(is_approved=True)
        ).order_by('?')[:num_questions]
    )

    quiz = Quiz.objects.create(
        category=category, time_limit=time_limit)
    quiz.questions.set(questions)
    quiz.save()

    answers = { question.id : list(question.incorrect_answers).append(question.correct_answer) for question in questions }
    print(answers)
    return render('quizzes/attempt_quiz.html', {'quiz': quiz, })



@login_required
def attempt_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, user=request.user)

    if request.method == 'POST':
        score = 0
        for question in quiz.questions.all():
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer == question.correct_answer:
                score += 1
        quiz.score = score
        quiz.save()
        return redirect('quiz_result', quiz_id=quiz.id)

    return render(request, 'quizzes/attempt_quiz.html', {'quiz': quiz})


def attempt_quiz(request):
    quiz = request.GET.get('quiz')
    number_of_questions = request.GET.get('number_of_questions')
    category = request.GET.get('category')
    difficulty = request.GET.get('difficulty')
    time_limit = request.GET.get('time_limit')

    # Now use these parameters to generate a quiz for the user

    return render(request, 'quizzes/attempt_quiz.html', {
        'quiz': quiz,
        'number_of_questions': number_of_questions,
        'category': category,
        'difficulty': difficulty,
        'time_limit': time_limit
    })





def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    user_result = UserResult(user=request.user, quiz=get_object_or_404(Quiz, id=quiz.id), score=0)
    results = []

    for question in quiz.questions.all():
        user_answer = request.POST.get(f'question_{question.id}')
        is_correct = user_answer == question.correct_answer
        if is_correct:
            user_result.score += 1

        results.append({
            'question': question,
            'user_answer': user_answer,
            'is_correct': is_correct,
        })

    return render(request, 'quizzes/quiz_result.html', {
        'quiz': quiz,
        'results': results,
        'score': user_result.score
    })

@login_required
def select_quiz_preferences(request):
    if request.method == 'POST':
        form = QuizSelectionForm(request.POST)
        if form.is_valid():
            # Process the form data
            num_questions = int(form.cleaned_data['num_questions'])
            category_id = form.cleaned_data['category_id']
            difficulty = form.cleaned_data['difficulty']
            time_limit = int(form.cleaned_data['time_limit']) * num_questions
            #--------------------------------------------------

            category = get_object_or_404(Category, id=category_id)

            difficulty_filter = Q()
            if difficulty in ["easy", "medium", "hard"]:
                difficulty_filter = Q(difficulty=difficulty)

            questions = list(
                # Using Django query utils for complex query
                Question.objects.filter(
                    Q(category=category) &
                    difficulty_filter &
                    Q(is_approved=True)
                ).order_by('?')[:num_questions]
            )

            quiz = Quiz.objects.create(
                category=category, time_limit=time_limit)
            quiz.questions.set(questions)
            quiz.save()

            return render(request, 'quizzes/attempt_quiz.html', {'quiz': quiz})

            # -------------------------------------------------

    else:
        form = QuizSelectionForm()

    return render(request, 'quizzes/select_quiz.html', {'form': form})






@login_required
def user_dashboard(request):
    user_results = UserResult.objects.filter(user=request.user)
    return render(request, 'quizzes/user_dashboard.html', {'user_results': user_results})
