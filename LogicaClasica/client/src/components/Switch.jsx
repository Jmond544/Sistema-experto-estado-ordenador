import { useState } from "react";

const Switch = ({
    setRespuestas,
    codigoAsociado,
}) => {
  const [isYes, setIsYes] = useState(false);

  const handleToggle = () => {
    if (isYes) {
      setRespuestas((prevState) => {
        return prevState.filter((item) => item !== codigoAsociado);
      });
    } else {
      setRespuestas((prevState) => {
        return [...prevState, codigoAsociado];
      });
    }
    setIsYes(!isYes);
  };

  return (
      <div className={`switch ${isYes ? "yes" : "no"}`} onClick={handleToggle}>
        <div className="switch-circle"></div>
        <span className="label yes-label">Sí</span>
        <span className="label no-label">No</span>
      </div>
  );
};

export default Switch;
