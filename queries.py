# PANAMA
# NAME OF ENTITIES
ENTITIES = '''
MATCH (e:Entity)
RETURN e.name as name LIMIT $limit
'''
