from html2image import Html2Image
hti = Html2Image()
hti.size = (500, 500)

hti.screenshot(
    html_file='./index.html', css_file='./index.css', save_as='page.png'
)