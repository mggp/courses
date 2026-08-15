/* ------------------------------------------------------------------
   quiz.js — reusable multiple-choice quiz widget.
   Markup:
     <div class="quiz" id="...">
       <p class="quiz-head"><span>Retrieval practice</span><span class="quiz-score"></span></p>
       <ol class="quiz-questions">
         <li class="quiz-question" data-correct="0" data-explain="Explanation shown after answering.">
           <p class="q-text">Question text?</p>
           <div class="quiz-options">
             <button type="button" class="quiz-option">First</button>
             <button type="button" class="quiz-option">Second</button>
             <button type="button" class="quiz-option">Third</button>
           </div>
           <p class="quiz-feedback"></p>
         </li>
       </ol>
     </div>
   Rules the author must follow: every option in a question has the
   same character length and the same word count, so formatting never
   leaks the answer. data-correct is the 0-based index of the right
   option. data-explain is shown after answering.
   ------------------------------------------------------------------ */
(function () {
  "use strict";

  function initQuiz(quiz) {
    var questions = Array.prototype.slice.call(quiz.querySelectorAll(".quiz-question"));
    var scoreEl = quiz.querySelector(".quiz-score");
    var total = questions.length;
    var answered = 0;
    var correct = 0;

    function renderScore() {
      if (!scoreEl) return;
      var msg = answered + " / " + total;
      if (answered === total) {
        msg += correct === total ? "  —  all correct" : "  —  review the misses";
      }
      scoreEl.textContent = msg;
    }
    renderScore();

    questions.forEach(function (q) {
      var options = Array.prototype.slice.call(q.querySelectorAll(".quiz-option"));
      var correctIndex = parseInt(q.getAttribute("data-correct"), 10);
      var explain = q.getAttribute("data-explain") || "";
      var feedback = q.querySelector(".quiz-feedback");

      options.forEach(function (opt, index) {
        opt.addEventListener("click", function () {
          if (q.classList.contains("done")) return;
          q.classList.add("done");
          answered += 1;

          var isRight = index === correctIndex;
          if (isRight) {
            correct += 1;
            opt.classList.add("right");
          } else {
            opt.classList.add("wrong");
            if (options[correctIndex]) options[correctIndex].classList.add("right");
          }

          if (feedback) {
            feedback.textContent = (isRight ? "Correct. " : "Not quite. ") + explain;
            feedback.classList.add("show");
          }
          options.forEach(function (o) { o.disabled = true; });
          renderScore();
        });
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    Array.prototype.forEach.call(document.querySelectorAll(".quiz"), initQuiz);
  });
})();
