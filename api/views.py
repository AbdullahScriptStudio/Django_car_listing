from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_view(request):
    data = {'hello':'world', 'num': 12}
    return Response(data)