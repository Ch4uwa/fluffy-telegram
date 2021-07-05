# Allows a user to enter a stock symbol (like "MSFT") in one program, and submit this choice to the other
# program. These programs can be a web client and a server, but you are free to solve this in any way you see
# fit. Just make sure that the two separate programs are communicating with one another;

# Downloads market data in the server-like program for whatever stock symbol the user submitted;

# Lets the user guess yesterday's closing price of the previously specified stock. Report back to the user if their
# guess was "Too low", "Too high" or "Correct" to the nearest $1;


import server_like


server_like.d_data("MSFT")
