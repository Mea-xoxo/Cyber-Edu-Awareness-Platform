from django.shortcuts import render,get_object_or_404
from .models import Topic,Question,Choice


def search(request):
    query = request.GET.get('q')
    results = Topic.objects.none()   
    if query:
        results = Topic.objects.filter(title__icontains = query)
    
    print("Result Count: " ,results)
    return render(request,'cyberedu/search.html',{
        'query': query,
        'results': results,
        'topics': Topic.objects.all()
    })
    
     
def home(request):
    topics = Topic.objects.all()
    return render(request,'cyberedu/home.html',{'topics':topics})

def topic_preview(request,id):
    topic = Topic.objects.get(id = id)
    
    return render(request,'cyberedu/topic_preview.html',{
        'topic': topic
    })

def phishing(request):
    return render(request,'cyberedu/phishing.html')


def topic_detail(request,id):
    topic = get_object_or_404(Topic,id =id)
    return render(request,'cyberedu/topic_detail.html',{'topic':topic})

def quiz_view(request,topic_id):
    topic = get_object_or_404(Topic, id = topic_id)
    questions = Question.objects.filter(topic=topic)
    
    if request.method == 'POST':
        results = []
        score = 0
        total = questions.count()
        
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')        
            
            selected_choice = None
            is_correct = False
            
            if selected_choice_id:
                selected_choice = Choice.objects.get(id = selected_choice_id)
                is_correct = selected_choice.is_correct
                if is_correct:
                    score += 1

            correct_answer = Choice.objects.filter(question = question,is_correct = True).first()
      
            results.append({
                'question':question,
                'selected': selected_choice,
                'correct': correct_answer,
                'is_correct': is_correct
                    })
                
            
        return render(request,'cyberedu/result.html',{
            'topic' : topic,
            'questions': questions,
            'score': score,
            'total': total,
            })
    return render(request,'cyberedu/quiz.html',{
        'topic':topic,
        'questions':questions
    })
# Create your views here.
