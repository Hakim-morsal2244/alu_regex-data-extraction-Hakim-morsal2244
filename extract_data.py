import re

# Sample text for testing
text = """
Emails: user@example.com, firstname.lastname@company.co.uk
URLs: https://www.example.com, https://subdomain.example.org/page
Phone Numbers: (123) 456-7890, 123-456-7890, 123.456.7890
Credit Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
Time (24-hour): 14:30, 02:45, 2:00, 11:59
Time (12-hour): 2:30 PM, 11:15 AM
HTML Tags: <p>Paragraph</p>, <div class="example">Content</div>
Hashtags: #example, #ThisIsAHashtag
Currency: $19.99, $1,234.56
"""

# Regular Expressions
patterns = {
    "Emails": re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text),
    "URLs": re.findall(r"https?://[^\s,]+", text),  # Fixed to remove commas
    "Phone Numbers": re.findall(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text),
    "Credit Cards": re.findall(r"\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}", text),
    "Time (24-hour)": re.findall(r"\b([01]?[0-9]|2[0-3]):([0-5][0-9])\b", text),  # Full time format
    "Time (12-hour)": re.findall(r"\b([1-9]|1[0-2]):([0-5][0-9])\s?(AM|PM|am|pm)\b", text),  # Fixed
    "HTML Tags": re.findall(r"<[^>]+>", text),
    "Hashtags": re.findall(r"#\w+", text),
    "Currency": re.findall(r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?", text),
}

# Print results
for key, matches in patterns.items():
    print("{}: {}\n".format(key, matches))
