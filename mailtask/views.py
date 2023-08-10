from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from .form import ReviewForm


class ReviewView(FormView):
    template_name = 'review_form.html'
    form_class =  ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg  = 'THank for review'
        return HttpResponse(msg)