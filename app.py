from flask import Flask, render_template, request, session, redirect, jsonify 
from flask_session import Session 
from cs50 import SQL 
from groq import Groq 
from dotenv import load_dotenv 
import os 
from datetime import datetime 
from functools import wraps 

load_dotenv() 

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY")) 
MODEL_NAME = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant") 

app = Flask(__name__) 
app.config["SESSION_PERMANENT"] = False 
app.config["SESSION_TYPE"] = "filesystem" 
Session(app) 
db = SQL("sqlite:///database.db") 

def login_required(f): 
    @wraps(f) 
    def decorated_function(*args, **kwargs): 
        if session.get("user_id") is None: 
            return redirect("/login") 
        return f(*args, **kwargs) 
    return decorated_function 

QUESTIONS = [ 
    "What happened today?", 
    "How did it make you feel?", 
    "What can you learn from this?", 
    "What advice would you give your future self?" 
    ] 

@app.route("/") 
@login_required 
def index(): 
    return render_template("index.html")
    
@app.route("/login", methods=["GET", "POST"])
def login(): 
    session.clear() 
    if request.method == "POST": 
        username = request.form.get("username") 
        rows = db.execute("SELECT * FROM users WHERE username = ?", username) 
        if len(rows) != 1: 
            return render_template("login.html", error="Invalid username") 
        if rows[0]["hash"] != request.form.get("password"): 
            return render_template("login.html", error="Invalid password") 
        session["user_id"] = rows[0]["id"] 
        return redirect("/") 
    return render_template("login.html") 

@app.route("/logout") 
def logout(): 
    session.clear() 
    return redirect("/") 

@app.route("/register", methods=["GET", "POST"]) 
def register(): 
    if request.method == "POST": 
        username = request.form.get("username") 
        password = request.form.get("password") 
        rows = db.execute("SELECT * FROM users WHERE username = ?", username) 
        if len(rows) > 0: 
            return render_template("register.html", error="Username already exists") 
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, password) 
        new_user = db.execute("SELECT id FROM users WHERE username = ?", username) 
        session["user_id"] = new_user[0]["id"]  
        return redirect("/") 
    return render_template("register.html") 

@app.route("/reflect") 
@login_required 
def reflect(): 
    return render_template("reflect_start.html") 

@app.route("/reflect/step/<int:step>", methods=["GET", "POST"])
@login_required
def reflect_step(step):
    # Ensure reflection session exists
    if "reflection" not in session:
        session["reflection"] = {}

    # Validate step number
    if step < 1 or step > len(QUESTIONS):
        return redirect("/reflect")

    if request.method == "POST":
        answer = request.form.get("answer", "")
        session["reflection"][f"q{step}"] = answer

        if step == len(QUESTIONS):
            db.execute(
                "INSERT INTO reflections (user_id, timestamp, q1, q2, q3, q4) VALUES (?, ?, ?, ?, ?, ?)",
                session["user_id"],
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                session["reflection"].get("q1"),
                session["reflection"].get("q2"),
                session["reflection"].get("q3"),
                session["reflection"].get("q4")
            )
            session.pop("reflection")
            return redirect("/reflect/history")

        return redirect(f"/reflect/step/{step + 1}")

    # GET request
    return render_template("reflect_step.html", step=step, question=QUESTIONS[step - 1])
    
@app.route("/reflect/history") 
@login_required 
def reflect_history(): 
        reflections = db.execute( "SELECT * FROM reflections WHERE user_id = ? ORDER BY id DESC", session.get("user_id") ) 
        return render_template("reflect_history.html", reflections=reflections)
        
@app.route("/ai_rephrase", methods=["POST"]) 
@login_required 
def ai_rephrase(): 
        user_text = request.form.get("text") 
        response = groq_client.chat.completions.create( 
            model="llama-3.1-8b-instant", 
            messages=[ {"role": "system", 
                        "content": "You are a calm, gentle writing assistant. Do NOT give medical advice."}, 
                        {"role": "user", "content": f"Rephrase this calmly: {user_text}"} ] )
        reply = response.choices[0].message.content 
        return jsonify({"rephrased": reply}) 
    
@app.route("/comfort", methods=["GET", "POST"]) 
@login_required 
def comfort():  
        return render_template("comfort.html")
    
@app.route("/ai_comfort", methods=["POST"]) 
@login_required 
def ai_comfort(): 
        situation = request.form.get("situation") 
        response = groq_client.chat.completions.create( 
            model="llama-3.1-8b-instant", 
            messages=[ {"role": "system", 
                        "content": "You are a calm, supportive assistant. Do NOT give medical advice."}, 
                        {"role": "user", "content": f"The user says: {situation}. Respond with gentle, supportive words."} ] ) 
        reply = response.choices[0].message.content 
        return {"comfort": reply} 
    
@app.route("/sound")
@login_required 
def sound(): 
        return render_template("soundboard.html") 
    

if __name__ == "__main__": app.run(debug=True)