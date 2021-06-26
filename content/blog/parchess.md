+++
title = "ParChess - New multi-player variant of Chess"
slug = "parchess"
date = 2021-06-26
+++

Chess is one of the oldest and greatest games ever. Over the years there have been many variants of the game like triple check, antichess, king of the hill. Chess.com and Lichess have added these variants on their website as well. 4 player chess is a variant that came out a few years ago that allowed 4 persons to play chess full board.

This post came from a shower thought that I had. Why do we move only 1 piece at a time in chess? Many agree that in the game, white is automatically advantages due to the first move. This is also why in armageddons, the rules are made to even the playing field. If having the first move is already so advantages then having 2 or more moves first would be a huge advantage. But is that true if both players have the same number of moves, should not the position still be fairly equal?

It's not that no one ever played with more number of moves. It has been played as a sort of odds game, where the stronger player allows the other to play 2 moves at a time. But the intention of playing multiple moves is a bit different in my thought up variant.

The variant which I'd like to call parchess which stands for parallel chess, It is simply to divide the board to enable N players to play simultaneously that is each player moves once per turn. Here N is a number greater than 1 (you can't play alone par-1-chess). And par-2-chess is normal chess where the board is divided into black and white. Then we have the below divisons:

|Variant Name|Number of players|Board division|
|---|---|---|
|par-1-chess|1|Entire board is yours|
|par-2-chess|2|{"player1": "white pieces", "player2": "black pieces"}|
|par-3-chess|3|{"player1": "white pieces", "player2": "king-side black pieces", "player3": "queen-side black pieces"}|
|par-4-chess|3|{"player1": "king-side white pieces", "player2": "queen-side white pieces", "player3": "king-side black pieces", "player4": "queen-side black pieces"}|
|par-5-chess|3|{"player1": "king-side white pieces", "player2": "queen-side white pieces", "player3": "king-side black pieces except king and the king's pawn", "player4": "black king and queen and their pawns", "player5": "queen-side black pieces except queen and queen's pawn"}|

The board divisions are very primative, maybe it would be more accurate taking dividing the board based on the sum of the piece values. I can imagine it being playable (mindbendingly) till par-16-chess where each player would have a piece and it's pawn. Although the actual gameplay might become unplayable after par-4-chess, mainly because all moves have to be made each turn. Each side has visibilty into their side's moves, we can't have them moving into the same square. And given it becomes more of a team game, depending on whether discussing moves be allowed or not, the time per move could increase a lot.