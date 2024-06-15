# guessing_game/game/views.py

from django.shortcuts import render
import random

def Guess(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(0, 100)
        request.session['attempt_left'] = 4

    number = request.session['number']
    attempt_left = request.session['attempt_left']
    result = ''
    msg = ''

    if request.method == 'POST':
        guess = int(request.POST['num'])
        if guess == number:
            result = 'You won!'
            del request.session['number']
            del request.session['attempt_left']
        else:
            attempt_left -= 1
            request.session['attempt_left'] = attempt_left
            if attempt_left == 0:
                result = f'You lost! The number was {number}'
                del request.session['number']
                del request.session['attempt_left']
            elif guess > number:
                msg = 'Too High'
            else:
                msg = 'Too Low'

    return render(request, 'guess.html', {'attempt_left': attempt_left, 'msg': msg, 'result': result})
