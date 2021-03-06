let now = new Date();
const WEEKDAY = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'];
let week = WEEKDAY[now.getDay()];
let date = now.getDate();

window.addEventListener('DOMContentLoaded', function () {
    var i = 29;

    document.getElementById('num-date').innerHTML = date;
    document.getElementById('day').innerHTML = week;

    for (i; i < 32; i++) {
        var result = '';
        result = '<li><span>' + i + "</span><img src='../static/img/null.png' id=" + i + "alt='' /></li>";
        document.getElementById('first-week-1').innerHTML += result;
    }
    i = 1;
    for (i; i < 31; i++) {
        if (i <= 4) {
            result = "<li onclick='dailyModal(" + i + ");'><span>0" + i + "</span><img src='../static/img/null.png' id=" + i + " alt='' /></li>";
            document.getElementById('first-week-2').innerHTML += result;
        } else if (i >= 5 && i <= 9) {
            result = "<li onclick='dailyModal(" + i + ");'><span>0" + i + "</span><img src='../static/img/null.png' id=" + i + " alt='' /></li>";
            document.getElementById('second-week').innerHTML += result;
        } else if (i >= 10 && i <= 11) {
            result = "<li onclick='dailyModal(" + i + ");'><span>" + i + "</span><img src='../static/img/null.png' id=" + i + " alt='' /></li>";
            document.getElementById('second-week').innerHTML += result;
        } else if (i >= 12 && i <= 18) {
            result = "<li onclick='dailyModal(" + i + ");'><span>" + i + "</span><img src='../static/img/null.png' id=" + i + " alt='' /></li>";
            document.getElementById('third-week').innerHTML += result;
        } else if (i >= 19 && i <= 25) {
            result = "<li onclick='dailyModal(" + i + ");'><span>" + i + "</span><img src='../static/img/null.png' id=" + i + " alt='' /></li>";
            document.getElementById('fourth-week').innerHTML += result;
        } else {
            result = "<li onclick='dailyModal(" + i + ");'><span>" + i + "</span><img src='../static/img/null.png' id=" + i + " alt='' /></li>";
            document.getElementById('fifth-week-1').innerHTML += result;
        }
    }
    i = 1;
    for (i; i < 3; i++) {
        if (i <= 2) {
            result = '<li><span>0' + i + "</span><img src='../static/img/null.png' id=" + i + " alt='' /></li>";
            document.getElementById('fifth-week-2').innerHTML += result;
        }
    }
    console.log(date)
    document.getElementById(date).className = 'active-day';
});

function statsModal() {
    console.log('st');
    document.getElementById('bg').style.display = 'block';
    document.getElementById('statsModal').style.display = 'block';

    const yolo_rate = document.getElementById('yoloRateText').innerHTML;
    const fire_rate = document.getElementById('fireRateText').innerHTML;
    console.log(yolo_rate);
    document.getElementById('yoloRate').style.width = yolo_rate;
    document.getElementById('fireRate').style.width = fire_rate;
}

function dailyModal(date) {
    document.getElementById('bg').style.display = 'block';
    document.getElementById('dailyModal').style.display = 'block';
    document.getElementById('modalDate').innerHTML = date;
    document.getElementById('date_only').value = date;
}

function close() {
    document.getElementById('bg').style.display = 'none';
    document.getElementById('statsModal').style.display = 'none';
    document.getElementById('dailyModal').style.display = 'none';
}
