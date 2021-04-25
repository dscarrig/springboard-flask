class BoggleCode {
    constructor(id, seconds = 60){
        this.body = $("#" + id);
        this.words = new Set();

        this.seconds = seconds;
        this.score = 0;
        
        this.timer = setInterval(this.tick.bind(this), 1000);
        this.showTimer();

        $(".submit-word", this.body).on("submit", this.handleSubmit.bind(this));
    }

    async handleSubmit(e){
        e.preventDefault();
        
        const $word = $("#word", this.body);
        let word = $word.val();

        if(this.words.has(word)){
            this.showMessage(`Word already found: ${word}`, "err");
            return;
        }

        const resp = await axios.get("/submit", { params: {word: word}});

        if (resp.data.result === "not-word") {
            this.showMessage(`${word} is not a valid English word`, "err");
          } else if (resp.data.result === "not-on-board") {
            this.showMessage(`${word} is not a valid word on this board`, "err");
          } else {
            this.showWord(word);
            this.score += word.length;
            this.showScore();
            this.words.add(word);
            this.showMessage(`Added: ${word}`, "ok");
          }

        $word.val("").focus();
    }

    showWord(word) {
        $(".words", this.board).append($("<li>", { text: word }));
    }

    showScore() {
        $(".score", this.board).text(this.score);
      }

    showMessage(msg, cls) {
        $(".msg", this.board)
          .text(msg)
          .removeClass()
          .addClass(`msg ${cls}`);
    }

    showTimer() {
        $(".timer", this.board).text(this.seconds);
      }

    async tick() {
      this.seconds -= 1;
      this.showTimer();

      if (this.seconds === 0) {
        console.log("TICK");
        clearInterval(this.timer);
        await this.scoreGame();
      }
    }
}