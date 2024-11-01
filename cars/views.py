from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        order_by = self.request.GET.get('order_by', 'model')
        valid_orderings = ['model', 'brand__name', 'factory_year']
        if order_by not in valid_orderings:
            order_by = 'model'
        cars = Car.objects.all().order_by(order_by)
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCreateView(UserPassesTestMixin, CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "Você não tem permissão para cadastrar um novo carro. Somente superusuários podem realizar essa ação.")
        return render(self.request, 'permission_denied.html')


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UserPassesTestMixin, UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "Você não tem permissão para editar este carro. Somente superusuários podem realizar essa ação.")
        return render(self.request, 'permission_denied.html')

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(UserPassesTestMixin, DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "Você não tem permissão para deletar um carro. Somente superusuários podem realizar essa ação.")
        return render(self.request, 'permission_denied.html')
    