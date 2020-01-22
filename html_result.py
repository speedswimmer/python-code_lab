from html.parser import HTMLParser
#parser shows only links
class MyHTMLParser(HTMLParser):
    print("------------ new parser section -------------------------")
    def handle_starttag(self, tag, attrs):
        if tag=="a":
            print("Encountered a start tag:",tag)
            for element in attrs:
                if element[0] == "href":
                    print("\tattr:", element)
#    def handle_endtag(self, tag):
#        print("Encountered end-tag: ",tag)
#    def handle_comment(self, data):
#        print("Encountered some comment", data)
    def handle_entityref(self, name):
        print("Encountered some ref:", name)

htmlFile = open("crawl_result.html", "r", encoding="utf-8")
content = htmlFile.read()

parser=MyHTMLParser()

parser.feed(content)
#parser.feed(s)
parser.close()