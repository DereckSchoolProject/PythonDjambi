from abc import ABC


class Peons(ABC):
    """ Representation of peons. """

    def __init__(self, color: str):
        """ Initialize methode. """
        self._is_alive = True
        self._color = color
        self._icon: str

    def available_move(self):
        """ Return True if the peons can move, else return False. """
        """ Methods not implemented """
        return True

    def after_move(self):
        """ Action after move. """
        """ Methods not implemented """
        return True

    def get_icon(self):
        """ Getter of icon. """
        return self._icon

    def get_color(self):
        """ Getter of color. """
        return self._color

    def set_color(self, color: str):
        """ Setter of color. """
        self._color = color

    def get_is_alive(self):
        """ Getter of is_alive. """
        return self._is_alive

    def set_is_alive(self, is_alive: bool):
        """ Setter of is_alive. """
        self._is_alive = is_alive

    icon = property(get_icon)
    color = property(get_color, set_color)
    is_alive = property(get_is_alive, set_is_alive)


class Chief(Peons):
    """ Representation of chief peons.
    Le Chef peut se déplacer en diagonales et en colonnes ouvertes, sans limitation de distance. Il ne peut pas sauter par-dessus des pièces vivantes ou mortes.
    Il peut tuer des pièces ennemies, en se positionnant sur la case occupée par sa victime. La pièce est alors retournée, et son cadavre placé sur une case libre de l'échiquier (excepté la case centrale).
    C'est la seule pièce qui peut occuper durablement le Labyrinthe, obtroyant à son parti des privilèges souvent décisifs (concrètement, le joueur dont le chef est au pouvoir bénéficie d'un tour de jeu supplémentaire après chaque joueur, ou de deux tours simultanés s'il n'a plus qu'un seul adversaire).
    """

    _icon: str = "icons/chief.png"

    def available_move(self):
        """ Return True if the peons can move, else return False. """
        """ Methods not implemented """
        return True

    def after_move(self):
        """ Action after move. """
        """ Methods not implemented """
        return True


class Assasins(Peons):
    """ Representation of assassins peons.
    L'assassin se déplace en diagonales et le long de colonnes libres. Pour tuer, il prend la place d'une pièce et celle-ci est alors placée à la position initiale (au début de son tour de jeu) de l'assassin.
    Il peut tuer un chef occupant le Labyrinthe, lieu d'exercice du pouvoir. Mais il est totalement exclus qu'un personnage aussi scabreux qu'un assassin possédant du sang sur ses mains s'en vienne à régner : il bénéficie alors d'un tour simultané pour évacuer cette case centrale, sans possibilité d'interactions supplémentaires.
    """

    _icon: str = "icons/assassin.png"

    def available_move(self):
        """ Return True if the peons can move, else return False. """
        """ Methods not implemented """
        return True

    def after_move(self):
        """ Action after move. """
        """ Methods not implemented """
        return True


class Militant(Peons):
    """ Representation of militant peons.
    Contrairement aux autres pièces, les Militants voient leurs mouvements limités : ils ne peuvent pas avancer de plus de deux cases à chaque mouvement, en diagonale ou sur une colonne libre.
    Pour tuer, ils prennent la place d'une pièce. Celle-ci est alors retournée, et son cadavre placé sur n'importe quelle case du terrain (hormis la case centrale).
    Ils peuvent traverser le Labyrinthe vide, mais ne peuvent pas s'y arrêter, et il leur est impossible de tuer un Chef occupant cette case.
    """

    _icon: str = "icons/militant.png"

    def available_move(self):
        """ Return True if the peons can move, else return False. """
        """ Methods not implemented """
        return True

    def after_move(self):
        """ Action after move. """
        """ Methods not implemented """
        return True


