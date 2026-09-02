/* Browser-only practice widgets. Each widget makes the learner produce an
   answer before it reveals the model answer or feedback. */
(function () {
  "use strict";

  function message(panel, text) {
    var target = panel.querySelector("[data-practice-message]");
    if (target) target.textContent = text;
  }

  function requireAnswer(panel) {
    var answer = panel.querySelector("textarea, input[type='text']");
    return answer && answer.value.trim().length > 0;
  }

  function gateReveal(panel) {
    var reveal = panel.querySelector("details[data-practice-reveal]");
    if (!reveal) return;
    reveal.addEventListener("toggle", function () {
      if (reveal.open && !requireAnswer(panel)) {
        reveal.open = false;
        message(panel, "Write your answer first, then open the comparison.");
      } else if (reveal.open) {
        message(panel, "");
      }
    });
  }

  function initCloze(panel) {
    var check = panel.querySelector("[data-practice-check]");
    if (!check) return;
    check.addEventListener("click", function () {
      var selects = Array.prototype.slice.call(panel.querySelectorAll("select"));
      if (selects.some(function (select) { return !select.value; })) {
        message(panel, "Choose an answer for each blank first.");
        return;
      }
      var misses = [];
      selects.forEach(function (select) {
        var option = select.options[select.selectedIndex];
        if (option.getAttribute("data-correct") !== "true") {
          misses.push(option.getAttribute("data-why"));
        }
      });
      message(panel, misses.length ? misses.join(" ") : "Correct. You kept the controls in their separate layers.");
    });
  }

  function initDefect(panel) {
    Array.prototype.forEach.call(panel.querySelectorAll("[data-defect-choice]"), function (choice) {
      choice.addEventListener("click", function () {
        var options = panel.querySelectorAll("[data-defect-choice]");
        Array.prototype.forEach.call(options, function (option) { option.classList.remove("right", "wrong"); });
        choice.classList.add(choice.getAttribute("data-correct") === "true" ? "right" : "wrong");
        message(panel, choice.getAttribute("data-why") || "");
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    Array.prototype.forEach.call(document.querySelectorAll("[data-practice]"), function (panel) {
      var type = panel.getAttribute("data-practice");
      if (type === "predict" || type === "explain") gateReveal(panel);
      if (type === "cloze") initCloze(panel);
      if (type === "defect") initDefect(panel);
    });
  });
})();
