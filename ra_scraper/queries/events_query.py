EVENTS_QUERY = """
    query GET_POPULAR_EVENTS($filters: FilterInputDtoInput, $pageSize: Int) {
    eventListings(
        filters: $filters
        pageSize: $pageSize
        page: 1
        sort: { attending: { priority: 1, order: DESCENDING } }
    ) {
        data {
        id
        listingDate
        event {
            ...eventFields
            __typename
        }
        __typename
        }
        __typename
    }
    }
    fragment eventFields on Event {
    id
    title
    attending
    date
    contentUrl
    flyerFront
    queueItEnabled
    newEventForm
    cost
    images {
        id
        filename
        alt
        type
        crop
        __typename
    }
    venue {
        id
        name
        contentUrl
        live
        __typename
    }
    artists {
        id
        contentUrl
        name
        facebook
        soundcloud
        instagram
        twitter
        followerCount
        country {
        id
        name
        urlCode
        }
        residentCountry {
        id
        name
        urlCode
        }
    }
    genres {
        id
        name
        slug
        __typename
    }
    __typename
    }
"""
