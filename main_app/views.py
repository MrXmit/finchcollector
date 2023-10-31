from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
# from .forms import FeedingForm


class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/finches/'

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a finch by excluding the name field!
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/' 

# def add_feeding(request, finch_id):
#   form = FeedingForm(request.POST)
#   if form.is_valid():
#     new_feeding = form.save(commit=False)
#     new_feeding.finch_id = finch_id
#     new_feeding.save()
#   return redirect('finch-detail', finch_id=finch_id)

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def finch_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })

def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })