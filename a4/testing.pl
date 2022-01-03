%FOR EXACTLY THE PROJECT EXAMPLE TRY: "place_mirrors(8,
% [[2,0,2,3],[4,4,2,6],[9,0,2,4]], X)."

%travel right
%travel(Position, NewPosition).
travel([X,Y, right],[A,Y, right]):- A is X + 1.
travel([X,Y,down],[X,B,down]):- B is Y + 1.
travel([X,Y,up],[X,B,up]):- B is Y - 1.


correctMirrorCount(Mirrors):- length(Mirrors, 0);length(Mirrors,1); length(Mirrors,2); length(Mirrors,3);length(Mirrors,4);length(Mirrors,5);length(Mirrors,6);length(Mirrors,7);length(Mirrors,8).

%
%travel([X,Y],[A,Y]):- A is X + 1.
%travel([X,Y],[X,B]):- B is Y + 1.
%travel([X,Y],[X,B]):- B is Y - 1.

%travel up
%travel(x, y + 1).
%travel down
%travel(x, y - 1).

deviate([X, Y, right], \, [X, B, down]):- B is Y + 1.
deviate([X, Y, right], /, [X, B, up]):- B is Y - 1.

deviate([X, Y, down], \, [A, Y, right]):- A is X + 1.
deviate([X, Y, up], /, [A, Y, right]):- A is X + 1.

getMove(CurrentState, NewState, Mirrors, Mirrors):- travel(CurrentState, NewState).
getMove([X, Y, Direction], NewState, Mirrors, [[X, Y, /]|Mirrors]):- deviate([X, Y, Direction], / , NewState).
getMove([X, Y, Direction], NewState, Mirrors, [[X, Y, \]|Mirrors]):- deviate([X, Y, Direction], \ , NewState).

notwithin([X,Y,W,H],[A,B,_]):- A < X + 1 ; A > X + W ; B < Y + 1 ; B > Y + H.

within([X, Y, W, H], [A, B,_]) :- X < A, A =< X+W, Y < B, B =< Y+H.

%notwithin([X,Y,W,H],[A,B]):- A < X + 1 ; A > X + W.
%notwithin([X,Y,W,H],[A,B]):- A < X + 1, !.
%notwithin([X,Y,W,H],[A,B]):- A > X + W, !.

%notwithin([X,Y,W,H],[A,B]):- B < Y + 1 ; B > Y + H.
%notwithin([X,Y,W,H],[A,B]):- B < Y + 1, !.
%notwithin([X,Y,W,H],[A,B]):- B > Y + H, !.

safeMoveV2([],[A,B,_]).
%within([X, Y, W, H], [A, B]) :- X < A, A =< X+W, Y < B, B =< Y+H.
safeMoveV2([X,Y,W,H],[A,B,_]):- notwithin([X,Y,W,H],[A,B,_]), !.
safeMoveV2([Head|Tail], [A,B,_]):- safeMoveV2(Head, [A,B,_]), safeMoveV2(Tail, [A,B,_]), !.

% Position = [X, Y, D]
% Move will happen in a given direction specified like goat or wolf in
% the example and then when hit unsafe move deviate will change
% direction and we assume mirror is there.
%deviate(Position, /, NewPosition)
%
% %
% Either place a mirrror as soon as possible or when hitting an object
% nextMove(Position, Mirrors, NewPosition, NewMirrors)
%   1. If mirror there (Mirrors contains Position), deviate
%   2. No mirror, put a mirror -> deviate
%   3. No mirror, go straight -> travel

place_mirrors(Laserheight, Obstacles, Ans):- solve([1, Laserheight, right],[12, Laserheight, right], Obstacles, [], Ans).

solve(LastState, LastState, Obstacles, Mirrors, Mirrors).
solve(CurrentState, LastState, Obstacles, Mirrors, Ans):-
    getMove(CurrentState, NewState, Mirrors, NewMirrors),
    safeMoveV2(Obstacles, NewState),
    within([0,0,12,10], NewState),
    correctMirrorCount(Mirrors),
    solve(NewState, LastState, Obstacles, NewMirrors, Ans).


% Can just take the correct path and calculate mirrors from that
% possibly instead of caluclating mirrors along the way.
%solve(Obstacles, AnsPath):- solve(Obstacles,[[1,8]],AnsPath).
%solve(Obstacles, [S|_], [S]):- S = [12,8], !.
% solve(Obstacles, [S|Path],[S|AnsPath]):- travel(S, NextState),
% within([0,0,12,10], NextState),
% not_member(NextState,[S|Path]),solve(Obstacles,[NextState, S | Path],
% AnsPath), safeMoveV2(Obstacles,NextState).


