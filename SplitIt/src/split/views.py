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

    if request.POST:
        if form.is_valid():
            temp = form.cleaned_data.get("choices") 
            print(temp) 

    return render(request, 'split/form_checkbox.html', context)


##def product_view(request):

  ##  products = Product.objects.all()

    ## return render(request)



# Print Output Sample
# {'exec_summary': True, 'scope': False, 'isms': True, 'methodology': False, 'recommendation': False}