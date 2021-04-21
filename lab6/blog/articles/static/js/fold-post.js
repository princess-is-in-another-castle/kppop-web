var foldBtns = document.getElementsByClassName("fold-button");
console.log(foldBtns)
for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function (event) {
        console.log("you clicked ", event.target);
    });


    foldBtns[i].addEventListener("click", function (e) {
        if (e.target.innerHTML === "развернуть") {
            e.target.innerHTML = "свернуть";
            event.target
                .parentElement
                .getElementsByClassName('one-post-folded')[0]
                .className = "one-post"
        } else {
            e.target.innerHTML = "развернуть";
            event.target
                .parentElement
                .getElementsByClassName('one-post')[0]
                .className = "one-post-folded"
        }
    });

}
