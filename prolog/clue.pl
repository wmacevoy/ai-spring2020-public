:- dynamic at/1.
:- dynamic contains/2.

connected(living_room,north,kichen).
connected(kitchen,south,living_room).
contains(kitchen,knife).
contains(kitchen,ms_white).

see(Thing) :-
    at(Location),
    contains(Location,Thing).

go(Direction) :-
    at(Location),
    connected(Location,Direction,Destination),
    retract(at(Location)),
    assert(at(Destination)).

get(Item) :-
    at(Location),
    contains(Location,Item),
    retract(contains(Location,Item)),
    assert(contains(self,Item)).

drop(Item) :-
    at(Location),
    contains(self,Item),
    retract(contains(self,Item)),
    assert(contains(Location,Item)).

inventory(Item) :- contains(self,Item).

at(kitchen).

    
    
