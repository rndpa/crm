document.addEventListener('DOMContentLoaded', () => {
    const summTodayObj = document.querySelectorAll('.summ__today');
    const summTodayEl = document.getElementById('summToday');

    let summToday = 0.0;
    let now = new Date();

    function summPrice(priceObj, summ) {
        for (const itm of priceObj) {
            summ += Math.round(parseFloat(itm.textContent.replace(',', '.').replace(' ', '')));
        }
        summTodayEl.textContent = `
        Выручка составляет ${summ} рублей
        `;
    }

    summPrice(summTodayObj, summToday)

})