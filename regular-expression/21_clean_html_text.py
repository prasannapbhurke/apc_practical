import re

html_doc = '<div><h1>Welcome</h1><p>This is a <b>sample</b> article with extra   spaces.</p></div>'

text_only = re.sub(r'<[^>]+>', ' ', html_doc)
text_only = re.sub(r'\s+', ' ', text_only)
cleaned_text = re.sub(r'[^a-zA-Z0-9 ]', '', text_only).strip()

print('Original HTML:', html_doc)
print('Cleaned Text Document:', cleaned_text)
