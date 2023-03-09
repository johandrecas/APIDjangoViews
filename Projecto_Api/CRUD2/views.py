from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Persona2
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.
class CRUD2(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
 

        if id > 0:

            found_person = list(Persona2.objects.filter(id=id).values())

            if len(found_person) > 0:
                data={'message  ':'Found','found_person':found_person}

                return JsonResponse(data)


            else:
                data={'message':'it happen a mistake...your id is empty'}
                return JsonResponse(data)

        else:

            all_peson = list(Persona2.objects.values())
            print('El id que me llego es ',id)

            if len(all_peson) > 0:
                data={'message':'sucessfull....','all_person':all_peson}
            
            else:
                data={'message':'it happen a mistake...'}

            return JsonResponse(data)



                




    
    def post(self,request):

        #ahora verifiquemos si llegan datos 
        # y los convertimos a json para poder extraer sus valores 
        jd = json.loads(request.body)
        print('Convirtiendo a Diccionario   ',jd)

        new_person = Persona2.objects.create(nombre=jd['nombre'],edad=jd['edad'],profesion=jd['profesion'])
       

        data={'message':'created success ','new_person':jd}

        return JsonResponse(data)


    def put(request):
        data={'messaege':'conexion Exitosa a el metodo put'}
        return JsonResponse(data)



    


