def paginate(query, skip: int = 0, limit: int = 100):
    return query.offset(skip).limit(limit)
