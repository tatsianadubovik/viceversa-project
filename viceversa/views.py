from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext'] # Получение текста от пользователей из поисковой строки
	words = user_text.split() # разбивает текст на слова
	number_of_words = len(words) # подсчитывает слова
	reversed_text = user_text[::-1] # Получение текста в обратном порядке
	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'number_of_words':number_of_words})