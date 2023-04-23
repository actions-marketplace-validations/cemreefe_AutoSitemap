import os

# Read the domain name from the input, or from the GitHub Pages custom domain setting
domain = os.environ.get('INPUT_DOMAIN', os.environ.get('GITHUB_PAGES_CNAME'))

# Get a list of all files in the repository
files = []
for root, _, filenames in os.walk('.'):
    for filename in filenames:
        files.append(os.path.join(root, filename))

# Generate the sitemap XML file
sitemap = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for file in files:
    if file.endswith('.md') or file.endswith('.html'):
        path = os.path.splitext(file)[0]
        sitemap += f'  <url>\n    <loc>https://{domain}/{path}</loc>\n  </url>\n'
sitemap += '</urlset>\n'

# Write the sitemap XML file to disk
with open('sitemap.xml', 'w') as f:
    f.write(sitemap)
