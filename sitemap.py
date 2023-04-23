import sys
from datetime import datetime

def create_sitemap(files):
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for file in files.split('\n'):
        if file:
            sitemap += f'<url><loc>https://github.com/USERNAME/REPO/blob/main/{file}</loc><lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod></url>\n'
    sitemap += '</urlset>'
    return sitemap

if __name__ == '__main__':
    files = sys.argv[1]
    sitemap = create_sitemap(files)
    with open('sitemap.xml', 'w') as f:
        f.write(sitemap)
