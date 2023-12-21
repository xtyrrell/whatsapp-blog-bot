# WhatsApp Blog Bot

This is a WhatsApp bot that you can send a photo to to update your website with that photo. The bot receives the message, pulls out the media_url, and uploads it to a GitHub repo into `assets/`, and adds an `&lt;img src="uploaded_image_path">` to the index.html to display the image on the homepage.

## Deploying

It's a Flask app so there are many options for deployment. There aren't really any requirements from the environment. I've chosen [Vercel Serverless Python Functions](https://vercel.com/docs/functions/serverless-functions/runtimes/python).

Make sure you set the environment variables (see .env.example).
