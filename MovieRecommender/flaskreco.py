from flask import Flask, render_template, url_for, flash, redirect
from forms import RecommendForm
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676ddev280ba245'
df = pd.read_csv("static/metadata_exploded.csv")
pd.set_option('display.max_rows', 25)

@app.route("/")
@app.route("/home", methods=['GET','POST'])
def home():
	form = RecommendForm()
	if form.validate_on_submit():
		genre = form.genre.data
		low_time = form.ldur.data
		high_time = form.udur.data
		low_year = form.lyear.data
		high_year = form.uyear.data
		movies = df.copy()
		#Filter based on the condition
		movies = movies[(movies['genre'] == genre) & (movies['runtime'] >= low_time) & (movies['runtime'] <= high_time) & (movies['year'] >= low_year) & (movies['year'] <= high_year)]
		if movies.shape[0] != 0:
			#Compute the values of C and m for the filtered movies
			C = movies['vote_average'].mean()
			m = movies['vote_count'].quantile(0.8)
			
			#Only consider movies that have higher than m votes. Save this in a new dataframe q_movies
			movies = movies.copy().loc[movies['vote_count'] >= m]
			
			#Calculate score using the IMDB formula
			movies['score'] = movies.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C),axis=1)

			#Sort movies in descending order of their scores
			movies = movies.sort_values('score', ascending=False)
			return movies.to_html(max_rows=25)
		else:
			print("Sorry we couldn't find any")
	return render_template('home.html',title='Home',form=form)


if __name__ == '__main__':
	app.run(debug=True)