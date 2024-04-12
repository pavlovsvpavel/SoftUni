window.addEventListener("load", solve);

function solve() {
    const playerInputElement = document.getElementById("player");
    const scoreInputElement = document.getElementById("score");
    const roundInputElement = document.getElementById("round");
    const addButtonElement = document.getElementById("add-btn");
    const sureListElement = document.getElementById("sure-list");
    const scoreboardListElement = document.getElementById("scoreboard-list");
    const clearButtonElement = document.querySelector(".btn.clear");

    addButtonElement.addEventListener("click", () => {
        const player = playerInputElement.value;
        const score = scoreInputElement.value;
        const round = roundInputElement.value;

        const dartLiElement = createDartElement(player, score, round);

        sureListElement.appendChild(dartLiElement);
        addButtonElement.setAttribute("disabled", "disabled");

        clearInputs();
    });

    clearButtonElement.addEventListener("click", () => {
        scoreboardListElement.innerHTML = "";
    });

    function createDartElement(player, score, round) {
        const editButtonElement = document.createElement("button");
        editButtonElement.classList.add("btn", "edit");
        editButtonElement.textContent = "edit";

        const okButtonElement = document.createElement("button");
        okButtonElement.classList.add("btn", "ok");
        okButtonElement.textContent = "ok";

        const playerPElement = document.createElement("p");
        playerPElement.textContent = `${player}`;
        const scorePElement = document.createElement("p");
        scorePElement.textContent = `Score: ${score}`;
        const roundPElement = document.createElement("p");
        roundPElement.textContent = `Round: ${round}`;

        const articleElement = document.createElement("article");
        articleElement.appendChild(playerPElement);
        articleElement.appendChild(scorePElement);
        articleElement.appendChild(roundPElement);

        const dartLiElement = document.createElement("li");
        dartLiElement.classList.add("dart-item");
        dartLiElement.appendChild(articleElement);
        dartLiElement.appendChild(editButtonElement);
        dartLiElement.appendChild(okButtonElement);

        editButtonElement.addEventListener("click", () => {
            player = playerInputElement.value = player;
            score = scoreInputElement.value = score;
            round = roundInputElement.value = round;

            dartLiElement.remove();
            addButtonElement.removeAttribute("disabled");
        });

        okButtonElement.addEventListener("click", (e) => {
            const [editBtn, okBtn] = dartLiElement.querySelectorAll('button');
            editBtn.remove();
            okBtn.remove();

            scoreboardListElement.appendChild(dartLiElement);
            addButtonElement.removeAttribute("disabled");
        });

        return dartLiElement;
    }

    function clearInputs() {
        playerInputElement.value = "";
        scoreInputElement.value = "";
        roundInputElement.value = "";
    }
}
