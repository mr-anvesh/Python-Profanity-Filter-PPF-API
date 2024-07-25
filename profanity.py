import os
import re
from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Database configuration
DATABASE_URI = 'mysql+mysqlconnector://root:Anvesh18@localhost/pwords'
engine = create_engine(DATABASE_URI)
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()

# Define the profanities table
profanities = Table('profanitywords', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('word', String(255)))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/filter', methods=['POST'])
def filter_profanity():
    if request.is_json:
        data = request.json
        text = data.get('text', '')
    else:
        text = request.form.get('text', '')

    if not text:
        if request.is_json:
            return jsonify({'error': 'No text provided'}), 400
        else:
            return render_template('index.html', filtered_text='No text provided')

    # Fetch all profanities from the database
    result = session.query(profanities).all()
    profanity_words = [row.word for row in result]

    # Replace profanity words in the text
    for word in profanity_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub(lambda x: '*' * len(x.group()), text)

    if request.is_json:
        return jsonify({'filtered_text': text})
    else:
        return render_template('index.html', filtered_text=text)

if __name__ == '__main__':
    app.run(debug=True)
