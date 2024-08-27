from django import forms
from .models import Question, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question_type', 'difficulty', 'category', 'question_text',
            'correct_answer', 'incorrect_answers'
            ]


class QuizSelectionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        """Setting the category fields dynamically from model"""
        super(QuizSelectionForm, self).__init__(*args, **kwargs)
        self.fields['category_id'].choices = [
            (category.id, category.name) for category in Category.objects.all()
        ]

    category_id = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    num_questions = forms.ChoiceField(
        choices=[
            (5, '5'),
            (10, '10'), (15, '15'),
            (20, '20'), (30, '30')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    difficulty = forms.ChoiceField(
        choices=[
            ('easy', 'Easy'),
            ('medium', 'Medium'),
            ('hard', 'Hard')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    time_limit = forms.ChoiceField(
        choices=[
            (0, 'No Limit'),
            (30, '30 seconds'),
            (60, '60 seconds'),
            (180, '180 seconds')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
