import random   # necessaire pour choisir aléatoirement une citation
import os   # necessaire pour que le token du bot n'apparaisse pas en clair dans le code
from dotenv import load_dotenv  # //
from discord.ext import commands    # necessaire poue que le bot réponde au commande


load_dotenv(dotenv_path="config")   # indique dans quel fichier se trouve le token
bot = commands.Bot(command_prefix='.')  # indique que le bot répondra au caractère .


c1 = "On gouverne mieux les hommes par leurs vices que par leurs vertus.\nNapoléon Bonaparte\nEmpereur des Français"
c2 = "L’avenir d’un enfant est l’oeuvre de sa mère.\nNapoléon Bonaparte\nEmpereur des Français"
c3 = "L’amour est une sottise faite à deux.\nNapoléon Bonaparte\nEmpereur des Français"
c4 = "L’imagination gouverne le monde.\nNapoléon Bonaparte\nEmpereur des Français"
c5 = "Ce que je cherche avant tout, c’est la grandeur : ce qui est grand est toujours beau.\nNapoléon Bonaparte\nEmpereur des Français"
c6 = "Les hommes de génie sont des météores destinés à brûler pour éclairer leur siècle.\nNapoléon Bonaparte\nEmpereur des Français"
c7 = "Ce n’est pas possible ; cela n’est pas français.\nNapoléon Bonaparte\nEmpereur des Français"
c8 = "La bonne politique est de faire croire aux peuples qu’ils sont libres.\nNapoléon Bonaparte\nEmpereur des Français"
c9 = "Une société sans religion est comme un vaisseau sans boussole.\nNapoléon Bonaparte\nEmpereur des Français"
c10 = "Le mensonge n'est bon à rien, puisqu'il ne trompe qu'une fois.\nNapoléon Bonaparte\nEmpereur des Français"
c11 = "La sévérité prévient plus de fautes qu'elle n'en réprime.\nNapoléon Bonaparte\nEmpereur des Français"
c12 = "Il faut vouloir vivre et savoir mourir.\nNapoléon Bonaparte\nEmpereur des Français"
c13 = "La froideur est la plus grande qualité d'un homme destiné à commander.\nNapoléon Bonaparte\nEmpereur des Français"
c14 = "Qui sait flatter sait aussi calomnier.\nNapoléon Bonaparte\nEmpereur des Français"
c15 = "On déjoue beaucoup de choses en feignant de ne pas les voir.\nNapoléon Bonaparte\nEmpereur des Français"
c16 = "L'homme n'est jamais si grand qu'à genoux devant Dieu.\nNapoléon Bonaparte\nEmpereur des Français"
c17 = "En guerre comme en amour, pour en finir, il faut se voir de près.\nNapoléon Bonaparte\nEmpereur des Français"
c18 = "Du sublime au ridicule, il n'y a qu'un pas.\nNapoléon Bonaparte\nEmpereur des Français"
c19 = "Je sais, quand il le faut, quitter la peau du lion pour prendre celle du renard.\nNapoléon Bonaparte\nEmpereur des Français"
c20 = "Le sot a un grand avantage sur l'homme d'esprit : il est toujours content de lui-même.\nNapoléon Bonaparte\nEmpereur des Français"
c21 = "Le coeur d'un homme d'Etat doit être dans sa tête.\nNapoléon Bonaparte\nEmpereur des Français"
c22 = "L'art d'être tantôt très audacieux et tantôt très prudent est l'art de réussir.\nNapoléon Bonaparte\nEmpereur des Français"
c23 = "On ne conduit le peuple qu'en lui montrant un avenir : un chef est un marchand d'espérance.\nNapoléon Bonaparte\nEmpereur des Français"
c24 = "L'habitude des faits les plus violents use moins le coeur que les abstractions : les militaires valent mieux que les avocats.\nNapoléon Bonaparte\nEmpereur des Français"
c25 = "Il n'y a qu'un secret pour mener le monde, c'est d'être fort, parce qu'il n'y a dans la force ni erreur, ni illusion ; c'est le vrai, mis à nu.\nNapoléon Bonaparte\nEmpereur des Français"
c26 = "La bravoure procède du sang, le courage vient de la pensée.\nNapoléon Bonaparte\nEmpereur des Français"
c27 = "La noblesse aurait subsisté si elle s'était occupée davantage des branches que des racines.\nNapoléon Bonaparte\nEmpereur des Français"
c28 = "Le général qui voit avec les yeux des autres n'est pas capable de commander une armée.\nNapoléon Bonaparte\nEmpereur des Français"
c29 = "L'homme n'est qu'un animal plus parfait que les autres et qui raisonne mieux.\nNapoléon Bonaparte\nEmpereur des Français"
c30 = "La haute politique n'est que le bon sens appliqué aux grandes choses.\nNapoléon Bonaparte\nEmpereur des Français"
c31 = "Le grand art, c'est de changer pendant la bataille. Malheur au général qui arrive au combat avec un système.\nNapoléon Bonaparte\nEmpereur des Français"
c32 = "Pour une femme qui nous inspire quelque chose de bon, il y a en cent qui nous font faire des sottises.\nNapoléon Bonaparte\nEmpereur des Français"
c33 = "Un homme combattra plus pour ses intérêts que pour ses droits.\nNapoléon Bonaparte\nEmpereur des Français"
c34 = "Un bon croquis vaut mieux qu’un long discours.\nNapoléon Bonaparte\nEmpereur des Français"
c35 = "L'impossible est le refuge des poltrons.\nNapoléon Bonaparte\nEmpereur des Français"
c36 = "L'intelligence ne se mesure pas des pieds à la tête, mais de la tête au ciel.\nNapoléon Bonaparte\nEmpereur des Français"
c37 = "La pauvreté, les privations et la misère sont l'école du bon soldat.\nNapoléon Bonaparte\nEmpereur des Français"
c38 = "La haute tragédie est l'école des grands hommes ; elle doit être celle des rois et des peuples ; c'est le point le plus élevé auquel un poète puisse parvenir.\nNapoléon Bonaparte\nEmpereur des Français"
c39 = "Notre ridicule défaut national est de n'avoir pas de plus grand ennemi de nos succès et de notre gloire que nous-mêmes.\nNapoléon Bonaparte\nEmpereur des Français"
c40 = "La France, c'est le français quand il est bien écrit.\nNapoléon Bonaparte\nEmpereur des Français"
c41 = "Les peuples passent, les trônes s'écroulent, l'église demeure.\nNapoléon Bonaparte\nEmpereur des Français"
c42 = "Dieu, lui aussi, a essayé de faire des ouvrages. Sa prose, c'est l'homme. Sa poésie, c'est la femme.\nNapoléon Bonaparte\nEmpereur des Français"
c43 = "Il est dans le caractère français d'exagérer, de se plaindre et de tout défigurer dès qu'on est mécontent.\nNapoléon Bonaparte\nEmpereur des Français"
c44 = "La supériorité de Mahomet est d'avoir fondé une religion en se passant de l'enfer.\nNapoléon Bonaparte\nEmpereur des Français"
c45 = "Une belle femme plaît aux yeux, une bonne femme plaît au coeur ; l'une est un bijou, l'autre un trésor.\nNapoléon Bonaparte\nEmpereur des Français"
c46 = "Les règlements sont faits pour les soldats et non pour les guerriers ; la bataille se rit du code, elle en exige un nouveau, innové par elle et pour elle et qui disparaît dès qu’elle est terminée.\nNapoléon Bonaparte\nEmpereur des Français"
c47 = "La première des vertus est le dévouement à la patrie.\nNapoléon Bonaparte\nEmpereur des Français"
c48 = "Dans tout ce qu'on entreprend, il faut donner les deux tiers à la raison, et l'autre tiers au hasard. Augmentez la première fraction, et vous serez pusillanime. Augmentez la seconde, vous serez téméraire.\nNapoléon Bonaparte\nEmpereur des Français"
c49 = "Le doute est l'ennemi des grandes entreprises.\nNapoléon Bonaparte\nEmpereur des Français"
c50 = "La morale est bien souvent le passeport de la médisance.\nNapoléon Bonaparte\nEmpereur des Français"
c51 = "J'ai fait mes plans avec les rêves de mes soldats endormis.\nNapoléon Bonaparte\nEmpereur des Français"
c52 = "On ne peut pas faire semblant d’être courageux.\nNapoléon Bonaparte\nEmpereur des Français"
c53 = "N'interrompez jamais un ennemi qui est en train de commettre une erreur.\nNapoléon Bonaparte\nEmpereur des Français"
c54 = "Il y a des gens qui se croient le talent de gouverner par la seule raison qu'ils gouvernent.\nNapoléon Bonaparte\nEmpereur des Français"
c55 = "La mort n'est rien, mais vivre vaincu et sans gloire c'est mourir tous les jours.\nNapoléon Bonaparte\nEmpereur des Français"
c56 = "Quand on veut on peut, quand on peut on doit.\nNapoléon Bonaparte\nEmpereur des Français"
c57 = "Lorsqu'un gouvernement est dépendant des banquiers pour l'argent, ce sont ces derniers, et non les dirigeants du gouvernement qui contrôlent la situation, puisque la main qui donne est au-dessus de la main qui reçoit.\nNapoléon Bonaparte\nEmpereur des Français"
c58 = "L'argent n'a pas de patrie ; les financiers n'ont pas de patriotisme et n'ont pas de décence ; leur unique objectif est le gain.\nNapoléon Bonaparte\nEmpereur des Français"
c59 = "Le succès ne s'explique pas. L'échec ne s'excuse pas.\nNapoléon Bonaparte\nEmpereur des Français"
c60 = "Si mon chapeau connaissait mon plan, je le mangerais.\nNapoléon Bonaparte\nEmpereur des Français"
c61 = "Je n'ai jamais fait de conquêtes qu'en me défendant. L'Europe n'a jamais cessé de combattre la France à cause de ses principes. J'étais forcé d'abattre sous peine d'être abattu.\nNapoléon Bonaparte\nEmpereur des Français"


@bot.event
async def on_ready():
    print("bot is active")  # indique lorsque le bot sera disponible, utile uniquement pour des test


@bot.command(name='cit')    # le bot répondra à la commande .cit
async def citation(ctx):
    await ctx.send(random.choice([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38, c39, c40, c41, c42, c43, c44, c45, c46, c47, c48, c49, c50, c51, c52, c53, c54, c55, c56, c57, c58, c59, c60, c61]))  # le bot écrit dans le channel oû la commande a été tapé


@bot.command(name='aide')   # le bot répond à la commande .aide
async def aide(ctx):
    await ctx.send("Liste des différentes commandes disponible :\n .aide\n.cit")


bot.run(os.getenv("TOKEN"))
