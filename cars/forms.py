from django import forms
from cars.models import Car
from django.core.exceptions import ValidationError
from datetime import datetime


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car  # Especifica o modelo associado ao ModelForm
        fields = '__all__'  #usando o all tras todos os campos, e quando inserir um novo puxara automaticamente


    def clean_value(self):
       value = self.cleaned_data.get('value')
       if value < 20000:
           self.add_error('value', 'pela politica da empresa valor minimo é de R$20.000,00 ')
       return value
    
# clean_ é usado para validações no forms sempre é usado o clean_'nome do campo que deseja validar'
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is None or value < 20000:
            self.add_error('value', 'Pela política da empresa, o valor mínimo é de R$20.000,00.')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year is None:
            raise ValidationError("Ano de fabricação não pode ser vazio.")
        
        current_year = datetime.now().year
        if factory_year < current_year - 20:
            self.add_error('factory_year', 'Pela política da empresa, não revendemos carros com mais de 20 anos de uso no mercado!')
        return factory_year


# class CarForm(forms.Form):
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all())
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     photo = forms.ImageField()


#     def save(self):
#         car = Car(
#             model = self.cleaned_data['model'],
#             brand = self.cleaned_data['brand'],
#             factory_year = self.cleaned_data['factory_year'],
#             model_year = self.cleaned_data['model_year'],
#             plate = self.cleaned_data['plate'],
#             value = self.cleaned_data['value'],
#             photo = self.cleaned_data['photo'],
#         )
#         car.save()
#         return car
    
#usando este metodo ele criara a tabela sozinho puxando os dados do campos da tabela do projeto, 
# a cima foi feioto manualmente e a baixo feito com modelform, e tambem caso adicionado novos campos tipo cor do carro, ele puxara automaticamente
