# API Exploration

This document describes how to use httpie to explore the API of projectfacts.

## Create a new device
This creates a new device named `pf-tui` with the type `de.fivepoint.other`. A device corresponds to a personal application. The device is associated with the user's account.

```shell
http POST $PF_BASE_URL/api/device \
  email=$PF_USER \
  password=$PF_PASSWORD
  deviceName='pf-tui' \
  deviceType='de.fivepoint.other' \
  'Cookie:cookie1=value1; cookie2=value2'
```

The variables `$PF_BASE_URL`, `$PF_USER`, and `$PF_PASSWORD` must be set in the environment. The `Cookie` header is optional but might be required for authentication if the API is protected by an SSO login. You can get the cookies by logging in to the web application and inspecting the network requests. Make sure the format is the same as in the example.

**Response**

If the input was correct, the response will look like this:

```json
{
    "_id": 72562433,
    "_idKey": "131",
    "_url": "https://**********/api/device/72562433",
    "apiHost": "https://**********/api",
    "deviceName": "pf-tui",
    "deviceType": "unknown",
    "externalAccess": false,
    "token": "YUrABDzPrfqQ12mC3EtQMImDB",
    "user": {
        "caption": "Your Name",
        "href": "https://**********/api/user/55373544",
        "idKey": "301",
        "title": "user",
        "value": 55903044
    }
}
```

The `_id` and the `token` fields are important and will only be displayed once. They will be used as basic authentication user name and password
for future call to the API.

## First API Call
When executing the first real API request you need to pass the device ID and the token as basic authentication credentials (as well as the cookies).
If you also pass the `session` option, a session file will be created and you don't need to pass the authentication credentials and cookies in subsequent API calls anymore:

```shell
http --session=./pf-session.json \
  -a "72562433:YUrABDzPrfqQ12mC3EtQMImDB" \
  GET $PF_BASE_URL/api/api \
  'Cookie:cookie1=value1; cookie2=value2'
```

This call is a dummy call to generate the session file, it only returns a list of the existing API endpoints.

## Filters and Queries
*projectfacts* offers filtering options by appending URL parameters separtated by `;`, e.g.

```shell
http --session=./pf-session.json \
  GET $PF_BASE_URL/api/time\;limit\=1\;sort\=\!lastModifiedDate
```

This query returns the most recent time entry.

**Response**

```json
{
    "_etag": {
        "value": "410d42193e38f08c7a4ce370adb75397",
        "weak": false
    },
    "_links": [
        {
            "caption": "Self",
            "href": "https://**********/api/time;limit=1;sort=!lastModifiedDate",
            "rel": "self"
        },
        {
            "caption": "|< firstPage",
            "href": "https://**********/api/time;offset=0;limit=1;sort=!lastModifiedDate",
            "rel": "first",
            "title": "First page of times of this CollectionResource"
        },
        {
            "caption": "> nextPage",
            "href": "https://**********/api/time;offset=1;limit=1;sort=!lastModifiedDate",
            "rel": "successor",
            "title": "Next page of times of this CollectionResource"
        },
        {
            "caption": ">| lastPage",
            "href": "https://**********/api/time;offset=2615;limit=1;sort=!lastModifiedDate",
            "rel": "last",
            "title": "Last page of times of this CollectionResource"
        }
    ],
    "_url": "https://**********/api/time;limit=1;sort=!lastModifiedDate",
    "items": [
        {
            "caption": "Dummy description",
            "href": "https://**********/api/time/93556479",
            "idKey": "20",
            "lastModifiedDate": "2024-02-08T14:37:30.000+00:00",
            "rel": "link",
            "title": "referenced resource",
            "value": 90213479
        }
    ],
    "limit": 1,
    "offset": 0,
    "size": 2615
}
```

It is also possible to query for values of a specific field, e.g.

```shell
http --session=./pf-session.json \
  GET $PF_BASE_URL/api/time\?date="2023-11-29"
```

This query returns all time entries for the date `2023-11-29`.

**Response**

