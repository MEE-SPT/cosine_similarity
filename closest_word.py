import numpy as np
from numpy import dot
from numpy.linalg import norm

def cal_word_sim(A,B):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    words = [A,B]
    idx_word = []
    idx_word = [[] for _ in range(2)]
    word_a_array, word_b_array =  np.zeros(26, dtype='int'), np.zeros(26, dtype='int')

    for idx, word in enumerate(words):
        for letter in word:
            idx_word[idx].append(alpha.find(letter))
    
    for idx in idx_word[0]:
        word_a_array[idx] = 1
    
    for idx in idx_word[1]:
        word_b_array[idx] = 1
    
    cos_sim = dot(word_a_array, word_b_array)/(norm(word_a_array)*norm(word_b_array))

    return cos_sim


def find_closest_word(input_word):

    # word table from COCO_INSTANCE_CATEGORY_NAMES 
    word_table = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
    ]

    sim_score = []

    for word in word_table:
        sim_score.append(cal_word_sim(input_word, word))
    
    sim_score = np.array(sim_score)
    closest_word = word_table[np.argmax(sim_score)]
    max_sim_score = np.amax(sim_score)

    return closest_word, max_sim_score


if __name__ == "__main__":
    while True:
        input_word = input("Enter a word (type n to exit): ")
        
        if input_word == "n":
            print("Bye")
            break
        else:
            closest_word, sim_score = find_closest_word(input_word)
            if sim_score >= 1:
                print(f'I have "{input_word}" in my table')
            else:
                print(f'the closest word from my table is "{closest_word}", with score: {sim_score:.3f}')