from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from my_api.models import Uuid
from my_api.api.serializers import UuidSerializer
from uuid import uuid1

@api_view(['GET', 'POST'])
def list_uuid(request):
    result = Uuid.objects.all().order_by('-time_created')
    data = {UuidSerializer(x).data['time_created'][:-1].replace('T', ' ') : UuidSerializer(x).data['uuid'].replace('-', '') for x in result}
    if request.method == 'GET':
        uuid_data = Uuid(uuid=uuid1())
        uuid_data.save()
        return Response(data)