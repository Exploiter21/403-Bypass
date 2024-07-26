import threading
import requests
import queue
import time

# Set the target URL and wordlist file
target_url = "https://google.com"
wordlist_file = "./wordlist.txt"

# Create a queue to hold the words to be processed
word_queue = queue.Queue()

# Load the wordlist into the queue
with open(wordlist_file, "r") as f:
    for word in f:
        word_queue.put(word.strip())

# Function to perform the brute force attack
def brute_force(word_queue):
    while not word_queue.empty():
        word = word_queue.get()
        url = f"{target_url}/{word}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Found directory: {url}")
        except requests.exceptions.RequestException:
            pass
        finally:
            word_queue.task_done()

# Create and start the threads
num_threads = 10  # adjust this value to change the number of threads
threads = []
for i in range(num_threads):
    t = threading.Thread(target=brute_force, args=(word_queue,))
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

print("Brute force complete!")