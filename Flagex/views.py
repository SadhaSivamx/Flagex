from django.shortcuts import render,redirect
from django.http import HttpResponse
from json import dumps
from django.shortcuts import redirect
from Flagex.models import scoreboard
# Create your views here.
def Save(request,name,score):
    g=scoreboard()
    g.na=name
    g.sc=score
    g.save()
    print('Saved sucessfully')
    return redirect('/End')
def Main(request):
    if request.POST:
        username=request.POST['name']
        request.session['user'] = username
        return redirect('/Game')
    else:
        return render(request,'Main.html')
def Game(request):
    if request.session.has_key('user'):
        import random
        Flags=['Abkhazia', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua_and_Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia_and_Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina_Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape_Verde', 'Chad', 'Chile', 'Colombia', 'Costa_Rica', 'Croatia', 'Cuba', 'Cyprus', 'Denmark', 'Djibouti', 'Dominica', 'East_Timor', 'Ecuador', 'Egypt', 'El_Salvador', 'Equatorial_Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea-Bissau', 'Guinea', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory_Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Nagorno-Karabakh', 'Namibia', 'Nauru', 'Nepal', 'New_Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North_Korea', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua_New_Guinea', 'Paraguay', 'Peru', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint_Kitts_and_Nevis', 'Saint_Lucia', 'Saint_Vincent_and_the_Grenadines', 'Samoa', 'San_Marino', 'Sao_Tome_and_Principe', 'Saudi_Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra_Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'Somaliland', 'South_Africa', 'South_Korea', 'South_Ossetia', 'South_Sudan', 'Spain', 'Sri_Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland_(Pantone)', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'the_Bahamas', 'the_Central_African_Republic', 'the_Comoros', 'the_Cook_Islands', 'the_Czech_Republic', 'the_Democratic_Republic_of_the_Congo', 'the_Dominican_Republic', 'the_Federated_States_of_Micronesia', 'The_Gambia', 'the_Marshall_Islands', 'the_Netherlands', "the_People's_Republic_of_China", 'the_Philippines', 'the_Republic_of_China', 'the_Republic_of_the_Congo', 'the_Sahrawi_Arab_Democratic_Republic', 'the_Solomon_Islands', 'the_Turkish_Republic_of_Northern_Cyprus', 'the_United_Arab_Emirates', 'the_United_Kingdom', 'the_United_States', 'the_Vatican_City', 'Togo', 'Tonga', 'Transnistria', 'Trinidad_and_Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
        Q=[]
        A=[]
        for x in range(5):
            Questions=[]
            Answer=''
            while len(Questions)!=3:
                op=random.choice(Flags)
                if op not in Questions:
                    Questions.append(op)
            Answer=random.choice(Questions)
            Q.append(Questions)
            A.append(Answer)
        Q=dumps(Q)
        A=dumps(A)
        name=dumps(request.session['user'])
        return render(request,'Game.html',{'Questions':Q,'Answers':A,'name':name})
    else:
        return redirect('/')
def End(request):
    return render(request,'End.html')