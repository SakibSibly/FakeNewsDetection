from django.contrib import admin
from .models import CustomUser, SearchData, MailingHistory, Feedback


admin.site.register(CustomUser)
admin.site.register(SearchData)
admin.site.register(MailingHistory)
admin.site.register(Feedback)