from account.views import RegisterView
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('account/',include('account.urls') ),
    path('home/',include('home.urls'))
]



# {
#   "data": {
#     "token": {
#       "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMjE2MTMxNCwiaWF0IjoxNzMyMDc0OTE0LCJqdGkiOiIyNWJkZmNjMzg3NTM0YTlmYmUxYjVhMjI2YWU5MjBkMiIsInVzZXJfaWQiOjN9.UaCvXpCPNMwj4OPMcu0No2rLvNCa74I0j_FzmONQRj0",
#       "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMDc1MjE0LCJpYXQiOjE3MzIwNzQ5MTQsImp0aSI6IjczYjQyOGFlZDVhZTRiMjFiOGU4ZTRlYzc2NzZhOTVmIiwidXNlcl9pZCI6M30.Ybc0Ww_lDcaCuIDCa2nwMXZfTe9aWgTd4tXTnTk750c"
#     }
#   },
#   "message": "login success.."
# }










# {
#   "data": {
#     "token": {
#       "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMjE2Mjc3MywiaWF0IjoxNzMyMDc2MzczLCJqdGkiOiJkZDIzNTBmNWI1M2E0ODdhOWMzOTU2MGNkNGI5MDQ5MiIsInVzZXJfaWQiOjJ9.zNewke8jAqzpSx5AuPoGaknJ_cOG7QqfXhF3jvhKB6M",
#       "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMDc2NjczLCJpYXQiOjE3MzIwNzYzNzMsImp0aSI6IjgzNTk2MzM4OGNkMDQxYmNiNWIyNzZjMDQ5NzI2MWZkIiwidXNlcl9pZCI6Mn0.MqiCG5ycWBndupLpKHv-SBJUQyQWTZAokdpemerZ7Bk"
#     }
#   },
#   "message": "login success.."

# }

