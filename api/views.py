from django.http import JsonResponse

def studentsView(request):
    students = {
        'id': 1,
        'name': 'API',
        'age': 29,
    }
    return JsonResponse(students)
