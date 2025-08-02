import os
from flask import Flask, render_template, request, session, redirect, url_for
from agent_logic import initialize_agent, get_agent_response

app = Flask(__name__)
# A secret key is required for Flask session management
app.secret_key = os.urandom(24) 

# Initialize the agent client once
CLIENT, AGENT_ID, THREAD_ID = initialize_agent()

@app.route('/', methods=['GET', 'POST'])
def chat():
    # Store agent details in session if not already there
    if 'agent_id' not in session:
        if not all([CLIENT, AGENT_ID, THREAD_ID]):
            return "Failed to initialize the AI Agent. Check your terminal for errors.", 500
        session['agent_id'] = AGENT_ID
        session['thread_id'] = THREAD_ID
        session['chat_history'] = []

    if request.method == 'POST':
        user_prompt = request.form.get('prompt')
        if user_prompt:
            # Add user message to history
            session['chat_history'].append({'role': 'user', 'content': user_prompt})
            
            # Get agent response
            agent_response = get_agent_response(CLIENT, session['thread_id'], session['agent_id'], user_prompt)
            
            # Add agent message to history
            session['chat_history'].append({'role': 'agent', 'content': agent_response})
            session.modified = True # Save the session
        
        return redirect(url_for('chat'))

    return render_template('index.html', chat_history=session.get('chat_history', []))

if __name__ == '__main__':
    app.run(debug=True, port=5001) # Using port 5001 to avoid conflicts