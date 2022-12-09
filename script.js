document.querySelector("button").addEventListener("click", (e) => {
        let textContent = e.target.textContent;
        if (textContent == "Click Me") {
            e.target.textContent = "I was clicked";
         }
         else {
           e.target.textContent = "Click Me";

         }
     });
