from django.shortcuts import redirect, render, get_object_or_404
from maincomment.models import MainComment, Comment
from .forms import CommentForm

def index2(request, pk):
    maincomment = get_object_or_404(MainComment, pk=pk)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.maincomment = maincomment
        comment.save()
        return redirect(request.path)
    return render(request, 'maincomment/index2.html', {
                            'maincomment': maincomment,
                            'form':form,
                            })

def comment_list(request):
    qs = Comment.objects.all().order_by('-id').select_related('main')
    return render(request, 'maincomment/index2.html',{
        'comment_list':qs,
    })
