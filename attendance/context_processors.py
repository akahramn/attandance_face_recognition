def nav_username(request):
    return {
        "USERNAME": request.session.get('username'),
        "INSTRUCTOR_ID": request.session.get('instructor_id'),
    }