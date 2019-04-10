
from .forms import *
from .models import *

from django.shortcuts import render, redirect




def comments(request):
    """Вывод полной статьи
    """

    comment = Comments.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user

            form.save()
            return redirect(comments)
    else:
        form = CommentForm()
    return render(request, "comment.html",
                  {
                   "comments": comment,
                   "form": form})
