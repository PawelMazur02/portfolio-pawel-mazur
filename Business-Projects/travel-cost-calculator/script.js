document.addEventListener('DOMContentLoaded', async () => {
    await populateCurrencyDropdown();
    document.getElementById('addItemButton').addEventListener('click', addItem);
    document.getElementById('currency').addEventListener('change', handleCurrencyChange);

    // Add input validation for number fields
    document.querySelectorAll('input[type="number"]').forEach(input => {
        input.addEventListener('input', validateDecimalPlaces);
        input.addEventListener('change', validateDecimalPlaces);
        input.step = "1";  // Ensure step is set to 1 for incrementing by 1
    });
});

async function populateCurrencyDropdown() {
    const prioritizedCurrencies = [
        { code: "PLN", currency: "Polski złoty" },
        { code: "EUR", currency: "Euro" },
        { code: "USD", currency: "Dolar amerykański" }
    ];

    try {
        const response = await fetch('https://api.nbp.pl/api/exchangerates/tables/A/?format=json');
        if (!response.ok) {
            throw new Error(`Error fetching currencies: ${response.statusText}`);
        }
        const data = await response.json();
        const currencies = data[0].rates;

        const currencyDropdown = document.getElementById('currency');

        // Add prioritized currencies first
        prioritizedCurrencies.forEach(currency => {
            const option = document.createElement('option');
            option.value = currency.code;
            option.textContent = `${currency.code} - ${currency.currency}`;
            currencyDropdown.appendChild(option);
        });

        // Add remaining currencies
        currencies.forEach(currency => {
            if (!prioritizedCurrencies.some(prior => prior.code === currency.code)) {
                const option = document.createElement('option');
                option.value = currency.code;
                option.textContent = `${currency.code} - ${currency.currency}`;
                currencyDropdown.appendChild(option);
            }
        });
    } catch (error) {
        console.error(error);
    }
}

function handleCurrencyChange() {
    const currency = document.getElementById('currency').value;
    const backgroundVideo = document.getElementById('backgroundVideo');

    if (currency === 'USD') {
        backgroundVideo.querySelector('source').src = 'background_USD.mp4';
    } else {
        backgroundVideo.querySelector('source').src = 'background.mp4';
    }
    backgroundVideo.load();
}

function addItem() {
    const costItems = document.getElementById('costItems');
    const newItemIndex = document.querySelectorAll('.cost-item').length;
    const newItem = document.createElement('div');
    newItem.classList.add('form-group', 'cost-item');
    newItem.innerHTML = `
        <label for="item${newItemIndex}Name">Nazwa pozycji:</label>
        <input type="text" id="item${newItemIndex}Name" name="item${newItemIndex}Name" placeholder="Np. Bilety wstępu">
        <label for="item${newItemIndex}Cost">Koszt:</label>
        <input type="number" id="item${newItemIndex}Cost" name="item${newItemIndex}Cost" min="0" step="1">
        <button type="button" onclick="confirmItem(${newItemIndex})">OK</button>
    `;
    costItems.appendChild(newItem);

    // Add input validation for the new number field
    const newInput = document.getElementById(`item${newItemIndex}Cost`);
    newInput.addEventListener('input', validateDecimalPlaces);
    newInput.addEventListener('change', validateDecimalPlaces);
    newInput.step = "1";  // Ensure step is set to 1 for incrementing by 1
}

function confirmItem(index) {
    const itemName = document.getElementById(`item${index}Name`).value;
    const itemCostLabel = document.querySelector(`label[for="item${index}Cost"]`);
    itemCostLabel.textContent = `Koszt ${itemName}:`;

    document.getElementById(`item${index}Name`).style.display = 'none';
    document.querySelector(`label[for="item${index}Name"]`).style.display = 'none';
    document.querySelector(`button[onclick="confirmItem(${index})"]`).style.display = 'none';
}

async function fetchExchangeRate(currency) {
    if (currency === 'PLN') {
        return 1;
    }

    try {
        const response = await fetch(`https://api.nbp.pl/api/exchangerates/rates/a/${currency}/?format=json`);
        if (!response.ok) {
            throw new Error(`Error fetching exchange rate for ${currency}: ${response.statusText}`);
        }
        const data = await response.json();
        return data.rates[0].mid;
    } catch (error) {
        console.error(error);
        return null;
    }
}

async function calculateTripCost() {
    const currency = document.getElementById('currency').value.toUpperCase();
    const exchangeRate = await fetchExchangeRate(currency);

    if (exchangeRate === null) {
        document.getElementById('totalCost').textContent = 'Błąd w pobieraniu kursu waluty. Proszę spróbować ponownie.';
        return;
    }

    let totalCost = 0;

    document.querySelectorAll('.cost-item').forEach(item => {
        const itemCost = parseFloat(item.querySelector(`input[type="number"]`).value);
        if (!isNaN(itemCost)) {
            totalCost += itemCost * exchangeRate;
        }
    });

    document.getElementById('totalCost').textContent = `${totalCost.toFixed(2)} Zł`;
}

function validateDecimalPlaces(event) {
    const value = event.target.value;
    const regex = /^\d+(\.\d{0,2})?$/;

    if (!regex.test(value)) {
        event.target.value = value.slice(0, -1);
    }
}
