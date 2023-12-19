# WhatsApp Blog Bot

This is a WhatsApp bot that you can send a photo to to update your website with that photo. The bot receives the message, pulls out the media_url, and uploads it to a GitHub repo, and adds an <code>&lt;img src="uploaded_image_path"></code> to the index.html.

## Deploying

It's a Flask app so there are many options for deployment. There aren't really any requirements from the environment. I've chosen [Vercel Serverless Python Functions](https://vercel.com/docs/functions/serverless-functions/runtimes/python).

Make sure you set the environment variables (see .env.example).