```json
{
    "_etag": {
        "value": "d8ac8f22320088d548e03d4298703096",
        "weak": false
    },
    "_links": [
        {
            "caption": "Self",
            "href": "https://**********/api/time?date=2023-11-29",
            "rel": "self"
        },
        {
            "caption": "|< firstPage",
            "href": "https://**********/api/time;offset=0?date=2023-11-29",
            "rel": "first",
            "title": "First page of times of this CollectionResource"
        },
        {
            "caption": ">| lastPage",
            "href": "https://**********/api/time;offset=0?date=2023-11-29",
            "rel": "last",
            "title": "Last page of times of this CollectionResource"
        }
    ],
    "_url": "https://**********/api/time?date=2023-11-29",
    "items": [
        {
            "caption": "Dummy description 1",
            "href": "https://**********/api/time/90104272",
            "idKey": "30",
            "lastModifiedDate": "2023-11-29T17:13:07.000+00:00",
            "rel": "link",
            "title": "referenced resource",
            "value": 90104272
        },
        {
            "caption": "Dummy description 2",
            "href": "https://**********/api/time/40124078",
            "idKey": "30",
            "lastModifiedDate": "2023-11-29T17:18:13.000+00:00",
            "rel": "link",
            "title": "referenced resource",
            "value": 40124078
        },
        {
            "caption": "Dummy description 3",
            "href": "https://**********/api/time/22103980",
            "idKey": "30",
            "lastModifiedDate": "2023-11-29T17:18:38.000+00:00",
            "rel": "link",
            "title": "referenced resource",
            "value": 22103980
        }
    ],
    "limit": 100,
    "offset": 0,
    "size": 3
}
```

## Model of a Time Entry

The following API call querys a specific time entry by its ID:

```shell
http --session=./pf-session.json \
  GET $PF_BASE_URL/api/time/81225679
```

**Response**

```json
{
    "_id": 81225679,
    "_idKey": "30",
    "_lastModifiedDate": "2024-02-08T14:37:30.000+00:00",
    "_links": [
        {
            "caption": "Self",
            "href": "https://**********/api/time/81225679",
            "rel": "self",
            "title": "Default URL of this resource"
        },
        {
            "caption": "Collection",
            "href": "https://**********/api/time",
            "rel": "collection",
            "title": "Default collection containing this resource"
        }
    ],
    "_url": "https://**********/api/time/81225679",
    "amount": 420,
    "amountBillable": 420,
    "area": {
        "caption": "dummy area",
        "href": "https://**********/api/timecategory/35012884",
        "idKey": "28",
        "optionsUrl": "https://**********/api/timecategory?categoryType=2",
        "title": "area of activity (timecategory type 2)",
        "value": 35012884
    },
    "begin": "2024-02-08T07:00:00.000+00:00",
    "color": null,
    "comment": null,
    "contact": null,
    "contractposition": null,
    "costcenterAuto": null,
    "costcenterOverride": null,
    "costtypeAuto": null,
    "costtypeOverride": null,
    "costunitAuto": null,
    "costunitOverride": null,
    "date": "2024-02-08",
    "description": "Dummy description",
    "end": "2024-02-08T14:45:00.000+00:00",
    "field": {
        "caption": "Remote Work",
        "href": "https://**********/api/timecategory/63129277",
        "idKey": "22",
        "optionsUrl": "https://**********/api/timecategory?categoryType=1",
        "title": "field of activity (timecategory type 1)",
        "value": 63129277
    },
    "hourlyRateExternal": 100.0,
    "invoiceposition": null,
    "project": {
        "caption": "Dummy Project",
        "href": "https://**********/api/project/70421959",
        "idKey": "21",
        "optionsUrl": "https://**********/api/project;parent=70417931;evaluate=isBookable?isActive=true&isTemplate=false&isDraft=false&projectStateType=2",
        "path": "Dummy/Path/To/Project",
        "title": "project",
        "value": 70421959
    },
    "referenceNumber": null,
    "ticket": null,
    "timetemplate": null,
    "worker": {
        "caption": "My Name",
        "href": "https://**********/api/user/65783514",
        "idKey": "901",
        "optionsUrl": "https://**********/api/user",
        "title": "coworker",
        "value": 65783514
    }
}
```

## Create a new Time Entry

The following API call creates a new time entry by sending a JSON object with the required fields:

```shell
http --session=./pf-session.json \
  POST $PF_BASE_URL/api/time < time.json
```

The file `time.json` contains the following JSON object:

```json
{
  "date": "2024-02-09",
  "begin": "2024-02-09T07:00:00.000+00:00",
  "end": "2024-02-09T15:00:00.000+00:00",
  "description": "This is a test",
  "area": {
    "value": 35012884
  },
  "field": {
    "value": 63129277
  },
  "project": {
    "value": 70421959
  }
}
```

The values for `area`, `field`, and `project` are the IDs of the corresponding objects from the previous API call. The `value` field is the ID of the object.

