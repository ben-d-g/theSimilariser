from theSimilariser import Similariser
import tkinter

similariser = Similariser()

def findSimilarity():
    similariser.updateTerms(term1.get(), term2.get())
    output["text"] = "The similarity coefficient of these terms is: " + str(similariser.calculateSimilarityCoefficient()) + "%"

root = tkinter.Tk()
message = tkinter.Label(root, text = "Welcome to the Similariser. Please enter your terms.")
message.grid(row = 0, column = 0)

term1 = tkinter.Entry(root)
term2 = tkinter.Entry(root)
term1.grid(row = 1, column = 0)
term2.grid(row = 1, column = 1)

goButton = tkinter.Button(root, text = "Go!", command = findSimilarity)
goButton.grid(row = 2, column = 0)

output = tkinter.Label(root, text = "")
output.grid(row = 2, column = 1)

root.mainloop()