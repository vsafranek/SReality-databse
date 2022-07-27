from load_data import load_from_sql

def run():
    print("create_database")
    html_file = open('index.html', 'w')


    data = load_from_sql()
    style="""<style>
            .grid-container {
              display: grid;
              grid-template-columns: auto auto auto;
              background-color: #2196F3;
              padding: 5px;
            }
            .grid-item {
              background-color: rgba(255, 255, 255, 0.8);
              border: 1px solid rgba(0, 0, 0, 0.8);
              padding: 5px;
              font-size: 10px;
              text-align: center;
            }
            </style>"""

    items=""""""
    id=0
    for line in data:
        id+=1
        name =line[1]
        name = name.replace("m²"," m<sup>2</sup>")
        nonBreakSpace = u'\xa0'
        name = name.replace(nonBreakSpace,"&nbsp")
        img= line[2]
        item = """
            <div class="grid-item"><br>
            <p>{id}</p>
            <h1>{name}</h1><br>
            <a href="{img}">
                <img alt="Qries" src="{img}">
            </a></div>
            
        """.format(id=id, name=name, img=img)
        items=items+item

    html = """\
    <html>
      <head>
       {style}
        </head>
      <body>
        <h1>SReality    
        </h1>
        <div class="grid-container">
            {content}
        </div>
      </body>
    </html>
    """.format(style=style,content=items)


    html_file.write(html)
    html_file.close()




if __name__ == "__main__":
    run()