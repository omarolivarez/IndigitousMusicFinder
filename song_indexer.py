import json

def get_song():

	# get user input; which song they want played first
	testing_select = input("Enter the song that you would like to listen to: ")

	# text formatting
	testing_select = testing_select.lower()
	testing_select = testing_select.strip()
	testing_select = testing_select.split()

	# return the song name in a list
	return testing_select

def get_author():

	# get user input; author of the song they want played first
	testing_author_select = input("Enter that song's artist: ")

	# text formatting
	testing_author_select = testing_author_select.lower()
	testing_author_select = testing_author_select.strip()
	testing_author_select = testing_author_select.split()	

	# return the artist name in a list
	return testing_author_select

def format_file(testing_select, testing_author_select):

	file_name = "./"
	for i in range(len(testing_select)):
		if i != len(testing_select)-1:
			file_name+=testing_select[i]
			file_name+="_"
		else:
			file_name+=testing_select[i]
	file_name+="_"
	last_name_position = len(testing_author_select)-1
	last_name = testing_author_select[last_name_position]
	last_name = last_name.lower()
	file_name += last_name
	file_name+=".txt"

	return file_name

def get_song_mood_and_weight(song_file):

	for line in song_file:
		line  = json.loads(line)
		mood_first_step = line["document_tone"]["tone_categories"]
		mood_second_step = mood_first_step[0]["tones"] # this is a list
		mood_final_step = mood_second_step[0]["tone_name"] #this is the actual mood
		mood_final_step2 = mood_second_step[0]['score']

	return mood_final_step, mood_final_step2

def get_song_phrase(song_file):

	for line in song_file:
		line  = json.loads(line)
		mood_first_step = line["sentences_tone"]
		print(mood_first_step)
		mood_final_step = mood_first_step[0]["text"] # this is a sentence
		print("HI")
		#mood_final_step = mood_second_step[0]["tone_name"] #this is the actual mood

	return mood_final_step

def main():

	print()

	# user input: name of first song they want played
	testing_select = get_song()

	print()
	# user input: name of artist of first song played
	testing_author_select = get_author()

	print()

	# create file_name for querying
	file_name = format_file(testing_select, testing_author_select)
	#print(file_name)

	first_song = open(file_name, "r")
	
	first_song_top_mood, first_song_weight = get_song_mood_and_weight(first_song)


	print("Song mood: ",first_song_top_mood)
	print("Song weight: ", first_song_weight)
	#first_song_phrase = get_song_phrase(first_song)
	#print(first_song_phrase)


	print()


	###########################################################
	'''
	song_dictionary = open("./song_data.txt", "r")


	song_to_select = input("Enter the song you would like to listen to: ")
	song_to_select = song_to_select.lower()

	for i in song_dictionary:
		i = i.lower()
		if i == song_to_select:
			document_tone = song_dictionary[i]
			tone_categories = next_dict['tone_categories']
			zero = tones_categories[0]
			tones = zero["tones"] # I have a feeling this won't work
			second_zero = tones[0]
			primary_mood = second_zero[0]
			primary_mood_weight = second_zero[1]'''






	first_song.close()
main()
