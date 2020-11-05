from django.dispatch import receiver
from .models import UserLoginActivity
from django.contrib.auth import authenticate, user_logged_in

@receiver(user_logged_in)
def log_user_logged_in_success(sender, user, **kwargs):
    print('Received')
    try:
        #user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        user_login_activity_log = UserLoginActivity(
                                                    #login_IP=get_client_ip(request),
                                                    login_username=user.username,
                                                    #user_agent_info=user_agent_info,
                                                    status=UserLoginActivity.SUCCESS)
        user_login_activity_log.save()
    except Exception as e:
        # log the error
        error_log.error("log_user_logged_in request: %s, error: %s" % (request, e))

