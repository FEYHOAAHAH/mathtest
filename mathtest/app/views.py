from django.shortcuts import render, redirect
from django.views import View
from .models import Question


class StartPageView(View):
    def get(self, request):
        return render(request, 'start_page.html')


class QuestionView(View):
    def get(self, request, difficulty):
        question = Question.objects.filter(difficulty=difficulty).first()
        context = {'question': question}
        return render(request, 'question_page.html', context)

    def post(self, request, difficulty):
        user_answer = int(request.POST.get('user_answer'))
        question = Question.objects.filter(difficulty=difficulty).first()
        correct_answer = question.correct_answer
        is_correct = user_answer == correct_answer
        context = {'question': question, 'user_answer': user_answer, 'is_correct': is_correct}
        return render(request, 'question_page.html', context)


class ResultsView(View):
    def get(self, request):
        # Предположим, что пользователь идентифицируется через сессию.
        # Замените этот код на вашу логику идентификации пользователя.

        # Пример кода:
        user_id = request.session.get('user_id')
        if user_id is None:
            return redirect('start_page')

        # Получите все вопросы, на которые пользователь ответил
        answered_questions = Question.objects.filter(user_answers__user_id=user_id)

        # Рассчитайте количество правильных ответов пользователя
        correct_answers_count = answered_questions.filter(user_answers__is_correct=True).count()

        # Определите, сдал ли пользователь тест (например, если более 70% правильных ответов)
        pass_percentage = 70
        passed_test = (correct_answers_count / answered_questions.count()) * 100 >= pass_percentage

        context = {
            'correct_answers_count': correct_answers_count,
            'total_questions': answered_questions.count(),
            'passed_test': passed_test,
        }

        return render(request, 'results_page.html', context)
