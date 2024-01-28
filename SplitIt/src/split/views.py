from django.shortcuts import render


# Create your views here.
from split.forms import CheckBoxForm
from split.models import Product

def form_checkbox(request):
    if request.method == 'POST':
        form = CheckBoxForm(request.POST or None)

        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = CheckBoxForm()

    context = {'form': form}

    products = Product.objects.all()
    context['products'] = products

    return render(request, 'split/form_checkbox.html', context)

# Print Output Sample
# {'exec_summary': True, 'scope': False, 'isms': True, 'methodology': False, 'recommendation': False}