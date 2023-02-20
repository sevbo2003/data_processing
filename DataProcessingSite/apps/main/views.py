from django.views import View
from django.urls import reverse
from django.contrib import messages
from django.http import FileResponse
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ATCForm, LanguageForm, PresentationForm, ActiveIngredientForm
from .models import ATC, Presentation, Language, ActiveIngredient
from apps.presentation.utils import ReadCsvAndSaveInDatabase
from apps.atc.utils import ReadAtcCsvAndSaveInDatabase


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = "authed/home.html"
        return render(request, template_name,
            {'languages': Language.objects.all()
            }
        )


class AtcView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = "authed/atc.html"
        file = ATC.objects.last() if ATC.objects.all() else None
        if file:
            header, rows = file.extract_rows()
            paginator = Paginator(rows, 50)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        else:
            header, page_obj = None, None
        return render(request, template_name,
            {
             'languages': Language.objects.all(),
             'file': file,
             'form': ATCForm(instance=file),
             'header': header,
             'page_obj': page_obj,
             'table': file.file_to_html() if file else None,
            }
        )
    
    def post(self, request):
        template_name = "authed/home.html"
        file = ATC.objects.last() if ATC.objects.all() else None
        form = ATCForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            ReadAtcCsvAndSaveInDatabase(form.instance.file.path)
        return redirect(reverse('atc'))


class DownloadATCFileView(LoginRequiredMixin, View):
    def get(self, request, file_uuid):
        atc = get_object_or_404(ATC, uuid=file_uuid)
        return FileResponse(atc.file, 
                            as_attachment=True)


class PresentationsView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = "authed/presentation.html"
        file = Presentation.objects.last() if Presentation.objects.all() else None
        if file:
            header, rows = file.extract_rows()
            paginator = Paginator(rows, 50)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        else:
            header, page_obj = None, None
        return render(request, template_name,
            {
             'languages': Language.objects.all(),
             'file': file,
             'form': PresentationForm(instance=file),
             'header': header,
             'page_obj': page_obj,
             'table': file.file_to_html() if file else None,
            }
        )
    
    def post(self, request):
        template_name = "authed/home.html"
        file = Presentation.objects.last() if Presentation.objects.all() else None
        if file:
            form = PresentationForm(request.POST, request.FILES, instance=file)
        else:
            form = PresentationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            ReadCsvAndSaveInDatabase(form.instance.file.path)
        return redirect(reverse('presentations'))


class ActiveIngredientsView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = "authed/active-ingredients.html"
        file = ActiveIngredient.objects.last() if ActiveIngredient.objects.all() else None
        if file:
            header, rows = file.extract_rows()
            paginator = Paginator(rows, 50)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        else:
            header, page_obj = None, None
        return render(request, template_name,
            {
             'languages': Language.objects.all(),
             'file': file,
             'form': ActiveIngredientForm(instance=file),
             'header': header,
             'page_obj': page_obj,
             'table': file.file_to_html() if file else None,
            }
        )
    
    def post(self, request):
        template_name = "authed/home.html"
        file = ActiveIngredient.objects.last() if ActiveIngredient.objects.all() else None
        if file:
            form = ActiveIngredientForm(request.POST, request.FILES, instance=file)
        else:
            form = ActiveIngredientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(reverse('active_ingredients'))


class DownloadPresentationsFileView(LoginRequiredMixin, View):
    def get(self, request, file_uuid):
        presentation = get_object_or_404(Presentation, uuid=file_uuid)
        return FileResponse(presentation.file, 
                            as_attachment=True)


class DownloadActiveIngredientsFileView(LoginRequiredMixin, View):
    def get(self, request, file_uuid):
        ingredient = get_object_or_404(ActiveIngredient, uuid=file_uuid)
        return FileResponse(ingredient.file, 
                            as_attachment=True)




class UploadCsvView(LoginRequiredMixin, View):
    def post(self, request,):
        template_name = "authed/csv_form_error.html"
        return render(request, template_name,
            {'languages': Language.objects.all()
            }
        )

class LanguageCreateView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = "authed/languages.html"
        form = LanguageForm()
        return render(request, template_name,
            {
                'languages': Language.objects.all(),
                'form': form,
            }
        )
    
    def post(self, request):
        template_name = "authed/languages.html"
        form = LanguageForm(request.POST, request.FILES)
        print("form is valid: ", form.is_valid())
        if form.is_valid():
            form.save()
        return redirect(reverse('home'))

class LanguageView(LoginRequiredMixin, View):
    def get(self, request, language):
        template_name = "authed/languages.html"
        form = LanguageForm()
        language = get_object_or_404(Language, name=language)
        return render(request, template_name,
            {
                'languages': Language.objects.all(),
                'language': language,
                'form': form,
            }
        )
    
    def post(self, request, language):
        template_name = "authed/languages.html"
        language = get_object_or_404(Language, name=language)
        form = LanguageForm(request.POST, instance=language)
        print("form is valid: ", form.is_valid())
        if form.is_valid():
            file = form.save(commit=False)
            file.processed = True
            file.save()
            # print(file.output_file)
            print(file.processed)
        return redirect(reverse('languages', kwargs={'language': language.name}))
    
    

class DownloadLanguageFileView(LoginRequiredMixin, View):
    def get(self, request, language):
        language = get_object_or_404(Language, name=language)
        return FileResponse(language.output_file, 
                            as_attachment=True)
    


import csv

def read_csv(request):
    with open(ATC.objects.last().file.path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return render(request, 'template.html', {'data': data})