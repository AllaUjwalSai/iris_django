from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults

def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        #Receiving data from client

        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        #unpickle model

        model = pd.read_pickle(r"C:\Users\ML\Desktop\iris-prediction-with-django\iris\prediction_model\model.pickle")

        #make prediction

        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width ]])

        classification = result[0]


        PredResults.objects.create(sepal_length=sepal_length,
                                   sepal_width=sepal_width,
                                   petal_length=petal_length,
                                   petal_width=petal_width,
                                   classification=classification)

        return JsonResponse({'result': classification,
                             'sepal_length': sepal_length,
                             'sepal_width': sepal_width,
                             'petal_length': petal_length,
                             'petal_width': petal_width},
                            safe=False)


def view_results(request):

    data = {"dataset": PredResults.objects.all()}
    return render(request, 'results.html', data)