let fullPool = [];      // every available player, combined from both files
let currentChoices = []; // the 10 players currently shown to pick from
let roster = [];         // the 8 players the user has drafted so far
const ROSTER_SIZE = 8;

// Load both datasets and merge them into one pool
async function loadPlayers() {
  const [legendsRes, seasonRes] = await Promise.all([
    fetch('data/players.json'),
    fetch('data/season_2025_26.json')
  ]);
  const legends = await legendsRes.json();
  const seasonPlayers = await seasonRes.json();

  fullPool = [...legends, ...seasonPlayers];
}

// Fisher-Yates shuffle - picks a random order without bias
function shuffle(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// Pull 10 random players from whatever's left in the pool
function drawNextChoices() {
  if (roster.length >= ROSTER_SIZE) {
    showFinalRoster();
    return;
  }

  const shuffled = shuffle(fullPool);
  currentChoices = shuffled.slice(0, 10);

  renderChoices();
}

// When the user clicks a player card
function pickPlayer(index) {
  const picked = currentChoices[index];
  roster.push(picked);

  // Remove the picked player from the pool so they can't show up again
  fullPool = fullPool.filter(p =>
    !(p.player === picked.player && p.season === picked.season)
  );

  drawNextChoices();
}

// --- Rendering (basic version, styling comes later) ---
function renderChoices() {
  const container = document.getElementById('draft-container');
  container.innerHTML = `<h2>Pick ${roster.length + 1} of ${ROSTER_SIZE}</h2>`;

  currentChoices.forEach((p, i) => {
    const card = document.createElement('div');
    card.className = 'player-card';
    card.innerHTML = `
      <strong>${p.player}</strong> (${p.season})<br>
      ${p.ppg} PPG, ${p.rpg} RPG, ${p.apg} APG
    `;
    card.onclick = () => pickPlayer(i);
    container.appendChild(card);
  });
}

function showFinalRoster() {
  const container = document.getElementById('draft-container');
  container.innerHTML = '<h2>Your Roster</h2>';

  roster.forEach(p => {
    const card = document.createElement('div');
    card.className = 'player-card';
    card.innerHTML = `<strong>${p.player}</strong> (${p.season})`;
    container.appendChild(card);
  });
}

// Kick things off once the page loads
window.onload = async () => {
  await loadPlayers();
  drawNextChoices();
};