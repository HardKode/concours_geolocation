from flask import Flask, render_template, request
from googleplaces import GooglePlaces, types, lang
from google_key import GOOGLE_MAP_API_KEY

google_places = GooglePlaces(GOOGLE_MAP_API_KEY)

app = Flask(__name__)

@app.route('/')
def geolocation():
        # You may prefer to use the text_search API, instead.
        query_result = google_places.nearby_search(location='NB, CA',
                                               radius=30000, types=[types.TYPE_SCHOOL], language=lang.FRENCH
                                               )

        return render_template('geolocation.html', places=query_result.places)

@app.route('/job')
def job():
       return render_template('job.html')

@app.route('/events')
def events():
       return render_template('events.html')

@app.route('/price_plan')
def price_plan():
       return render_template('price_plan.html')

@app.route('/our_team')
def our_team():
       return render_template('our_team.html')

@app.route('/contact')
def contact():
       return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)
