class Element(object):

    def __init__(self, content=None):
        pass
    def append(self, new_content):
        self.content +=new_content
    def render(self, file_out, ind=""):
        pass

'''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>PythonClass = Revision 1087:</title>
    </head>
    <body>
        <h2>PythonClass - Class 6 example</h2>
        <p style="text-align: center; font-style: oblique;">
            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
        </p>
        <hr />
        <ul style="line-height:200%" id="TheList">
            <li>
                The first item in a list
            </li>
            <li style="color: red">
                This is the second item
            </li>
            <li>
                And this is a
                <a href="http://google.com">link</a>
                to google
            </li>
        </ul>
    </body>
</html>
'''