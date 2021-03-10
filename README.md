# Information Retrieval
Information Retrieval VUB - Project

Positional index of the form:

{"word" : [total_occurrences, {doc_ID_1 : [POS_1, POS_2], doc_ID_2 : [POS_1]}]}

For example:

{"mama" : [ 123, {1: [1,2], 5: [10,20]}]}

The word "mama" has an total occurrences of 123 across the documents, and appears in document 1 at position [1,2] and in document 5 in position [10,20]
## Usage
```bash
python main.py query --query_type --stem --mode
```

query: query to execute.

--query_type: perform proximity _query_ in the form: word_1/k%word_2, e.g. beatles/3%concert

--stem: --stem to stem the words or --nostem to not stem the words.

--mode : --save to create and save the positional index of the dataset, --load to load it from a previously created positional index.

## Example
To generate create a positional index and execute a proximity query between the words _beatles_ and _concert_, no stemming.
```bash
python main.py  concert/3%beatles --proximity --nostem --save
```
To load a positional index and execute a proximity query between the words _beatles_ and _concert_, stemming enabled.
```bash
python main.py concert/3%beatles --proximity --stem --load
```
