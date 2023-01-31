# A faire

## Pour tout le monde
faire un affichage d'un parcours en profondeur, permettant de représenter
l'arbre de façon arborescente.

l'affichage avec le programme tree.py doit donner le code suivant,
faire une méthode print_tree dans la class **Binary_tree**
<pre>
0/0
	3/1
		4/2
			5/3
				7/4
					8/5
				6/4
	2/1
</pre>

## Pour les personnes plus courageuses (facultatif)
Faire l'affichage suivant:
<pre>
    0/0
2/1     3/1
            4/2
                5/3
            6/4     7/4
                        85
</pre>
c'est plus tendu, informatiquement c'est pas plus compliqué que l'exercice 
précédent, par contre il faut bien réfléchir comment faire l'algorithme
qui permet de faire ce genre d'affichage.


## Pour aller plus loin (facultatif)
- faire une méthode qui permet de connaitre la taille de l'arbre
- faire une méthode qui permet de connaitre la hauteur de l'abre
- faire un arbre binaire de recherche :

Un **arbre binaire de recherche** est un arbre binaire dans lequel l'étiquette d'un nœud est appelé clé et est un entier. L'arbre binaire vérifie deux propriétés :

- Les clés de tous les nœuds du sous-arbre gauche d'un nœud x sont inférieures ou égales à la clé de x
- Les clés de tous les nœuds du sous-arbre droit d'un nœud x sont strictement supérieures à la clé de x.`


Le principe est le suivant on donne une liste de valeur aléatoire et l'arbre
de recherche les places selon les 2 règles précédentes.

Donc possiblement quand on ajoute un noeuds ils faut en décalé d'autres
on implémentera deux méthodes facile à coder trouvé le **min** et le **max** de 
l'arbre

Exemple d'arbre binaire de recherche :
<pre>
            32
        27      35
    16      30      36
</pre>
