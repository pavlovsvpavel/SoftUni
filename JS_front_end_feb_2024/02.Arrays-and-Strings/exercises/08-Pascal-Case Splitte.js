function solve(string) {
    string = string.split(/(?=[A-Z])/);

    console.log(string.join(", "));
}


solve('SplitMeIfYouCanHaHaYouCantOrYouCan')
solve('HoldTheDoor')
solve('ThisIsSoAnnoyingToDo')