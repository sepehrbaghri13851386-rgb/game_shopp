from django.shortcuts import render, redirect, get_object_or_404
from .forms import ComentForm
from .models import coment, Reply

def contact(request):
    if request.method == 'POST':
        form = ComentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ComentForm()
    return render(request, 'contact.html', {'form': form})

def reply_comment(request, comment_id):
    # فقط ادمین می‌تونه ریپلای بده
    if not request.user.is_staff:
        return redirect('/')
    
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if text:
            comment = get_object_or_404(coment, id=comment_id)
            Reply.objects.create(comment=comment, text=text)
    
    # برگشت به همون صفحه‌ای که ریپلای از اونجا زده شده
    next_url = request.POST.get('next', '/')
    return redirect(next_url)
