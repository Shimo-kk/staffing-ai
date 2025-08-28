from itsdangerous import URLSafeSerializer, URLSafeTimedSerializer
from app.internal.share.environment.environment import Environment

session_serializer = URLSafeSerializer(Environment.SECRET_KEY)
csrf_serializer = URLSafeTimedSerializer(Environment.SECRET_KEY, salt="csrf-token")
