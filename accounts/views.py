from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from .serializers import UserSerializer,PasswordCheckSerializer, SubSerializer, ChangePasswordSerializer
from .utils import send_verification_email
import uuid

User = get_user_model() # 필수 지우면 큰일남

class SignupAPIView(APIView): # 회원가입
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.verification_token = str(uuid.uuid4())
            user.is_active = False
            user.save()
            send_verification_email(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailAPIView(APIView):
    def get(self, request, token):
        user = get_object_or_404(User, verification_token=token)
        user.verification_token = ''
        user.save()
        if user.verification_token == '':
            user.is_active = True
            user.save()
        return HttpResponse('이메일 인증이 완료되었습니다. 이제 로그인할 수 있습니다.')


class LogoutAPIView(APIView): # 로그아웃
    def post(self, request):
        refresh = request.data.get("refresh")
        if refresh is None:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = RefreshToken(refresh)
            token.blacklist()
            return Response({'message:로그아웃 되셨습니다'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DeleteAPIView(APIView): # 회원탈퇴
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        serializer = PasswordCheckSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            user = authenticate(username=request.user.username, password=password)
            if user is not None:
                user.soft_delete()
                return Response({"message":"탈퇴 완료하였습니다"},status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Mypage(ListAPIView): # 마이 페이지
    permission_classes = [IsAuthenticated]

    def get_queryset(self): # 내가 쓴 글 역참조 로직
        return User.objects.none()

    def get(self, request, username):
        my_page = get_object_or_404(User, username=username)
        if my_page == request.user:
            serializer = UserSerializer(my_page)
            sub_serializer = SubSerializer(my_page)
            return Response({'내 정보':serializer.data, '구독중인 사람':sub_serializer.data['subscribings'], '내가 작성한 글':sub_serializer.data['articles'] },status=200)
        return Response({"message": "다시 시도"}, status=400)
    

class SubscribeView(APIView):  # 구독 기능
    permission_classes = [IsAuthenticated]
    def post(self, request, username):
        # 구독 대상 사용자 조회
        user = get_object_or_404(User, username=username)
        me = request.user
        if me in user.subscribes.all(): # 내가 대상 사용자를 이미 구독하고 있는지 확인
            user.subscribes.remove(me)
            return Response("구독취소를 했습니다.", status=status.HTTP_200_OK)
        else:
            if username != me.username:
                user.subscribes.add(me)
                return Response("구독했습니다.", status=status.HTTP_200_OK)
            else:
                return Response("자신의 계정은 구독할 수 없습니다.", status=status.HTTP_200_OK)
        

# password 변경
class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        # print(serializer)  # 디버깅용

        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                return Response({'message': '비밀번호를 성공적으로 변경하였습니다.'}, status=200)
            return Response({'error': '비밀번호가 같습니다 새 비밀번호를 입력해주세요'}, status=400)
        return Response(serializer.errors, status=400)


class PasswordResetRequestView(APIView): # password 재설정
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_url = f"{request.scheme}://{request.get_host()}/reset/{uid}/{token}/"
            # message = f"안녕하세요 {user.username}님,\n\n비밀번호 재설정을 위해 아래 링크를 클릭하세요:\n{reset_url}\n\n감사합니다."
            message = f'uid: {uid}  |  token: {token}'
            send_mail(
                'Password Reset Request',
                message,
                'noreply@gmail.com',
                [user.email],
                fail_silently=False,
            )
        return Response({"message": "해당 이메일을 사용하는 계정이 있는 경우, 비밀번호 재설정 메일을 전송합니다."}, status=status.HTTP_200_OK)
    

class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            new_password = request.data.get('new_password')
            user.set_password(new_password)
            user.save()
            return Response({"message": "비밀번호가 변경되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid token or user ID."}, status=status.HTTP_400_BAD_REQUEST)