# Pokem_Buyer_Bot
![](static/project_name.png)
# Introduction
This project is a Pokem buying bot designed to purchase Pokem products faster than other buyers.

Here’s what it does during a standard purchase:
- Logs in with the selected account on the merchant Pokem website
- Continuously checks for the availability of the target product (while not logged in)
- Once the product is available, adds it to the cart (while logged in)
- Verifies the cart
- Automatically fills in the checkout form
- Selects the delivery method (pickup point option works!)
- Places the order

(Note: To ensure that only my friends and I use this bot, the word "poke e mon" is referred to as "pokem" throughout the repository to avoid being indexed on GitHub. The project remains public so my friends can access it.)



# Comment l'utiliser ?
### Configuration principale
- Copier Coller le fichier config/config1_example.ini en le renommant config/config1.ini

![](static/copie_colle_config_file.png)

- Créer votre compte personnel sur le site:
![](static/name_website_to_bot.png)

- Remplir l'ensemble des champs de config1.ini en utilisant vos identifiants de compte personnel et vos informations personnelles.
- Si vous voulez effectuer plusieurs achats avec plusieurs comptes, il suffira de créer des fichiers config2.ini, config3.ini, etc...

### lancer le programme

Toutes les actions ont été automatisés sur des fichiers .bat afin que vous n'ayez plus que a double cliquer sur les fichiers .bat pour lancer le bot. (ne fonctionne que sur Windows).

Voici les différentes actions disponibles avec les différents fichiers .bat disponibles:
- **test_one_config.bat**
(Tester le programme jusqu'au bouton d'achat pour un fichier de config.ini que vous choisissez (sans acheter))
- **test_all_config.bat**
(Tester le programme jusqu'au bouton d'achat pour chacun des fichiers de config.ini (sans acheter))
- **choose_pickup_point_one_config.bat**
  (Tester le programme pour un fichier de config.ini que vous choisissez jusqu'au moment de choisir le point relais.))
- **run_one_config.bat**
(Lancer le programme pour un fichier de config.ini que vous choisissez (En achetant le produit uniquement sur le fichier de config.ini choisi))
- **run_all_config.bat**
(Lancer le programme pour chacun des fichiers de config.ini (En achetant le produit pour chacun des fichiers de config.ini))