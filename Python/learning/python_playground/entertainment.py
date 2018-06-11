
import classes
import fresh_tomatoes

toy_story = classes.Movie("Toy Story", "Toys come to life.", "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg", "https://www.youtube.com/watch?v=4KPTXpQehio")
school_of_rock = classes.Movie("School of Rock", "Jack Black.", "http://www.gstatic.com/tv/thumb/movieposters/33094/p33094_p_v7_aa.jpg", "https://www.youtube.com/watch?v=3PsUJFEBC74")

movies = [toy_story, school_of_rock]
#fresh_tomatoes.open_movies_page(movies)

print classes.Movie.__doc__


#print toy_story.storyline
#toy_story.showTrailer()
