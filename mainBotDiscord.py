import random   # nécessaire pour choisir aléatoirement une citation
import os   # nécessaire pour que le token du bot n'apparaisse pas en clair dans le code
import discord
from dotenv import load_dotenv  # nécessaire pour que le token du bot n'apparaisse pas en clair dans le code
from discord.ext import commands    # nécessaire pour que le bot réponde à la commande


load_dotenv(dotenv_path="config")   # indique dans quel fichier se trouve le token
bot = commands.Bot(command_prefix='.')  # indique que le bot répondra au caractère.


c1 = "On gouverne mieux les hommes par leurs vices que par leurs vertus.\nNapoléon Bonaparte\n1er Empereur des Français"
c2 = "L’avenir d’un enfant est l’œuvre de sa mère.\nNapoléon Bonaparte\n1er Empereur des Français"
c3 = "L’amour est une sottise faite à deux.\nNapoléon Bonaparte\n1er Empereur des Français"
c4 = "L’imagination gouverne le monde.\nNapoléon Bonaparte\n1er Empereur des Français"
c5 = "Ce que je cherche avant tout, c’est la grandeur : ce qui est grand est toujours beau.\nNapoléon Bonaparte\n1er Empereur des Français"
c6 = "Les hommes de génie sont des météores destinés à brûler pour éclairer leur siècle.\nNapoléon Bonaparte\n1er Empereur des Français"
c7 = "Ce n’est pas possible ; cela n’est pas Français.\nNapoléon Bonaparte\n1er Empereur des Français"
c8 = "La bonne politique est de faire croire aux peuples qu’ils sont libres.\nNapoléon Bonaparte\n1er Empereur des Français"
c9 = "Une société sans religion est comme un vaisseau sans boussole.\nNapoléon Bonaparte\n1er Empereur des Français"
c10 = "Le mensonge n'est bon à rien, puisqu'il ne trompe qu'une fois.\nNapoléon Bonaparte\n1er Empereur des Français"
c11 = "La sévérité prévient plus de fautes qu'elle n'en réprime.\nNapoléon Bonaparte\n1er Empereur des Français"
c12 = "Il faut vouloir vivre et savoir mourir.\nNapoléon Bonaparte\n1er Empereur des Français"
c13 = "La froideur est la plus grande qualité d'un homme destiné à commander.\nNapoléon Bonaparte\n1er Empereur des Français"
c14 = "Qui sait flatter sait aussi calomnier.\nNapoléon Bonaparte\n1er Empereur des Français"
c15 = "On déjoue beaucoup de choses en feignant de ne pas les voir.\nNapoléon Bonaparte\n1er Empereur des Français"
c16 = "L'homme n'est jamais si grand qu'à genoux devant Dieu.\nNapoléon Bonaparte\n1er Empereur des Français"
c17 = "En guerre comme en amour, pour en finir, il faut se voir de près.\nNapoléon Bonaparte\n1er Empereur des Français"
c18 = "Du sublime au ridicule, il n'y a qu'un pas.\nNapoléon Bonaparte\n1er Empereur des Français"
c19 = "Je sais, quand il le faut, quitter la peau du lion pour prendre celle du renard.\nNapoléon Bonaparte\n1er Empereur des Français"
c20 = "Le sot a un grand avantage sur l'homme d'esprit : il est toujours content de lui-même.\nNapoléon Bonaparte\n1er Empereur des Français"
c21 = "Le cœur d'un homme d'État doit être dans sa tête.\nNapoléon Bonaparte\n1er Empereur des Français"
c22 = "L'art d'être tantôt très audacieux et tantôt très prudent est l'art de réussir.\nNapoléon Bonaparte\n1er Empereur des Français"
c23 = "On ne conduit le peuple qu'en lui montrant un avenir : un chef est un marchand d'espérance.\nNapoléon Bonaparte\n1er Empereur des Français"
c24 = "L'habitude des faits les plus violents use moins le cœur que les abstractions : les militaires valent mieux que les avocats.\nNapoléon Bonaparte\n1er Empereur des Français"
c25 = "Il n'y a qu'un secret pour mener le monde, c'est d'être fort, parce qu'il n'y a dans la force ni erreur, ni illusion ; c'est le vrai, mis à nu.\nNapoléon Bonaparte\n1er Empereur des Français"
c26 = "La bravoure procède du sang, le courage vient de la pensée.\nNapoléon Bonaparte\n1er Empereur des Français"
c27 = "La noblesse aurait subsisté si elle s'était occupée davantage des branches que des racines.\nNapoléon Bonaparte\n1er Empereur des Français"
c28 = "Le général qui voit avec les yeux des autres n'est pas capable de commander une armée.\nNapoléon Bonaparte\n1er Empereur des Français"
c29 = "L'homme n'est qu'un animal plus parfait que les autres et qui raisonne mieux.\nNapoléon Bonaparte\n1er Empereur des Français"
c30 = "La haute politique n'est que le bon sens appliqué aux grandes choses.\nNapoléon Bonaparte\n1er Empereur des Français"
c31 = "Le grand art, c'est de changer pendant la bataille. Malheur au général qui arrive au combat avec un système.\nNapoléon Bonaparte\n1er Empereur des Français"
c32 = "Pour une femme qui nous inspire quelque chose de bon, il y a en cent qui nous font faire des sottises.\nNapoléon Bonaparte\n1er Empereur des Français"
c33 = "Un homme combattra plus pour ses intérêts que pour ses droits.\nNapoléon Bonaparte\n1er Empereur des Français"
c34 = "Un bon croquis vaut mieux qu’un long discours.\nNapoléon Bonaparte\n1er Empereur des Français"
c35 = "L'impossible est le refuge des poltrons.\nNapoléon Bonaparte\n1er Empereur des Français"
c36 = "L'intelligence ne se mesure pas des pieds à la tête, mais de la tête au ciel.\nNapoléon Bonaparte\n1er Empereur des Français"
c37 = "La pauvreté, les privations et la misère sont l'école du bon soldat.\nNapoléon Bonaparte\n1er Empereur des Français"
c38 = "La haute tragédie est l'école des grands hommes ; elle doit être celle des rois et des peuples ; c'est le point le plus élevé auquel un poète puisse parvenir.\nNapoléon Bonaparte\n1er Empereur des Français"
c39 = "Notre ridicule défaut national est de n'avoir pas de plus grand ennemi de nos succès et de notre gloire que nous-mêmes.\nNapoléon Bonaparte\n1er Empereur des Français"
c40 = "La France, c'est le Français quand il est bien écrit.\nNapoléon Bonaparte\n1er Empereur des Français"
c41 = "Les peuples passent, les trônes s'écroulent, l'église demeure.\nNapoléon Bonaparte\n1er Empereur des Français"
c42 = "Dieu, lui aussi, a essayé de faire des ouvrages. Sa prose, c'est l'homme. Sa poésie, c'est la femme.\nNapoléon Bonaparte\n1er Empereur des Français"
c43 = "Il est dans le caractère Français d'exagérer, de se plaindre et de tout défigurer dès qu'on est mécontent.\nNapoléon Bonaparte\n1er Empereur des Français"
c44 = "La supériorité de Mahomet est d'avoir fondé une religion en se passant de l'enfer.\nNapoléon Bonaparte\n1er Empereur des Français"
c45 = "Une belle femme plaît aux yeux, une bonne femme plaît au cœur ; l'une est un bijou, l'autre un trésor.\nNapoléon Bonaparte\n1er Empereur des Français"
c46 = "Les règlements sont faits pour les soldats et non pour les guerriers ; la bataille se rit du code, elle en exige un nouveau, innové par elle et pour elle et qui disparaît dès qu’elle est terminée.\nNapoléon Bonaparte\n1er Empereur des Français"
c47 = "La première des vertus est le dévouement à la patrie.\nNapoléon Bonaparte\n1er Empereur des Français"
c48 = "Dans tout ce qu'on entreprend, il faut donner les deux tiers à la raison et l'autre tiers au hasard. Augmentez la première fraction, et vous serez pusillanime. Augmentez la seconde, vous serez téméraire.\nNapoléon Bonaparte\n1er Empereur des Français"
c49 = "Le doute est l'ennemi des grandes entreprises.\nNapoléon Bonaparte\n1er Empereur des Français"
c50 = "La morale est bien souvent le passeport de la médisance.\nNapoléon Bonaparte\n1er Empereur des Français"
c51 = "J'ai fait mes plans avec les rêves de mes soldats endormis.\nNapoléon Bonaparte\n1er Empereur des Français"
c52 = "On ne peut pas faire semblant d’être courageux.\nNapoléon Bonaparte\n1er Empereur des Français"
c53 = "N'interrompez jamais un ennemi qui est en train de commettre une erreur.\nNapoléon Bonaparte\n1er Empereur des Français"
c54 = "Il y a des gens qui se croient le talent de gouverner par la seule raison qu'ils gouvernent.\nNapoléon Bonaparte\n1er Empereur des Français"
c55 = "La mort n'est rien, mais vivre vaincu et sans gloire, c'est mourir tous les jours.\nNapoléon Bonaparte\n1er Empereur des Français"
c56 = "Quand on veut, on peut, quand on peut, on doit.\nNapoléon Bonaparte\n1er Empereur des Français"
c57 = "Lorsqu'un gouvernement est dépendant des banquiers pour l'argent, ce sont ces derniers, et non les dirigeants du gouvernement qui contrôlent la situation, puisque la main qui donne est au-dessus de la main qui reçoit.\nNapoléon Bonaparte\n1er Empereur des Français"
c58 = "L'argent n'a pas de patrie ; les financiers n'ont pas de patriotisme et n'ont pas de décence ; leur unique objectif est le gain.\nNapoléon Bonaparte\n1er Empereur des Français"
c59 = "Le succès ne s'explique pas. L'échec ne s'excuse pas.\nNapoléon Bonaparte\n1er Empereur des Français"
c60 = "Si mon chapeau connaissait mon plan, je le mangerais.\nNapoléon Bonaparte\n1er Empereur des Français"
c61 = "Je n'ai jamais fait de conquêtes qu'en me défendant. L'Europe n'a jamais cessé de combattre la France à cause de ses principes. J'étais forcé d'abattre sous peine d'être abattu.\nNapoléon Bonaparte\n1er Empereur des Français"
c62 = "L'artiste a le pouvoir de réveiller la force d'agir qui sommeille dans d'autres âmes.\nFriedrich Nietzsche\nPhilosophe Allemand"
c63 = "Le poison dont meurt une nature plus faible est un fortifiant pour le fort.\nFriedrich Nietzsche\nPhilosophe Allemand"
c64 = "La moralité, c'est l'instinct du troupeau chez l'individu.\nFriedrich Nietzsche\nPhilosophe Allemand"
c65 = "Celui qui se sait profond s'efforce d'être clair ; celui qui voudrait sembler profond à la foule s'efforce d'être obscur.\nFriedrich Nietzsche\nPhilosophe Allemand"
c66 = "Tous les épuisés maudissent le soleil : Pour eux la valeur des arbres - C'est l'ombre !\nFriedrich Nietzsche\nPhilosophe Allemand"
c67 = "Un grand but vous rend supérieur, non seulement à vos actions et à vos juges, mais à la justice elle-même.\nFriedrich Nietzsche\nPhilosophe Allemand"
c68 = "Parfois, les gens ne veulent pas entendre la vérité parce qu'ils ne veulent pas que leurs illusions les détruisent.\nFriedrich Nietzsche\nPhilosophe Allemand"
c69 = "Ce qu'on fait n'est jamais compris, mais seulement loué ou blâmé.\nFriedrich Nietzsche\nPhilosophe Allemand"
c70 = "Toute habitude rend notre main plus ingénieuse et notre génie plus maladroit.\nFriedrich Nietzsche\nPhilosophe Allemand"
c71 = "Où se trouve ton plus grand danger ? Dans la pitié.\nFriedrich Nietzsche\nPhilosophe Allemand"
c72 = "Le châtiment est fait pour améliorer celui qui châtie.\nFriedrich Nietzsche\nPhilosophe Allemand"
c73 = "Que dit ta conscience ? Tu dois devenir l'Homme que tu es.\nFriedrich Nietzsche\nPhilosophe Allemand"
c74 = "Ce sont les paroles les moins tapageuses qui suscitent la tempête et les pensées qui mènent le monde viennent sur des pattes de colombe.\nFriedrich Nietzsche\nPhilosophe Allemand"
c75 = "Bonne mâchoire et bon estomac - C'est ce que je te souhaite ! Et quand tu auras digéré mon livre, Tu t'entendras certes avec moi !\nFriedrich Nietzsche\nPhilosophe Allemand"
c76 = "Quand on veut remuer la foule ne doit-on pas être son propre comédien ?\nNe doit-on pas nécessairement se transposer d'abord soi-même sur le plan d'une précision grotesque pour donner et sa cause et tout son personnage sous cette forme simplifiée et grossie.\nFriedrich Nietzsche\nPhilosophe Allemand"
c77 = "Celui qui sait commander trouve toujours ceux qui doivent obéir.\nFriedrich Nietzsche\nPhilosophe Allemand"
c78 = "L’homme a besoin de ce qu’il y a de pire en lui s’il veut parvenir à ce qu’il a de meilleur.\nFriedrich Nietzsche\nPhilosophe Allemand"
c79 = "La maturité de l’homme, c’est d’avoir retrouvé le sérieux qu’on avait au jeu quand on était enfant.\nFriedrich Nietzsche\nPhilosophe Allemand"
c80 = "Si ton œil était plus aigu tu verrais tout en mouvement.\nFriedrich Nietzsche\nPhilosophe Allemand"
c81 = "Qui vit de combattre un ennemi a tout intérêt de le laisser en vie.\nFriedrich Nietzsche\nPhilosophe Allemand"
c82 = "La conscience est la dernière et la plus tardive évolution de la vie organique, et par conséquent ce qu'il y a de moins accompli et de plus fragile en elle.\nFriedrich Nietzsche\nPhilosophe Allemand"
c83 = "Vouloir le vrai, c'est s'avouer impuissant à le créer.\nFriedrich Nietzsche\nPhilosophe Allemand"
c84 = "La femme n'est pas encore capable d'amitié : elle ne connaît que l'amour.\nFriedrich Nietzsche\nPhilosophe Allemand"
c85 = "Pour le fort rien n'est plus dangereux que la pitié.\nFriedrich Nietzsche\nPhilosophe Allemand"
c86 = "On veut la liberté aussi longtemps qu'on n'a pas la puissance ; mais si on a la puissance, on veut la suprématie.\nFriedrich Nietzsche\nPhilosophe Allemand"
c87 = "Dieu aussi a son enfer : c'est son amour des hommes.\nFriedrich Nietzsche\nPhilosophe Allemand"
c88 = "Ne dépouillez pas la femme de son mystère.\nFriedrich Nietzsche\nPhilosophe Allemand"
c89 = "L’État est le plus froid des monstres froids. Il ment froidement ; et voici le mensonge qui s’échappe de sa bouche : “Moi l’État, je suis le peuple.\nFriedrich Nietzsche\nPhilosophe Allemand"
c90 = "Dans la vengeance et en amour, la femme est plus barbare que l'homme.\nFriedrich Nietzsche\nPhilosophe Allemand"
c91 = "Croyez-moi ! Le secret pour récolter la plus grande fécondité, la plus grande jouissance de l'existence, consiste à vivre dangereusement !\nFriedrich Nietzsche\nPhilosophe Allemand"
c92 = "Celui qui ne veut agir et parler qu'avec justesse finit par ne rien faire du tout.\nFriedrich Nietzsche\nPhilosophe Allemand"
c93 = "L'architecte est une sorte d'oratoire de la puissance au moyen des formes.\nFriedrich Nietzsche\nPhilosophe Allemand"
c94 = "On n'attaque pas seulement pour faire du mal à quelqu'un mais peut-être aussi pour le seul plaisir de prendre conscience de sa force.\nFriedrich Nietzsche\nPhilosophe Allemand"
c95 = "Mieux vaut ne rien savoir que beaucoup savoir à moitié !\nFriedrich Nietzsche\nPhilosophe Allemand"
c96 = "Nos devoirs - ce sont les droits que les autres ont sur nous.\nFriedrich Nietzsche\nPhilosophe Allemand"
c97 = "Nul vainqueur ne croit au hasard.\nFriedrich Nietzsche\nPhilosophe Allemand"
c98 = "Faites donc ce que vous voulez - mais soyez d’abord de ceux qui peuvent vouloir !\nFriedrich Nietzsche\nPhilosophe Allemand"
c99 = "Il faut retenir son cœur, car si on le laissait aller, combien vite, alors, on perdrait la tête !\nFriedrich Nietzsche\nPhilosophe Allemand"
c100 = "Qui ne croit en lui-même, ment toujours.\nFriedrich Nietzsche\nPhilosophe Allemand"
c101 = "On paie mal un maître en ne restant toujours que l’élève.\nFriedrich Nietzsche\nPhilosophe Allemand"
c102 = "Rire, c'est se réjouir d'un préjudice, mais avec bonne conscience.\nFriedrich Nietzsche\nPhilosophe Allemand"
c103 = "Le défaut le plus répandu de notre type de formation et d’éducation : personne n'apprend, personne n'aspire, personne n'enseigne... à supporter la solitude.\nFriedrich Nietzsche\nPhilosophe Allemand"
c104 = "La culture, c'est avant tout une unité de style qui se manifeste dans toutes les activités d'une nation.\nFriedrich Nietzsche\nPhilosophe Allemand"
c105 = "Quand on a la foi, on peut se passer de la vérité.\nFriedrich Nietzsche\nPhilosophe Allemand"
c106 = "La femme est la seconde faute de Dieu.\nFriedrich Nietzsche\nPhilosophe Allemand"
c107 = "Beaucoup de brèves folies, c'est là ce que vous appelez l'amour. Et votre mariage met fin à beaucoup de brèves folies par une longue sottise.\nFriedrich Nietzsche\nPhilosophe Allemand"
c108 = "Promesse de la science : la science moderne a pour but aussi peu de douleur que possible.\nFriedrich Nietzsche\nPhilosophe Allemand"
c109 = "Vénérez la maternité, le père n'est jamais qu'un hasard.\nFriedrich Nietzsche\nPhilosophe Allemand"
c110 = "Voilà un envieux : ne lui souhaitez pas d'enfants ; il serait jaloux d'eux parce qu'il ne peut plus avoir leur âge.\nFriedrich Nietzsche\nPhilosophe Allemand"
c111 = "Le ver se recroqueville quand on marche dessus. C'est plein de sagesse. Par là il amoindrit la chance de se faire de nouveau marcher dessus. Dans le langage de la morale : l'humilité.\nFriedrich Nietzsche\nPhilosophe Allemand"
c112 = "Contre maint défenseur. La plus perfide façon de nuire à une cause est de la défendre intentionnellement avec de mauvaises raisons.\nFriedrich Nietzsche\nPhilosophe Allemand"
c113 = "Le serpent qui ne peut changer de peau, meurt. Il en va de même des esprits que l'on empêche de changer d'opinion : ils cessent d'être esprit.\nFriedrich Nietzsche\nPhilosophe Allemand"
c114 = "Nos défauts sont les yeux par lesquels nous voyons l'idéal.\nFriedrich Nietzsche\nPhilosophe Allemand"
c115 = "Le mariage est la forme la plus menteuse des relations sexuelles ; c'est pourquoi il jouit de l'approbation des consciences pures.\nFriedrich Nietzsche\nPhilosophe Allemand"
c116 = "La connaissance est pour l'humanité un magnifique moyen de s'anéantir elle-même.\nFriedrich Nietzsche\nPhilosophe Allemand"
c117 = "Une belle femme a tout de même quelque chose de commun avec la vérité : toutes deux donnent plus de bonheur lorsqu'on les désire que lorsqu'on les possède.\nFriedrich Nietzsche\nPhilosophe Allemand"
c118 = "Les singes sont bien trop bons pour que l'homme puisse descendre d'eux.\nFriedrich Nietzsche\nPhilosophe Allemand"
c119 = "Ce qui ne me détruit pas me rend plus fort.\nFriedrich Nietzsche\nPhilosophe Allemand"
c120 = "Au fond, il n'y a qu'un seul chrétien, et il est mort sur la croix.\nFriedrich Nietzsche\nPhilosophe Allemand"
c121 = "Ce qu'on fait par amour l'est toujours par-delà le bien et le mal.\nFriedrich Nietzsche\nPhilosophe Allemand"
c122 = "Quiconque lutte contre des monstres devrait prendre garde, dans le combat, à ne pas devenir monstre lui-même. Et quant à celui qui scrute le fond de l'abysse, l'abysse le scrute à son tour.\nFriedrich Nietzsche\nPhilosophe Allemand"
c123 = "Il est plus facile de renoncer à une passion que de la maîtriser.\nFriedrich Nietzsche\nPhilosophe Allemand"
c124 = "On oublie sa faute quand on l'a confessée à un autre, mais d'ordinaire l'autre ne l'oublie pas.\nFriedrich Nietzsche\nPhilosophe Allemand"
c125 = "Dieu est une pensée qui rend courbe ce qui est droit, fait tourner ce qui est immobile.\nFriedrich Nietzsche\nPhilosophe Allemand"
c126 = "Dans toute morale ascétique, l'homme adore une part de soi-même sous les espèces de Dieu, et il a besoin pour cela de changer en diable la part qui reste... \nFriedrich Nietzsche\nPhilosophe Allemand"
c127 = "Que dire ? L'homme n'est qu'une méprise de Dieu ? Ou bien Dieu une méprise de l'homme ?\nFriedrich Nietzsche\nPhilosophe Allemand"
c128 = "Quand on ne trouve plus la grandeur de Dieu, on ne la trouve plus nulle part, il faut la nier ou la créer.\nFriedrich Nietzsche\nPhilosophe Allemand"
c129 = "S'il y a un Dieu, comment supporter de ne l'être pas ?\nFriedrich Nietzsche\nPhilosophe Allemand"
c130 = "Dieu a aussi son enfer : c'est son amour des hommes.\nFriedrich Nietzsche\nPhilosophe Allemand"
c131 = "À trop admirer les vertus des autres on peut perdre le sens des siennes propres tant et si bien qu'en ne les exerçant plus, on les oublie complètement sans recevoir pour autant celles des autres en compensation.\nFriedrich Nietzsche\nPhilosophe Allemand"
c132 = "Celui qui nie sa propre vanité la possède généralement sous une forme si brutale qu'il ferme instinctivement les yeux devant elle pour ne pas avoir à se mépriser.\nFriedrich Nietzsche\nPhilosophe Allemand"
c133 = "La fortune ne devrait être possédée que par les gens d'esprit : autrement, elle représente un danger public.\nFriedrich Nietzsche\nPhilosophe Allemand"
c134 = "Traiter tous les hommes avec la même bienveillance et prodiguer indistinctement sa bonté peut tout aussi bien témoigner d'un profond mépris des hommes que d'un amour sincère à leur égard.\nFriedrich Nietzsche\nPhilosophe Allemand"
c135 = "La jalousie qui se tait s'accroît dans le silence.\nFriedrich Nietzsche\nPhilosophe Allemand"
c136 = "L'amitié naît lorsqu'on a pour l'autre une estime supérieure à celle qu'on a pour soi-même.\nFriedrich Nietzsche\nPhilosophe Allemand"
c137 = "Accepter d'autrui qu'il subvienne à des besoins nombreux et même superflus, et aussi parfaitement que possible, finit par vous réduire à un état de dépendance.\nFriedrich Nietzsche\nPhilosophe Allemand"
c138 = "La colère vide l'âme de toutes ses ressources, de sorte qu'au fond paraît la lumière.\nFriedrich Nietzsche\nPhilosophe Allemand"
c139 = "Qu'est-ce donc que l'amour, si ce n'est de se comprendre et de se réjouir en voyant quelqu'un d'autre vivre, agir et sentir différemment de nous, parfois même à l'opposé ?\nFriedrich Nietzsche\nPhilosophe Allemand"
c140 = "Ce n'est pas le doute, c'est la certitude qui rend fou.\nFriedrich Nietzsche\nPhilosophe Allemand"
c141 = "Les pensées sont les ombres de nos sentiments.\nFriedrich Nietzsche\nPhilosophe Allemand"
c142 = "Pour celui qui est très seul, le bruit est déjà une consolation.\nFriedrich Nietzsche\nPhilosophe Allemand"
c143 = "Féconder le passé en engendrant l'avenir, tel est le sens du présent.\nFriedrich Nietzsche\nPhilosophe Allemand"
c144 = "Les unions qui sont conclues par amour ont l'erreur pour père et la nécessité pour mère.\nFriedrich Nietzsche\nPhilosophe Allemand"
c145 = "Le fanatisme est la seule forme de volonté qui puisse être insufflée aux faibles et aux timides.\nFriedrich Nietzsche\nPhilosophe Allemand"
c146 = "Le christianisme et l'alcool, les deux plus grands agents de corruption.\nFriedrich Nietzsche\nPhilosophe Allemand"
c147 = "Ce qui se dit la nuit ne voit jamais le jour.\nFriedrich Nietzsche\nPhilosophe Allemand"
c148 = "La morale n'est qu'une interprétation - ou plus exactement une fausse interprétation - de certains phénomènes.\nFriedrich Nietzsche\nPhilosophe Allemand"
c149 = "L’homme a créé le péché et il repousserait cet enfant unique rien que parce qu’il déplaît à Dieu, le grand-père du péché ?\nFriedrich Nietzsche\nPhilosophe Allemand"
c150 = "Cette femme est belle et intelligente : hélas, combien elle serait devenue plus intelligente si elle n’était pas belle.\nFriedrich Nietzsche\nPhilosophe Allemand"
c151 = "La vérité est une femme : ses voiles, ses pudeurs et ses mensonges lui appartiennent essentiellement.\nFriedrich Nietzsche\nPhilosophe Allemand"
c152 = "La femme est une surface qui mime la profondeur.\nFriedrich Nietzsche\nPhilosophe Allemand"
c153 = "La philosophie est à mes yeux un explosif effroyable qui met tout en danger.\nFriedrich Nietzsche\nPhilosophe Allemand"
c154 = "C’est bien un signe de l’astuce des femmes qu’elles aient su presque partout sa faire entretenir, comme des frelons dans la ruche.\nFriedrich Nietzsche\nPhilosophe Allemand"
c155 = "Au fond du cœur, l'homme n'est que méchant ; mais au fond du cœur, la femme est mauvaise.\nFriedrich Nietzsche\nPhilosophe Allemand"
c156 = "Les principes servent à tyranniser, justifier, honorer, vilipender ou dissimuler les habitudes ; deux hommes qui ont au fond les mêmes principes peuvent les faire servir à des fins radicalement différentes.\nFriedrich Nietzsche\nPhilosophe Allemand"
c157 = "Les conditions nouvelles qui entraîneront en gros l’apparition d’hommes tous pareils et pareillement médiocres sont éminemment propres à donner naissance à des hommes d’exception du genre le plus dangereux et le plus séduisant.\nFriedrich Nietzsche\nPhilosophe Allemand"
c158 = "Les hommes aux pensées profondes, dans leurs rapports avec les autres hommes, ont toujours l’impression d’être des comédiens, parce qu’ils sont forcés, pour être compris, de simuler une superficie.\nFriedrich Nietzsche\nPhilosophe Allemand"
c159 = "Limites de notre ouïe - On n’entend que les questions auxquelles on est en mesure de trouver une réponse.\nFriedrich Nietzsche\nPhilosophe Allemand"
c160 = "La métaphysique, la morale, la religion, la science, sont considérées comme des formes diverses de mensonge : il faut leur aide pour croire à la vie.\nFriedrich Nietzsche\nPhilosophe Allemand"
c161 = "C’est de nos vertus que nous sommes le mieux punis.\nFriedrich Nietzsche\nPhilosophe Allemand"
c162 = "La vanité d’autrui n’offense notre goût que lorsqu’elle choque notre propre vanité.\nFriedrich Nietzsche\nPhilosophe Allemand"
c163 = "Quel est le sceau de la liberté acquise ? Ne plus avoir honte de soi-même.\nFriedrich Nietzsche\nPhilosophe Allemand"
c164 = "Le génie réside dans l'instinct.\nFriedrich Nietzsche\nPhilosophe Allemand"
c165 = "La terre est comme la poitrine d'une femme : utile autant qu'agréable.\nFriedrich Nietzsche\nPhilosophe Allemand"
c166 = "La valeur d’une chose réside parfois non dans ce qu’on en tire, mais dans ce qu’on paie pour elle, dans ce qu’elle nous coûte.\nFriedrich Nietzsche\nPhilosophe Allemand"
c167 = "Le droit des autres est une concession faite par notre sentiment de puissance au sentiment de puissance de ces autres.\nFriedrich Nietzsche\nPhilosophe Allemand"
c168 = "Seul ce qui ne cesse de nous faire souffrir reste dans la mémoire.\nFriedrich Nietzsche\nPhilosophe Allemand"
c169 = "On se refuse de croire aux sottises des hommes intelligents ; quelle entorse aux droits de l'homme !\nFriedrich Nietzsche\nPhilosophe Allemand"
c170 = "Les avocats d'un criminel sont rarement assez artistes pour utiliser, au profit du coupable, la beauté terrible de son acte.\nFriedrich Nietzsche\nPhilosophe Allemand"
c171 = "L'étroite voie de notre ciel propre passe toujours par la volupté de notre propre enfer.\nFriedrich Nietzsche\nPhilosophe Allemand"
c172 = "Ce qui détruit les illusions, les siennes et celles des autres, la nature le punit avec toute la rigueur d'un tyran.\nFriedrich Nietzsche\nPhilosophe Allemand"
c173 = "L'effort des philosophes tend à comprendre ce que les contemporains se contentent de vivre.\nFriedrich Nietzsche\nPhilosophe Allemand"
c174 = "La souffrance d'autrui est chose qui doit s'apprendre.\nFriedrich Nietzsche\nPhilosophe Allemand"
c175 = "Méfiez-vous de tous ceux en qui l'instinct de punir est puissant.\nFriedrich Nietzsche\nPhilosophe Allemand"
c176 = "Les hommes d'action roulent comme roule la pierre, conformément à l'absurdité de la mécanique.\nFriedrich Nietzsche\nPhilosophe Allemand"
c177 = "À lutter avec les mêmes armes que ton ennemi, tu deviendras comme lui.\nFriedrich Nietzsche\nPhilosophe Allemand"
c178 = "Celui qui ne dispose pas des deux tiers de sa journée pour lui-même est un esclave, qu'il soit d'ailleurs ce qu'il veut : politique, marchand, fonctionnaire, érudit.\nFriedrich Nietzsche\nPhilosophe Allemand"
c179 = "L'homme souffre si profondément qu'il a dû inventer le rire.\nFriedrich Nietzsche\nPhilosophe Allemand"
c180 = "Rêver de la vie, c'est justement ce que j'appelle : être éveillé.\nFriedrich Nietzsche\nPhilosophe Allemand"
c181 = "Il faut savoir se perdre pour un temps si l'on veut apprendre quelque chose des êtres que nous ne sommes pas nous-mêmes.\nFriedrich Nietzsche\nPhilosophe Allemand"
c182 = "Ne pas confondre : les comédiens périssent faute d'être loués, les hommes vrais faute d'être aimés.\nFriedrich Nietzsche\nPhilosophe Allemand"
c183 = "Ma seule ambition de poète est de recomposer, de ramener à l'unité, ce qui n'est que fragment, énigme, effroyable hasard.\nFriedrich Nietzsche\nPhilosophe Allemand"
c184 = "Une âme délicate est gênée de savoir qu'on lui doit des remerciements, une âme grossière, de savoir qu'elle en doit.\nFriedrich Nietzsche\nPhilosophe Allemand"
c185 = "Une heure d'ascension dans les montagnes fait d'un gredin et d'un saint deux créatures à peu près semblables. La fatigue est le plus court chemin vers l'égalité, vers la fraternité. Et durant le sommeil s'ajoute la liberté.\nFriedrich Nietzsche\nPhilosophe Allemand"
c186 = "Ne vaut-il pas mieux tomber entre les mains d'un meurtrier que dans les rêves d'une femme en rut ?\nFriedrich Nietzsche\nPhilosophe Allemand"
c187 = "L'homme véritable veut deux choses : le danger et le jeu. C'est pourquoi il veut la femme, le jouet le plus dangereux.\nFriedrich Nietzsche\nPhilosophe Allemand"
c188 = "La perspective certaine de la mort pourrait mêler à la vie une goutte délicieuse et parfumée d’insouciance - mais, âmes bizarres d’apothicaires, vous avez fait de cette goutte un poison infect, qui rend répugnante la vie toute entière !\nFriedrich Nietzsche\nPhilosophe Allemand"
c189 = "Ce qui me bouleverse, ce n'est pas que tu m'aies menti, c'est que désormais, je ne pourrai plus te croire.\nFriedrich Nietzsche\nPhilosophe Allemand"
c190 = "La terre a une peau et cette peau a des maladies ; une de ces maladies s'appelle l'homme.\nFriedrich Nietzsche\nPhilosophe Allemand"
c191 = "Parmi toutes les variétés de l'intelligence découvertes jusqu'à présent, l'instinct est, de toutes, la plus intelligente.\nFriedrich Nietzsche\nPhilosophe Allemand"
c192 = "La mission suprême de l’art consiste à libérer nos regards des terreurs obsédantes de la nuit, à nous guérir des douleurs convulsives que nous causent nos actes volontaires.\nFriedrich Nietzsche\nPhilosophe Allemand"
c193 = "Il n’y a qu’un seul monde et il est faux, cruel, contradictoire, séduisant et dépourvu de sens. Un monde ainsi constitué est le monde réel. Nous avons besoin de mensonges pour conquérir cette réalité, cette vérité.\nFriedrich Nietzsche\nPhilosophe Allemand"
c194 = "Vivre de telle sorte qu'il te faille désirer revivre, c'est là ton devoir.\nFriedrich Nietzsche\nPhilosophe Allemand"
c195 = "Si vous ne pouvez être des saints de la connaissance, soyez-en au moins les guerriers.\nFriedrich Nietzsche\nPhilosophe Allemand"
c196 = "Un animal grégaire, un être docile, maladif, médiocre, l’Européen d’aujourd’hui !\nFriedrich Nietzsche\nPhilosophe Allemand"
c197 = "Veux-tu avoir la vie facile ? Reste toujours près du troupeau et oublie-toi en lui.\nFriedrich Nietzsche\nPhilosophe Allemand"
c198 = "Cupidon est avant tout un petit régisseur de théâtre.\nFriedrich Nietzsche\nPhilosophe Allemand"
c199 = "Tous ceux qui sont habitués au succès sont pleins d'astuces pour présenter toujours leurs défauts et leurs faiblesses comme de la force apparente : ce pourquoi ils doivent les connaître particulièrement bien.\nFriedrich Nietzsche\nPhilosophe Allemand"
c200 = "Avoir honte de son immoralité, c'est un premier degré de l'échelle ; arrivé en haut, on aura honte aussi de sa propre moralité.\nFriedrich Nietzsche\nPhilosophe Allemand"
c201 = "Il n'y a pas de phénomènes moraux, rien qu'une interprétation morale des phénomènes.\nFriedrich Nietzsche\nPhilosophe Allemand"
c202 = "Quand la paix règne, l'homme belliqueux se fait la guerre à lui-même.\nFriedrich Nietzsche\nPhilosophe Allemand"
c203 = "Nul ne ment autant qu'un homme indigné.\nFriedrich Nietzsche\nPhilosophe Allemand"
c204 = "Peu de gens sont faits pour l'indépendance, c'est le privilège des puissants.\nFriedrich Nietzsche\nPhilosophe Allemand"
c205 = "Ne faut-il pas commencer par se haïr, lorsque l’on doit s’aimer.\nFriedrich Nietzsche\nPhilosophe Allemand"
c206 = "Les médecins les plus dangereux sont ceux qui, comédiens nés, imitent le médecin-né avec un art consommé d'illusion.\nFriedrich Nietzsche\nPhilosophe Allemand"
c207 = "Si l'on comprenait à l'aide de la raison comment peut être clément et juste ce Dieu qui fait preuve de tant de colère, à quoi servirait la foi ?\nFriedrich Nietzsche\nPhilosophe Allemand"
c208 = "Le plus important des événements récents, le fait que Dieu est mort, commence déjà à projeter sur l'Europe ses premières ombres.\nFriedrich Nietzsche\nPhilosophe Allemand"
c209 = "Ce qui peut être commun est toujours de peu de valeur.\nFriedrich Nietzsche\nPhilosophe Allemand"
c210 = "Il faut mettre en question la valeur même des valeurs morales.\nFriedrich Nietzsche\nPhilosophe Allemand"
c211 = "Pour vivre seul, il faut être une bête ou un dieu, dit Aristote. Reste un troisième cas, il faut être les deux à la fois : philosophe.\nFriedrich Nietzsche\nPhilosophe Allemand"
c212 = "Nous devons penser de toute façon. Alors pourquoi ne pas penser grand ?\nDonald Trump\n45ème président des États-Unis"
c213 = "Montrez-moi quelqu'un qui n'a pas d'égo et je vous montrerai un perdant. Avoir un égo sain ou une haute opinion de soi, c'est un vrai truc positif dans la vie !\nDonald Trump\n45ème président des États-Unis"
c214 = "Si votre seul objectif est de devenir riche, alors vous n'y parviendrez jamais.\nDonald Trump\n45ème président des États-Unis"
c215 = "Quand quelqu'un vous attaque, ripostez. Soyez brutal, soyez féroce.\nDonald Trump\n45ème président des États-Unis"
c216 = "Je peux dire immédiatement si un homme est un gagnant ou un perdant rien qu'a sa façon de se comporter sur un terrain de golf.\nDonald Trump\n45ème président des États-Unis"
c217 = "J'aime le cinéma et la télévision autant que n'importe qui, mais la lecture est pour moi une manière de me ressourcer.\nDonald Trump\n45ème président des États-Unis"
c218 = "Si vous voulez vraiment réussir, vous allez devoir vous y coller tous les jours, comme moi. La réussite, c'est pas pour les feignasses.\nDonald Trump\n45ème président des États-Unis"
c219 = "La plupart des gens pensent petit parce qu'ils ont peur de la réussite, peur de la décision, peur de gagner.\nDonald Trump\n45ème président des États-Unis"
c220 = "Sans passion, vous n'avez pas d'énergie, sans énergie, vous n'avez rien.\nDonald Trump\n45ème président des États-Unis"
c221 = "Les champions courent le kilomètre de plus.\nDonald Trump\n45ème président des États-Unis"
c222 = "Le business n'est pas un restaurant, mais un buffet. Si vous attendez qu'on vous serve vous n'aurez rien. Il faut aller se servir.\nDonald Trump\n45ème président des États-Unis"
c223 = "L'interdiction des armes à feu est une idée dont le temps est venu.\nJoe Biden\n46ème président des États-Unis"
c224 = "Assurez-vous de deux choses. Soyez prudent - les microphones sont toujours chauds et comprenez qu'à Washington, DC, c'est une gaffe quand vous dites la vérité.\nJoe Biden\n46ème président des États-Unis"
c225 = "C'est facile d'être vice-président - vous n'avez rien à faire.\nJoe Biden\n46ème président des États-Unis"
c226 = "Aucun Américain ordinaire ne se soucie de ses droits constitutionnels.\nJoe Biden\n46ème président des États-Unis"
c227 = "Aucune nation ne devrait menacer ses voisins en amassant des troupes le long de la frontière.\nJoe Biden\n46ème président des États-Unis"
c228 = "Mon père avait une expression. Il disait : Joey, un emploi est beaucoup plus qu'un chèque de paie. C'est votre dignité. C'est un respect. Il s'agit de votre place dans votre communauté.\nJoe Biden\n46ème président des États-Unis"
c229 = "Aucune nation ne devrait attiser l'instabilité dans le pays de son voisin.\nJoe Biden\n46ème président des États-Unis"


