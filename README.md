# Recommandation_systems
this repository contains my work on a specifique type of recommandation system : content_based

it contains a jupyter notebbok of my work
i also create api using djangorestframework

the main idea here is to compute cosine_similarity between the title provide by the user and the description of the differents courses present in our database then return the courses having the greatest similarities

to use this , you need to install the requirements by using pip install -r requirements.txt in your terminal.

It's generally better to use a virtual enviroment.

if you want to use a virtual enviroment you must first create it by using the command python -m venv your_environment_name and activate it using
your_enviromment_name\Scripts\activate if you are on windows or your_environment_name\bin\activate on linux

for instance if i want to create and use a virtual environment myenv on windows, i should excute this in my terminal
python -m venv myenv
myenv\Scripts\activate

then run pip install -r requirements.txt in your terminal and it will download necessary packages in your virtual environnement

