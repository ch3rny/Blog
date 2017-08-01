from django.shortcuts import render, redirect
from .forms import AddReview
from .models import Review
from django.utils import timezone


# Create your views here.
def ReviewCreate(request):
    form = AddReview()
    if request.method == "POST":
        form = AddReview(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.created_date = timezone.now()
            if 'attachment' in request.FILES:
                review.attachment = request.FILES['attachment']
            review.save()
            return redirect('post_list')
        else:
            form = AddReview()
    return render(request, 'feedback/add_review.html', {'form': form, })

