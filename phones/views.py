from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,UpdateView,ListView
from django.db import models

from .models import PhonesModel,PhoneStatustype 
from .forms import PhoneForm

class PhonesListView(ListView):
    template_name = 'phone/list.html'
    context_object_name = 'phones'
    def get_queryset(self) -> QuerySet[Any]:
        queryset = PhonesModel.objects.all()
        # queryset = PhonesModel.objects.filter(status=PhoneStatustype.available.value)
        if search_q := self.request.GET.get('q'):
            queryset = queryset.filter(brand_name__icontains=search_q)
        if self.request.GET.get('korea_search'):
            queryset = queryset.filter(brand_nationality__icontains='Korea')
        if self.request.GET.get('nationality'):
            queryset = queryset.filter(brand_nationality=models.F('manufacturing_country'))
        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)

class PhoneCreatedView(CreateView):
    template_name = 'Phone/create.html'
    queryset = PhonesModel.objects.all()
    form_class = PhoneForm
    
    def get_success_url(self):
        return reverse_lazy("phones:phone-list")


class PhoneUpdatedView(UpdateView):
    template_name = 'Phone/update.html'
    queryset = PhonesModel.objects.all()
    form_class = PhoneForm

    def get_success_url(self):
        return reverse_lazy("phones:phone-list")

# class PhoneDeleteView(DeleteView):
#     template_name = 'Phone/delete.html'
#     queryset = PhonesModel.objects.all()

#     def get_success_url(self):
#         return reverse_lazy("phones:phone-list")

