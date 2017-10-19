import fb_auth_token\

fb_username = "johnmarshtit123@gmail.com"
fb_password = "1234billi"
fb_access_token = fb_auth_token.get_fb_access_token(fb_username, fb_password)
fb_user_id = fb_auth_token.get_fb_id(fb_access_token)
host = 'https://api.gotinder.com'
print(fb_access_token);
print(fb_user_id);
file_object  = open("config.py", "w")
file_object.write("host = \"https://api.gotinder.com\"\n");
file_object.write("fb_access_token = \"" + str(fb_access_token) + "\"\n");
file_object.write("fb_user_id = \"" + str(fb_user_id) + "\"");
# Your real config file should simply be named "config.py"
# Just insert your fb_username and fb_password in string format
# and the fb_auth_token.py module will do the rest!