@bot.event
async def on_ready():
    print("bot is active")  # indique lorsque le bot sera disponible, utile uniquement pour un test


@bot.command(name='citation')    # le bot répondra à la commande .citation
async def citation(ctx):
    msg = await ctx.send(random.choice([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38, c39, c40, c41, c42, c43, c44, c45, c46, c47, c48, c49, c50, c51, c52, c53, c54, c55, c56, c57, c58, c59, c60, c61, c62, c63, c64, c65, c66, c67, c68, c69, c70, c71, c72, c73, c74, c75, c76, c77, c78, c79, c80, c81, c82, c83, c84, c85, c86, c87, c88, c89, c90, c91, c92, c93, c94, c95, c96, c97, c98, c99, c100, c101, c102, c103, c104, c105, c106, c107, c108, c109, c110, c111, c112, c113, c114, c115, c116, c117, c118, c119, c120, c121, c122, c123, c124, c125, c126, c127, c128, c129, c130, c131, c132, c133, c134, c135, c136, c137, c138, c139, c140, c141, c142, c143, c144, c145, c146, c147, c148, c149, c150, c151, c152, c153, c154, c155, c156, c157, c158, c159, c160, c161, c162, c163, c164, c165, c166, c167, c168, c169, c170, c171, c172, c173, c174, c175, c176, c177, c178, c179, c180, c181, c182, c183, c184, c185, c186, c187, c188, c189, c190, c191, c192, c193, c194, c195, c196, c197, c198, c199, c200, c201, c202, c203, c204, c205, c206, c207, c208, c209, c210, c211, c212, c213, c214, c215, c216, c217, c218, c219, c220, c221, c222, c223, c224, c225, c226, c227, c228, c229]))  # citation aléatoire
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")


