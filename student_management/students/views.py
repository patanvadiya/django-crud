from django.shortcuts import render, redirect, get_object_or_404
from .models import Student,StudentImage
from .forms import StudentForm
from django.http import HttpResponse


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_create(request):
    # if request.method == 'POST':
    #     form = StudentForm(request.POST)
        
    #     if form.is_valid():
            
    #         form.save()
    #         return redirect('student_list')
    # else:
    #     form = StudentForm()
    if request.method == 'POST':
        # Extract data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        hobbies = request.POST.getlist('hobby')  
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')

        # Save the data to the database
        student = Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            hobby=", ".join(hobbies),  
            date_of_birth=date_of_birth,
            address=address
        )
        student.save()
        images = request.FILES.getlist('images')  
        for image in images:
            StudentImage.objects.create(student_id=str(student.id), image=image) 


        return redirect('student_list')  # Redirect to a success page or student list

    return render(request, 'students/student_form.html')

def student_edit(request, id):
    # student = get_object_or_404(Student, id=id)
    # if request.method == 'POST':
    #     form = StudentForm(request.POST, instance=student)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('student_list')
    # else:
    #     form = StudentForm(instance=student)
    # return render(request, 'students/student_edit.html', {'form': form, 'student': student})

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        # Update the student with new data
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')
        student.hobby = ", ".join(request.POST.getlist('hobby')) 
        student.date_of_birth = request.POST.get('date_of_birth')
        student.address = request.POST.get('address')
        student.save()

        return redirect('student_list')

    hobbies = student.hobby.split(", ") if student.hobby else []

    return render(request, 'students/student_edit.html', {
        'student': student,
        'hobbies': hobbies,
    })

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})

def student_image(request,id): 
    images = StudentImage.objects.filter(student_id=id)
    
    # return HttpResponse(images.id)
    

    return render(request, 'students/student_images.html', {'images': images})
