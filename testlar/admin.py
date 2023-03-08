from django.contrib import admin


from .models import Question, QuizModel, Answer, Result


@admin.register(QuizModel)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'tugatish']


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['name', 'is_right']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['name', 'quiz','image_question']
    list_display = ['name', 'quiz','image_question']
    inlines = [AnswerInlineModel]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_right', 'question']

@admin.register(Result)
class ResultAdmiin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'total_question', 'corrent_question', 'total', 'create_at','id','quiz_id']
    list_filter = ['quiz']