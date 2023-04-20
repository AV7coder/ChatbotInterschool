from flask import Flask,render_template, request
from googlesearch import search
app=Flask(__name__)
app.config['SECRET_KEY']='qwertyuiopasdfghjklzxcvbnm'
@app.route('/', methods=['GET', 'POST']) 
def index():
    qa={

   

      "questions": [

   

        {

   

          "question": "What are the typical symptoms of COVID-19?",

   

          "answer": "Typical symptoms of COVID-19 include fever, cough, fatigue, loss of smell or taste, headache, sore throat, body aches, and shortness of breath. However, it's important to note that symptoms can vary greatly from person to person.",




          "keyword": ["symptom","symptoms"]

   

        },

   

        {

   

          "question": "How long does it take to recover from COVID-19?",

   

          "answer": "Recovery time from COVID-19 varies from person to person and depends on the severity of the illness. Mild cases may recover within a few days to a week, while more severe cases can take several weeks or longer to recover."

         

          ,"keyword":["long","recover", "time","recovery"]

        },

   

        {

   

          "question": "Can I spread the virus to others if I don't have symptoms?",

   

          "answer": "Yes, it's possible to spread the virus to others, even if you don't have symptoms. This is why it's important to follow public health guidelines such as wearing masks and practicing physical distancing, especially when around others who may be at higher risk for severe illness."

   

          ,"keyword": ["spread"]

        },

   

        {

   

          "question": "What treatments are available for COVID-19?",

   

          "answer": "There are several treatments available for COVID-19, including antiviral medications, immune-based therapies, and supportive care such as oxygen therapy and fluid management. Treatment options may vary depending on the severity of the illness and other factors."

          ,"keyword":["treatments","treatment","treat"]

        },

   

        {

   

          "question": "What can I do to manage my symptoms at home?",

   

          "answer": "To manage symptoms at home, it's important to get plenty of rest, stay hydrated, and take over-the-counter medications such as acetaminophen or ibuprofen to relieve fever and pain. It's also important to monitor your symptoms and seek medical attention if they worsen."

          ,"keyword":["home", "symptoms", "manage", "symptom"]

        },

   

        {

   

          "question": "How long should I self-isolate if I have COVID-19?",

   

          "answer": "The recommended duration of self-isolation for COVID-19 varies depending on factors such as symptoms and test results. Generally, individuals with COVID-19 should self-isolate for at least 10 days after symptom onset and until they have been fever-free for at least 24 hours without the use of fever-reducing medication."

          ,"keyword":["self-isolate","long","time"]

        },

   

        {

   

          "question": "When can I go back to work or school after having COVID-19?",

   

          "answer": "The recommended duration of time before returning to work or school after having COVID-19 varies depending on factors such as symptoms and test results. Generally, individuals with COVID-19 should follow the advice of their healthcare provider and local health department regarding when it is safe to return to work or school."

          ,"keyword":["back", "after"]

        },

   

        {

   

          "question": "Can I get COVID-19 more than once?",

   

          "answer": "It's possible to get COVID-19 more than once, although it's unclear how common this is or how long immunity lasts after infection. It's important to continue following public health guidelines even after recovering from COVID-19."

          ,"keyword":["more", "once"]

        },




        {

            "question": "How can I protect myself and others from getting COVID-19?",

          "answer": "In those situations, use as many prevention strategies as you can, such as practicing hand hygiene, consistently and correctly wearing a high-quality mask, improving ventilation, and keeping your distance, when possible, from the person who is sick or who tested positive."

          ,"keyword": ["protect","prevent"]

        }    

    ]

}
    if  request.method == 'POST':
        a=""
        search_text = request.form.get('search')
        for i in qa["questions"]:
            for j in i:
                if j=="answer":
                    a=i[j]
                if j=="keyword":
                    for y in i[j]:
                        if y in search_text:
                            output=a
        mainResult = []
        for i in search(search_text,tld="co.in", num=1, stop=5, pause=1): 
            mainResult.append(i)  
        print(mainResult) 
        displayResult = {
            "1":output,
            "2":"Here are some additional links:",
            "3":mainResult[0],
            "3":mainResult[1],
            "4":mainResult[2],
            "5":mainResult[3],
            "6":mainResult[4],
        }
        return render_template("index.html",data=displayResult)
    return render_template("index.html")
if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)