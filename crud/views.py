from django.shortcuts import render
from django.http import HttpResponse
from crud.forms import NewPerson
from crud.models import Person

def index(request):
    person_list = Person.objects.order_by('first_name')
    response_dict = {
        'person_list': person_list,
    }
    return render(request, 'crud/index.html', context=response_dict)


def addNewPerson(request):
    # return HttpResponse("Hello World!")
    form = NewPerson()

    # Check to see if we get a POST back.
    if request.method == 'POST':
        # In which case we pass in that request
        form = NewPerson(request.POST)

        # Check to see form is valid
        if form.is_valid():
            # print('Form Validation Success. Print to console.')
            # print("Name: " + form.cleaned_data['name'])
            # print("Is Male: " + str(form.cleaned_data['is_male']))
            # print("Birthdate: " + str(form.cleaned_data['birthdate']))
            # print("Height: " + str(form.cleaned_data['height']))
            # print("Weight: " + str(form.cleaned_data['weight']))
            # print("Email: " + form.cleaned_data['email'])
            # print("address: " + form.cleaned_data['address'])
            # print("Saving...")
            form.save(commit=True)
            print('saved')
            return addNewPerson(request)
        else:
            print("ERROR FORM INVALID!")
    return render(request, 'crud/personform.html', {'form': form})
