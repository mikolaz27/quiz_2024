from quiz.models import Category, Question, Quiz


def sample_quiz(title: str, **params):
    default = {
        "description": "Some description",
        "category": Category.objects.create(name="TestCategory"),
    }
    default.update(params)
    return Quiz.objects.create(title=title, **default)


def sample_question(quiz: Quiz, order_number: int, **params):
    default = {"text": "Text for testing"}
    default.update(params)
    return Question.objects.create(quiz=quiz, order_number=order_number, **default)
