import rasterio as rio

def loading_tile(tile, dsm_or_dtm):
    try:
        #Path to the tile file
        path = "D:/3DHouseproject/"+dsm_or_dtm.upper()+"_split/tile_"+str(tile)+".tif"
        digital_map= rio.open(path, masked=True)
        return digital_map
    except AttributeError as error :
        print(error)
        print('Check the path to the file containing the tiles.')
        print('Did you correctly indicated "DSM" or "DTM" as the second argument ?')