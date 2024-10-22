from rest_framework.permissions import BasePermission

class IsOrganizer(BasePermission):
    def has_permission(self, request,view):
        if request.user:
            if  request.user.is_authenticated and request.user.user_profile.type=='ORG':
                return True
            
        return False
    
class IsVisitor(BasePermission):
    def has_permission(self, request,view):
        if request.user:
            if  request.user.is_authenticated and request.user.user_profile.type=='VI':
                return True
            
        return False
    