from rest_framework import viewsets, status
from rest_framework.response import Response
from students.models import Student, University
from .serializers import StudentSerializer, UniversitySerializer


class UniversityViewSet(viewsets.ViewSet):
    """
    Gère les opérations CRUD pour les universités.
    """

    # ➕ Ajouter une université
    def create(self, request):
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Université ajoutée avec succès", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 🔍 Lister toutes les universités
    def list(self, request):
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ViewSet):
    """
    Gère les opérations CRUD pour les étudiants.
    """

    # ➕ Ajouter un étudiant
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Étudiant ajouté avec succès", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 🔍 Lister tous les étudiants
    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
