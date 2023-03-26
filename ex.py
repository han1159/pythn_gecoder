from geopy.geocoders import Nominatim
if __name__=='__main__':
    ad=input('Enter Location:')
    user='Foundations of Python Network Programming example search1.py'
    location=Nominatim(user_agent=user).geocode(ad)
    print(location.latitude,location.longitude)