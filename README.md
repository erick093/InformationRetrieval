# InformationRetrieval
Information Retrieval VUB - Project

Positional index of the form:

{"word" : [total_occurrences, {doc_ID_1 : [POS_1, POS_2]}, {doc_ID_2 : [POS_1]} ] }
For example:

{"mama" : [ 123, {1: [1,2]}, {5: [10,20]}  ]}

The word "mama" has an total occurrences of 123 across the documents, and appears in document 1 at position [1,2] and in document 5 in position [10,20]
## Usage
```bash
python main.py word --mode
```

word : Placeholder of {word} is the word which you want to see the positional index

--mode : --save to create and save the positional index of the dataset, --load to load it from a previously created positional index

## Example
To generate create a positional index and see the index of the word "american"
```bash
python main.py american --save
```
To load a positional index and see the index of the word "american"
```bash
python main.py american --load
```
