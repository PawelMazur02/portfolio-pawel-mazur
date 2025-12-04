# Travel Cost Calculator

A simple but practical web application that calculates the total cost of a trip based on user-provided expenses.  
This project was created as part of an IT project management course and demonstrates basic front-end development, dynamic DOM manipulation and API consumption.

---

## Features

### Add dynamic cost items
Users can add multiple cost rows such as:
- transport  
- accommodation  
- food  
- additional custom expenses  

Each row automatically updates the total.

### Automatic currency conversion (NBP API)
The application connects to the **NBP (National Bank of Poland) API** to fetch the current USD→PLN exchange rate.

Depending on the selected currency:
- prices are recalculated  
- the final result is displayed in PLN or USD  

### Dynamic background video
The background changes depending on the selected currency:

- 🇵🇱 PLN → `background.mp4`  
- 🇺🇸 USD → `background_USD.mp4`  

### Clean & responsive layout
Built with simple HTML, CSS and vanilla JavaScript.

---

## Tech Stack

- **HTML5** – UI structure  
- **CSS3** – layout, styling, responsive design  
- **JavaScript (Vanilla)** – logic, API communication, DOM manipulation  
- **External API** – NBP exchange rates  
- **Media** – MP4 background videos  

---

## What I Learned

- Building small interactive web apps  
- Working with external APIs (fetch, JSON parsing)  
- Handling DOM events and dynamic UI updates  
- Improving UX with visual effects  
- Structuring a multi-file GitHub project  


