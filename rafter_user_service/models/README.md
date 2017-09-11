API
==========

Browse it at: `/api/`. Currently serving:

```
{
    "projects": "/api/projects/",
    "observations": "/api/observations/",
    "investigations": "/api/investigations/",
    "project_states": "/api/project_states/",
    "teams": "/api/teams/"
}
```

## Get

- **All projects**: `/api/projects/`

```
[
    {
        "id": 1,
        "description": "Lorem ipsum et al",
        "team": 1,
        "project_state": 1,
        "created_by": "admin",
        "modified_by": "admin",
        "date_created": "2017-09-07T19:04:35.629296Z",
        "last_modified": "2017-09-07T19:04:35.629340Z"
    },
    ...
```

- **Single project** `/api/projects/1/`

```
{
    "id": 1,
    "description": "Lorem ipsum et al",
    "team": 1,
    "project_state": 1,
    "created_by": "admin",
    "modified_by": "admin",
    "date_created": "2017-09-07T19:04:35.629296Z",
    "last_modified": "2017-09-07T19:04:35.629340Z"
}
```

- **Observations for a project**: `/api/observations/?project=1`

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

Send a POST with JSON data that looks like the GET responses, but leave out auto-generated fields. 

- **Create a new Observation**: POST to `/api/observations` (`id, created_by, modified_by, date_created, last_modified` are not included again):

```
{
    "comment": "An observation about project 1",
    "project": 1,
}
```

## Update

Send a PUT with new JSON data to the single item URL.

- **Update Observation** with ID 6: send PUT to `/api/observations/6/` with data:

```
{
    "comment": "Edited observation about project 1",
    "project": 1,
}
```

## Delete

Send a DELETE to the single item URL.

- **Delete Observation** with ID 6: send DELETE to `/api/observations/6/`
