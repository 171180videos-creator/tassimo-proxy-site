async function loadOffers() {
    const container = document.getElementById('offers');
    try {
        const res = await fetch('http://localhost:5000/api/offers');
        const offers = await res.json();
        container.innerHTML = '';
        offers.forEach(o => {
            const div = document.createElement('div');
            div.className = 'offer';
            div.innerHTML = `<h3>${o.produkt}</h3><p>${o.preis} – ${o.haendler} (bis ${o.gueltig_bis})</p>`;
            container.appendChild(div);
        });
    } catch (err) {
        container.innerHTML = 'Fehler beim Laden der Angebote.';
        console.error(err);
    }
}
loadOffers();
