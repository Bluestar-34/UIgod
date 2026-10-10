"""Compile catalog.json from style metadata, pinned collections and editorial.json."""
from library_data import build
if __name__=='__main__':
    result=build()
    print('Catalog built:',len(result['entries']),'entries')
