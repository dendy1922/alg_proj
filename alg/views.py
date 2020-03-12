from django.shortcuts import render
from .forms import AlgForm
from .utils import alg_parser
from django.contrib import messages
from .models import Algorithm_execution_result, Alg


def upload(request):

    form = AlgForm()
    context = {'form': form, }

    if request.method == "POST":

        form = AlgForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                data = request.FILES['file'].read()
                data = str(data, 'utf-8').split()
                mas = [int(i) for i in data]

            except ValueError:
                messages.add_message(request, messages.INFO, 'Wrong data in the file')
                return render(request, 'upload.html', context=context)

            algorithm = request.POST['algorithms']
            ins = alg_parser(algorithm)
            new_mas = ins.realize(mas)

            name = Alg.objects.get(name__iexact=algorithm)
            new_obj = Algorithm_execution_result(name_alg=name,
                                                 timing=new_mas['timing'],
                                                 input_mas=mas,
                                                 result_mas=new_mas['result'])
            new_obj.save()

            context['obj'] = new_obj
            return render(request, 'result.html', context=context)
    else:
        form = AlgForm()
    return render(request, 'upload.html', context=context)
