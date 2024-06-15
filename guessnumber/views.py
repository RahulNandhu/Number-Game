# guessing_game/game/views.py

from django.shortcuts import render
import random

def Guess(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(2, 100)
        request.session['attempt_left'] = 4

    number = request.session['number']
    attempt_left = request.session['attempt_left']
    result = ''
    msg = ''
    div=10
    for i in range(10,1,-1):
        if number%i==0:
            div=i
            qstn = f'X is a multiply of {div}'
            break
        else:
            qstn=f'X is a prime number'


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
            elif guess >number and guess - number < 2*(div):
                msg = 'not that High , but you almost there'
            elif guess > number:
                msg= 'Too high'
            elif guess < number and number -guess < 2*(div):
                msg = 'not that low , but you almost there'
            else:
                msg = 'Too Low'

    return render(request, 'guess.html', {'attempt_left': attempt_left, 'msg': msg, 'result': result,'qstn':qstn})
