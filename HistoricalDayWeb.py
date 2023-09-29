import requests
from datetime import datetime

today = datetime.today().strftime('%m/%d')
response = requests.get(f"https://history.muffinlabs.com/date/{today}")
data = response.json()
events = data['data']['Events']

# Create an HTML page with CSS styling
html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Historical Events for {today}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }}
        h1 {{
            background-color: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            margin-bottom: 10px;
            background-color: #fff;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
        }}
        strong {{
            color: #333;
        }}
    </style>
</head>
<body>
    <h1>Historical Events for {today}</h1>
    <ul>
        {''.join([f"<li><strong>Year: {event['year']}</strong> - {event['text']}</li>" for event in reversed(events)])}
    </ul>
</body>
</html>
"""

# Save the HTML to a file
with open('index.html', 'w') as file:
    file.write(html_page)
