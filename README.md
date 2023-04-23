# AutoSitemap

AutoSitemap is a GitHub Actions workflow that automatically generates a sitemap.xml file for your static website hosted on GitHub Pages. With AutoSitemap, you can ensure that search engines can easily crawl and index all of the pages on your website, without having to manually update the sitemap file every time you add or remove content.

## Setup

To set up AutoSitemap for your GitHub Pages website, follow these steps:

1. Generate a personal access token (PAT) with the `public_repo` scope on GitHub. You can create a new PAT in your GitHub account settings under "Developer settings" > "Personal access tokens". Make sure to copy the token value to your clipboard, as you won't be able to access it again once you leave the page.

2. Add the PAT as a secret to your GitHub repository. Go to the repository's settings, then navigate to "Secrets". Click on "New repository secret" and enter `PAT` for the name, then paste in the token value from step 1. Click "Add secret" to save the secret to your repository.

3. Add the AutoSitemap workflow to your GitHub repository. In your repository, create a new file under `.github/workflows` with the name `autositemap.yml`. Copy the following code into the file:


```
name: AutoSitemap

on:
push:
branches:
- main

jobs:
generate-sitemap:
runs-on: ubuntu-latest
steps:
- name: Checkout code
uses: actions/checkout@v2
- name: Generate sitemap
uses: username/AutoSitemap@v1.0
path: .
exclude:
- assets
- images
- name: Commit changes
uses: stefanzweifel/git-auto-commit-action@v4
with:
commit_message: "Auto-generated sitemap.xml"
commit_user_name: "AutoSitemap"
commit_user_email: "${{ github.actor }}@users.noreply.github.com"
```

4. (Optional) Customize the `path` and `exclude` parameters in the workflow to specify which files and directories should be included or excluded from the sitemap. By default, the workflow includes all `.html` and `.md` files in the repository, and excludes the `assets` and `images` directories.

5. Commit the changes to your repository. When you push changes to the `main` branch of your repository, the AutoSitemap workflow will automatically run and generate a sitemap.xml file in the root of your repository.

That's it! With AutoSitemap set up, you can ensure that your GitHub Pages website has an up-to-date sitemap that's easily discoverable by search engines.
