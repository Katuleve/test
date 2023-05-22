from transformers import pipeline
generator = pipeline('text-generation', model='distilgpt2')

res = generator(
    'IN this course we will teach you how to',
    max_legth = 30,
    num_return_sequences = 2)

print(res)