@bot.command(name='napoléon')   # le bot répondra à la commande .napoléon
async def napoleon(ctx):
    msg = await ctx.send(random.choice([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38, c39, c40, c41, c42, c43, c44, c45, c46, c47, c48, c49, c50, c51, c52, c53, c54, c55, c56, c57, c58, c59, c60, c61]))  # citation aléatoire de napoléon
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")


@bot.command(name='nietzsche')  # le bot répondra à la commande .nietzsche
async def nietzsche(ctx):
    msg = await ctx.send(random.choice([c62, c63, c64, c65, c66, c67, c68, c69, c70, c71, c72, c73, c74, c75, c76, c77, c78, c79, c80, c81, c82, c83, c84, c85, c86, c87, c88, c89, c90, c91, c92, c93, c94, c95, c96, c97, c98, c99, c100, c101, c102, c103, c104, c105, c106, c107, c108, c109, c110, c111, c112, c113, c114, c115, c116, c117, c118, c119, c120, c121, c122, c123, c124, c125, c126, c127, c128, c129, c130, c131, c132, c133, c134, c135, c136, c137, c138, c139, c140, c141, c142, c143, c144, c145, c146, c147, c148, c149, c150, c151, c152, c153, c154, c155, c156, c157, c158, c159, c160, c161, c162, c163, c164, c165, c166, c167, c168, c169, c170, c171, c172, c173, c174, c175, c176, c177, c178, c179, c180, c181, c182, c183, c184, c185, c186, c187, c188, c189, c190, c191, c192, c193, c194, c195, c196, c197, c198, c199, c200, c201, c202, c203, c204, c205, c206, c207, c208, c209, c210, c211]))  # citation aléatoire de nietzsche
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")


