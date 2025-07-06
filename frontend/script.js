const API = "http://localhost:5000";

// BMI
document.getElementById("bmi-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const height = parseFloat(document.getElementById("bmi-height").value);
  const weight = parseFloat(document.getElementById("bmi-weight").value);

  const res = await fetch(`${API}/bmi`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ height, weight }),
  });
  const data = await res.json();
  document.getElementById("bmi-result").textContent = `BMI: ${data.bmi} (${data.category})`;
});

// Calorie
document.getElementById("calorie-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const age = parseInt(document.getElementById("calorie-age").value);
  const height = parseFloat(document.getElementById("calorie-height").value);
  const weight = parseFloat(document.getElementById("calorie-weight").value);
  const gender = document.getElementById("calorie-gender").value;
  const activity = document.getElementById("calorie-activity").value;

  const res = await fetch(`${API}/daily-calories`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ age, height, weight, gender, activity }),
  });
  const data = await res.json();
  document.getElementById("calorie-result").textContent = `Recommended: ${data.recommended_calories} kcal/day`;
});

// Diet Suggestion
document.getElementById("diet-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const goal = document.getElementById("diet-goal").value;
  const res = await fetch(`${API}/diet-suggestion`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ goal }),
  });
  const data = await res.json();
  document.getElementById("diet-result").textContent = data.suggestion;
});

// Health Check
document.getElementById("health-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const age = parseInt(document.getElementById("health-age").value);
  const weight = parseFloat(document.getElementById("health-weight").value);

  const res = await fetch(`${API}/health-check`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ age, weight }),
  });
  const data = await res.json();
  document.getElementById("health-result").textContent = `Health Status: ${data.status}`;
});

// Exercise
document.getElementById("exercise-btn").addEventListener("click", async () => {
  const res = await fetch(`${API}/exercise-recommendation`);
  const data = await res.json();
  document.getElementById("exercise-result").innerHTML = "<ul>" + data.exercises.map(e => `<li>${e}</li>`).join("") + "</ul>";
});