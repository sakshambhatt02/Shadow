import React from "react";
import { motion } from "framer-motion";
import Squares from "./components/Squares";

export default function App() {
  const handleStart = async (option) => {
    const response = await fetch(`http://localhost:5000/start/${option}`);
    const data = await response.json();
    alert(data.message);
  };

  const handleStop = async (option) => {
    const response = await fetch(`http://localhost:5000/stop/${option}`);
    const data = await response.json();
    alert(data.message);
  };
  return (
    <div className="relative w-full min-h-screen bg-black">
      {/* Background Animation */}
      <div className="absolute inset-0">
        <Squares
          speed={0.3}
          squareSize={40}
          direction="up"
          borderColor="#fff"
          hoverFillColor="#222"
        />
      </div>

      {/* Main Content */}
      <div className="relative z-10 flex flex-col items-center justify-center min-h-screen p-6 gap-10">
        {/* Title Section */}
        <div className="text-center p-6 bg-zinc-700 rounded-xl w-full max-w-xl">
          <motion.h1
            className="text-4xl md:text-5xl text-yellow-500 font-semibold"
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
          >
            S.H.A.D.O.W
          </motion.h1>
          <motion.p
            className="text-lg md:text-xl text-white font-semibold tracking-wider mt-3"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1, ease: "easeOut", delay: 0.3 }}
          >
            <span className="text-red-400">S</span>mart{" "}
            <span className="text-red-400">H</span>and and{" "}
            <span className="text-red-400">A</span>udio{" "}
            <span className="text-red-400">D</span>riven{" "}
            <span className="text-red-400">O</span>perating{" "}
            <span className="text-red-400">W</span>izard
          </motion.p>
        </div>

        {/* Cards Section */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10 w-full max-w-6xl">
          {/* Voice Assistant */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 1, ease: "easeOut" }}
            className="w-full h-64 sm:h-96 flex flex-col bg-zinc-500 rounded-lg hover:border-2 hover:border-gray-500 hover:scale-110 transition-transform duration-300 overflow-hidden"
          >
            <div className="w-full h-[80%] flex justify-center items-center">
              <img
                src="./assets/voice_assistant.png"
                alt="voice assistant"
                className="w-full h-full object-cover "
              />
            </div>
            <div className="w-full h-[20%] flex items-center justify-center gap-4 p-2">
              <button
                onClick={() => handleStart("voice-assistant")}
                className="px-4 py-2 bg-blue-500 hover:bg-blue-700 rounded-xl text-white"
              >
                Start Voice Assistant
              </button>
              <button
                onClick={() => handleStop("voice-assistant")}
                className="bg-white hover:bg-red-500 rounded-full"
              >
                <img
                  src="./assets/exit.png"
                  alt="exit"
                  className="w-10 h-10 object-cover"
                />
              </button>
            </div>
          </motion.div>

          {/* Virtual Mouse */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 3, ease: "easeOut" }}
            className="w-full h-64 sm:h-96 flex flex-col bg-zinc-500 rounded-lg hover:border-2 hover:border-gray-500 hover:scale-110 transition-transform duration-300 overflow-hidden"
          >
            <div className="w-full h-[80%] flex justify-center items-center">
              <img
                src="./assets/mouse.png"
                alt="virtual mouse"
                className="w-full h-full object-cover"
              />
            </div>
            <div className="w-full h-[20%] flex items-center justify-center gap-4 p-2">
              <button
                onClick={() => handleStart("virtual-mouse")}
                className="px-4 py-2 bg-blue-500 hover:bg-blue-700 rounded-xl text-white"
              >
                Start Virtual Mouse
              </button>
              <button
                onClick={() => handleStop("virtual-mouse")}
                className="bg-white hover:bg-red-500 rounded-full"
              >
                <img
                  src="./assets/exit.png"
                  alt="exit"
                  className="w-10 h-10 object-cover"
                />
              </button>
            </div>
          </motion.div>

          {/* Virtual Keyboard */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 5, ease: "easeOut" }}
            className="w-full h-64 sm:h-96 flex flex-col bg-zinc-500 rounded-lg hover:border-2 hover:border-gray-500 hover:scale-110 transition-transform duration-300 overflow-hidden"
          >
            <div className="w-full h-[80%] flex justify-center items-center">
              <img
                src="./assets/keyboard.png"
                alt="virtual keyboard"
                className="w-full h-full object-cover"
              />
            </div>
            <div className="w-full h-[20%] flex items-center justify-center gap-4">
              <button
                onClick={() => handleStart("virtual-keyboard")}
                className="px-4 py-2 bg-blue-500 hover:bg-blue-700 rounded-xl text-white"
              >
                Start Virtual Keyboard
              </button>
              <button
                onClick={() => handleStop("virtual-keyboard")}
                className="bg-white hover:bg-red-500 rounded-full"
              >
                <img
                  src="./assets/exit.png"
                  alt="exit"
                  className="w-10 h-10 object-cover"
                />
              </button>
            </div>
          </motion.div>
        </div>
      </div>
    </div>
  );
}
