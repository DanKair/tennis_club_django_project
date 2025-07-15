from members.models import Player
# from django.utils import timezone   This will be needed when creating users to shell manually


# main logic for adding players to db
# Use this as your hint / template for adding new models to db
player1 = Player(first_name="Elena", last_name="Rybakina", email="elena_rybakina@example.com", age=25, matches_played=100)
player1.save()
player2 = Player(first_name="Alexander", last_name="Bublik", email="alex_bublik@example.com", age=27, matches_played=310)
player2.save()
player3 = Player(first_name="Julia", last_name="Putenciva", email="julia_putenciva@tennis.com", age=30, matches_played=754)
player3.save()