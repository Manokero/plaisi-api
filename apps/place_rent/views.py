from rest_framework import viewsets
from .models import HouseImage, HouseRent
from .seralizers import HouseImageSerializer, HouseRentSerializer
# from rest_framework.views import ViewSet
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class HouseRentView(viewsets.ModelViewSet):
    queryset = HouseRent.objects.all()
    serializer_class = HouseRentSerializer

class HouseImageView(viewsets.ModelViewSet):
    queryset = HouseImage.objects.all()
    serializer_class = HouseImageSerializer

# class ImageView(viewsets.ModelViewSet):
#     parser_classes = (MultiPartParser, FormParser)
#     queryset = HouseImage.objects.all()
#     serializer_class = HouseImageSerializer

#     def get(self, request):
#         # all_images = HouseImage.objects.all()
#         serializer = HouseImageSerializer(queryset, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     def post(self, request, *args, **kwargs):
#         property_id = request.data['property_place']

#         # converts querydict to original dict
#         images = dict((request.data).lists())['image']
#         flag = 1
#         arr = []
#         for img_name in images:
#             modified_data = modify_input_for_multiple_files(property_id,
#                                                             img_name)
#             file_serializer = HouseImageSerializer(data=modified_data)
#             if file_serializer.is_valid():
#                 file_serializer.save()
#                 arr.append(file_serializer.data)
#             else:
#                 flag = 0

#         if flag == 1:
#             return Response(arr, status=status.HTTP_201_CREATED)
#         else:
#             return Response(arr, status=status.HTTP_400_BAD_REQUEST)
