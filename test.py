import sys
import gensim.downloader as api
import gensim.models
import time

start = time.time()

dataset = api.load("text8")

print("Beginning training of the model...")
model = gensim.models.word2vec.Word2Vec(dataset, vector_size=50, epochs=20)

print("Training complete!")
print("Saving vector keys to disk...")

vectors = model.wv
vectors.save('vectors.kv')

print(f"Finished in {str(time.time()-start)[:5]}s with no errors")