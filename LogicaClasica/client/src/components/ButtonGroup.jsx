import { useState, useEffect } from "react";

const ButtonGroup = ({ nameItem, titles, selected, setSelected }) => {
  const [selectedIndex, setSelectedIndex] = useState(() => {
    const initialIndex = titles.indexOf(selected[nameItem]);
    return initialIndex !== -1 ? initialIndex : 0;
  });

  const handleClick = (index) => {
    setSelectedIndex(index);
    setSelected((prevSelected) => ({
      ...prevSelected,
      [nameItem]: titles[index],
    }));
  };

  useEffect(() => {
    const newIndex = titles.indexOf(selected[nameItem]);
    if (newIndex !== -1) {
      setSelectedIndex(newIndex);
    }
  }, [selected, titles, nameItem]);

  return (
    <div className="relative w-full max-w-md mx-auto">
      {/* Botones */}
      <div className="flex relative z-10">
        {titles.map((title, index) => (
          <button
            key={index}
            onClick={() => handleClick(index)}
            className={`flex-1 py-2 text-center transition-colors duration-300 focus:outline-none ${
              selectedIndex === index ? "text-pink-700" : "text-gray-500"
            }`}
          >
            {title}
          </button>
        ))}
      </div>
      {/* Indicador animado */}
      <div
        className="absolute bottom-0 left-0 w-1/3 h-1 bg-pink-700 transition-transform duration-300 ease-in-out"
        style={{ transform: `translateX(${selectedIndex * 100}%)` }}
      />
    </div>
  );
};

export default ButtonGroup;