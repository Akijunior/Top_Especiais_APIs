// 1ª Questão

var firstName = "Mateus";
var interest = "draw";
var hobby = "read";
var awesomeMessage = "Hi, my name is " + firstName + ". I love " + interest +
    ". In my spare time, I like to " + hobby + ".";
console.log(awesomeMessage);

// 2ª Questão

var musicians = 1;
if (musicians === 0) {
    console.log("not a group");
} else if (musicians === 1) {
    console.log("solo");
} else if (musicians === 2) {
    console.log("duet");
} else if (musicians === 3) {
    console.log("trio");
} else if (musicians === 4) {
    console.log("quartet");
} else if (musicians > 4) {
    console.log("this is a large group");
} else {
    console.log("not a group");
}

// ou

var musicians = 0;

var options = ["solo", "duet", "trio", "quartet"];
console.log(musicians > 4 ? "this is a large group" : musicians < 1 ? "not a group" : options[musicians - 1]);


// 3ª Questão

for (var x = 0; x < 26; x++) {
    for (var y = 0; y < 100; y++) {
        console.log(x + "-" + y);
    }
}

// 4ª Questão

var x = 1;

while (x < 21) {
    if (x % 5 === 0 && x % 3 === 0)
        console.log("JuliaJames");
    else if (x % 3 === 0)
        console.log("Julia");
    else if (x % 5 === 0)
        console.log("James");
    else
        console.log(x);
    x += 1;
}

// 5ª Questão

var laugh = function(num) {
    var text = ""
    for (var i = 0; i < num; i++) {
        text += "ha";
    }
    text += "!";
    return text;
}
console.log(laugh(10));

// 6ª Questão

var numbers = [
    [243, 12, 23, 12, 45, 45, 78, 66, 223, 3],
    [34, 2, 1, 553, 23, 4, 66, 23, 4, 55],
    [67, 56, 45, 553, 44, 55, 5, 428, 452, 3],
    [12, 31, 55, 445, 79, 44, 674, 224, 4, 21],
    [4, 2, 3, 52, 13, 51, 44, 1, 67, 5],
    [5, 65, 4, 5, 5, 6, 5, 43, 23, 4424],
    [74, 532, 6, 7, 35, 17, 89, 43, 43, 66],
    [53, 6, 89, 10, 23, 52, 111, 44, 109, 80],
    [67, 6, 53, 537, 2, 168, 16, 2, 1, 8],
    [76, 7, 9, 6, 3, 73, 77, 100, 56, 100]
];

for (var row = 0; row < numbers.length; row++) {
    for (var column = 0; column < numbers[row].length; column++) {
        if (numbers[row][column] % 2 === 0)
            numbers[row][column] = "even";
        else
            numbers[row][column] = "odd";
    }
}
console.log(numbers);

// 7ª Questão

var savingsAccount = {
    balance: 1000,
    interestRatePercent: 1,
    deposit: function addMoney(amount) {
        if (amount > 0) {
            savingsAccount.balance += amount;
        }
    },
    withdraw: function removeMoney(amount) {
        var verifyBalance = savingsAccount.balance - amount;
        if (amount > 0 && verifyBalance >= 0) {
            savingsAccount.balance -= amount;
        }
    },
    printAccountSummary: function printAccountSummary() {
        return "Welcome!\nYour balance is currently $" + savingsAccount.balance +
            " and your interest rate is " + savingsAccount.interestRatePercent + "%.";

    }
};
console.log(savingsAccount.printAccountSummary());