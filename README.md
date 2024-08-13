# theSimilariser

The Similariser is a way to compare the *similarity* of two concepts. This is achieved by comparing the links found in the Wikipedia articles for each concept.

This is a project that I worked on a while ago. For the sake of reference I am adding it to Github, hence why everything was made in one go.

## Similarity metric

Currently the similarity of the two concepts is measured using the following metric:

$$ 50 \left( \frac{ \text{log} | A \cap B | }{\text{log} |A|} + \frac{ \text{log} | A \cap B | }{\text{log} |B|} \right) $$

Where $A$ and $B$ represent the set of pages linked to by the first and second term's Wikipedia article.

## GUI

A quick tkinter GUI has been made to interact with theSimilariser.py. This is not the nicest of solutions, but it is there and it works.