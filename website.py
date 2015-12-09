import webbrowser


#styles and scripting for the page

main_page_head = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset = "utf-8">
        <title>Web Site</title>
         <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
         <style type="text/css" media="screen">

             .resource-row li {
                display:inline;
             }
             .resource-row li a {
                width: 100px;
                display: inline-block;
             }
         </style>
         <script type="text/javascript" charset="utf-8">
         </script>
    </head>
'''

main_page_content='''
<body>
    <div class="container">
        <h1>Resources for Tech Interview</h1>
        <a>If you want to apply for a job in a Tech Compamy you should....</a>
        <div class="menu-resources">
            <a>Type of resource</a>
            <select>
                <option selected>All selected</option>
                <option>Online Courses</option>
                <option>Problems</option>
                <option>Contest</option>
            </select>
            <a>Languages</a>
            <select>
                <option selected>All selected</option>
                <option>English</option>
                <option>Spanish</option>
            </select>
        </div>
        <div class="resources">
            {resource_row}
        </div>
    </div>
</body>
</html>
'''

resource_row = '''
    <ul class="resource-row">
        <li><a>{resource_title}</a></li>
        <li><a>{resource_information}</a></li>
        <li><a>{resource_type}</a></li>
        <li><a>{resource_language}</a></li>
    </ul>
    '''


def create_resources_content(resources):
    content=''
    for resource in resources:
        content += resource_row.format(
        resource_title = resource.name,
        resource_information = resource.description,
        resource_type = resource.style,
        resource_language = resource.language
        )
    return content
    

def open_resources_page(resources):
    output_file = open('website.html','w')
    rendered_content = main_page_content.format(
        resource_row = create_resources_content(resources))
    
    output_file.write(main_page_head + rendered_content)

    output_file.close()
