from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
	message = "hahahaha You dont have access"
	def has_object_permission(self, request, view, obj):
		if (request.user == obj.author) or (request.user.is_staff):
			return True
		else:
			return False