import re
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Database configuration
DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost/pwords'
engine = create_engine(DATABASE_URI)
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()

# Define the profanities table
profanities = Table('profanitywords', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('word', String(255)))

@app.route('/filter', methods=['POST'])
def filter_profanity():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Fetch all profanities from the database
    result = session.query(profanities).all()
    profanity_words = [row.word for row in result]

    # Replace profanity words in the text
    for word in profanity_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub(lambda x: '*' * len(x.group()), text)

    return jsonify({'filtered_text': text})

if __name__ == '__main__':
    app.run(debug=True)
