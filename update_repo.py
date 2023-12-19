from pathlib import Path
from github import Github


def upload_image_and_update_html(
    github_token, repo_name, image_filename, image_content
):
    # Initialize GitHub API client
    g = Github(github_token)
    repo = g.get_repo(repo_name)

    print(f"Updating repo {repo_name}")

    repo.create_file(
        f"assets/{image_filename}", f"Upload {image_filename}", image_content
    )

    # Get index.html content
    contents = repo.get_contents("index.html")
    html_content = contents.decoded_content.decode()

    # Find the line to insert the new image tag
    lines = html_content.split("\n")
    for i, line in enumerate(lines):
        if '<div class="images">' in line:
            # Insert new line
            new_line = f'            <img src="assets/{image_filename}" />'
            lines.insert(i + 1, new_line)
            break

    # Update index.html in the repo
    updated_html_content = "\n".join(lines)
    repo.update_file(
        contents.path,
        f"Update index.html with {image_filename}",
        updated_html_content,
        contents.sha,
    )
