const page = document.querySelector("[data-mock-page]");
const choices = [...document.querySelectorAll("[data-choice]")];
const feedback = document.querySelector("[data-feedback]");
const reveal = document.querySelector("[data-reveal]");
const controls = [...document.querySelectorAll("[data-control]")];

let prediction = "";

choices.forEach((choice) => {
  choice.addEventListener("click", () => {
    prediction = choice.dataset.choice;
    choices.forEach((candidate) => {
      candidate.setAttribute("aria-pressed", String(candidate === choice));
    });
    feedback.className = "feedback";
    feedback.textContent = "Prediction saved. Reveal the intended order, then test what changes it.";
  });
});

reveal.addEventListener("click", () => {
  if (!prediction) {
    feedback.className = "feedback";
    feedback.textContent = "Choose what caught your eye first. The prediction is the useful part.";
    return;
  }

  const caughtAction = prediction === "action";
  feedback.className = caughtAction ? "feedback good" : "feedback";
  feedback.textContent = caughtAction
    ? "That is the defect. The secondary action competes with the page title, so the reading order is ambiguous."
    : "Reasonable. The page is deliberately flat, so attention can vary by reader. That ambiguity is the defect.";
});

controls.forEach((control) => {
  const target = document.querySelector(control.dataset.target);
  const output = control.closest(".control").querySelector("output");

  const apply = () => {
    const value = Number(control.value);
    target.style.setProperty(control.dataset.property, `${value}${control.dataset.unit}`);
    output.value = control.dataset.label.replace("{value}", value);
    page.classList.remove("flat");
  };

  control.addEventListener("input", apply);
});

document.querySelector("[data-reset]").addEventListener("click", () => {
  page.classList.add("flat");
  document.querySelector(".mock-title").removeAttribute("style");
  document.querySelector(".mock-copy").removeAttribute("style");
  document.querySelector(".mock-actions").removeAttribute("style");
  controls.forEach((control) => {
    control.value = control.defaultValue;
    const output = control.closest(".control").querySelector("output");
    output.value = "Not applied";
  });
});