@bot.command(name='trump')  # le bot répondra à la commande .trump
async def trump(ctx):
    msg = await ctx.send(random.choice([c212, c213, c214, c215, c216, c217, c218, c219, c220, c221, c222]))  # citation aléatoire de trump
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")


@bot.command(name='biden')  # le bot répondra à la commande .biden
async def biden(ctx):
    msg = await ctx.send(random.choice([c212, c223, c224, c225, c226, c227, c228, c229]))  # citation aléatoire de biden
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")


@bot.command(name='info')   # le bot répond à la commande .info
async def info(ctx):
    await ctx.send("Ce bot a pour fonction de te faire réfléchir et de développer ton intellect par les citations.\n Et pourquoi pas de te donner envie de lire les œuvres et auteurs en question.\n229 citations disponibles.\nAuteurs et sources implémentés : Napoléon Bonaparte, Friedrich Nietzsche, Donald Trump, Joe Biden.\nÀ venir : La Bible, Dostoïevski, Le Coran, De Gaulle, Orwell, Voltaire.\nPour une liste des commandes disponibles : .aide\nCode source trouvable sur : https://github.com/GueguenA/Discord-Citation\nPour me contacter sur discord : Alex le thrasheu#3961")


@bot.command(name='aide')   # le bot répond à la commande .aide
async def aide(ctx):
    await ctx.send("Liste des différentes commandes disponible :\n .aide : affiche cette aide\n.info : pour plus d'infos sur ce bot\n.citation : affiche une citation aléatoire\n.napoléon : affiche une citation aléatoire de Napoléon\n.nietzsche : affiche une citation aléatoire de Nietzsche\n.trump : affiche une citation aléatoire de Trump\n.biden : affiche uen citation aléatoire de Biden")


bot.run(os.getenv("TOKEN"))
