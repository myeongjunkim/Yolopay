let now = new Date();
const WEEKDAY = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'];
let week = WEEKDAY[now.getDay()];
let date = now.getDate();

window.addEventListener('DOMContentLoaded', function () {
    document.getElementById('num-date').innerHTML = date;
    document.getElementById('day').innerHTML = week;
});

function statsModal() {
    console.log('st');
    document.getElementById('bg').style.display = 'block';
    document.getElementById('statsModal').style.display = 'block';
}

function dailyModal() {
    document.getElementById('bg').style.display = 'block';
    document.getElementById('dailyModal').style.display = 'block';
}

function close() {
    document.getElementById('bg').style.display = 'none';
    document.getElementById('statsModal').style.display = 'none';
    document.getElementById('dailyModal').style.display = 'none';
}
