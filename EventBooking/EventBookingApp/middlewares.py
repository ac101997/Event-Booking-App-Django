from django.shortcuts import HttpResponse


class MyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print("This is before view in call method")
        response =self.get_response(request)
        print("This is after view in call method")
        return response

    def process_request(self,request):
        print("this is process request")
        return None

    def process_view(request):
        print("this is process view")
        return None

    def process_response(self, request,response):
        print("this is process response")
        return response