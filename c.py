from django.http import HttpResponse

from .b import Ask

def detail(request, ask_id):
    return HttpResponse("What is your MBTI %s." % ask_id)

def results(request, ask_id):
    return HttpResponse("infp %s." % ask_id)
    return HttpResponse("enfp %s." % ask_id)
    return HttpResponse("esfj %s." % ask_id)
    return HttpResponse("isfj %s." % ask_id)
    return HttpResponse("isfp %s." % ask_id)
    return HttpResponse("intp %s." % ask_id)
    return HttpResponse("infj %s." % ask_id)
    return HttpResponse("enfj %s." % ask_id)
    return HttpResponse("entp %s." % ask_id)
    return HttpResponse("estj %s." % ask_id)
    return HttpResponse("istj %s." % ask_id)
    return HttpResponse("intj %s." % ask_id)
    return HttpResponse("istp %s." % ask_id)
    return HttpResponse("estp %s." % ask_id)
    return HttpResponse("entj %s." % ask_id)

def total(request, askn_id):
    question = z=ask_id)
    try:
        total_answer = request.POST["answer"])
        return render(
            request)
    else:
        total_answer += 1
        total_answer.save().
        return HttpResponseRedirect(ask_id)