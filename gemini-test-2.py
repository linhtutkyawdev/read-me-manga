from google import genai

YOUR_GEMINI_API_KEY = 'AIzaSyBS3RZlU6phkxlQvKIL-3x2xtnSV112TOs'
YOUR_MODEL_NAME = 'gemini-2.0-flash'


client = genai.Client(api_key = YOUR_GEMINI_API_KEY)

with open('test.pdf', 'rb') as f:
    file_bytes = f.read()

for chunk in client.models.generate_content_stream(
    model='gemini-2.0-flash',
    contents=["""
ttached is a PDF containing a chapter of a visual story. I need a script for text-to-speech (TTS) that narrates this chapter, page by page.  Please follow these instructions:

1. **Page Numbering:** Each section of the script must begin with the corresponding page number from the PDF (e.g., "Page 1:", "Page 2:", etc.).

2. **Visual Description:**  Describe the key visual elements on each page.  Be specific. For example, instead of "A person is standing," say "A young woman with red hair, wearing a blue coat, stands nervously by the window."

3. **Narrative Flow:** Connect the visuals into a cohesive narrative. Describe the actions, emotions, and any implied dialogue or thoughts of the characters.

4. **TTS Optimization:**  The script must be suitable for TTS.  Use clear, concise language. Avoid onomatopoeia (e.g., "boom!") or exclamations (e.g., "Wow!"). Describe sounds instead (e.g., "The cannon fired," "He gasped in surprise").  Avoid overly dramatic or theatrical phrasing.

5. **Tone:** The overall tone of the narration should be [Specify desired tone: e.g., "serious and suspenseful," "lighthearted and humorous," "informative and descriptive"].

6. **Example:**  For a page showing a character looking at a map, a good script entry would be: "Page 3:  A close-up of a weathered map fills the frame.  A young man with a determined expression traces a route with his finger.  He appears focused and resolute."

Please provide the complete script for the entire chapter.
""" ,
        genai.types.Part.from_bytes(data=file_bytes, mime_type='application/pdf'),
    ],
):
    print(chunk.text, end='')