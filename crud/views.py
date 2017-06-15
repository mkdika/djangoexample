from django.shortcuts import render
from django.http.response import HttpResponse
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from django.urls import reverse
from crud.forms import NewPerson
from crud.models import Person



def index(request):
    # person_list = Person.objects.order_by('first_name') # find all Person order by its first_name
    person_list = Person.objects.raw('SELECT * FROM tb_person ORDER BY first_name')  # use native/raw queries
    response_dict = {
        'person_list': person_list,
    }
    return render(request, 'crud/index.html', context=response_dict)


def deletePerson(request, uid):
    p = Person.objects.get(pk=uid)
    p.delete()
    print('Deleted UID=' + uid)
    return redirect(reverse("index"))


def editPerson(request, uid):
    p = Person.objects.get(pk=uid)
    if request.method == 'GET':
        form = NewPerson(initial=model_to_dict(p))
        return render(request, 'crud/personform.html', {'form': form})
    elif request.method == 'POST':
        # Check to see form is valid
        form = NewPerson(request.POST, instance=p)
        if form.is_valid():
            print('Form Validation Success. Print to console.')
            print("UID: " + form.cleaned_data['uid'])
            print("First Name: " + form.cleaned_data['first_name'])
            print("Lastname Name: " + form.cleaned_data['last_name'])
            print("Is Male: " + str(form.cleaned_data['is_male']))
            print("Birth Date: " + str(form.cleaned_data['birth_date']))
            print("Birth Time: " + str(form.cleaned_data['birth_time']))
            print("Email: " + form.cleaned_data['email'])
            print("Address: " + form.cleaned_data['address'])
            print("Height: " + str(form.cleaned_data['first_name']))
            print("Weight: " + str(form.cleaned_data['first_name']))
            print("Last Education: " + form.cleaned_data['last_education'])
            if form.cleaned_data['first_name'] is None:
                print("Photo is Null")
            else:
                print("Photo is NOT Null")

            print("Saving...")
            form.save(commit=True)
            print('Saved!')
            return redirect(reverse("index"))
        else:
            print(form.errors)
            return HttpResponse('invalid')


def addNewPerson(request):
    # Generate form base on View
    form = NewPerson()

    # Check to see if we get a POST back.
    if request.method == 'POST':
        # In which case we pass in that request
        form = NewPerson(request.POST)

        # Check to see form is valid
        if form.is_valid():
            print('Form Validation Success. Print to console.')
            print("UID: " + form.cleaned_data['uid'])
            print("First Name: " + form.cleaned_data['first_name'])
            print("Lastname Name: " + form.cleaned_data['last_name'])
            print("Is Male: " + str(form.cleaned_data['is_male']))
            print("Birth Date: " + str(form.cleaned_data['birth_date']))
            print("Birth Time: " + str(form.cleaned_data['birth_time']))
            print("Email: " + form.cleaned_data['email'])
            print("Address: " + form.cleaned_data['address'])
            print("Height: " + str(form.cleaned_data['first_name']))
            print("Weight: " + str(form.cleaned_data['first_name']))
            print("Last Education: " + form.cleaned_data['last_education'])
            if form.cleaned_data['first_name'] is None:
                print("Photo is Null")
            else:
                print("Photo is NOT Null")

            print("Saving...")
            form.save(commit=True)
            print('Saved!')
            return redirect(reverse("index"))
        else:
            print(form.errors)
            return HttpResponse('invalid')
    return render(request, 'crud/personform.html', {'form': form})
