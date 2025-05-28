import os, requests
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LogInForm, UrlRequestForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import RequestMp3
from bs4 import BeautifulSoup
from google.cloud import texttospeech
from django.conf import settings
from django.core.files.base import ContentFile
from django.contrib import messages


#homepage
def home(request):

    return render(request, 'tts/index.html')


#Registering a new user

def register(request):
    form=CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
    
    context = {'form':form}

    return render(request, "tts/register.html", context)


#login exisitng users

def my_login(request):
    form = LogInForm()
    if request.method =="POST":
        form=LogInForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('')
            
    context = {'form': form}

    return render(request, 'tts/my-login.html', context=context)


#Request and MP3 file

@login_required(login_url='my-login')
def request(request):
    form = UrlRequestForm
    if request.method == "POST":
        form = UrlRequestForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user #assign user to model user field
            article_text = []
            #check to see if URL has been previously requested. Prevents calling API numerous times for same MP3 file.
            if RequestMp3.objects.filter(requested_url = form.cleaned_data['requested_url']).exists():
                if RequestMp3.objects.filter(requested_url = form.cleaned_data['requested_url'],user=request.user).exists():
                    messages.success(request, "Already here")
                    return redirect('dashboard')
                else:
                    prev_req = RequestMp3.objects.filter(requested_url = form.cleaned_data['requested_url']).first()
                    obj.title = prev_req.title
                    obj.audio_file = prev_req.audio_file
                    obj.text_file = prev_req.text_file
                    return redirect('dashboard')
            else:
                article_text = scrape_page(form.cleaned_data['requested_url']) #scrape
                obj.audio_file = access_api(article_text[1]) #Generate MP3
                obj.title = article_text[0]
                obj.save()
            return redirect('dashboard')

    context = {'form':form}
    return render(request, 'tts/request.html', context=context)


@login_required(login_url='my-login')
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('my-login')
    my_records = RequestMp3.objects.filter(user = request.user) #Be sure to assign user when creating
    
    #my_records = RequestMp3.objects.all

    context = {"records": my_records}

    return render(request, 'tts/dashboard.html', context=context)


# log out

def user_logout(request):

    auth.logout(request)

    return redirect("")

#check size of text and use appropriate api call
def access_api(text):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/worth/OneDrive/Documents/CS/webscraping/demo_service_account.json'

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    output_folder = settings.MEDIA_ROOT / "mp3_files"
    os.makedirs(output_folder, exist_ok=True)

    file_name = "output.mp3"  #Make name dynamic
    file_path = output_folder / file_name


    # The response's audio_content is binary.
    with open(file_path, 'wb') as output:
        output.write(response.audio_content)
        return ContentFile(response.audio_content, name="output.mp3")

    """
    with open(file_path, "wb") as output:
        output.write(response.audio_content)
        print('Audio content written to file "output.mp3"')"
    """

def scrape_page(url):
    response = requests.get(url)
    article_lines = []
    if response.status_code == 200:

        html_wanted = response.text
        soup = BeautifulSoup(html_wanted,'lxml')

        main_body_article = soup.find('article') 

        paragraphs = main_body_article.find_all('div', class_= 'ssrcss-uf6wea-RichTextComponentWrapper ep2nwvo0')

        for paragraph in paragraphs:
            lines = paragraph.find_all('p')
            for line in lines:
                if line.find('a') is None: #This fucking line!!!!!!
                    article_lines.append(line.get_text())
                    
                    
        article_lines = "\n".join(article_lines)#outside loop as it turns list into string object
        headline = main_body_article.find('header')
        headline_text = headline.get_text()
        return [headline_text, article_lines]

    else:
         return response.raise_for_status()
