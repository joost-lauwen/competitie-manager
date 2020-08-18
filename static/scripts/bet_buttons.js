function ButtonClick_BetHome() {
  document.getElementById("id_gamble").value = 1;
  document.getElementById("bet_home").className = "btn btn-warning-clicked";
  document.getElementById("bet_away").className = "btn btn-warning";
  document.getElementById("bet_draw").className = "btn btn-warning";
}

function ButtonClick_BetDraw() {
  document.getElementById("id_gamble").value = 2;
  document.getElementById("bet_draw").className = "btn btn-warning-clicked";
  document.getElementById("bet_home").className = "btn btn-warning";
  document.getElementById("bet_away").className = "btn btn-warning";
}

function ButtonClick_BetAway() {
  document.getElementById("id_gamble").value = 3;
  document.getElementById("bet_away").className = "btn btn-warning-clicked";
  document.getElementById("bet_home").className = "btn btn-warning";
  document.getElementById("bet_draw").className = "btn btn-warning";
}
