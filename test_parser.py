from app.parser import extract_text_from_pdf

pdf_path = "resumes/Gourav_Resume_.pdf"   # Change this to your actual PDF name

text = extract_text_from_pdf(pdf_path)

print(text[:2000])   # Print first 2000 characters