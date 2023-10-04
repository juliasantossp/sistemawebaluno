# study_app/views.py
@login_required
def calculate_grade(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    total_grade = 0
    for task in tasks:
        # Implemente a lógica para calcular a nota de cada tarefa
        # e adicione à total_grade
        # Você também pode adicionar notas de outras fontes, como provas e trabalhos
    np = total_grade * 0.2 + overall_grade * 0.8
    if np >= 7:
        status = "Aprovado"
    elif np >= 3:
        status = "Final"
    else:
        status = "Reprovado"
    return render(request, 'calculate_grade.html', {'np': np, 'status': status})