class Reporter(Peons):
    """ Representation of reporter peons.
    Le Reporter se déplacement en diagonales, et le long de colonnes libres, sans limitation de distance. Il ne peut pas sauter par dessus des pièces mortes ou vivantes. Il ne peut pas occuper la case centrale du trône, mais peut déclencher un scandale compromettant irrémédiablement un chef au pouvoir (et permettant au Reporter de prétendre au prix Pulitzer). Dans ce cas, le cadavre du chef déchu vient obstruer le trône, rendant impossible toute action gouvernementale, et seule l'action d'un Nécromobile permettra de résorber cette situation.
    Il ne peut tuer qu'à l'issue d'un déplacement : une pièce ennemie peut venir à ses côtés sans être éliminée. Le Reporter lors de son tour de jeu devra effectuer un mouvement sur une éventuelle autre case adjacente pour déclencher un scandale.
    Si, à l'issue de son déplacement, le Reporter se trouve en contact avec plusieurs pièces ennemies, il devra choisir une victime. Son reportage ne peut impliquer qu'une seule personne (à moins d'être un Reporter de type Fox News, voir variante de règles ci-dessous).
    Si le Reporter venait à être déplacé par un Provocateur, il ne peut pas agir sur la pièce contigüe à la case où il aura été parachuté. Le Reporter n'agit donc que de son propre chef, à l'issue de déplacements orchestrés de longue main par les instances dirigeantes de son parti.
    """

    _icon: str = "icons/reporter.png"

    def available_move(self):
        """ Return True if the peons can move, else return False. """
        """ Methods not implemented """
        return True

    def after_move(self):
        """ Action after move. """
        """ Methods not implemented """
        return True


class Diplomat(Peons):
    """ Representation of diplomat peons.
    Le Provocateur se déplace en diagonales ou en colonnes ouvertes, sans limite de distance. Son déplacement est toutefois limité par les pièces vivantes et mortes. Il ne peut pas manipuler les pièces mortes : ce dégoutant travail de basse extraction n'est pas à la hauteur de son prestige, et est réservé au Nécromobile.
    Un Provocateur peut venir chasser un Chef au pouvoir, et le forcer à abdiquer, mettant ainsi fin à son règne despotique. Homme de l'ombre, sa place n'est toutefois pas au sommet de l'appareil d'État : il dispose alors d'un mouvement supplémentaire pour évacuer la case du trône. Lors de cette évacuation, il ne peut pas interagir avec d'autres pièces, et donc effectuer une autre manipulation (à moins que la variante de règle n°7 soit activée, voir ci-dessous).
    """

    _icon: str = "icons/diplomate.png"

    def available_move(self):
        """ Return True if the peons can move, else return False. """
        """ Methods not implemented """
        return True

    def after_move(self):
        """ Action after move. """
        """ Methods not implemented """
        return True


class Necromobile(Peons):
    """ Representation of necromobile peons.
    Le nécromobile se déplace en diagonales ou le long d'une colonne libre, sans limitation de distance. Il ne peut pas sauter par dessus des pièces vivantes et mortes. Son pouvoir de manipulation est réservé aux pièces mortes : il ne peut manipuler des vivants, honnête privilège réservé aux Diplomates.
    Un nécromobile ne peut stationner sur la case du trône. Mais il peut arriver en cours de partie qu'un Chef soit tué lors de l'exercice de son règne, et que son cadavre vienne obstruer la case du trône. Seul un nécromobile pourra alors résorber cette situation d'un pouvoir fantoche enseveli dans son Mausolée : il peut ainsi venir sur la case centrale, effectuer son office, et dispose alors d'un mouvement supplémentaire (sans possibilité d'interaction supplémentaire) pour évacuer le pouvoir. Il est en effet inconcevable de laisser un fossoyeur exercer les responsabilités suprêmes.
    """

    _icon: str = "icons/necromobile.png"

    def available_move(self):
        """ Return True if the peons can move, else return False. """
        """ Methods not implemented """
        return True

    def after_move(self):
        """ Action after move. """
        """ Methods not implemented """
        return True
