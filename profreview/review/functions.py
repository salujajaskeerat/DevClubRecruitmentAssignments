import re
from django.contrib.auth.models import User
# Function to Evaluate the Prof Net Ratings
def net_rating(r):
	# r is dictionary that store all rating for prof/course
	l=int(r.count())
	s=0
	# total number of ratings for him
	for i in r:
		s+=int(i.rating1)
	if l!=0 :

		return (s/l)
	else :
		return 0.0
# def likes(comment):
# 	s=list()
# 	for com in comment:
# 		l=List.object.filter(comment=com)
# 		s.append(l.count())

def valid_email(email):
	# Pattern we Need in Mail
	pattern1=re.compile(r'[a-z]{2}\d{7}@iitd\.ac\.in?')
	pattern2=re.compile(r'[a-z]{2}\d{7}@cse\.iitd\.ac\.in?')
	matches1=pattern1.match(email)
	matches2=pattern2.match(email)
	if( matches1 is None) and (matches2 is None) :
		return False
	else: 
		return True
#  The above functions works very fine

def extract_roll(email):
	pattern=re.compile(r'[a-z]{2}\d{7}?')
	matches=pattern.match(email)
	if(matches is not None):
		return(matches.group(0))
	else:
		return None

	# this code also works fine

def email_exists(email):
	users=User.objects.all()
	bool=False

	for user in users:
		Email=user.email
		if(extract_roll(Email)==extract_roll(email)):
			bool=True
			break

	return bool