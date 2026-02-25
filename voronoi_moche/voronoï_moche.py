import matplotlib.pyplot as plt
import numpy as np
from points import Points
from point import Point
from json import load
from math import sqrt

#coucou les loulou ça marche !!!

def json_loader(chemin:str="liste_de_sites.json"):

    with open(chemin, "r", encoding="utf-8") as fp:
        données = load(fp)

    return données

def afficher_point(fig,points:Points):
    for point in points.liste_points :
        plt.plot(point.x,point.y)
    
def grillage(fig,extremum_cadrillage:Points):
    ax = fig.add_subplot(1, 1, 1)


    point_min = extremum_cadrillage.liste_points[0]
    point_max = extremum_cadrillage.liste_points[1]
    
    plt.xlim(point_min.x,point_max.x)
    plt.ylim(point_min.y,point_max.y)

    grid_x_ticks = np.arange(point_min.x, point_max.x, 0.1)
    grid_y_ticks = np.arange(point_min.y, point_max.y, 0.1)

    ax.set_xticks(grid_x_ticks , minor=True)
    ax.set_yticks(grid_y_ticks , minor=True)

    ax.grid(which='both')

    ax.grid(which='minor', alpha=0.2, linestyle='--')
    

def calculer_distance(x:Point, y:Point, p1, p2):
    return sqrt(abs(x-p1)**2 + abs(y-p2)**2)

def voronoi_moche(fig,liste_points:Points):
    pass

if __name__ == "__main__":
    
    fig = plt.figure()

    donnees_points_brutes = json_loader()
    points = Points(donnees_points_brutes)

    afficher_point(fig,points)

    cadrillage_extremum = points.get_extrumum_points_of_cadrillage()
    grillage(fig,cadrillage_extremum)

    voronoi_moche(fig,points)

    plt.savefig("matplotlib_grid_01.png", bbox_inches='tight')

    plt.close()