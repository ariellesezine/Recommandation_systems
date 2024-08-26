from django.shortcuts import render
from rest_framework.views import APIView
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np
import pickle
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent
#print(BASE_DIR)
vectorizer = os.path.join(BASE_DIR, 'templates/assets/vectorizer_fited.pkl')
with open(vectorizer, 'rb') as file:
    loaded_vectorizer = pickle.load(file)

description = os.path.join(BASE_DIR, 'templates/assets/description_fit_transformed.pkl')
with open(description,'rb') as file:
    loaded_description = pickle.load(file)

index_and_coursename = os.path.join(BASE_DIR, 'templates/assets/index_course_name.json')    
with open(index_and_coursename, 'rb') as file:
    loaded_dictionary = json.load(file)

def recommandation_deploy(title):
    title=title.split(" ")
    title=loaded_vectorizer.transform(title)
    similarities = cosine_similarity(title,loaded_description)
    indices_similaires = np.argsort(similarities[0])[::-1]
    indices_similaires=indices_similaires[:10]
    indices_similaires=[str(i) for i in indices_similaires ]
    # Obtenir les titres des livres recommandés
    cours_recommandes = [loaded_dictionary[i] for i in indices_similaires]
    #livres_recommandes = [loaded_dictionary[str(2605)] ]
    #print("Livres recommandés:", livres_recommandes)
    return cours_recommandes


class Apiviews(APIView):

    def post(self, request, *args, **kwargs):
        title=request.data.get('coursename')
        print("----------------------------------------------------------")
        cours=recommandation_deploy(title)
        context = {
        'cours':cours
        }
        values=[cour for cour in cours]
        return render(request, 'results.html', context)#={"recomand":cours})

    def get(self,request):
        return render(request,'home.html')
