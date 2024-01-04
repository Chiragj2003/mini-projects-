import time
import random 
print("Welcome to the Typing Speed and Accuracy Test!")
print("You will be prompted to type a random sentence. Ready? Go!\n")
a=["India is the seventh-largest country in the world by land area.",
"The capital of India is New Delhi and the official language is Hindi.",
"India is known for its rich cultural heritage, with over 2,000 ethnic groups and more than 1,600 languages spoken across the country.",
"The Indian economy is the fifth-largest in the world by nominal GDP and the third-largest by purchasing power parity."
"The Indian subcontinent is home to many iconic landmarks and tourist destinations, such as the Taj Mahal, the Golden Temple, and the Himalayas."
"The national animal of India is the Bengal tiger and the national bird is the peacock.",
"The country has a rich history of arts, literature, and music, with classical dance forms such as Bharatanatyam and Kathak, and traditional musical instruments like the sitar and tabla.",
"Indian cuisine is known for its diverse flavors and spices, with popular dishes such as butter chicken, biryani, and samosas.",
"India has a large film industry known as Bollywood, which produces thousands of movies each year in Hindi and other regional languages.",
"Mahatma Gandhi, who led India to independence from British rule, is widely regarded as one of the most influential figures in modern history."]
b= random.randint(0,9)
sentence = a[b]
print(sentence)

start_time = time.time()
user_input = input()
end_time = time.time()

time_taken = end_time - start_time
num_chars = len(user_input)

# Calculate typing speed and accuracy
typing_speed = num_chars / time_taken
correct_chars = sum([1 for i in range(num_chars) if user_input[i] == sentence[i]])
accuracy = (correct_chars / num_chars) * 100

print(f"\nYou typed: '{user_input}'")
print(f"Time taken: {time_taken:.2f} seconds")
print(f"Your typing speed: {typing_speed:.2f} characters per second")
print(f"Accuracy: {accuracy:.2f}%")

type_speed = int((typing_speed*accuracy)/100)
print(f"Your typing speed: {type_speed} characters per second")