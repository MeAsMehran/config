
"""
DRF Permission Notes (for Future Reference)


===>> has_permission(request, view)
Called before accessing any object.
Controls general access to the view (e.g. list, create).
Use for checks like IsAuthenticated, IsAdminUser, etc.



===>> has_object_permission(request, view, obj)
Called after the object is retrieved.
Controls access to a specific object (e.g. detail, update, delete).
Use to restrict actions to owners or based on object fields.


🧠 Tip:
Always return True/False based on the logic you need.
Both methods must pass for access to be granted.
"""


from rest_framework.permissions import BasePermission


# We copied the IsAdminUser from the main permission file in restframe work(I copied from .venv/lib/restframework folder) and modify it here to IsSuperUser
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)



# These are the safe methods which don't change data
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')   # This SAFE_METHOD is in root permissions file and could import above in the following from rest_framework.permissions import BasePermission , SAFE_METHOD

# We copied the IsAuthenticatedOrReadOnly from the main permission file in restframe work(I copied from .venv/lib/restframework folder) and modify it here to IsStaffOrReadOnly
# We can now add this class to setting general permissions!!
class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and            # this checks if the user is authenticated or not
            request.user.is_staff       # we change is_authenticated to is_staff
        )

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            # Get access to superuser
            request.user.is_authenticated and request.user.is_superuser or
            # Get access to author of object
            request.user.is_authenticated and obj.author == request.user
        )

class IsSuperUserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view, ):
        # if request.method in SAFE_METHODS and \
        #         request.user.is_authenticated and \
        #         request.user.is_staff:
        #     return True

        return bool(
            # Get access to authors read only
            request.method in SAFE_METHODS and
            request.user and
            request.user.is_staff or
            # Get access to superuser full
            request.user and
            request.user.is_superuser
        )