import React from "react";

export default function App() {
  // const startAssistant = () => {
  //   const SpeechRecognition =
  //     window.SpeechRecognition || window.webkitSpeechRecognition;
  //   const recognition = new SpeechRecognition();
  //   recognition.start();
  //   recognition.onresult = (event) => {
  //     const speechToText = event.results[0][0].transcript;
  //     console.log(speechToText);
  //   };
  // };

  const startAssistant = () => {
    fetch("http://localhost:5000/voice_assistant")
      .then((response) => response.json())
      .then((data) => {
        alert(data.message || "Error starting voice assistant");
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };
  return (
    <>
      <main className="relative w-full h-screen flex flex-col items-center bg-white gap-10 overflow-hidden">
        <div className="w-full h-full">
          <img
            src="./assets/images/Ravenwood.jpg"
            alt="bg"
            className="w-full h-full object-cover"
          />
        </div>
        <div className="absolute z-[99] w-full h-full bg-black/60"></div>
        <div className="absolute z-[999] w-full h-full flex flex-col items-center justify-center gap-10">
          <div className="text-center p-4 bg-white/10 mt-10 rounded-xl gap-5">
            <h1 className="text-5xl text-yellow-500 font-semibold">
              S.H.A.D.O.W
            </h1>
            <p className="text-xl text-white font-semibold tracking-wider">
              <span className="text-red-400">S</span>mart{" "}
              <span className="text-red-400">H</span>and and{" "}
              <span className="text-red-400">A</span>udio{" "}
              <span className="text-red-400">D</span>riven{" "}
              <span className="text-red-400">O</span>perating{" "}
              <span className="text-red-400">W</span>izard
            </p>
          </div>
          <div className="w-full h-full flex justify-center items-center">
            <div className="w-[80%] flex justify-center items-center relative">
              <img
                src="./assets/images/wizard.png"
                className="w-[40%] h-[65%] object-contain bg-none"
                alt="shadow"
              />
              <button onClick={startAssistant}>
                <img
                  src="./assets/images/voice.png"
                  alt="voice"
                  title="Voice Assistant"
                  className="absolute top-[50px] left-80 w-20 h-20 p-2 bg-zinc-300 rounded-full cursor-pointer hover:scale-120 hover:rotate-360 duration-900 transition-transform shadow-xl shadow-red-600 hover:shadow-blue-600"
                />
              </button>
              <img
                src="./assets/images/mouse.png"
                alt="mouse"
                title="Virtual Mouse"
                className="absolute top-[50px] right-80 w-20 h-20 p-2 bg-zinc-300 rounded-full cursor-pointer hover:scale-120 hover:rotate-[-20deg] duration-300 transition-transform shadow-xl shadow-red-600 hover:shadow-blue-600"
              />
              <img
                src="./assets/images/keyboard.png"
                alt="keyboard"
                title="Virtual Keyboard"
                className="absolute bottom-35 left-80 w-20 h-20 p-2 bg-zinc-300 rounded-full cursor-pointer hover:scale-120 transition-transform shadow-xl shadow-red-600 hover:shadow-blue-600"
              />
              <img
                src="./assets/images/exit.png"
                alt="exit"
                title="Exit"
                className="absolute bottom-35 right-80 w-20 h-20 bg-zinc-300 rounded-full cursor-pointer hover:scale-120 transition-transform shadow-xl shadow-red-600 hover:shadow-blue-600"
              />
            </div>
          </div>
        </div>
      </main>
    </>
  );
}
