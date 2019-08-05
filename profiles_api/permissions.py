from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is editing their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allows users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Checkuser is trying to update their own status"""
        """alllows anyusers to use safe methods"""
        """only allows unsafe methods where user id == reqest id"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
