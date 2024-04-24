from django.urls import path
from stdapp.views import *
urlpatterns=[
        path('university/list',university_list,name='university_list'),
        path('batch/list',batch_list,name='batch_list'),
        path('student/list',student_list,name='student_list'),
        path('batch/add',add_batch,name='add_batch'),
        path('student/add',add_student,name='add_student'),
        path('batch/<int:batch_id>/view',batch_view,name='batch_view'),
        path('student/<int:student_id>/view',student_view,name='student_view'),
        path('batch/<int:batch_id>/delete',batch_delete,name='batch_delete'),
        path('student/<int:student_id>/delete',student_delete,name='student_delete'),
        path('batch/<int:batch_id>/edit',batch_edit,name='batch_edit'),
        path('student/<int:student_id>/edit',student_edit,name='student_edit'),
        path('batch/<int:batch_id>/update',batch_update,name='batch_update'),
        path('student/<int:student_id>/update',student_update,name='student_update'),
        path('batch/<int:batch_id>/students',BatchWithProduct.as_view(),name='batch-with-students'),
        path('university/<int:university_id>/',UniversityViews.as_view(),name='university-view'),
]