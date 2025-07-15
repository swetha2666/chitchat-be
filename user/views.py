from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import User
from .userSerializer import UserSerializer , LoginSerializer
from rest_framework.response import Response
import jwt
from datetime import datetime , timedelta

#FBV
@api_view(["POST"])
def login(request):
    try:
        serializerData = LoginSerializer(request.data)
        clientUserData = serializerData.data
        realUserData = User.objects.get(userName = request.data["userName"])
        realUserData = UserSerializer(realUserData).data

        payload = {
            "userId" : clientUserData["userName"],
            "college" : "BVC",
            'exp': datetime.utcnow() + timedelta(hours=2),
            'iat': datetime.utcnow(),
        }

        token = jwt.encode(payload , "secrect-key")

        if realUserData["password"] == clientUserData["password"]:
            print(clientUserData)
            return Response(data={
                "msg" : "Success",
                "token" : token,
                "login" : 1,
                "code" : "100"
            })
        else:
            return Response({
                "msg" : "Login Failed Ra",
                "login": 0
            })
    except Exception as err:
        return Response({"msg" : "Error Occured in the try" , "error" : err})

@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"code" : 1 , "msg" : "Account Creation Successfull" , "userData" : serializer.data })
    else:
        return Response({"code" : 0 , "msg" : "failed" , "err" :serializer.errors})
    


@api_view(["POST"])  
def dummy(request):
    id_card = request.headers["Authorization"]
    print(id_card)
    id_card = id_card.split(" ")[1]

    user_data = jwt.decode(id_card , "secrect-key" , algorithms="HS256")
    
    return Response(
        {"msg" : "id card scanned" , "idcard" : id_card , "userData" : user_data}
    )