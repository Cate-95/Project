from django.shortcuts import render
from .models import CalorieData

def calculate_calories(request):
    if request.method == 'POST':
        date = request.POST['date']
        calories_consumed = int(request.POST['calories_consumed'])
        goal_calories = int(request.POST['goal_calories'])

        calorie_data = CalorieData(date=date, calories_consumed=calories_consumed, goal_calories=goal_calories)
        calorie_data.save()

        context = {'calorie_data': calorie_data}
        return render(request, 'calculator/calorie_calculator.html', context)
    else:
        return render(request, 'calculator/calorie_calculator.html')
