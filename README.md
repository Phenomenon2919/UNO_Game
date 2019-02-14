# Program to derive the winner of a UNO game.

## Input format
* *Input would be provided from the server*
The game state provided by the server consists of the following information in this exact order:
1. Number of players
2. Number of rounds in the game
3. Round ID, R
4. Player ID, P , followed by cards with player P at end of round R. The individual cards in the deck are separated by a comma(','). The player ID and deck are separated by a colon(':'). This is repeated for all players. Note that the deck will be empty for the winner and thus will be not be included in round state.
5. '0' signifying data for round R has ended and data for next round will begin.

Each of the above values are separated by pipes('||') before sending to client. This entire string
is sent to the client terminated by a newline character('\n'). Here is a sample game state sent
by server to client:

**3||2||1||1:2,0,S,W||3:0,1,S||0||2||2:F,6||3:4,5,W,3,0||0||**

Here is an expanded version of the above input with explanation of each field:
Field Description
3 --> Number of players
2 --> Number of rounds
1 --> Start of state of round 1 of game.
1:2,0,S,W --> Cards with player 1(here - 2, 0, skip and wild) at end of current round(1).
3:0,1,S --> Cards with player 3 at end of current round(1).
0 --> End of state of round 1.
2 --> Start of state of round 2 of game.
2:F,6 --> Cards with player 2 at end of current round(2).
3:4,5,W,3,0 --> Cards with player 3 at end of current round(2).
0 --> End of state of round 2.

## Output format
The server expects a JSON object as response from the client. The JSON object must contain
the following information:
• Round winners: A dictionary mapping between round IDs and round winning player IDs.
• Scores: A dictionary mapping between player IDs and their final scores.
• Overall winner: ID of player who has won the game.
For the example game state described in input format section, the correct client response would
be the JSON string

**{"round_winners": {"1": 2, "2": 1}, "overall_winner": 1, "scores": {"1": 118,
"2": 93, "3": 0}}**

* Output is sent back to the server

## Executing the python program
* $ python2 client.py <Server IP Address> <Server port>
 
