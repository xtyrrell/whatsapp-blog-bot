import uuid
import logging
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

from update_repo import upload_image_and_update_html
from utils import MIMETYPE_TO_EXTENSION
from env import env

logger = logging.getLogger(__name__)


app = Flask(__name__)


def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)


@app.route("/message", methods=["POST"])
def receive_message():
    sender = request.form.get("From")
    message = request.form.get("Body")
    media_url = request.form.get("MediaUrl0")
    debug_message = f'{sender} sent "{message}" with media_url "{media_url}"'
    print(debug_message)

    if not media_url:
        return respond("Please send an image! 🖼️💔")

    r = requests.get(media_url)
    content_type = r.headers["Content-Type"]
    # username = sender.split(":")[1]  # remove the whatsapp: prefix from the number

    print("content_type is", content_type)

    image_id = uuid.uuid4()
    extension = MIMETYPE_TO_EXTENSION.get(content_type)
    if extension is None:
        return respond("The file that you submitted is not a supported image type. 💔")

    image_filename = str(image_id) + extension

    try:
        print("Updating website repo...")
        upload_image_and_update_html(
            env.get("GITHUB_TOKEN"), env.get("GITHUB_REPO"), image_filename, r.content
        )
        print("Done!")
    except Exception as e:
        print("Exception: ", e)
        logger.exception()
        return respond(
            "Oops, couldn't add that image to your website. Please try again! 🙏"
        )

    return respond("Image added to your website! 🫣🤝↗️")
