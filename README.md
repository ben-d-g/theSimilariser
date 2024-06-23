# theSimilariser

The similariser is a method of comparing the similarity of two things. \
This works by comparing the links on the wikipedia page for the two things.

## A note on the similarity coefficient

Currently the coefficient of similarity is given by

$$
\frac{|A \cap B|}{|A|} + \frac{|A \cap B|}{|B|}
$$

Where $A$ and $B$ are the sets of links on each page. I am not entirely happy with this. I feel that this should be weighted in some way - a page with a small number of links could have a bigger impact than we want.\
Also, perhaps we should use lists instead of sets, so if a page is repeated many times it has more of an impact.

## GUI

Tkinter has been used to give the similariser a GUI. This is not nice, but it does the job.

## Errors

Currently no measures are put in place to catch errors. Maybe I will get on that soon.