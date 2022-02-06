import speech_recognition as sr
import turtle as t

r = sr.Recognizer()
def dajSlowo():	
	with sr.Microphone() as source:
		print("Podaj komende: ")
		audio = r.listen(source)		
    	
	return audio

z=t.Turtle()
z.shape('turtle')
z.color('red')

while True:
	slowo=r.recognize_google(dajSlowo(),language="pl-PL")
	slowo=str(slowo).lower()	
	print(f"twoja komenda to {slowo}")
	if slowo=="idź do przodu":
		print("idę do przodu")
		t.forward(100)
	elif slowo=="idź w prawo":
		print("idę w prawo")
		t.right(90)
		t.forward(100)
	elif slowo=="idź do tyłu":
		print("idę do tyłu")
		t.right(180)
		t.forward(100)
	elif slowo=="idź w lewo":
		print("idę w lewo")
		t.right(270)
		t.forward(100)
	elif slowo=="koniec":
		exit(1)
	else:
		print("bledna komenda")
