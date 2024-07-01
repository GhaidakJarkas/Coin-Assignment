from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from rest_framework import status

from coins.api.serializers import CoinSerializer
from coins.models import Coin


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def coins(request):
    if request.method == 'POST':
        print(request.data)
        serializer = CoinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Coin added successfully"}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    coins = Coin.objects.all()
    serializer = CoinSerializer(coins, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)