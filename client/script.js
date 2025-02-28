// function voiceAssistant() {
//   fetch("http://localhost:5000/voice_assistant")
//     .then((response) => response.json())
//     .then((data) => alert(data.output || data.error))
//     .catch((error) => console.error("Error:", error));
// };


document.getElementById("startAssistant").addEventListener("click", () => {
  fetch("http://localhost:5000/voice_assistant")
      .then(response => response.json())
      .then(data => {
          alert(data.message || "Error starting voice assistant");
      })
      .catch(error => {
          console.error("Error:", error);
      });
});
