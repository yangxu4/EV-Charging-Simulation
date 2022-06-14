# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 21:02:24 2022
Data of charging station and electric vehicles
@author: XU Yang
"""
from shapely.geometry import Polygon, Point
import numpy as np

# The 30 polygons represent the 30 regions in King county
poly_1 = Polygon([(47.346987, -122.242515),
                  (47.346987, -122.077033),
                  (47.245001, -122.077033),
                  (47.245001, -122.242515)])

poly_2 = Polygon([(47.644980, -122.230492), (47.579376, -122.184634),
                  (47.644980, -122.184634), (47.579376, -122.230492)])

poly_3 = Polygon([(47.640900, -122.183788),(47.552460, -122.183788),
                 (47.640900, -122.104481),(47.552460, -122.104481)])

poly_4 = Polygon([(47.343152, -122.052915), (47.341855, -121.997401),
                  (47.287833, -122.047650), (47.288157, -121.986633)])

poly_5 = Polygon([(47.776427, -122.227520), (47.734188, -122.170356),
                 (47.776427, -122.170356), (47.734188, -122.227520)])

poly_6 = Polygon([(47.654226, -121.926806), (47.654434, -121.890720),
                 (47.639335, -121.925367), (47.639058, -121.891542)])

poly_7 = Polygon([(47.751783, -121.995996), (47.751575, -121.945105), 
                  (47.725094, -121.996818), (47.723918, -121.944591)])

poly_8 = Polygon([(47.275615, -122.105463) ,(46.998617, -121.328028),
                 (47.275615, -121.328028) ,(46.998617, -122.105463)])

poly_9 = Polygon([(47.603204, -121.964008), (47.539969, -121.843845),
                 (47.603204, -121.843845), (47.539969, -121.964008)])

poly_10 = Polygon([(47.639058, -121.891542),(47.639058,-122.293503),
                  (47.257966,-121.891542),(47.257966, -122.293503)])

poly_11 = Polygon([(47.570346, -122.097348),(47.570346,-121.980275),
                  (47.523767,-122.097348),(47.523767, -121.980275)])

poly_12 = Polygon([(47.776865, -122.270298),(47.776865,-122.229271),
                  (47.728622,-122.270298),(47.728622, -122.229271)])

poly_13 = Polygon([(47.423446, -122.278997),(47.423446,-122.146352),
                  (47.349057,-122.278997),(47.349057, -122.146352)])

poly_14 = Polygon([(47.726850, -122.247896),(47.726850,-122.165499),
                  (47.647346,-122.247896),(47.647346, -122.165499)])

poly_15 = Polygon([(47.391957, -122.059882),(47.391957,-122.017025),
                  (47.344416,-122.059882),(47.344416, -122.017025)])

poly_16 = Polygon([(47.751437, -121.995688), (47.750124, -121.945516), 
                   (47.727515, -121.996202), (47.721662, -121.953598)])

poly_17 = Polygon([(47.592642, -122.253292), (47.592642, -122.210592), 
                   (47.537259, -122.253292), (47.537259, -122.210592)])

poly_18 = Polygon([(47.512724, -121.813039), (47.512724, -121.759746), 
                   (47.478256, -121.813039), (47.478256, -121.759746)])

poly_19 = Polygon([(47.274736, -122.262547), (47.272835, -122.229063), 
                   (47.243301, -122.259892), (47.243201, -122.246764)])

poly_20 = Polygon([(47.374788, -122.011393), (47.368045, -121.921099), 
                   (47.344438, -122.017229), (47.336179, -121.934832)])

poly_21 = Polygon([(47.707802, -122.162601), (47.707802, -121.966141), 
                   (47.630013, -122.162601), (47.630013, -121.966141)])

poly_22 = Polygon([(47.503232, -122.243578), (47.503232, -122.150052), 
                   (47.431778, -122.243578), (47.431778, -122.150052)])

poly_23 = Polygon([(47.650013, -122.088020), (47.650013, -121.973288), 
                   (47.577730, 122.088020), (47.577730, -121.973288)])

poly_24 = Polygon([(47.650288, -122.364147), (47.632544, -122.320193), 
                   (47.596794, -122.336130), (47.599290, -122.316734)])

poly_25 = Polygon([(47.481460, -122.361443), (47.476607, -122.219405), 
                   (47.396504, -122.324452), (47.396790, -122.219899)])

poly_26 = Polygon([(47.783152, -122.395437), (47.775447, -122.282221),
                   (47.670165, -122.411786), (47.658978, -122.269522)])

poly_27 = Polygon([(47.596849, -122.391311), (47.587835, -122.285774), 
                   (47.498172, -122.376274), (47.495726, -122.260155)])

poly_28 = Polygon([(47.552149, -121.893776), (47.544733, -121.714562), 
                   (47.485372, -121.885537), (47.485372, -121.814812)])

poly_29 = Polygon([(47.510118, -122.477813), (47.467166, -122.432838), 
                   (47.337575, -122.523984), (47.384948, -122.381819)])

poly_30 = Polygon([(47.775816, -122.174721), (47.775816, -122.112213), 
                   (47.733930, -122.176161), (47.733515, -122.135242)])
# number of EVs in each region
ev_num = [645, 1307, 2737, 92, 404, 144, 239, 88, 105, 429,
     1344, 427, 974, 2254, 449, 171, 1067, 243, 24, 30,
     2717, 1085, 1941, 1808, 371, 4809, 3218, 299, 310, 
     1082]

total_ev = np.array(ev_num).sum()

# number of CSs in each region
cs_num = [22, 105, 75, 0, 19, 0, 5, 1, 1, 10, 26, 3, 17, 34,
     1, 0, 15, 4, 0, 0, 26, 50, 8, 241, 41, 63, 56, 5, 1, 17]

cs_locations = [[47.300908, -122.179686], 
                [47.615513, -122.201697], 
                [47.592994, -122.147396], 
                [0,0], 
                [47.759120, -122.198509], 
                [0,0],
                [47.735422, -121.951604], # location in Duvall
                [47.203640, -121.981914], 
                [47.568155, -121.899905], 
                [47.314791, -122.330582], 
                [47.544860, -122.037266], 
                [47.755057, -122.245750],
                [47.390727, -122.213474], 
                [47.698437, -122.192278], 
                [47.368361, -122.037566], 
                [0,0], 
                [47.574182, -122.221729],
                [47.496314, -121.789050],
                [0,0], 
                [0,0], 
                [47.674618, -122.107283], 
                [47.482586, -122.193796], 
                [47.612667, -122.035559], 
                [47.619934, -122.339929],
                [47.438770, -122.273096], 
                [47.720433, -122.326273], 
                [47.537883, -122.315674], 
                [47.523933, -121.830496], 
                [47.428400, -122.466659], 
                [47.757434, -122.153954]] 

poly_set = [poly_1, poly_2, poly_3, poly_4, poly_5, 
            poly_6, poly_7, poly_8, poly_9, poly_10, 
            poly_11, poly_12, poly_13, poly_14, poly_15, 
            poly_16, poly_17, poly_18, poly_19, poly_20, 
            poly_21, poly_22, poly_23, poly_24, poly_25, 
            poly_26, poly_27, poly_28, poly_29, poly_30]