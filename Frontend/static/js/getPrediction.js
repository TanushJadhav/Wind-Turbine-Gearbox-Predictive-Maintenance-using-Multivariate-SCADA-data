// Initial result value
let initialResult = "Please submit the form to get your Forcasted Temperature";

// Display initial result
document.getElementById("result").innerHTML =
  "<strong>Predicted Temperature: </strong> " + initialResult;

document
  .getElementById("predictionForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    fetch("/predict", {
      method: "POST",
      body: JSON.stringify(Object.fromEntries(formData)),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        const predictionResult = data.prediction;
        let resultMessage = "";
        let resultColor = "";

        if (predictionResult === "High") {
          resultMessage =
            "Higher Spending Score: Indicates a higher capacity or willingness to spend. It suggests that the individual or household has a relatively higher disposable income after covering essential expenses and savings. They might afford more luxuries, investments, or have the capability to spend on non-essential items or experiences without affecting their financial stability significantly.";
          resultColor = "red";
        } else if (predictionResult === "Average") {
          resultMessage =
            "Average Spending Score: This indicates a moderate capacity or willingness to spend. Individuals with an average score may have a balanced approach to managing their finances, allocating funds for all types of spending. They might make thoughtful decisions when it comes to non-essential purchases.";
          resultColor = "yellow";
        } else if (predictionResult === "Low") {
          resultMessage =
            "Lower Spending Score: Suggests a more conservative spending behavior. Individuals with lower scores might prioritize savings, essential expenses, or have a limited disposable income for discretionary spending. They might be more cautious or constrained in their spending habits.";
          resultColor = "green";
        }

        const resultElement = document.getElementById("result");
        resultElement.innerHTML =
          '<strong>Your Spending Score Category is:</strong> <b style="color: ' +
          resultColor +
          ';">' +
          predictionResult +
          "</b> <br> " +
          resultMessage;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
