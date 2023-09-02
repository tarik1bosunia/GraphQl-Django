import graphene
from graphene_django import DjangoObjectType, DjangoListField

from quiz.models import Quiz, Question, Answer, Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')


class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'category')


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title', 'quiz')


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('question', 'answer_text')


class Query(graphene.ObjectType):
    quiz = graphene.String()

    all_quizzes = DjangoListField(QuizType)


schema = graphene.Schema(query=Query)
