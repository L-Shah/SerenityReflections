# SERENITYREFLECTIONS

#### Video Demo: (https://youtu.be/cKIBpOT3mWQ?si=5ypYVIRHAzh4eOSN)

---

## Description

SerenityReflectionsis a Flask-based web application designed to help users practice daily self-reflection, receive gentle emotional support using AI along with a customisable soundboard. 
The application guides users through a structured reflection process, stores their responses securely, and allows them to revisit past reflections. 
In addition, it integrates an AI assistant that can calmly rephrase user thoughts without changing the initial meaning of content.Comfort AI provides comforting and motivating responses during emotionally challenging moments.
The soundboard contains a variety of sounds/ambiences wheter to relax, unwind or focus on studies.

The project solves the problem of unstructured journaling and emotional overwhelm by offering guided questions, reflection history, and AI-powered emotional assistance.
It is intended for individuals who want to build self-awareness regarding their emotions, process their feelings about daily experiences, also receive supportive, non-medical feedback in a private environment or create a customisable enviroment according to their neccessity.

---

## Motivation and Purpose

The motivation behind this project was to combine web development skills with an interest in mental well-being and reflective practices.
Many people including me want to journal or reflect but struggle with consistency or knowing what to write in order to understand why I am feeling a certain way to this situation.
personally speaking understanding your feelings and emotions on your own helps a lot when it comes to personal growth and understanding repetitive actions your brain takes in a difficult situation.
Re readng previous entries helps you track down habits or traits that affect your mental health and once you understand those overcoming them becomes easier.  
This project was inspired by guided journaling apps and the idea that AI, when used responsibly, can support emotional clarity without replacing professional help.
Also many personal growth content creators and students at Harvard, Yale, Stanford and other Universities post routines on social media practicing journaling and understanding yourself which helps them a lot in their day to day life, all that has been a part of the purpose for creating SerenityReflections

From a learning perspective, the project was an opportunity to practice full-stack development using Flask, session management, SQL databases, and third-party AI APIs, while also focusing on clean user experience and ethical AI usage.

---

## Features and Functionality

->User Authentication
  Users can register, log in, and log out.
  Sessions are managed using Flask-Session.
  Protected routes ensure only authenticated users can access personal content.

->Guided Reflection Flow
  Users answer a sequence of reflection questions step by step.
  Responses are temporarily stored in the session.
  Completed reflections are saved to a SQLite database with timestamps.

->Reflection History
  Users can view previous reflections in reverse chronological order.
  Enables long-term self-review and personal growth tracking.

->AI-Powered Reflection Rephrasing
  Users can request a calmer rephrasing of their written reflections.
  Designed to help users reframe thoughts in a balanced way.

->Comfort AI
  Users describe an emotionally difficult situation.
  The AI responds with gentle, supportive, non-medical language.
  
->Ambient Soundboard
  Users can play calming sounds such as rain, waves, fire, forest ambience, lo-fi music, and brown noise.
  Sounds can be played simultaneously and loop continuously.
  Individual volume controls allow users to create personalized soundscapes.

---

## Project Structure

->app.py
  Main Flask application file.
  Handles routing, authentication, database interaction, and AI integration.
  Defines routes for reflection, history, soundboard, AI rephrasing, and Comfort AI.
  Includes a custom login_required decorator.

->Frontend JavaScript

 -reflection.js
   Sends reflection text to the /ai_rephrase route using Fetch API.
   Updates the page dynamically with the AI response.

 -soundboard.js
   Controls ambient audio playback.
   Manages looping sounds, volume sliders, and play/pause buttons.

->static/styles.css
  Includes all the styling abouth the html pages and overall webapp.

->Templates
  HTML templates rendered with Jinja.
  Include pages for login, registration, reflection steps, history, comfort AI, and soundboard.
	-comfort.html
	-indexhtml
	-layout.html
	-login.html
	-reflect_history.html
	-reflect_start.html
	-reflect-step.html
	-register.html
	-soundboard.html

->database.db
  SQLite database storing users and reflections.
  Keeps user data persistent and private.

->static/sounds/
  Contains ambient audio files used by the soundboard and Comfort AI.

->Environment Configuration
 .env file stores sensitive information such as the Groq API key.

---


---



---

## Installation and Usage

Requirements
 Python 3
 Flask
 flask-session
 cs50
 python-dotenv
 groq

Installation
(terminal)
 pip install flask flask-session cs50 python-dotenv groq

Environment Setup
 Create a .env file:
  GROQ_API_KEY=your_api_key_here
  GROQ_MODEL=llama-3.1-8b-instant

Run the Application
(terminal)
 python app.py


Open your browser and navigate to:
 http://127.0.0.1:5000
 
---

## Conclusion

SerenityReflections is a guided reflection and emotional support web application that combines Flask, SQL, frontend JavaScript, and AI integration in a responsible and user-centered way.
Building this project strengthened my understanding of backend development, session management, database design, asynchronous frontend communication, and ethical AI usage. 
The project demonstrates how technology can support mindfulness and self-reflection while respecting user safety and boundaries.



