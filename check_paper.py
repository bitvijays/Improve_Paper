import fitz
import fitz.utils
from fitz.utils import getColorList
### READ IN PDF
doc = fitz.open("input.pdf")
# Define colors
CYAN = (0, 255, 255)
GOLD = (1, 1, 0)
GREEN = (0, 1, 0)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 1)
ORANGE = (255, 165, 0)
LIGHTCORAL = (240, 128, 128)
RED = (1, 0, 0)
GRAY0 = (0, 0, 0)

CHECKLIST_WORDS = ["voice", "repeatation", "qualifiers", "choice_of_words", "Obfuscation_Straw_Men"]
CHECKLIST_COLORS = [MAGENTA, CYAN, GOLD, GREEN, RED]


def highlight_text(text, color):
	""" Highlight the text based on certain color """

	# Get the number of pages in the document
	num_pages = doc.pageCount
	# Read each page
	for i in range(0, num_pages):
		page = doc[i]
		# Find the instance of the word searched
		text_instances = page.searchFor(text)
		# Highlight each instance
		for inst in text_instances:
			highlight = page.addHighlightAnnot(inst)
			highlight.setColors({"stroke":color})
			highlight.update()



def main():	

	### OUTPUT
	i = 0
	# We have defined the wordlists in CHECKLIST_WORDS
	for item in CHECKLIST_WORDS:
		filename = "words_check/" + item + ".txt"
		file_ptr = open(filename, 'r')
		# And respective color for particular file
		color = CHECKLIST_COLORS[i]

		for line in file_ptr:
			if line.startswith("#"):
				pass
			else:
				highlight_text(line, color)
		i = i + 1
	
	# Save the output
	doc.save("output.pdf", garbage=4, deflate=True, clean=True)


if __name__ == "__main__":
    main()
