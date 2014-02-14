FORMAT: 1A
HOST: http://api.gtdtodoapi.com

# GTD TODO API
This is an example API, written as a companion to a blog post at SendGrid.com

## Folder [/folder{id}]
A single Folder object, it represents a single folder.

Required attributes: 

- `id`          Automatically assigned
- `name`
- `description`

Optional attributes:
- `parent`      ID of folder that is the parent. Set to 0 if no parent
- `meta`        A catch-all attribute to add custom features

+ Parameters
    + id (required, int) ... Unique folder ID in the form of an integer

+ Model (application/hal+json)

    + Body

            {
                "id": 1,
                "name": "Health",
                "description": "This represents projects that are related to health"
                "parent": 0,
                "meta": "NULL"
            }
            
## Retrieve a single Folder [GET]

+ Response 200 (application/json)

    [Folder][]
    
+ Response 404 (application/json)

        { 
            "error": "Resource not found" 
        }
    
### Edit a Folder [PATCH]

+ Request (application/json)

        {
            "description": "A collection of health related projects",
        }

+ Response 200
    
    [Folder][]

+ Response 404

        { 
            "error": "Resource not found"
        }

+ Response 400

        { 
            "error": "Resource modification failed"
        }

## Delete a Folder [DELETE]

+ Response 200

        { 
            "result": True
        }

## Create a Folder [POST]

+ Request (application/json)

        {
            "name": "Diet",
            "description": "A collection of projects related to Diet",
            "parent": 1
        }

+ Response 201

    [Folder][]
    
+ Response 400

        { 
            "error": "Resource modification failed"
        }

# Folder Collection [/folder]
Get all of the Folders.

+ Model (application/hal+json)

    + Body

            {
                "folders": [
                    {
                        "id": 1,
                        "name": "Health",
                        "description": "This represents projects that are related to health"
                        "parent": 0,
                        "meta": "NULL"
                    },
                    {
                        "id": 1,
                        "name": "Diet",
                        "description": "A collection of projects related to Diet",
                        "parent": 1,
                        "meta": "NULL"
                    }
                ]
            }



## List all Folders [GET]

+ Response 200

    [Folder Collection][]
