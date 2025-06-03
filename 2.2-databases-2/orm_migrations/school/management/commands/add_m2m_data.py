from django.core.management.base import BaseCommand
from school.models import Student,Teacher

#команда для добавления учителя для ученика в базу данных
class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        Student.objects.get(name='Бабаева Вера Ивановна').teachers.add(Teacher.objects.get(name='Карякин Владимир Владимирович'))
        Student.objects.get(name='Погорелов Денис Витальевич').teachers.add(Teacher.objects.get(name='Наумкин Анатолий Андреевич'))
        Student.objects.get(name='Погорелов Денис Витальевич').teachers.add(Teacher.objects.get(name='Филатова Елена Александровна'))
        Student.objects.get(name='Осипов Иван Вячеславович').teachers.add(Teacher.objects.get(name='Карякин Владимир Владимирович'))
        Student.objects.get(name='Осипов Иван Вячеславович').teachers.add(Teacher.objects.get(name='Наумкин Анатолий Андреевич'))
        Student.objects.get(name='Осипов Иван Вячеславович').teachers.add(Teacher.objects.get(name='Филатова Елена Александровна'))