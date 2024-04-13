window.addEventListener("load", solve);

function solve() {
    const contactNameInputElement = document.getElementById('name');
    const contactPhoneInputElement = document.getElementById('phone');
    const contactCategoryInputElement = document.getElementById('category');
    const addButtonElement = document.getElementById("add-btn");
    const checkListElement = document.getElementById("check-list");
    const saveListElement = document.getElementById("contact-list");

    addButtonElement.addEventListener("click", () => {
        const name = contactNameInputElement.value;
        const phone = contactPhoneInputElement.value;
        const category = contactCategoryInputElement.value;

        const contactLiElement = createContactElement(name, phone, category);

        checkListElement.appendChild(contactLiElement);
        addButtonElement.setAttribute("disabled", "disabled");

        clearInputs();
    });

    function createContactElement(name, phone, category) {
        const editButtonElement = document.createElement("button");
        editButtonElement.classList.add("edit-btn");

        const saveButtonElement = document.createElement("button");
        saveButtonElement.classList.add("save-btn");

        const buttonsDivElement = document.createElement("div");
        buttonsDivElement.classList.add("buttons");
        buttonsDivElement.appendChild(editButtonElement);
        buttonsDivElement.appendChild(saveButtonElement);

        const namePElement = document.createElement("p");
        namePElement.textContent = `name:${name}`;
        const phonePElement = document.createElement("p");
        phonePElement.textContent = `phone:${phone}`;
        const categoryPElement = document.createElement("p");
        categoryPElement.textContent = `category:${category}`;

        const articleElement = document.createElement("article");
        articleElement.appendChild(namePElement);
        articleElement.appendChild(phonePElement);
        articleElement.appendChild(categoryPElement);

        const contactLiElement = document.createElement("li");
        contactLiElement.appendChild(articleElement);
        contactLiElement.appendChild(buttonsDivElement);

        editButtonElement.addEventListener('click', () => {
            contactNameInputElement.value = name;
            contactPhoneInputElement.value = phone;
            contactCategoryInputElement.value = category;

            contactLiElement.remove();
            addButtonElement.removeAttribute("disabled");
        });

        saveButtonElement.addEventListener("click", () => {
            buttonsDivElement.remove();

            const deleteButtonElement = document.createElement('button');
            deleteButtonElement.classList.add('del-btn');

            contactLiElement.appendChild(deleteButtonElement);
            saveListElement.appendChild(contactLiElement);

            deleteButtonElement.addEventListener("click", () => {
                contactLiElement.remove();
            });
        });

        return contactLiElement;
    }

    function clearInputs() {
        contactNameInputElement.value = '';
        contactPhoneInputElement.value = '';
        contactCategoryInputElement.value = '';
    }
}  