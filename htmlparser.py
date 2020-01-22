from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    print("------------ new parser section -------------------------")
    def handle_starttag(self, tag, attrs):
        if tag =="a ":
#            print(len(attrs))
#            print("Encountered start tag: ", tag)
            for element in attrs:
                if element[0] == "data-gtm-payload":
                    txt = element[1].split(",")
                    typ = type(txt)
                    num = len(txt)
                    print("\tattribut ist vom Typ %s und enthält %i Element:"%(typ, num),txt)
            def handle_data(self, data):
                print("Encountered some data:", len(data), type(data))

htmlFile = open("crawl_result.html", "r", encoding="utf-8")
content = htmlFile.read()

parser=MyHTMLParser()

parser.feed(content)
#parser.feed(s)
parser.close()
