from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from app.models import Student, StudentCard
from app.forms import UpdateStudentForm, UpdateCardForm, CreateCardForm

class StudentList(View):
    def get(self, request):
        tutor_id = request.user.id
        students = Student.objects.filter(tutor_id=tutor_id).order_by('first_name')
        context = {"students": students}
        return render(request, "student_list.html", context)

class StudentCardView(View):
    def get(self, request, student_id):
        tutor_id = request.user.id
        student = Student.objects.get(id=student_id, tutor_id=tutor_id)
        student_cards = StudentCard.objects.filter(student_id=student_id, tutor_id=tutor_id)

        card_data = []
        for card in student_cards:
            days = [day.name for day in card.day.all()]
            card_data.append({"lesson": card, "days": days})

        context = {"student": student,
                   "card_data": card_data}

        return render(request, "student_card.html", context)

class UpdateStudentCard(View):
    def get(self, request, student_id, student_card_id):
        student = get_object_or_404(Student, id=student_id)
        student_card = get_object_or_404(StudentCard, student_id=student_id, id=student_card_id)

        student_form = UpdateStudentForm(instance=student)
        card_form = UpdateCardForm(instance=student_card)

        context = {
                    "student_form": student_form,
                    "card_form": card_form,
                    "student": student,
                    "student_card": student_card,
            }

        return render(request, "edit_student_card.html", context)

    def post(self, request, student_id, student_card_id):
        student = get_object_or_404(Student, id=student_id)
        student_card = get_object_or_404(StudentCard, student__id=student_id, id=student_card_id)

        student_form = UpdateStudentForm(request.POST, instance=student)
        card_form = UpdateCardForm(request.POST, instance=student_card)

        if student_form.is_valid() and card_form.is_valid():
            student_form.save()
            card_form.save()
            return redirect("app:student_card", student_id=student_id)

        else:
            context = {
                    "student_form": student_form,
                    "card_form": card_form,
                    "student": student,
            }
            return render(request, "edit_student_card", context)

class CreateStudent(View):
    def get(self, request):
        create_student_form = UpdateStudentForm()
        create_card_form = CreateCardForm()

        context = {
            "create_student_form": create_student_form,
            "create_card_form": create_card_form,
        }

        return render(request, "create_student.html", context)

    def post(self,request):
        pass