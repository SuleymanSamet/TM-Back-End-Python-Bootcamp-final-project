from django.shortcuts import redirect, render
from .forms import ContactForm
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message', '').lower()
        response = chat(message)
        return JsonResponse({'response': response})
    else:
        return render(request, 'chatbot.html')


def chat(message):
    merhabalar = ['merhaba', 'selam', 'naber', 'hey', 'günaydın']
    markalar = ['bmw', 'mercedes', 'audi', 'volkswagen', 'toyota']
    modeller = ['x1', 'a180', 'a3', 'golf', 'corolla']
    yakitlar = ['benzin', 'dizel', 'hibrit']
    arac_kiralama_sorulari = ['araç kiralama nasıl yapılır', 'araç kiralamak istiyorum', 'araç kiralama fiyatları',
                              'hangi araçları kiralayabilirim', 'araç teslimatı nasıl yapılıyor']
    arac_kiralama_cevaplari = [
        'Araç kiralamak için web sitemizi ziyaret edebilir veya telefonla rezervasyon yapabilirsiniz.',
        'Tabii, hangi tarihler arasında kiralamak istiyorsunuz?',
        'Fiyatlarımız web sitemizde mevcuttur, inceleyebilirsiniz.',
        'Flota eklediğimiz araçların listesi web sitemizde mevcut, inceleyebilirsiniz.',
        'Araç teslimatı konumunuza veya belirlediğiniz bir noktaya yapılabilir. Detaylar için bizimle iletişime geçebilirsiniz.']
    if message.lower() in arac_kiralama_sorulari:
        return random.choice(arac_kiralama_cevaplari)
    if message in markalar:
        return f"{message} markalı araçlar için şu anda uygun fiyatlarımız bulunmaktadır."
    elif message in modeller:
        return f"{message} model araçlarımız ile ilgili bilgi almak için lütfen iletişime geçiniz."
    elif message in yakitlar:
        return f"{message} yakıt türü ile çalışan araçlarımız bulunmaktadır."
    else:
        return "Ne hakkında bilgi almak istediğinizi anlayamadım. Lütfen tekrar deneyin."




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, "contact.html", context)


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def client(request):
    return render(request, "client.html")


def gallery(request):
    return render(request, "gallery.html")


def services(request):
    return render(request, "services.html")

