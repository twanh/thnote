from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.context_processors import csrf
from .models import Note
from .forms import AddNoteForm, SearchForm

def index(request):
    notes = Note.objects.all()
    args = {}
    args.update(csrf(request))
    args['notes'] = notes
    return render(request, 'notes/index.html', context=args)

def search(request):
    if  request.method == 'POST':
        search_query = request.POST['query']
    else:
        search_query = '' 
    notes = Note.objects.filter(title__contains=search_query)
    return render(request, 'notes/ajax_search.html', {'notes': notes})

def detail(request, pk):
    notes = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/details.html', context={'notes': notes})


def favorite(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if note.is_favorite:
        note.is_favorite = False
    else: 
        note.is_favorite = True

    note.save()
    return HttpResponseRedirect(reverse('notes:note-detail', kwargs={
        'pk': pk,
    }))


class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'note', 'color']

class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'note', 'color']


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notes:index')