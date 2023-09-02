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
    # quiz = graphene.String()

    # all_quizzes = DjangoListField(QuizType)
    #
    # def reslove_all_quizzes(root, info):
    #     return Quiz.objects.filter(id=1)

    # quizzes = graphene.List(QuizType)
    # quiz_by_id = graphene.Field(QuizType, id=graphene.Int())
    #
    # def resolve_quizzes(root, info, **kwargs):
    #     return Quiz.objects.all()
    #
    # def resolve_quiz_by_id(root, info, id):
    #     # Querying a single question
    #     return Quiz.objects.get(pk=id)

    question_all = graphene.List(QuestionType)
    question_by_id = graphene.Field(QuestionType, id=graphene.Int())
    answer_list_by_question_id = graphene.List(AnswerType, questionId=graphene.Int())

    def resolve_question_by_id(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_answer_list_by_question_id(root, info, questionId):
        # Querying a single question
        return Answer.objects.filter(question=questionId)


schema = graphene.Schema(query=Query)
