from django.http import HttpResponse

def students(request):
    students = [
        {
            'id': 1,
            'name': 'Galang',
            'age': 29,
        }
    ]
    return HttpResponse(students)
