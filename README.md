Game ALgorithm:
2) Game 3 Algorithm
1)  functions 
                a)  random_non_square() Function:
i) This function generates a random number between 100 & 500
ii) the function generates random numbers until a number, not a square is found.
iii) Finally, the function returns the non-square number.

b) get_valid_moves(pile) Function:

i) This function takes as input the current size of the pile.
ii) It generates a list of valid moves for a player to remove coins from the pile.
iii) The valid moves are non-zero square numbers up to the square root of the pile size.
iv) Return a list that contains square numbers from 1 to the largest square < or = to pile.

               c) def get_valid_pile(pile) Function:
i) This function checks if the square of the integer square root of pile is not equal to pile.
ii) If so it returns a list containing square numbers from 1 to the largest square less than or equal to pile.
iii) Otherwise, return a list containing only the pile.
               d) def manual_choice(pile) Function:   
-	i) Get the list of valid moves for the current pile using get_valid_pile(pile) function.
-	ii)  while loop:
(1) Allow the user to input a number between 1 and 1000.
(2) Check if the input is < or = 0 or if it's a square number.
(3) If it's invalid, print an error message and allow the user to input again.
(4) If it's valid, return the input.

e) player_1() and player_2() Functions:
i)  These functions allow Player 1 and Player 2 to take their turns.
ii) They allow the players to input the number of coins they want to remove from the pile.
iii) They validate the input to ensure the number is a non-zero square.
iv) If the input is invalid (< or = 0 or not a square number), they allow the players to choose again until a valid input is provided.
v) Once there is a valid input they show the chosen number of coins.



2) game loop
1)	form an outer while loop.
2)	Print ("Subtract a square") which is the name of the game.
3)	Form a nested while loop:
a)	While the pile size is greater than 0:
i)	Player 1's Turn:
(1)	Allow Player 1 to remove coins from the pile.
(2)	Update the pile size after Player 1's turn.
(3)	Display the updated pile size.
(4)	Check if Player 1 has won. If he did, end the game and declare Player 1 as the winner.
ii)	Player 2's Turn:
(1)	Allow Player 2 to remove coins from the pile.
(2)	Update the pile size after Player 2's turn.
(3)	Display the updated pile size.
(4)	Check if Player 2 has won. If he did, end the game and declare Player 2 as the winner.
4)	After the game ends and a winner is declared (when the pile size is 0 or less), ask the players if they want to play again(Y/N).
a)	If the players choose ‘N’, end the game and print (Game Over).
