import information
import website

coding_bat = information.Resource("Coding bat",
                                  "List of problemas",
                                  "Practice",
                                  "English")

code_chef = information.Resource("Code chef",
                                  "List of problemas",
                                  "Practice",
                                  "English")

resources = [coding_bat, code_chef]
website.open_resources_page(resources)
