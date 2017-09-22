API
==========

Browse it at: `/api/`. Currently serving:

```
{
    "analyses": "/api/analyses/",
    "experiments": "/api/experiments/",
    "hypotheses": "/api/hypotheses/",
    "investigations": "/api/investigations/",
    "mechanisms": "/api/mechanisms/",
    "observations": "/api/observations/",
    "projects": "/api/projects/",
    "teams": "/api/teams/",
    "theories": "/api/theories/"
}
```

## GET

- *All projects*: `/api/projects/` (Note: projects expand nested relations [`team` and `project_state`] for GET requests but required IDs only for POSTs).

```
[
    {
        "description": "A stub project",
        "team": {
            "name": "Testing Team",
            "description": "Team for testing",
            "location": "The cloud",
            "website": "dac.cs.vt.edu",
            "affiliation": "VT",
            "created_by": "admin",
            "modified_by": "admin",
            "id": 1,
            "date_created": "2017-09-11T16:05:19.722000Z",
            "last_modified": "2017-09-11T16:05:19.722000Z"
        },
        "project_state": {
            "name": "READY",
            "description": "State for ready things"
        },
        "investigations": [
            "http://localhost:8000/api/investigations/1/",
            "http://localhost:8000/api/investigations/2/"
        ],
        "id": 1,
        "created_by": "admin",
        "modified_by": "admin",
        "date_created": "2017-09-11T16:06:36.878000Z",
        "last_modified": "2017-09-11T16:06:36.878000Z"
    },
    ...
```

- Get only the *project with `ID=1`* at `/api/projects/1/`

- *Observations for a project*: `/api/observations/?project=1`

```
[
    {
        "comment": "I think this project is great",
        "project": 1,
        "date_created": "2017-09-07T18:35:33.439871Z",
        "last_modified": "2017-09-07T18:35:33.439900Z",
        "created_by": "admin",
        "modified_by": "admin"
    },
    ...
```

## Create

Send a POST with JSON data that looks like the GET responses, but leave out auto-generated fields (these are usually `id`, `created_by`, `modified_by`, `date_created`, `last_modified`).

- *Create a new Project*: POST the following to `/api/projects`

```
{
    "description": "Here is a new project",
    "team": 1,
    "project_state": 2
}
```

- *Create a new Observation*: POST to the following `/api/observations`

```
{
    "comment": "An observation about project 1",
    "project": 1,
}
```

## Update

Send a PUT with new JSON data to the single item URL.

- *Update Observation* with ID 6: send PUT to `/api/observations/6/` with data:

```
{
    "comment": "Edited observation about project 1",
    "project": 1,
}
```

## Delete

Send a DELETE to the single item URL.

- *Delete Observation* with ID 6: send DELETE to `/api/observations/6/`


## Testing data

Load some sample data into the database with `./manage.py loaddata rafter_user_service/initial_data.json`

This will make an admin user with password `correcthorsebatterystaple`.
