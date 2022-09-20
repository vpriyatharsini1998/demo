import fitz
filename ="EE20M802_Thesis.pdf"
search_term   = "Chapter 1"
search_term_1 = "Chapter 2"
search_term_2 = "Chapter 3"
search_term_3 = "Chapter 4"
search_term_4 = "Chapter 5"

pdf_document = fitz.open(filename)
for current_page in range(len(pdf_document)):
   # page = pdf_document.loadPage(current_page)
    print(search_term,search_term_1,search_term_2,search_term_3,search_term_4)
    print(search_term)
    break
    if current_page.searchFor(search_term):
        print(current_page(search_term)
   # if page.searchFor(search_term):
    #   print("%s found on page %d" % (search_term, current_page))
        
 
