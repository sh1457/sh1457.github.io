+++
title = "ParChess"
description = "An idea for a variant of chess based on multiple piece moves per turn"
date = 2021-06-26
updated = 2022-01-17
draft = true
[taxonomies]
tags = ["idea", "chess"]
+++

4 player chess is a variant that came out a few years ago that allowed 4 persons to play chess full board. Chess is one of the oldest and greatest games ever. Over the years there have been many variants <!-- more --> of the game like triple check, anti-chess, king of the hill. [Chess.com](https://www.chess.com/variants) and [Lichess.org](https://lichess.org) have added these variants on their website as well.

![4 player chess](4-player-board.jpg)

#### Why do we move only 1 piece at a time in chess?

Many agree that in the game, that white automatically gains an advantage from the first move. The player who goes first poses a question in the form of choice opening. The player who goes second is at many times guided into responding to the opening rather than developing their own flow. Modern chess theory has developed to the point where a master knows the ins and outs of the various openings and there is usually no surprises till the middle game.

We can draw parallels to a debate, where the argument provided the first speaker and the summary provided by the last speaker is of the greatest impact among all the impactful statements and retorts in between. Naturally the advantage of going first in the debate is to set the context (_choose the opening_) and capture the flow (set traps or limit the opponents).

This is also why in armageddons the [rules](https://www.chess.com/terms/armageddon-chess) are made to level the playing field for black.

If having the first move is already so advantages, then would having 2 or more moves first be a much bigger advantage? Theoretically, given the state of modern chess theory not much would have changed. Then, is it fair to say that if both players have the same number of moves per turn, the position should be fairly equal?

It's hard to say for sure. But surely there will be many variations in the openings, openings would become much more than attack or defense. It might enable openings where simultaneous attack and defense is possible or a swiftly developed attack on one side. If such an 2-step attack comes into the picture, the defense will need to think whether they should defend the 1st step or the 2nd step or both. Let's call this variant **multi-chess**, a chess where players can move N pieces per turn.

It's not the first time that multiple moves have been seen. In a sort of odds game, where one player allows the other to make N moves as white before the game starts. This is an **asymmetric** game where the game starts from an unequal position.

I have not seen many games where a player allows the other to make N moves every turn while they make only 1 move each turn. In fact that might be too difficult of an odds. Imagine being attacked on 2 fronts while being able to defend only 1 side. But the intent of playing multiple moves is a bit different in my thought up variant.

The variant which I'd like to propose as **par-chess** which stands for parallel chess, To put it simply, it's a team match of chess formed by dividing the board into N regions to enable N players to play simultaneously that is each player of each team moves 1 piece per turn. Here N is a number greater than 0. And par-2-chess is normal chess. Then we have the below divisions:

| Variant Name | Board                                                 |
| ------------ | ----------------------------------------------------- |
| par-1-chess  | ![base board](base-board.jpg)                         |
| par-2-chess  | ![base board par-2-chess](base-board-par-2-chess.jpg) |
| par-3-chess  | ![base board par-3-chess](base-board-par-3-chess.jpg) |
| par-4-chess  | ![base board par-4-chess](base-board-par-4-chess.jpg) |
| par-5-chess  | ![base board par-5-chess](base-board-par-5-chess.jpg) |

The board divisions are very primitive, maybe it needs more logic to it. Like making regions based on the sum of the piece values. I can imagine it being playable (theoretically) till par-16-chess where each player would have a piece and it's pawn. The variant goes up to par-32-chess wherein each player controls a single piece. Almost feels chaotic when 16 moves occur each turn.

I feel the concept is an in between of Turn-based Strategy (TBS) and Real-Time Strategy (RTS) game mechanics to chess which is purely turn-based.

Interestingly enough found this version of [RTS chess](https://rtschess.herokuapp.com). No turns at all, after moving a piece it has a cool-down time before moving it again.
