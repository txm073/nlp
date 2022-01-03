from gensim.models import KeyedVectors
import os

os.chdir(os.path.dirname(__file__))

model = KeyedVectors.load('vectors.kv')
print(model.most_similar_cosmul(positive=["king","woman"],negative=["man"]))

def similar():
    while True:
        try:
            responses = model.similar_by_word(input("\nEnter a word: "))
            reply = []
            for resp in responses:
                reply.append(resp[0])
            print(", ".join(reply))

        except KeyboardInterrupt:
            break

        except KeyError:
            print("Couldn't find that word...")

similar()