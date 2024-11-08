from django.http import JsonResponse


def custom_page_not_found(request, exception):
    return JsonResponse({"error": "Page not found"}, status=404)
