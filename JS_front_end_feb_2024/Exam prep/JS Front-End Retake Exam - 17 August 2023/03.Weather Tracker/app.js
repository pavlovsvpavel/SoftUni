const baseUrl = 'http://localhost:3030/jsonstore/tasks/'

const loadHistoryButton = document.getElementById('load-history');
const addWeatherButton = document.getElementById('add-weather');
const editWeatherButton = document.getElementById('edit-weather');
const weatherListElement = document.getElementById('list');
const locationInputElement = document.getElementById('location');
const temperatureInputElement = document.getElementById('temperature');
const dateInputElement = document.getElementById('date');
const formWeatherElement = document.getElementById('form');


loadHistoryButton.addEventListener('click', loadHistory);
addWeatherButton.addEventListener('click', addWeather);
editWeatherButton.addEventListener('click', editWeatherRecord);
weatherListElement.addEventListener('click', deleteWeatherRecord);
    
function createWeatherElement(record) {
    const changeButtonElement = document.createElement('button');
    changeButtonElement.classList.add('change-btn');
    changeButtonElement.textContent = 'Change';
    changeButtonElement.addEventListener('click', (e) => changeWeatherRecord(e, record));

    const deleteButtonElement = document.createElement('button');
    deleteButtonElement.classList.add('delete-btn');
    deleteButtonElement.textContent = 'Delete';

    const buttonsDivElelemnt = document.createElement('div');
    buttonsDivElelemnt.classList.add('buttons-container');
    buttonsDivElelemnt.appendChild(changeButtonElement);
    buttonsDivElelemnt.appendChild(deleteButtonElement);

    const locationH2Element = document.createElement('h2');
    locationH2Element.textContent = record.location;

    const dateH3Element = document.createElement('h3');
    dateH3Element.textContent = record.date;

    const temperatureH3Element = document.createElement('h3');
    temperatureH3Element.setAttribute('id', 'celsius');
    temperatureH3Element.textContent = record.temperature;

    const containerDivElement = document.createElement('div');
    containerDivElement.classList.add('container');

    containerDivElement.appendChild(locationH2Element);
    containerDivElement.appendChild(dateH3Element);
    containerDivElement.appendChild(temperatureH3Element);
    containerDivElement.appendChild(buttonsDivElelemnt);

    containerDivElement.setAttribute('data-id', record._id);

    return containerDivElement;

}

function clearInputFields() {
    locationInputElement.value = '';
    temperatureInputElement.value = '';
    dateInputElement.value = '';
}

async function loadHistory() {
    const response = await fetch(baseUrl);
    const weatherRecords = await response.json();

    weatherListElement.innerHTML = '';

    const weatherListFragment = document.createDocumentFragment();

    Object
        .values(weatherRecords)
        .forEach(record => {
            weatherListFragment.appendChild(createWeatherElement(record));
        })

    weatherListElement.appendChild(weatherListFragment);
}

async function addWeather() {
    const weatherRecord = getInputData();

    const response = await fetch(baseUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(weatherRecord)
    });

    if(!response.ok) {
        return;
    }

    clearInputFields();

    await loadHistory();
}

function changeWeatherRecord(e, record) {
    // const weatherElement = e.currentTarget.closest('.container')
    const weatherElement = e.currentTarget.parentElement.parentElement;  // Only for Judge
    weatherElement.remove();

    locationInputElement.value = record.location;
    temperatureInputElement.value = record.temperature;
    dateInputElement.value = record.date;

    formWeatherElement.setAttribute('data-id', record._id);

    editWeatherButton.removeAttribute('disabled');

    addWeatherButton.setAttribute('disabled', 'disabled');
}

function editWeatherRecord() {
    const weatherRecord = getInputData();

    const weatherRecordId = formWeatherElement.getAttribute('data-id');

    weatherListElement.removeAttribute('data-id');

    fetch(`${baseUrl}${weatherRecordId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({...weatherRecord, _id: weatherRecordId}),
    })
        .then(response => {
            if (!response.ok) {
                return;
            }

        loadHistory();

        editWeatherButton.setAttribute('disabled', 'disabled');

        addWeatherButton.removeAttribute('disabled');

        clearInputFields();
        });
}

function deleteWeatherRecord(e) {
    if (e.target.tagName !== 'BUTTON' || !e.target.classList.contains('delete-btn'))  {
        return;
    }

    const weatherElement = e.target.parentElement.parentElement;

    const weatherRecordId = weatherElement.getAttribute('data-id');

    fetch(`${baseUrl}${weatherRecordId}`, {
        method: 'DELETE',
    })
        .then(res => {
            if (!res.ok) {
                return;
            }

            weatherElement.remove();
        });
}


function getInputData() {
    return {
        location: locationInputElement.value,
        temperature: temperatureInputElement.value,
        date: dateInputElement.value
    }
}