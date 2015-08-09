from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Student, Mark

def create_student(**args):
    return Student.objects.create(**args)

class StudentMethodTests(TestCase):
    ''' Unit tests. '''
    
    def test_fullname_generation(self):
        ''' fullname should return [firstname lastname]'''
        student = create_student(firstname="Foo", lastname="Lano")
        self.assertEqual(student.fullname(), "Foo Lano")
        
class StudentIndexTests(TestCase):
    ''' Functional tests : index.html '''
    
    def test_students_list(self):
        create_student(firstname="Foo", lastname="Lano")
        response = self.client.get(reverse('students:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Foo Lano")
        
class StudentShowTests(TestCase):
    ''' Functional tests : show.html '''
    
    def test_student_details(self):
        student = create_student(firstname="Foo", lastname="Lano")
        response = self.client.get(reverse('students:show', args=(student.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Foo Lano")
        