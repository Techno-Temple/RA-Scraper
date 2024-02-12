LOCATIONS_QUERY = """
    query GET_ALL_LOCATIONS_QUERY {
    countries {
        id
        name
        urlCode
        topCountry
        order
        areas {
        id
        name
        isCountry
        urlName
        parentId
        subregion {
            id
            name
            urlName
            country {
            id
            name
            urlCode
            __typename
            }
            __typename
        }
        country {
            id
            name
            urlCode
            __typename
        }
        __typename
        }
        __typename
    }
    }
"""
