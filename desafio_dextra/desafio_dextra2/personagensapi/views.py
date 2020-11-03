from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.http import JsonResponse

from .models import *
from .pagination import *
from .serializers import *


class PersonagensList(APIView):
    def get(self, request):
        try:
            lista_personagens = Personagem.objects.all()
            paginator = PaginacaoPersonagem()
            result_page = paginator.paginate_queryset(lista_personagens, request)
            serializer = PersonagensSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = PersonagensSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PersonagensDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero"},
                                     status=status.HTTP_400_BAD_REQUEST)
            personagem = Personagem.objects.get(pk=pk)
            serializer = PersonagensSerializer(personagem)
            return Response(serializer.data)
        except Personagem.DoesNotExist:
            return JsonResponse({'mensagem': "O personagem não existe"},
                                     status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "O ocorreu um erro no servidor"},
                                     status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero"},
                                    status=status.HTTP_400_BAD_REQUEST)
            personagem = Personagem.objects.get(pk=pk)
            serializer = PersonagensSerializer(personagem, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Personagem.DoesNotExist:
            return JsonResponse({'mensagem': "A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)

        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            personagem = Personagem.objects.get(pk=pk)
            personagem.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Personagem.DoesNotExist:
            return JsonResponse({'mensagem': "A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)