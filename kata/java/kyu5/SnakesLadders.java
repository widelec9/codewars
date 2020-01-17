package kyu5;

public class SnakesLadders {
	private int[] board = {0,
	                       0, 38, 0, 0, 0, 0, 14, 31, 0, 0,
	                       0, 0, 0, 0, 26, 6, 0, 0, 0, 0,
	                       42, 0, 0, 0, 0, 0, 0, 84, 0, 0,
	                       0, 0, 0, 0, 0, 44, 0, 0, 0, 0,
	                       0, 0, 0, 0, 0, 25, 0, 0, 11, 0,
	                       67, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	                       0, 19, 0, 60, 0, 0, 0, 0, 0, 0,
	                       91, 0, 0, 53, 0, 0, 0, 98, 0, 0,
	                       0, 0, 0, 0, 0, 0, 94, 0, 68, 0,
	                       0, 88, 0, 0, 75, 0, 0, 0, 80, 0};
	private byte player = 0;
	private int[] square = {0, 0};
	private boolean gameOver = false;
	
	public String play(int die1, int die2) {
		if (gameOver == true) {
			return "Game over!";
		}
		
		int nextSquare = (square[player] + die1 + die2 <= 100) ? (square[player] + die1 + die2) : (200 - square[player] - die1 - die2);
		square[player] = board[nextSquare] == 0 ? nextSquare : board[nextSquare];
		
		if (square[player] == 100) {
			gameOver = true;
			return String.format("Player %d Wins!", player + 1);
		}
		
		if (die1 != die2) {
			player ^= 1;
			return String.format("Player %d is on square %d", (player ^ 1) + 1, square[player ^ 1]);
		}
		return String.format("Player %d is on square %d", player + 1, square[player]);
	}
}