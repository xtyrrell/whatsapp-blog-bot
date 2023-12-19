from app import app

# Vercel Serverless Functions looks for api/*.py to find the Flask app.
# And we're using vercel.json to rewrite all request paths to this file
app
