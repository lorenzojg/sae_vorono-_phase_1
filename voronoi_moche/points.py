from point import Point
from errors.NotEnoughPointsError import NotEnoughPointsError

class Points():

    def __init__(self,donnees:list[dict[str,str]]=None): # type: ignore
        self._liste_points : list[Point] = []
        if donnees is not None :
            for element in donnees :
                for x,y in element.items():
                    new_point = Point(float(x),float(y))
                    self._liste_points.append(new_point)
    
    def ajout_from_point(self,point:"Point"):
        self._liste_points.append(point)

    def ajout_from_coordonates(self,x:float,y:float):
        new_point = Point(x,y)
        self._liste_points.append(new_point)

    # ----

    def get_extrumum_points_of_cadrillage(self):
        if len(self._liste_points)<2:
            raise NotEnoughPointsError("Il n'y a pas assez de points dans la liste pour calculer un cadrillage.")
        
        point_min : Point = Point()
        point_max : Point = Point()
        is_first_iteration : bool = True

        for point in self._liste_points:
            if is_first_iteration :
                point_min, point_max = point,point
                is_first_iteration = False
            else :
                if point.x < point_min.x or point.y < point_min.y :
                    point_min = point
                elif point.x > point_max.x or point.y > point_max.y :
                    point_max = point
    
        coordonnees_cadrillage = Points()
        coordonnees_cadrillage.ajout_from_coordonates(point_min.x, point_min.y)
        coordonnees_cadrillage.ajout_from_coordonates(point_max.x,point_max.y)

        return coordonnees_cadrillage


    @property
    def liste_points(self):
        return self._liste_points