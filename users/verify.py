# import requests
#from .models import NewUser

# class GoogleAccessTokenAuthentication(ModelBackend):
#     def authenticate_with_google_token(self, user_info):
#         print("in authenticate_with_google_token")
#         try:
#             # Verify the access token with Google and get user information
#             # Replace this with your logic to verify the Google access token

#             # Assuming you get user_info and email from Google response
            

#             # Check if a user with the provided email exists in your system
#             user = NewUser.objects.filter(email=user_info["email"]).first()
#             print(
#                 "user in authenticate_with_google_token",
#                 user
#             )

#             if user:
#                 return user
#             else:
#                 print("creating user")
#                 # Create a new user using user_info if not exists
#                 user = NewUser.objects.create_user(email=user_info["email"], )
#                 user.save()
#                 print("user saved")
#                 return user
#         except Exception as e:
#             return None

#     def authenticate(self, request, access_token=None):
#         if access_token:
#             user = self.authenticate_with_google_token(access_token)
#             return user

#         return None


# def verify_google_access_token(access_token):
#     # URL for Google's OAuth 2.0 userinfo endpoint
#     userinfo_url = "https://www.googleapis.com/oauth2/v3/userinfo"

#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }

#     response = requests.get(userinfo_url, headers=headers)

#     if response.status_code == 200:
#         user_info = response.json()
#         return user_info
#     else:
#         return None

# # Example usage
# access_token = "ya29.a0AfB_byCnspzZOJpep1Uoo822RcF80Qdha0_tRa-ZrdF2IHYHxZPIShsN8sjMrcJeztrTfpIKTceEpbSDkBoUV2Uhufv_CSd1U4siqjXJo2LwLMkyYkDOmDFCTjilCAhm5gYxrF3BoUb8nSy62VFGo_M0pk_-Q1K8d1faZgaCgYKAXoSARESFQHsvYls4ySty0lhlFNNZT5JUH98IA0173"
# user_info = verify_google_access_token(access_token)

# if user_info:
#     print("User information:", user_info)
#     #GoogleAccessTokenAuthentication.authenticate_with_google_token(user_info)
# else:
#     print("Access token verification failed")





